"""
FAO-56 Dual Crop Coefficient (Kcb + Ke) Soil Water Balance Engine
Calculates daily root zone depletion (Dr), readily available water (RAW), total available water (TAW),
and soil water stress coefficient (Ks).
"""

import math
from typing import Dict, Any

class FAODualCropCoefficientEngine:
    # Soil Texture Hydraulics Reference:
    # [Field Capacity (FC) % by volume, Permanent Wilting Point (PWP) % by volume]
    SOIL_HYDRAULICS = {
        "Sand": (0.12, 0.04),
        "Loamy Sand": (0.16, 0.07),
        "Sandy Loam": (0.22, 0.10),
        "Loam": (0.28, 0.14),
        "Silt Loam": (0.32, 0.16),
        "Clay Loam": (0.35, 0.19),
        "Silty Clay": (0.38, 0.22),
        "Clay (Black Cotton)": (0.42, 0.25)
    }

    # Basal Crop Coefficients (Kcb) for growth stages: (Ini, Mid, End)
    CROP_KCB = {
        "Rice (Paddy)": (1.05, 1.20, 0.90),
        "Wheat": (0.15, 1.10, 0.25),
        "Maize (Corn)": (0.15, 1.15, 0.35),
        "Cotton": (0.15, 1.15, 0.50),
        "Tomato": (0.15, 1.10, 0.70),
        "Potato": (0.15, 1.10, 0.65),
        "Soybean": (0.15, 1.10, 0.30),
        "Sugarcane": (0.30, 1.20, 0.70)
    }

    @classmethod
    def calculate_soil_water_balance(
        cls,
        crop: str,
        soil_type: str,
        root_depth_m: float,
        reference_et0_mm: float,
        stage_fraction: float = 0.5, # 0.0=Ini, 0.5=Mid, 1.0=End
        current_depletion_mm: float = 15.0,
        irrigation_applied_mm: float = 0.0,
        effective_rainfall_mm: float = 0.0
    ) -> Dict[str, Any]:
        """
        Calculates daily soil water deficit and determines whether irrigation trigger threshold is reached.
        """
        # 1. Soil Hydraulic Properties
        fc, pwp = cls.SOIL_HYDRAULICS.get(soil_type, cls.SOIL_HYDRAULICS["Sandy Loam"])
        
        # Total Available Water (TAW) in root zone (mm)
        # TAW = 1000 * (FC - PWP) * Zr
        taw_mm = 1000.0 * (fc - pwp) * max(0.1, root_depth_m)

        # 2. Readily Available Water (RAW) in mm
        # RAW = p * TAW (where p is average soil water depletion fraction ~0.45-0.55)
        depletion_fraction_p = 0.50
        raw_mm = depletion_fraction_p * taw_mm

        # 3. Crop Evapotranspiration (ETc) with Basal Kcb
        kcb_tuple = cls.CROP_KCB.get(crop, (0.15, 1.10, 0.50))
        if stage_fraction < 0.25:
            kcb = kcb_tuple[0]
        elif stage_fraction < 0.75:
            kcb = kcb_tuple[1]
        else:
            kcb = kcb_tuple[2]

        # 4. Water Stress Coefficient (Ks)
        # If depletion Dr > RAW, transpiration is reduced: Ks = (TAW - Dr) / (TAW - RAW)
        if current_depletion_mm > raw_mm:
            ks = max(0.0, (taw_mm - current_depletion_mm) / (taw_mm - raw_mm + 1e-6))
        else:
            ks = 1.0

        # Soil Evaporation Coefficient (Ke) ~ 0.15 for moist topsoil
        ke = 0.15
        kc_actual = (ks * kcb) + ke
        etc_actual_mm = kc_actual * reference_et0_mm

        # 5. Updated Root Zone Depletion (Dr)
        # Dr_new = Dr_prev - Rainfall - Irrigation + ETc
        new_depletion_mm = current_depletion_mm - effective_rainfall_mm - irrigation_applied_mm + etc_actual_mm
        new_depletion_mm = max(0.0, min(taw_mm, new_depletion_mm))

        # 6. Irrigation Advice
        irrigation_needed = new_depletion_mm >= raw_mm
        recommended_water_mm = round(new_depletion_mm, 1) if irrigation_needed else 0.0

        return {
            "crop": crop,
            "soil_type": soil_type,
            "taw_mm": round(taw_mm, 1),
            "raw_mm": round(raw_mm, 1),
            "root_zone_depletion_mm": round(new_depletion_mm, 1),
            "crop_evapotranspiration_etc_mm": round(etc_actual_mm, 2),
            "water_stress_coefficient_ks": round(ks, 2),
            "actual_crop_coefficient_kc": round(kc_actual, 2),
            "irrigation_trigger_status": "TRIGGER_IRRIGATION" if irrigation_needed else "SOIL_MOISTURE_ADEQUATE",
            "recommended_irrigation_volume_mm": recommended_water_mm,
            "recommended_liters_per_hectare": round(recommended_water_mm * 10000.0, 0)
        }
