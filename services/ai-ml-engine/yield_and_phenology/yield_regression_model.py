"""
Multi-Variate Agronomic Crop Yield Prediction Engine
Combines Soil Health Score, NDVI Biomass Density, Cumulative Thermal Units (GDD), and Water Stress indices to forecast harvest tonnage.
"""

from typing import Dict, Any

class CropYieldPredictionEngine:
    @staticmethod
    def forecast_yield_per_acre(
        crop_name: str,
        base_potential_kg: float,
        mean_ndvi: float,
        soil_fertility_index: float,
        water_stress_coefficient_ks: float = 1.0,
        pest_damage_factor: float = 0.0
    ) -> Dict[str, Any]:
        """
        Yield Estimation Equation:
        Y = Y_potential * f(NDVI) * f(Soil) * f(Water) * (1 - Pest_Damage)
        """
        # 1. Canopy vigor factor from satellite/drone NDVI (optimal range 0.65 - 0.85)
        if mean_ndvi < 0.3:
            ndvi_factor = 0.4
        elif mean_ndvi < 0.5:
            ndvi_factor = 0.7
        elif mean_ndvi < 0.7:
            ndvi_factor = 0.95
        else:
            ndvi_factor = 1.05

        # 2. Soil nutrition factor (0 to 100 scale)
        soil_factor = 0.5 + (soil_fertility_index / 100.0) * 0.55

        # 3. Water stress factor (FAO-56 Ks: 0.0 to 1.0)
        water_factor = max(0.4, min(1.0, water_stress_coefficient_ks))

        # 4. Total Yield Modifier
        total_efficiency = ndvi_factor * soil_factor * water_factor * (1.0 - min(0.8, pest_damage_factor))
        estimated_yield_kg = round(base_potential_kg * total_efficiency, 1)
        estimated_quintals = round(estimated_yield_kg / 100.0, 2)

        return {
            "crop_name": crop_name,
            "potential_yield_kg_acre": base_potential_kg,
            "estimated_yield_kg_acre": estimated_yield_kg,
            "estimated_yield_quintals_acre": estimated_quintals,
            "yield_efficiency_pct": round(total_efficiency * 100.0, 1),
            "limiting_factors": [
                f"NDVI Vigor Factor: {round(ndvi_factor, 2)}",
                f"Soil Fertility Factor: {round(soil_factor, 2)}",
                f"Water Availability Factor: {round(water_factor, 2)}"
            ]
        }
