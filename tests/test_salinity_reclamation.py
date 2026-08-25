"""
Unit Tests for Soil Salinity Reclamation Engine
"""

from services.ai_ml_engine.datasets.soil_salinity_reclamation import SoilSalinityReclamationEngine

def test_soil_salinity_gypsum_calculation():
    res = SoilSalinityReclamationEngine.calculate_gypsum_and_leaching(
        ec_e_ds_m=5.5,
        initial_esp_pct=22.0,
        target_esp_pct=10.0,
        cec_meq_100g=28.0
    )
    assert res["soil_classification"] == "SALINE_SODIC_SOIL"
    assert res["gypsum_requirement_tonnes_ha"] > 0
    assert res["optimal_leaching_fraction"] > 0
    assert "Agricultural Gypsum" in res["recommended_amendment"]
