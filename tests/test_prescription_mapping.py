"""
Unit Tests for Drone Variable Rate Prescription Generator
"""

import numpy as np
from services.gis_remote_sensing.drone.variable_rate_prescription import VariableRatePrescriptionEngine

def test_variable_rate_nitrogen_prescription():
    ndvi = np.array([
        [0.2, 0.3, 0.5],
        [0.6, 0.8, 0.85],
        [0.45, 0.75, 0.9]
    ], dtype=np.float32)
    
    res = VariableRatePrescriptionEngine.generate_nitrogen_prescription_zones(ndvi, base_nitrogen_rate_kg_ha=100.0)
    assert "management_zones" in res
    assert "weighted_average_application_rate_kg_ha" in res
    assert res["weighted_average_application_rate_kg_ha"] > 0
    assert res["management_zones"]["zone_low_vigor_boost"]["prescribed_rate_kg_ha"] == 130.0
