"""
Variable Rate Application (VRA) Prescription Map Generator for Agricultural Drones & Sprayers
"""

import numpy as np
from typing import Dict, Any, List

class VariableRatePrescriptionEngine:
    """
    Translates calibrated multispectral vegetation index rasters (NDVI/NDRE)
    into multi-zone prescriptive nitrogen and fungicide application rate tables.
    """
    @classmethod
    def generate_nitrogen_prescription_zones(
        cls,
        ndvi_raster: np.ndarray,
        base_nitrogen_rate_kg_ha: float = 120.0
    ) -> Dict[str, Any]:
        """Classifies parcel pixels into 3 management zones with inverse or direct nitrogen compensation."""
        zone_low = ndvi_raster < 0.40       # Stunted / severe deficiency -> High N boost
        zone_med = (ndvi_raster >= 0.40) & (ndvi_raster < 0.70) # Optimal vegetative -> Maintenance N
        zone_high = ndvi_raster >= 0.70     # Dense / lush canopy -> Reduced N to prevent lodging

        rate_low = base_nitrogen_rate_kg_ha * 1.30
        rate_med = base_nitrogen_rate_kg_ha * 1.00
        rate_high = base_nitrogen_rate_kg_ha * 0.75

        total_pixels = ndvi_raster.size
        pct_low = (np.sum(zone_low) / total_pixels) * 100.0
        pct_med = (np.sum(zone_med) / total_pixels) * 100.0
        pct_high = (np.sum(zone_high) / total_pixels) * 100.0

        prescription_map = np.zeros_like(ndvi_raster, dtype=np.float32)
        prescription_map[zone_low] = rate_low
        prescription_map[zone_med] = rate_med
        prescription_map[zone_high] = rate_high

        weighted_avg_n = float(np.mean(prescription_map))
        standard_flat_n = base_nitrogen_rate_kg_ha
        fertilizer_saved_pct = ((standard_flat_n - weighted_avg_n) / standard_flat_n) * 100.0

        return {
            "management_zones": {
                "zone_low_vigor_boost": {"area_pct": round(pct_low, 1), "prescribed_rate_kg_ha": rate_low},
                "zone_medium_vigor_maintenance": {"area_pct": round(pct_med, 1), "prescribed_rate_kg_ha": rate_med},
                "zone_high_vigor_saving": {"area_pct": round(pct_high, 1), "prescribed_rate_kg_ha": rate_high}
            },
            "weighted_average_application_rate_kg_ha": round(weighted_avg_n, 2),
            "estimated_fertilizer_cost_reduction_pct": round(max(0.0, fertilizer_saved_pct), 2)
        }
