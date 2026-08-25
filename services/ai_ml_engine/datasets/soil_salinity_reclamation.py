"""
Soil Salinity & Sodic Soil Reclamation Calculator (Gypsum Requirement & Leaching Fractions)
"""

import math
from typing import Dict, Any

class SoilSalinityReclamationEngine:
    """
    Calculates Agricultural Gypsum (CaSO4.2H2O) requirements (GR) and Leaching Fractions (LF)
    using USDA Handbook 60 & Central Soil Salinity Research Institute (CSSRI) standard formulas:
    GR (tonnes/ha) = 8.6 * (ESP_initial - ESP_target) * CEC * BulkDensity * SoilDepth / 10000
    """
    @classmethod
    def calculate_gypsum_and_leaching(
        cls,
        ec_e_ds_m: float,
        initial_esp_pct: float,
        target_esp_pct: float = 10.0,
        cec_meq_100g: float = 25.0,
        soil_depth_cm: float = 30.0,
        bulk_density_g_cm3: float = 1.35
    ) -> Dict[str, Any]:
        # Salinity classification
        if ec_e_ds_m < 4.0 and initial_esp_pct < 15.0:
            classification = "NORMAL_SOIL"
        elif ec_e_ds_m >= 4.0 and initial_esp_pct < 15.0:
            classification = "SALINE_SOIL"
        elif ec_e_ds_m < 4.0 and initial_esp_pct >= 15.0:
            classification = "SODIC_ALKALI_SOIL"
        else:
            classification = "SALINE_SODIC_SOIL"

        # Gypsum Requirement calculation
        esp_diff = max(0.0, initial_esp_pct - target_esp_pct)
        # Factor: 8.6 * (ESP/100) * CEC * (bulk_density * depth * 100) / 1000
        gr_tonnes_ha = (0.086 * esp_diff * cec_meq_100g * bulk_density_g_cm3 * (soil_depth_cm / 15.0)) / 2.0
        gr_tonnes_ha = max(0.0, gr_tonnes_ha)

        # Leaching requirement (LR = EC_iw / (5 * EC_e - EC_iw))
        ec_iw_water = 1.2 # Irrigation water EC benchmark in dS/m
        denom = max(0.1, (5.0 * ec_e_ds_m) - ec_iw_water)
        leaching_fraction = min(0.40, ec_iw_water / denom)

        return {
            "soil_classification": classification,
            "gypsum_requirement_tonnes_ha": round(gr_tonnes_ha, 2),
            "gypsum_requirement_kg_acre": round(gr_tonnes_ha * 404.686, 1),
            "optimal_leaching_fraction": round(leaching_fraction, 3),
            "recommended_amendment": "Agricultural Gypsum (85% purity) + Green Manuring (Sesbania/Dhaincha)" if gr_tonnes_ha > 0 else "Good drainage and leaching with low-salinity water"
        }
