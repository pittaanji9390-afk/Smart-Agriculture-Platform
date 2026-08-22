"""
Data Schemas and Pydantic Models for AgriSphere Platform
"""

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime

class SensorReading(BaseModel):
    zone_id: str = Field(..., description="Field Zone Identifier")
    zone_name: str
    crop_type: str
    timestamp: datetime = Field(default_factory=datetime.now)
    soil_moisture_10cm: float = Field(..., description="Soil Moisture % at 10cm depth")
    soil_moisture_30cm: float = Field(..., description="Soil Moisture % at 30cm depth")
    soil_moisture_60cm: float = Field(..., description="Soil Moisture % at 60cm depth")
    soil_temperature: float = Field(..., description="Soil Temperature in Celsius")
    soil_ph: float = Field(..., description="Soil pH Level (0-14)")
    nitrogen_ppm: float = Field(..., description="Nitrogen level in mg/kg")
    phosphorus_ppm: float = Field(..., description="Phosphorus level in mg/kg")
    potassium_ppm: float = Field(..., description="Potassium level in mg/kg")
    ambient_temperature: float = Field(..., description="Ambient Air Temperature in Celsius")
    relative_humidity: float = Field(..., description="Relative Humidity %")
    solar_radiation_w_m2: float = Field(..., description="Solar Radiation in W/m2")
    precipitation_mm: float = Field(..., description="Rainfall accumulation in mm")
    vpd_kpa: float = Field(..., description="Vapor Pressure Deficit in kPa")
    battery_level_pct: float = Field(default=98.5, description="Probe battery %")
    health_status: str = Field(default="OPTIMAL", description="OPTIMAL, WARNING, STRESS, CRITICAL")

class ZoneTelemetryResponse(BaseModel):
    zones: List[SensorReading]
    system_status: str = "ONLINE"
    timestamp: datetime = Field(default_factory=datetime.now)

class CropRecommendationRequest(BaseModel):
    nitrogen: float = Field(..., ge=0, le=300, description="Nitrogen content in soil (kg/ha or ppm)")
    phosphorus: float = Field(..., ge=0, le=200, description="Phosphorus content in soil (kg/ha or ppm)")
    potassium: float = Field(..., ge=0, le=300, description="Potassium content in soil (kg/ha or ppm)")
    temperature: float = Field(..., ge=-10, le=60, description="Temperature in Celsius")
    humidity: float = Field(..., ge=0, le=100, description="Relative Humidity %")
    ph: float = Field(..., ge=3.0, le=11.0, description="Soil pH value")
    rainfall: float = Field(..., ge=0, le=4000, description="Annual or seasonal rainfall in mm")

class CropMatch(BaseModel):
    crop: str
    confidence_score: float
    description: str
    ideal_conditions: Dict[str, Any]
    growing_duration_days: int
    estimated_yield_per_acre_kg: float
    fertilizer_guideline: str

class CropRecommendationResponse(BaseModel):
    recommended_crops: List[CropMatch]
    soil_fertility_index: float
    soil_health_grade: str
    limiting_nutrients: List[str]

class FertilizerCalculationRequest(BaseModel):
    crop_name: str
    field_area_acres: float = 1.0
    current_n: float
    current_p: float
    current_k: float
    soil_type: str = "Loamy"

class FertilizerSchedule(BaseModel):
    stage_name: str
    days_after_sowing: int
    urea_kg: float
    dap_kg: float
    mop_kg: float
    organic_compost_kg: float
    instructions: str

class FertilizerCalculationResponse(BaseModel):
    crop_name: str
    field_area_acres: float
    total_urea_needed_kg: float
    total_dap_needed_kg: float
    total_mop_needed_kg: float
    total_organic_manure_kg: float
    npk_deficit: Dict[str, float]
    application_schedule: List[FertilizerSchedule]
    organic_alternatives: List[str]

class DiseaseDiagnosisRequest(BaseModel):
    crop_name: Optional[str] = "Tomato"
    symptoms_observed: List[str]
    affected_parts: List[str]
    weather_condition: Optional[str] = "Humid"

class DiseaseDiagnosisResponse(BaseModel):
    disease_name: str
    causal_agent: str
    confidence_pct: float
    severity_level: str
    symptom_summary: str
    chemical_treatments: List[Dict[str, str]]
    organic_remedies: List[str]
    preventive_measures: List[str]

class IrrigationControlRequest(BaseModel):
    zone_id: str
    action: str = Field(..., description="START, STOP, AUTO_SCHEDULE, SET_THRESHOLD")
    duration_minutes: Optional[int] = 15
    moisture_threshold_pct: Optional[float] = 35.0

class IrrigationZoneStatus(BaseModel):
    zone_id: str
    zone_name: str
    valve_open: bool
    mode: str = "AUTO"  # AUTO, MANUAL, SCHEDULED
    moisture_threshold_pct: float
    current_moisture_pct: float
    pump_runtime_today_mins: int
    water_applied_liters: float
    next_scheduled_run: Optional[str] = None
    et0_rate_mm_day: float

class MandiPriceItem(BaseModel):
    commodity: str
    state: str
    market_name: str
    modal_price_rs_per_quintal: float
    min_price: float
    max_price: float
    price_change_pct: float
    trend: str # UP, DOWN, STABLE
    arrival_date: str

class MandiMarketResponse(BaseModel):
    market_items: List[MandiPriceItem]
    top_gainers: List[MandiPriceItem]
    updated_at: datetime = Field(default_factory=datetime.now)

class ChatMessage(BaseModel):
    role: str # user, assistant, system
    content: str

class ChatRequest(BaseModel):
    message: str
    language: str = "en"  # en, hi, te
    zone_context: Optional[str] = None
    chat_history: Optional[List[ChatMessage]] = []

class ChatResponse(BaseModel):
    reply: str
    language: str
    suggested_actions: List[str]
