"""Soil Data Subpackage Aggregator"""
from typing import Dict, Any
from . import andhra_pradesh
from . import telangana
from . import karnataka
from . import tamil_nadu
from . import maharashtra
from . import gujarat
from . import punjab
from . import haryana
from . import rajasthan
from . import madhya_pradesh_1
from . import madhya_pradesh_2
from . import uttar_pradesh_1
from . import uttar_pradesh_2
from . import bihar
from . import west_bengal
from . import odisha

NATIONAL_DISTRICT_SOIL_REGISTRY: Dict[str, Dict[str, Any]] = {}
NATIONAL_DISTRICT_SOIL_REGISTRY.update(andhra_pradesh.SOIL_DATA_ANDHRA_PRADESH)
NATIONAL_DISTRICT_SOIL_REGISTRY.update(telangana.SOIL_DATA_TELANGANA)
NATIONAL_DISTRICT_SOIL_REGISTRY.update(karnataka.SOIL_DATA_KARNATAKA)
NATIONAL_DISTRICT_SOIL_REGISTRY.update(tamil_nadu.SOIL_DATA_TAMIL_NADU)
NATIONAL_DISTRICT_SOIL_REGISTRY.update(maharashtra.SOIL_DATA_MAHARASHTRA)
NATIONAL_DISTRICT_SOIL_REGISTRY.update(gujarat.SOIL_DATA_GUJARAT)
NATIONAL_DISTRICT_SOIL_REGISTRY.update(punjab.SOIL_DATA_PUNJAB)
NATIONAL_DISTRICT_SOIL_REGISTRY.update(haryana.SOIL_DATA_HARYANA)
NATIONAL_DISTRICT_SOIL_REGISTRY.update(rajasthan.SOIL_DATA_RAJASTHAN)
NATIONAL_DISTRICT_SOIL_REGISTRY.update(madhya_pradesh_1.SOIL_DATA_MADHYA_PRADESH_1)
NATIONAL_DISTRICT_SOIL_REGISTRY.update(madhya_pradesh_2.SOIL_DATA_MADHYA_PRADESH_2)
NATIONAL_DISTRICT_SOIL_REGISTRY.update(uttar_pradesh_1.SOIL_DATA_UTTAR_PRADESH_1)
NATIONAL_DISTRICT_SOIL_REGISTRY.update(uttar_pradesh_2.SOIL_DATA_UTTAR_PRADESH_2)
NATIONAL_DISTRICT_SOIL_REGISTRY.update(bihar.SOIL_DATA_BIHAR)
NATIONAL_DISTRICT_SOIL_REGISTRY.update(west_bengal.SOIL_DATA_WEST_BENGAL)
NATIONAL_DISTRICT_SOIL_REGISTRY.update(odisha.SOIL_DATA_ODISHA)
