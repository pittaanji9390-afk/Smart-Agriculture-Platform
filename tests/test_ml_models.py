"""
Unit Tests for Agronomic ML Engine & Plant Disease Diagnosis
"""

from backend.app.models.schemas import CropRecommendationRequest, FertilizerCalculationRequest, DiseaseDiagnosisRequest
from backend.app.services.ml_engine import AgronomicMLEngine
from backend.app.services.disease_engine import PlantDiseaseEngine

def test_crop_recommendation_paddy():
    req = CropRecommendationRequest(
        nitrogen=85.0,
        phosphorus=42.0,
        potassium=45.0,
        temperature=29.0,
        humidity=80.0,
        ph=6.5,
        rainfall=1800.0
    )
    res = AgronomicMLEngine.recommend_crops(req)
    assert len(res.recommended_crops) > 0
    top_crop = res.recommended_crops[0]
    assert "Rice" in top_crop.crop or "Tomato" in top_crop.crop
    assert top_crop.confidence_score > 60.0

def test_fertilizer_schedule_calculation():
    req = FertilizerCalculationRequest(
        crop_name="Rice (Paddy)",
        field_area_acres=2.0,
        current_n=30.0,
        current_p=15.0,
        current_k=20.0
    )
    res = AgronomicMLEngine.calculate_fertilizer_schedule(req)
    assert res.total_urea_needed_kg > 0
    assert res.total_dap_needed_kg > 0
    assert len(res.application_schedule) == 3

def test_disease_diagnosis_early_blight():
    req = DiseaseDiagnosisRequest(
        crop_name="Tomato",
        symptoms_observed=["concentric rings", "bullseye", "brown spots"],
        affected_parts=["Leaves"]
    )
    res = PlantDiseaseEngine.diagnose_by_symptoms(req)
    assert "Early Blight" in res.disease_name
    assert len(res.chemical_treatments) > 0
    assert len(res.organic_remedies) > 0
