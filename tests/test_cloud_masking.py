"""
Unit Tests for Sentinel-2 QA60 Cloud Masking
"""

import numpy as np
from services.gis_remote_sensing.satellite.cloud_masking_qa60 import Sentinel2CloudMaskEngine

def test_cloud_masking_detection():
    qa60 = np.zeros((10, 10), dtype=np.uint16)
    # Set 10 pixels to opaque cloud (bit 10 = 1024)
    qa60[0, :] = 1024
    
    clear_mask = Sentinel2CloudMaskEngine.generate_clear_sky_mask(qa60)
    assert np.sum(clear_mask) == 90
    
    cloud_pct = Sentinel2CloudMaskEngine.compute_cloud_cover_percentage(qa60)
    assert cloud_pct == 10.0
