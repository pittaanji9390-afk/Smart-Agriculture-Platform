"""
National District-Level Soil Agronomic Database
Modularized across regional soil submodules.
"""
from typing import Dict, Any
from .soil_data import NATIONAL_DISTRICT_SOIL_REGISTRY

class NationalSoilDatabaseEngine:
    @classmethod
    def get_district_soil_profile(cls, district: str, state: str = None) -> Dict[str, Any]:
        for k, v in NATIONAL_DISTRICT_SOIL_REGISTRY.items():
            if v["district"].lower() == district.lower():
                if state is None or v["state"].lower() == state.lower():
                    return v
        return list(NATIONAL_DISTRICT_SOIL_REGISTRY.values())[0]
