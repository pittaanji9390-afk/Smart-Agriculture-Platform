"""Commodity Grades Subpackage"""
from typing import Dict, Any, List
from . import grade_batch_01
from . import grade_batch_02
from . import grade_batch_03
from . import grade_batch_04
from . import grade_batch_05
from . import grade_batch_06
from . import grade_batch_07
from . import grade_batch_08
from . import grade_batch_09
from . import grade_batch_10

NATIONAL_COMMODITY_GRADE_STANDARDS: List[Dict[str, Any]] = []
NATIONAL_COMMODITY_GRADE_STANDARDS.extend(grade_batch_01.GRADES_GRADE_BATCH_01)
NATIONAL_COMMODITY_GRADE_STANDARDS.extend(grade_batch_02.GRADES_GRADE_BATCH_02)
NATIONAL_COMMODITY_GRADE_STANDARDS.extend(grade_batch_03.GRADES_GRADE_BATCH_03)
NATIONAL_COMMODITY_GRADE_STANDARDS.extend(grade_batch_04.GRADES_GRADE_BATCH_04)
NATIONAL_COMMODITY_GRADE_STANDARDS.extend(grade_batch_05.GRADES_GRADE_BATCH_05)
NATIONAL_COMMODITY_GRADE_STANDARDS.extend(grade_batch_06.GRADES_GRADE_BATCH_06)
NATIONAL_COMMODITY_GRADE_STANDARDS.extend(grade_batch_07.GRADES_GRADE_BATCH_07)
NATIONAL_COMMODITY_GRADE_STANDARDS.extend(grade_batch_08.GRADES_GRADE_BATCH_08)
NATIONAL_COMMODITY_GRADE_STANDARDS.extend(grade_batch_09.GRADES_GRADE_BATCH_09)
NATIONAL_COMMODITY_GRADE_STANDARDS.extend(grade_batch_10.GRADES_GRADE_BATCH_10)
