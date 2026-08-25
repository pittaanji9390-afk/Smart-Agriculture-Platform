"""Crop Encyclopedia Subpackage"""
from typing import Dict, Any, List
from . import crop_batch_01
from . import crop_batch_02
from . import crop_batch_03
from . import crop_batch_04
from . import crop_batch_05
from . import crop_batch_06
from . import crop_batch_07
from . import crop_batch_08
from . import crop_batch_09
from . import crop_batch_10

COMPREHENSIVE_CROP_ENCYCLOPEDIA: List[Dict[str, Any]] = []
COMPREHENSIVE_CROP_ENCYCLOPEDIA.extend(crop_batch_01.CROPS_CROP_BATCH_01)
COMPREHENSIVE_CROP_ENCYCLOPEDIA.extend(crop_batch_02.CROPS_CROP_BATCH_02)
COMPREHENSIVE_CROP_ENCYCLOPEDIA.extend(crop_batch_03.CROPS_CROP_BATCH_03)
COMPREHENSIVE_CROP_ENCYCLOPEDIA.extend(crop_batch_04.CROPS_CROP_BATCH_04)
COMPREHENSIVE_CROP_ENCYCLOPEDIA.extend(crop_batch_05.CROPS_CROP_BATCH_05)
COMPREHENSIVE_CROP_ENCYCLOPEDIA.extend(crop_batch_06.CROPS_CROP_BATCH_06)
COMPREHENSIVE_CROP_ENCYCLOPEDIA.extend(crop_batch_07.CROPS_CROP_BATCH_07)
COMPREHENSIVE_CROP_ENCYCLOPEDIA.extend(crop_batch_08.CROPS_CROP_BATCH_08)
COMPREHENSIVE_CROP_ENCYCLOPEDIA.extend(crop_batch_09.CROPS_CROP_BATCH_09)
COMPREHENSIVE_CROP_ENCYCLOPEDIA.extend(crop_batch_10.CROPS_CROP_BATCH_10)
