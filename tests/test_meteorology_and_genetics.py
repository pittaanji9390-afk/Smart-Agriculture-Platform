"""
Unit Tests for Crop Varietal Gene Bank Registry & Micro-Climate Agro-Meteorological Advisories
"""

from services.ai_ml_engine.datasets.varietal_gene_bank_database import NATIONAL_CROP_GENE_BANK_REGISTRY
from services.gis_remote_sensing.weather_forecasting.microclimate_weather_engine import AgroMeteorologicalGridCell_001

def test_crop_gene_bank_registry():
    assert len(NATIONAL_CROP_GENE_BANK_REGISTRY) >= 200
    for entry in NATIONAL_CROP_GENE_BANK_REGISTRY[:20]:
        assert "gene_accession_id" in entry
        assert "variety_name" in entry
        assert "target_trait" in entry
        assert "major_qtl_markers" in entry
        assert entry["genetic_purity_score"] > 95.0

def test_microclimate_weather_advisory():
    advisory = AgroMeteorologicalGridCell_001.forecast_microclimate_advisory(
        synoptic_t_max_c=34.0,
        synoptic_t_min_c=22.0,
        synoptic_rh_pct=65.0,
        synoptic_wind_speed_kmh=10.0,
        canopy_closure_fraction=0.8
    )
    assert "adjusted_canopy_temp_max_c" in advisory
    assert "adjusted_canopy_temp_min_c" in advisory
    assert "canopy_vpd_kpa" in advisory
    assert advisory["canopy_vpd_kpa"] > 0
    assert "pesticide_spray_window_open" in advisory
    assert "spray_delta_t_celsius" in advisory
