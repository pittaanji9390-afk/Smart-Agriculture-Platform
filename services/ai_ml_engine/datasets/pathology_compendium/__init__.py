"""Pathology Compendium Subpackage"""
from typing import Dict, Any, List
from . import pathology_batch_01
from . import pathology_batch_02
from . import pathology_batch_03
from . import pathology_batch_04
from . import pathology_batch_05
from . import pathology_batch_06
from . import pathology_batch_07
from . import pathology_batch_08

PLANT_PATHOLOGY_COMPENDIUM: List[Dict[str, Any]] = []
PLANT_PATHOLOGY_COMPENDIUM.extend(pathology_batch_01.PATHOLOGY_PATHOLOGY_BATCH_01)
PLANT_PATHOLOGY_COMPENDIUM.extend(pathology_batch_02.PATHOLOGY_PATHOLOGY_BATCH_02)
PLANT_PATHOLOGY_COMPENDIUM.extend(pathology_batch_03.PATHOLOGY_PATHOLOGY_BATCH_03)
PLANT_PATHOLOGY_COMPENDIUM.extend(pathology_batch_04.PATHOLOGY_PATHOLOGY_BATCH_04)
PLANT_PATHOLOGY_COMPENDIUM.extend(pathology_batch_05.PATHOLOGY_PATHOLOGY_BATCH_05)
PLANT_PATHOLOGY_COMPENDIUM.extend(pathology_batch_06.PATHOLOGY_PATHOLOGY_BATCH_06)
PLANT_PATHOLOGY_COMPENDIUM.extend(pathology_batch_07.PATHOLOGY_PATHOLOGY_BATCH_07)
PLANT_PATHOLOGY_COMPENDIUM.extend(pathology_batch_08.PATHOLOGY_PATHOLOGY_BATCH_08)
