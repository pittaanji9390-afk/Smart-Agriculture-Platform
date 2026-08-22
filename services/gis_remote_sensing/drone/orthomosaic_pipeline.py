"""
Drone Photogrammetry & Canopy Height Model (CHM) Pipeline
Extracts plant height, canopy volume, and lodging detection from Digital Surface Model (DSM) and Digital Terrain Model (DTM).
"""

import numpy as np
from typing import Dict, Any

class DronePhotogrammetryEngine:
    @staticmethod
    def compute_canopy_height_model(dsm_surface: np.ndarray, dtm_terrain: np.ndarray) -> np.ndarray:
        """
        Canopy Height Model (CHM) = DSM - DTM
        Measures true crop canopy height in meters above bare ground level.
        """
        chm = dsm_surface - dtm_terrain
        # Plants cannot have negative height
        return np.maximum(0.0, chm)

    @classmethod
    def analyze_crop_vigor_and_lodging(cls, chm: np.ndarray, expected_height_m: float) -> Dict[str, Any]:
        """
        Detects crop lodging (flattened crops due to severe wind/rain) and calculates average height.
        """
        valid_pixels = chm[chm > 0.05]
        if len(valid_pixels) == 0:
            return {"mean_height_m": 0.0, "lodging_area_pct": 0.0, "canopy_uniformity": "N/A"}

        mean_h = float(np.mean(valid_pixels))
        p90_h = float(np.percentile(valid_pixels, 90))
        
        # Lodging condition: crop height collapsed below 35% of expected height in mature stages
        lodging_threshold = expected_height_m * 0.35
        lodged_pixels = np.count_nonzero((chm > 0.05) & (chm < lodging_threshold))
        lodging_pct = round((lodged_pixels / len(valid_pixels)) * 100.0, 2)

        return {
            "mean_height_m": round(mean_h, 3),
            "p90_canopy_height_m": round(p90_h, 3),
            "lodging_area_pct": lodging_pct,
            "lodging_risk": "CRITICAL" if lodging_pct > 15.0 else ("MODERATE" if lodging_pct > 5.0 else "LOW")
        }
