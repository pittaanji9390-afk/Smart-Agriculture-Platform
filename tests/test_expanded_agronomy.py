"""
Unit Tests for Expanded 60+ Crop Catalog, BBCH Growth Phenology & Multivariate Yield Engine
"""

from services.ai_ml_engine.crop_recommendation.crop_catalog_expanded import EXPANDED_CROP_CATALOG
from services.ai_ml_engine.yield_and_phenology.bbch_phenology_tracker import BBCHPhenologyTracker
from services.ai_ml_engine.yield_and_phenology.yield_regression_model import CropYieldPredictionEngine

def test_crop_catalog_completeness():
    assert len(EXPANDED_CROP_CATALOG) >= 30
    for crop in EXPANDED_CROP_CATALOG:
        assert "crop" in crop
        assert "ideal_n" in crop
        assert "duration_days" in crop
        assert crop["duration_days"] > 40

def test_bbch_phenology_tracking():
    # Test Tomato GDD accumulation
    daily_gdd = BBCHPhenologyTracker.calculate_daily_gdd("Tomato", t_max=32.0, t_min=20.0)
    assert daily_gdd == 16.0 # (26 - 10)

    stage_info = BBCHPhenologyTracker.determine_bbch_stage("Tomato", accumulated_gdd=800.0)
    assert "bbch_code" in stage_info
    assert stage_info["bbch_code"] == 37 # Stem Elongation stage
    assert stage_info["progress_pct"] > 40.0

def test_yield_prediction_engine():
    pred = CropYieldPredictionEngine.forecast_yield_per_acre(
        crop_name="Rice (Paddy)",
        base_potential_kg=2400.0,
        mean_ndvi=0.72,
        soil_fertility_index=80.0,
        water_stress_coefficient_ks=1.0
    )
    assert pred["estimated_yield_kg_acre"] > 2000.0
    assert pred["estimated_yield_quintals_acre"] > 20.0
