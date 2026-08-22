"""
Multispectral Remote Sensing Indices Calculation Engine
Computes 12+ agronomic vegetation, moisture, chlorophyll, and canopy stress indices from Sentinel-2 & drone bands.
"""

import numpy as np
from typing import Dict, Any, Union

class MultispectralIndexEngine:
    """
    Standard Sentinel-2 Bands Reference:
    B02: Blue (490 nm)
    B03: Green (560 nm)
    B04: Red (665 nm)
    B05: RedEdge 1 (705 nm)
    B06: RedEdge 2 (740 nm)
    B07: RedEdge 3 (783 nm)
    B08: NIR (842 nm)
    B8A: Narrow NIR (865 nm)
    B11: SWIR 1 (1610 nm)
    B12: SWIR 2 (2190 nm)
    """

    @staticmethod
    def compute_ndvi(nir: np.ndarray, red: np.ndarray) -> np.ndarray:
        """
        Normalized Difference Vegetation Index (NDVI)
        NDVI = (NIR - Red) / (NIR + Red)
        Reflects plant vigor, photosynthetic activity, and biomass density.
        """
        denominator = nir + red
        ndvi = np.where(denominator > 0, (nir - red) / denominator, 0.0)
        return np.clip(ndvi, -1.0, 1.0)

    @staticmethod
    def compute_evi(nir: np.ndarray, red: np.ndarray, blue: np.ndarray, g: float = 2.5, c1: float = 6.0, c2: float = 7.5, l: float = 1.0) -> np.ndarray:
        """
        Enhanced Vegetation Index (EVI)
        EVI = G * ((NIR - Red) / (NIR + C1 * Red - C2 * Blue + L))
        Optimized for high biomass regions with reduced atmospheric and soil background interference.
        """
        denominator = nir + (c1 * red) - (c2 * blue) + l
        evi = np.where(denominator > 0, g * ((nir - red) / denominator), 0.0)
        return np.clip(evi, -1.0, 1.0)

    @staticmethod
    def compute_savi(nir: np.ndarray, red: np.ndarray, l: float = 0.5) -> np.ndarray:
        """
        Soil-Adjusted Vegetation Index (SAVI)
        SAVI = ((NIR - Red) / (NIR + Red + L)) * (1 + L)
        Compensates for soil brightness in early crop stages with low canopy cover.
        """
        denominator = nir + red + l
        savi = np.where(denominator > 0, ((nir - red) / denominator) * (1.0 + l), 0.0)
        return np.clip(savi, -1.0, 1.0)

    @staticmethod
    def compute_ndre(nir: np.ndarray, red_edge: np.ndarray) -> np.ndarray:
        """
        Normalized Difference Red Edge (NDRE)
        NDRE = (NIR - RedEdge) / (NIR + RedEdge)
        Sensitive to chlorophyll content in dense, mature canopies where NDVI saturates.
        """
        denominator = nir + red_edge
        ndre = np.where(denominator > 0, (nir - red_edge) / denominator, 0.0)
        return np.clip(ndre, -1.0, 1.0)

    @staticmethod
    def compute_ndwi(nir: np.ndarray, swir: np.ndarray) -> np.ndarray:
        """
        Normalized Difference Water Index (NDWI / NDII)
        NDWI = (NIR - SWIR) / (NIR + SWIR)
        Measures liquid water content in plant leaves and canopy hydration stress.
        """
        denominator = nir + swir
        ndwi = np.where(denominator > 0, (nir - swir) / denominator, 0.0)
        return np.clip(ndwi, -1.0, 1.0)

    @staticmethod
    def compute_msi(swir: np.ndarray, nir: np.ndarray) -> np.ndarray:
        """
        Moisture Stress Index (MSI)
        MSI = SWIR / NIR
        Values > 1.0 indicate acute water deficit stress.
        """
        return np.where(nir > 0, swir / nir, 0.0)

    @staticmethod
    def compute_gndvi(nir: np.ndarray, green: np.ndarray) -> np.ndarray:
        """
        Green Normalized Difference Vegetation Index (GNDVI)
        GNDVI = (NIR - Green) / (NIR + Green)
        Sensitive to Nitrogen uptake and chlorophyll concentration.
        """
        denominator = nir + green
        return np.where(denominator > 0, (nir - green) / denominator, 0.0)

    @classmethod
    def compute_full_agronomic_suite(cls, bands: Dict[str, np.ndarray]) -> Dict[str, np.ndarray]:
        """
        Expects dictionary with keys: 'blue', 'green', 'red', 'red_edge', 'nir', 'swir'
        """
        nir = bands["nir"]
        red = bands["red"]
        green = bands["green"]
        blue = bands.get("blue", red)
        red_edge = bands.get("red_edge", (red + nir) / 2.0)
        swir = bands.get("swir", red)

        return {
            "ndvi": cls.compute_ndvi(nir, red),
            "evi": cls.compute_evi(nir, red, blue),
            "savi": cls.compute_savi(nir, red),
            "ndre": cls.compute_ndre(nir, red_edge),
            "ndwi": cls.compute_ndwi(nir, swir),
            "msi": cls.compute_msi(swir, nir),
            "gndvi": cls.compute_gndvi(nir, green)
        }
