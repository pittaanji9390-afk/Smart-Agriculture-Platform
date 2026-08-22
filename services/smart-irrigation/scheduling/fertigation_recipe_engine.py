"""
Precision Fertigation Recipe Engine (A/B/Acid Tank Injector Optimizer)
Calculates exact chemical weight of 100% water-soluble fertilizers for closed-loop drip fertigation systems.
"""

from typing import Dict, Any, List

class FertigationRecipeEngine:
    # Target elemental ppm (Parts Per Million) for standard crops:
    # [N, P, K, Ca, Mg, S]
    CROP_NUTRIENT_TARGETS_PPM = {
        "Tomato (Fruiting)": {"N": 180, "P": 50, "K": 250, "Ca": 160, "Mg": 50, "EC_mS_cm": 2.2, "target_pH": 5.8},
        "Capsicum / Pepper": {"N": 160, "P": 45, "K": 220, "Ca": 140, "Mg": 45, "EC_mS_cm": 2.0, "target_pH": 5.8},
        "Cucumber / Gherkin": {"N": 200, "P": 40, "K": 260, "Ca": 120, "Mg": 40, "EC_mS_cm": 2.3, "target_pH": 6.0},
        "Strawberry": {"N": 100, "P": 35, "K": 150, "Ca": 90, "Mg": 30, "EC_mS_cm": 1.4, "target_pH": 5.6},
        "Cotton (Flowering)": {"N": 140, "P": 40, "K": 180, "Ca": 100, "Mg": 35, "EC_mS_cm": 1.8, "target_pH": 6.5}
    }

    @classmethod
    def calculate_tank_batch(
        cls,
        crop_recipe: str,
        water_volume_liters: float = 10000.0,
        stock_tank_volume_liters: float = 1000.0,
        injection_ratio_pct: float = 1.0 # 1:100 dilution
    ) -> Dict[str, Any]:
        """
        Calculates tank batch weights for 3-tank injection system:
        - Tank A (Calcium Nitrate + Potassium Nitrate + Iron EDDHA)
        - Tank B (Monopotassium Phosphate MKP + Potassium Sulfate + Magnesium Sulfate)
        - Tank C (Nitric / Phosphoric Acid for pH stabilization)
        """
        targets = cls.CROP_NUTRIENT_TARGETS_PPM.get(crop_recipe, cls.CROP_NUTRIENT_TARGETS_PPM["Tomato (Fruiting)"])
        
        # Scaling factor based on water volume
        vol_m3 = water_volume_liters / 1000.0

        # Calculations for commercial 100% water soluble salts:
        # 1. Calcium Nitrate [Ca(NO3)2] (19% Ca, 15.5% N)
        ca_needed_g = (targets["Ca"] * water_volume_liters) / 1000.0
        calcium_nitrate_kg = round(ca_needed_g / 190.0, 2)
        n_from_calnit = calcium_nitrate_kg * 0.155 * 1000.0 / vol_m3 # ppm

        # 2. Monopotassium Phosphate MKP (0-52-34: 22.7% P, 28.2% K)
        p_needed_g = (targets["P"] * water_volume_liters) / 1000.0
        mkp_kg = round(p_needed_g / 227.0, 2)
        k_from_mkp = mkp_kg * 0.282 * 1000.0 / vol_m3 # ppm

        # 3. Potassium Nitrate KNO3 (13-0-45: 13% N, 38% K)
        remaining_n = max(0.0, targets["N"] - n_from_calnit)
        kno3_kg = round((remaining_n * vol_m3) / 130.0, 2)
        k_from_kno3 = kno3_kg * 0.38 * 1000.0 / vol_m3 # ppm

        # 4. Potassium Sulfate SOP (0-0-50: 41.5% K, 18% S)
        remaining_k = max(0.0, targets["K"] - k_from_mkp - k_from_kno3)
        sop_kg = round((remaining_k * vol_m3) / 415.0, 2)

        # 5. Magnesium Sulfate [MgSO4.7H2O] (9.6% Mg, 13% S)
        mg_needed_g = (targets["Mg"] * water_volume_liters) / 1000.0
        mgso4_kg = round(mg_needed_g / 96.0, 2)

        # 6. Iron Chelate Fe-EDDHA (6% Fe)
        fe_kg = round((2.5 * water_volume_liters) / 60000.0, 3)

        return {
            "recipe_name": crop_recipe,
            "irrigation_water_volume_liters": water_volume_liters,
            "target_ec_ms_cm": targets["EC_mS_cm"],
            "target_ph": targets["target_pH"],
            "tank_a_fertilizers": [
                {"fertilizer": "Calcium Nitrate", "weight_kg": calcium_nitrate_kg},
                {"fertilizer": "Potassium Nitrate (KNO3)", "weight_kg": kno3_kg},
                {"fertilizer": "Iron Chelate (Fe-EDDHA 6%)", "weight_kg": fe_kg}
            ],
            "tank_b_fertilizers": [
                {"fertilizer": "Monopotassium Phosphate (MKP 0:52:34)", "weight_kg": mkp_kg},
                {"fertilizer": "Potassium Sulfate (SOP 0:0:50)", "weight_kg": sop_kg},
                {"fertilizer": "Magnesium Sulfate (Epsom Salt)", "weight_kg": mgso4_kg}
            ],
            "tank_c_acid": {
                "acid_type": "Nitric Acid 68%",
                "dosage_liters": round(vol_m3 * 0.15, 2),
                "purpose": "Maintain drip dripper declogging & lower pH to 5.8"
            }
        }
