"""
Sentinel-2 QA60 Cloud and Cirrus Bitmask Decoder & Atmospheric Correction Masker
"""

import numpy as np
from typing import Dict, Any, Tuple

class Sentinel2CloudMaskEngine:
    """
    Decodes QA60 bitmask flags from Sentinel-2 Level-1C / Level-2A products:
    - Bit 10: Opaque clouds
    - Bit 11: Cirrus clouds
    """
    OPAQUE_CLOUD_BIT = 10
    CIRRUS_CLOUD_BIT = 11

    @classmethod
    def generate_clear_sky_mask(cls, qa60_raster: np.ndarray) -> np.ndarray:
        """Returns boolean mask where True indicates clear sky, False indicates cloud or cirrus contamination."""
        opaque_clouds = (qa60_raster & (1 << cls.OPAQUE_CLOUD_BIT)) != 0
        cirrus_clouds = (qa60_raster & (1 << cls.CIRRUS_CLOUD_BIT)) != 0
        cloud_free_mask = ~(opaque_clouds | cirrus_clouds)
        return cloud_free_mask

    @classmethod
    def compute_cloud_cover_percentage(cls, qa60_raster: np.ndarray) -> float:
        """Calculates percentage of scene obscured by opaque or cirrus clouds."""
        clear_mask = cls.generate_clear_sky_mask(qa60_raster)
        total_pixels = qa60_raster.size
        clear_pixels = np.sum(clear_mask)
        cloud_pct = ((total_pixels - clear_pixels) / float(total_pixels)) * 100.0
        return round(cloud_pct, 2)
