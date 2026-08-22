"""
BBCH Phenological Growth Stage Scale Engine & Growing Degree Day (GDD) Accumulator
Tracks standard BBCH stages (00-99) for precision fertilization, pesticide spray windows, and irrigation scheduling.
"""

from typing import Dict, Any, List
from datetime import datetime, date

class BBCHPhenologyTracker:
    """
    Standard Principal BBCH Growth Stages:
    Stage 0: Germination / Sprouting (00-09)
    Stage 1: Leaf Development (10-19)
    Stage 2: Tillering / Side Shoot Formation (20-29)
    Stage 3: Stem Elongation / Rosette Growth (30-39)
    Stage 4: Booting / Development of Harvestable Vegetative Parts (40-49)
    Stage 5: Inflorescence Emergence / Heading (50-59)
    Stage 6: Flowering / Anthesis (60-69)
    Stage 7: Fruit / Grain Development (70-79)
    Stage 8: Ripening / Maturation of Fruit & Seed (80-89)
    Stage 9: Senescence & Dormancy (90-99)
    """

    CROP_BASE_TEMPERATURES = {
        "Rice (Paddy)": 10.0,
        "Wheat": 4.5,
        "Maize (Corn)": 10.0,
        "Cotton": 15.0,
        "Tomato": 10.0,
        "Potato": 7.0,
        "Soybean": 10.0,
        "Chickpea": 8.0
    }

    CROP_GDD_REQUIREMENTS = {
        "Rice (Paddy)": {"vegetative": 850, "flowering": 1400, "maturity": 2100},
        "Wheat": {"vegetative": 600, "flowering": 1100, "maturity": 1750},
        "Maize (Corn)": {"vegetative": 750, "flowering": 1300, "maturity": 1950},
        "Cotton": {"vegetative": 900, "flowering": 1600, "maturity": 2400},
        "Tomato": {"vegetative": 550, "flowering": 1050, "maturity": 1600}
    }

    @classmethod
    def calculate_daily_gdd(cls, crop: str, t_max: float, t_min: float) -> float:
        """Calculates single-day thermal accumulation (GDD) with crop baseline cutoff"""
        t_base = cls.CROP_BASE_TEMPERATURES.get(crop, 10.0)
        t_mean = (t_max + t_min) / 2.0
        return max(0.0, t_mean - t_base)

    @classmethod
    def determine_bbch_stage(cls, crop: str, accumulated_gdd: float) -> Dict[str, Any]:
        targets = cls.CROP_GDD_REQUIREMENTS.get(crop, cls.CROP_GDD_REQUIREMENTS["Tomato"])
        
        if accumulated_gdd < targets["vegetative"] * 0.3:
            code = 12
            name = "Leaf Development (2-4 true leaves unfolded)"
            action = "Basal fertilizer application and weed management window"
        elif accumulated_gdd < targets["vegetative"]:
            code = 25
            name = "Active Tillering / Vegetative Canopy Closure"
            action = "First top-dressing of Nitrogen (Urea) + ensure adequate root moisture"
        elif accumulated_gdd < targets["flowering"] * 0.8:
            code = 37
            name = "Stem Elongation / Flag Leaf Just Visible"
            action = "Critical irrigation timing; scout for foliar blights/rusts"
        elif accumulated_gdd < targets["flowering"]:
            code = 55
            name = "Inflorescence Emergence / Heading Stage"
            action = "Apply Potassium and micronutrient foliar spray (Boron/Zinc)"
        elif accumulated_gdd < targets["maturity"] * 0.8:
            code = 65
            name = "Full Flowering / Anthesis Stage"
            action = "Avoid broad-spectrum chemical sprays during pollinator activity"
        elif accumulated_gdd < targets["maturity"]:
            code = 75
            name = "Milk-Dough / Fruit Sizing Stage"
            action = "Maintain uniform soil moisture; protect against fruit borers"
        else:
            code = 89
            name = "Physiological Maturity / Harvest Readiness"
            action = "Cease irrigation 7-10 days prior to harvest for uniform drying"

        pct_complete = min(100.0, round((accumulated_gdd / targets["maturity"]) * 100.0, 1))

        return {
            "bbch_code": code,
            "stage_name": name,
            "accumulated_gdd": round(accumulated_gdd, 1),
            "target_maturity_gdd": targets["maturity"],
            "progress_pct": pct_complete,
            "recommended_agronomic_action": action
        }
