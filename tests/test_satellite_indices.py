"""
Unit Tests for Satellite Remote Sensing & Multispectral Indices
"""

import numpy as np
from services.gis_remote_sensing.satellite.spectral_indices import MultispectralIndexEngine

def test_ndvi_computation():
    nir = np.array([0.8, 0.6, 0.4])
    red = np.array([0.1, 0.2, 0.3])
    ndvi = MultispectralIndexEngine.compute_ndvi(nir, red)
    assert len(ndvi) == 3
    assert ndvi[0] > ndvi[1] > ndvi[2]
    assert np.all(ndvi >= -1.0) and np.all(ndvi <= 1.0)

def test_evi_and_savi_computation():
    nir = np.array([0.7, 0.5])
    red = np.array([0.15, 0.25])
    blue = np.array([0.05, 0.10])
    evi = MultispectralIndexEngine.compute_evi(nir, red, blue)
    savi = MultispectralIndexEngine.compute_savi(nir, red)
    assert len(evi) == 2
    assert len(savi) == 2
    assert evi[0] > 0.0
    assert savi[0] > 0.0

def test_full_suite():
    bands = {
        "nir": np.array([0.75]),
        "red": np.array([0.12]),
        "green": np.array([0.22]),
        "blue": np.array([0.08]),
        "swir": np.array([0.18])
    }
    res = MultispectralIndexEngine.compute_full_agronomic_suite(bands)
    assert "ndvi" in res
    assert "ndwi" in res
    assert "msi" in res
