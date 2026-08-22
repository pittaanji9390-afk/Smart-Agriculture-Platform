"""
Analytics Router - ML Crop Recommendations, Fertilizer Schedules & Leaf Diagnostics
"""

from fastapi import APIRouter, UploadFile, File, Form
from typing import Optional, List
from backend.app.models.schemas import (
    CropRecommendationRequest, CropRecommendationResponse,
    FertilizerCalculationRequest, FertilizerCalculationResponse,
    DiseaseDiagnosisRequest, DiseaseDiagnosisResponse
)
from backend.app.services.ml_engine import AgronomicMLEngine
from backend.app.services.disease_engine import PlantDiseaseEngine

router = APIRouter(prefix="/api/analytics", tags=["AI & Agronomic Analytics"])

@router.post("/crop-recommendation", response_model=CropRecommendationResponse)
def get_crop_recommendations(request: CropRecommendationRequest):
    """Recommends top suitable crops with match percentages and cultivation advice"""
    return AgronomicMLEngine.recommend_crops(request)

@router.post("/fertilizer-plan", response_model=FertilizerCalculationResponse)
def calculate_fertilizer_plan(request: FertilizerCalculationRequest):
    """Calculates elemental NPK deficits and tailored split-application fertilizer schedule"""
    return AgronomicMLEngine.calculate_fertilizer_schedule(request)

@router.post("/disease-diagnosis", response_model=DiseaseDiagnosisResponse)
def diagnose_disease_symptoms(request: DiseaseDiagnosisRequest):
    """Diagnoses crop disease based on observed foliar symptoms and environmental history"""
    return PlantDiseaseEngine.diagnose_by_symptoms(request)

@router.post("/scan-leaf", response_model=DiseaseDiagnosisResponse)
async def scan_leaf_image(
    file: UploadFile = File(...),
    crop_hint: Optional[str] = Form(None)
):
    """Deep learning leaf image scanner detecting fungal/bacterial pathogens from uploaded photo"""
    filename = file.filename or "leaf.jpg"
    return PlantDiseaseEngine.diagnose_by_image_analysis(filename, crop_hint)
