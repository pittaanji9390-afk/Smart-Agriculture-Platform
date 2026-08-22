"""
Machine Learning and Agronomic Decision Support Engine
Provides Crop Recommendation, Fertilizer Optimization, and Yield Forecasting
"""

import math
from typing import List, Dict, Any
from backend.app.models.schemas import (
    CropRecommendationRequest, CropRecommendationResponse, CropMatch,
    FertilizerCalculationRequest, FertilizerCalculationResponse, FertilizerSchedule
)

# Comprehensive Agricultural Agronomic Profiles Database
CROP_DATABASE = [
    {
        "crop": "Rice (Paddy)",
        "ideal_n": 80, "ideal_p": 40, "ideal_k": 40,
        "temp_min": 20, "temp_max": 38, "humidity_min": 75, "humidity_max": 95,
        "ph_min": 5.5, "ph_max": 7.2, "rainfall_min": 1500, "rainfall_max": 3000,
        "duration_days": 125, "avg_yield_kg_per_acre": 2400,
        "description": "High water-requiring staple cereal, excels in clayey-loam soils with high organic matter and sub-tropical temperatures.",
        "guideline": "Split application of Nitrogen in 3 stages (Basal, Tillering, Panicle Initiation). DAP at basal stage."
    },
    {
        "crop": "Wheat",
        "ideal_n": 100, "ideal_p": 50, "ideal_k": 50,
        "temp_min": 12, "temp_max": 25, "humidity_min": 50, "humidity_max": 70,
        "ph_min": 6.0, "ph_max": 7.5, "rainfall_min": 400, "rainfall_max": 1000,
        "duration_days": 120, "avg_yield_kg_per_acre": 1900,
        "description": "Cool-season cereal crop requiring well-drained loamy soils and moderate, well-distributed irrigation.",
        "guideline": "Half Nitrogen + full P & K at sowing; remaining N at Crown Root Initiation (CRI) and Jointing stages."
    },
    {
        "crop": "Maize (Corn)",
        "ideal_n": 120, "ideal_p": 60, "ideal_k": 50,
        "temp_min": 18, "temp_max": 32, "humidity_min": 55, "humidity_max": 80,
        "ph_min": 5.8, "ph_max": 7.5, "rainfall_min": 500, "rainfall_max": 1100,
        "duration_days": 105, "avg_yield_kg_per_acre": 3100,
        "description": "Versatile, high biomass-producing cereal requiring high nitrogen nutrition and excellent root zone drainage.",
        "guideline": "Heavy feeder. Apply Zinc Sulfate alongside NPK at basal preparation. Top-dress N at knee-high and tasseling."
    },
    {
        "crop": "Cotton",
        "ideal_n": 100, "ideal_p": 50, "ideal_k": 60,
        "temp_min": 22, "temp_max": 36, "humidity_min": 45, "humidity_max": 75,
        "ph_min": 6.5, "ph_max": 8.2, "rainfall_min": 500, "rainfall_max": 1000,
        "duration_days": 160, "avg_yield_kg_per_acre": 1200,
        "description": "Deep-rooted commercial fiber crop suited for black cotton (vertisol) and alluvial soils.",
        "guideline": "Avoid excessive early Nitrogen to prevent vegetative overgrowth. Boost Potassium during square and boll formation."
    },
    {
        "crop": "Tomato",
        "ideal_n": 110, "ideal_p": 60, "ideal_k": 90,
        "temp_min": 18, "temp_max": 30, "humidity_min": 50, "humidity_max": 75,
        "ph_min": 6.0, "ph_max": 7.0, "rainfall_min": 450, "rainfall_max": 800,
        "duration_days": 100, "avg_yield_kg_per_acre": 12000,
        "description": "High-value solanaceous vegetable requiring consistent moisture, calcium nutrition, and warm temperatures.",
        "guideline": "Calcium nitrate spray to prevent Blossom End Rot. Regular fertigation with 19:19:19 and 0:0:50."
    },
    {
        "crop": "Chilli / Red Pepper",
        "ideal_n": 100, "ideal_p": 50, "ideal_k": 70,
        "temp_min": 20, "temp_max": 35, "humidity_min": 50, "humidity_max": 70,
        "ph_min": 6.0, "ph_max": 7.5, "rainfall_min": 600, "rainfall_max": 1200,
        "duration_days": 150, "avg_yield_kg_per_acre": 2200,
        "description": "Spicy commercial cash crop flourishing in warm climates and well-drained fertile sandy loam.",
        "guideline": "Foliar micronutrient sprays (Boron, Zinc) during flowering. Controlled irrigation to prevent root rot."
    },
    {
        "crop": "Chickpea (Gram)",
        "ideal_n": 20, "ideal_p": 50, "ideal_k": 30,
        "temp_min": 15, "temp_max": 28, "humidity_min": 35, "humidity_max": 60,
        "ph_min": 6.0, "ph_max": 8.0, "rainfall_min": 300, "rainfall_max": 650,
        "duration_days": 95, "avg_yield_kg_per_acre": 850,
        "description": "Leguminous pulse crop that fixes atmospheric nitrogen; highly drought-tolerant and soil-enriching.",
        "guideline": "Inoculate seeds with Rhizobium & PSB cultures. Minimal nitrogen requirement; prioritize Phosphorus."
    },
    {
        "crop": "Sugarcane",
        "ideal_n": 220, "ideal_p": 80, "ideal_k": 110,
        "temp_min": 24, "temp_max": 38, "humidity_min": 60, "humidity_max": 85,
        "ph_min": 6.2, "ph_max": 7.8, "rainfall_min": 1200, "rainfall_max": 2200,
        "duration_days": 330, "avg_yield_kg_per_acre": 38000,
        "description": "Long-duration high-tonnage perennial grass crop requiring copious water and warm tropical sunshine.",
        "guideline": "Large organic manure basal dose. Apply NPK in 4 split doses up to grand growth phase."
    },
    {
        "crop": "Groundnut (Peanut)",
        "ideal_n": 25, "ideal_p": 50, "ideal_k": 40,
        "temp_min": 22, "temp_max": 33, "humidity_min": 50, "humidity_max": 75,
        "ph_min": 5.8, "ph_max": 7.2, "rainfall_min": 450, "rainfall_max": 750,
        "duration_days": 110, "avg_yield_kg_per_acre": 1100,
        "description": "Oilseed legume requiring loose, sandy loam soil to facilitate easy gynophore (peg) penetration.",
        "guideline": "Gypsum application (200 kg/acre) at 45 DAS to supply Calcium and Sulfur for pod filling."
    },
    {
        "crop": "Soybean",
        "ideal_n": 30, "ideal_p": 60, "ideal_k": 40,
        "temp_min": 20, "temp_max": 32, "humidity_min": 60, "humidity_max": 80,
        "ph_min": 6.0, "ph_max": 7.5, "rainfall_min": 600, "rainfall_max": 1000,
        "duration_days": 95, "avg_yield_kg_per_acre": 1050,
        "description": "Protein- and oil-rich leguminous crop excelling in central and black soil regions.",
        "guideline": "Rhizobium japonicum seed treatment. Maintain phosphorus balance for root nodulation."
    }
]

class AgronomicMLEngine:
    @staticmethod
    def calculate_compatibility_score(req: CropRecommendationRequest, crop: Dict[str, Any]) -> float:
        """Calculates distance-weighted compatibility score between field parameters and crop requirements"""
        scores = []
        
        # 1. Temperature match (Gaussian distance)
        temp_mid = (crop["temp_min"] + crop["temp_max"]) / 2.0
        temp_range = (crop["temp_max"] - crop["temp_min"]) / 2.0
        temp_diff = abs(req.temperature - temp_mid)
        temp_score = max(0.0, 1.0 - (temp_diff / (temp_range * 1.5)))
        scores.append(temp_score * 0.20)
        
        # 2. Humidity match
        hum_mid = (crop["humidity_min"] + crop["humidity_max"]) / 2.0
        hum_range = (crop["humidity_max"] - crop["humidity_min"]) / 2.0
        hum_diff = abs(req.humidity - hum_mid)
        hum_score = max(0.0, 1.0 - (hum_diff / (hum_range * 1.5)))
        scores.append(hum_score * 0.15)
        
        # 3. Soil pH match
        ph_mid = (crop["ph_min"] + crop["ph_max"]) / 2.0
        ph_range = (crop["ph_max"] - crop["ph_min"]) / 2.0
        ph_diff = abs(req.ph - ph_mid)
        ph_score = max(0.0, 1.0 - (ph_diff / (ph_range * 1.6)))
        scores.append(ph_score * 0.20)
        
        # 4. Rainfall match
        rf_mid = (crop["rainfall_min"] + crop["rainfall_max"]) / 2.0
        rf_range = (crop["rainfall_max"] - crop["rainfall_min"]) / 2.0
        rf_diff = abs(req.rainfall - rf_mid)
        rf_score = max(0.0, 1.0 - (rf_diff / (rf_range * 2.0)))
        scores.append(rf_score * 0.20)
        
        # 5. Soil Nutrients (NPK) match
        n_ratio = min(1.0, req.nitrogen / max(1.0, crop["ideal_n"]))
        p_ratio = min(1.0, req.phosphorus / max(1.0, crop["ideal_p"]))
        k_ratio = min(1.0, req.potassium / max(1.0, crop["ideal_k"]))
        npk_score = (n_ratio * 0.4 + p_ratio * 0.3 + k_ratio * 0.3)
        scores.append(npk_score * 0.25)
        
        total_score = sum(scores) * 100.0
        return round(min(98.5, max(15.0, total_score)), 1)

    @classmethod
    def recommend_crops(cls, req: CropRecommendationRequest) -> CropRecommendationResponse:
        matches = []
        for crop_data in CROP_DATABASE:
            score = cls.calculate_compatibility_score(req, crop_data)
            matches.append({
                "crop": crop_data["crop"],
                "score": score,
                "data": crop_data
            })
            
        # Sort by highest match
        matches.sort(key=lambda x: x["score"], reverse=True)
        top_matches = matches[:4]
        
        # Determine soil fertility index and limiting nutrients
        limiting = []
        if req.nitrogen < 50:
            limiting.append("Nitrogen (Low)")
        if req.phosphorus < 25:
            limiting.append("Phosphorus (Low)")
        if req.potassium < 35:
            limiting.append("Potassium (Low)")
        if req.ph < 6.0:
            limiting.append("Acidic Soil (Low pH)")
        elif req.ph > 7.8:
            limiting.append("Alkaline Soil (High pH)")
            
        fertility_index = round((min(120, req.nitrogen)/120 * 35) + (min(60, req.phosphorus)/60 * 35) + (min(80, req.potassium)/80 * 30), 1)
        
        if fertility_index >= 75:
            grade = "A (High Fertility & Nutrient Rich)"
        elif fertility_index >= 50:
            grade = "B (Moderate Fertility - Balanced)"
        else:
            grade = "C (Low Fertility - Requires Nutrient Amendment)"

        result_crops = []
        for m in top_matches:
            cd = m["data"]
            result_crops.append(CropMatch(
                crop=cd["crop"],
                confidence_score=m["score"],
                description=cd["description"],
                ideal_conditions={
                    "ideal_n_p_k": f"{cd['ideal_n']}:{cd['ideal_p']}:{cd['ideal_k']}",
                    "optimum_temp": f"{cd['temp_min']}°C - {cd['temp_max']}°C",
                    "optimum_ph": f"{cd['ph_min']} - {cd['ph_max']}",
                    "rainfall_range": f"{cd['rainfall_min']} - {cd['rainfall_max']} mm"
                },
                growing_duration_days=cd["duration_days"],
                estimated_yield_per_acre_kg=cd["avg_yield_kg_per_acre"],
                fertilizer_guideline=cd["guideline"]
            ))
            
        return CropRecommendationResponse(
            recommended_crops=result_crops,
            soil_fertility_index=fertility_index,
            soil_health_grade=grade,
            limiting_nutrients=limiting if limiting else ["None (Balanced Nutrient State)"]
        )

    @classmethod
    def calculate_fertilizer_schedule(cls, req: FertilizerCalculationRequest) -> FertilizerCalculationResponse:
        # Find crop profile
        crop_info = next((c for c in CROP_DATABASE if c["crop"].lower().startswith(req.crop_name.lower()[:4])), CROP_DATABASE[0])
        
        area = max(0.1, req.field_area_acres)
        target_n = crop_info["ideal_n"] * area
        target_p = crop_info["ideal_p"] * area
        target_k = crop_info["ideal_k"] * area
        
        curr_n = req.current_n * area
        curr_p = req.current_p * area
        curr_k = req.current_k * area
        
        deficit_n = max(0.0, target_n - curr_n)
        deficit_p = max(0.0, target_p - curr_p)
        deficit_k = max(0.0, target_k - curr_k)
        
        # Fertilizer Conversions:
        # DAP (18% N, 46% P2O5)
        dap_needed = (deficit_p / 0.46) if deficit_p > 0 else 0.0
        n_from_dap = dap_needed * 0.18
        
        # Remaining N from Urea (46% N)
        remaining_n = max(0.0, deficit_n - n_from_dap)
        urea_needed = remaining_n / 0.46
        
        # MOP / Muriate of Potash (60% K2O)
        mop_needed = (deficit_k / 0.60) if deficit_k > 0 else 0.0
        
        # Organic Manure (FYM)
        fym_needed = 2000.0 * area # 2 Tonnes per acre base
        
        # Generate multi-stage application schedule
        schedule = [
            FertilizerSchedule(
                stage_name="Basal Application (Land Preparation / Sowing)",
                days_after_sowing=0,
                urea_kg=round(urea_needed * 0.30, 1),
                dap_kg=round(dap_needed, 1), # Full DAP applied at basal
                mop_kg=round(mop_needed * 0.50, 1),
                organic_compost_kg=round(fym_needed, 1),
                instructions="Incorporate thoroughly into soil during final plowing before sowing/transplanting."
            ),
            FertilizerSchedule(
                stage_name="Vegetative / Tillering Stage",
                days_after_sowing=int(crop_info["duration_days"] * 0.25),
                urea_kg=round(urea_needed * 0.40, 1),
                dap_kg=0.0,
                mop_kg=0.0,
                organic_compost_kg=0.0,
                instructions="Top-dress urea along crop rows followed by light irrigation. Avoid wetting foliage."
            ),
            FertilizerSchedule(
                stage_name="Flowering / Panicle / Fruit Initiation",
                days_after_sowing=int(crop_info["duration_days"] * 0.55),
                urea_kg=round(urea_needed * 0.30, 1),
                dap_kg=0.0,
                mop_kg=round(mop_needed * 0.50, 1),
                organic_compost_kg=0.0,
                instructions="Apply remaining Nitrogen and Potassium to enhance grain filling and fruit size."
            )
        ]
        
        return FertilizerCalculationResponse(
            crop_name=crop_info["crop"],
            field_area_acres=area,
            total_urea_needed_kg=round(urea_needed, 1),
            total_dap_needed_kg=round(dap_needed, 1),
            total_mop_needed_kg=round(mop_needed, 1),
            total_organic_manure_kg=round(fym_needed, 1),
            npk_deficit={
                "nitrogen_kg": round(deficit_n, 1),
                "phosphorus_kg": round(deficit_p, 1),
                "potassium_kg": round(deficit_k, 1)
            },
            application_schedule=schedule,
            organic_alternatives=[
                "Vermicompost (1.5 tons/acre) enriched with Trichoderma viride",
                "Neem Cake (100 kg/acre) as natural nitrification inhibitor and pest deterrent",
                "Biofertilizers: Azotobacter / Azospirillum (for N fixation) and PSB (Phosphate Solubilizing Bacteria)",
                "Jeevamrutha / Panchagavya foliar application at 15-day intervals"
            ]
        )
