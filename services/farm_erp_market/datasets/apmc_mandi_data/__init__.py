"""Mandi Registry Subpackage"""
from typing import Dict, Any, List
from . import mandi_zone_01
from . import mandi_zone_02
from . import mandi_zone_03
from . import mandi_zone_04
from . import mandi_zone_05
from . import mandi_zone_06
from . import mandi_zone_07
from . import mandi_zone_08
from . import mandi_zone_09
from . import mandi_zone_10

NATIONAL_APMC_MANDI_REGISTRY: List[Dict[str, Any]] = []
NATIONAL_APMC_MANDI_REGISTRY.extend(mandi_zone_01.MANDIS_MANDI_ZONE_01)
NATIONAL_APMC_MANDI_REGISTRY.extend(mandi_zone_02.MANDIS_MANDI_ZONE_02)
NATIONAL_APMC_MANDI_REGISTRY.extend(mandi_zone_03.MANDIS_MANDI_ZONE_03)
NATIONAL_APMC_MANDI_REGISTRY.extend(mandi_zone_04.MANDIS_MANDI_ZONE_04)
NATIONAL_APMC_MANDI_REGISTRY.extend(mandi_zone_05.MANDIS_MANDI_ZONE_05)
NATIONAL_APMC_MANDI_REGISTRY.extend(mandi_zone_06.MANDIS_MANDI_ZONE_06)
NATIONAL_APMC_MANDI_REGISTRY.extend(mandi_zone_07.MANDIS_MANDI_ZONE_07)
NATIONAL_APMC_MANDI_REGISTRY.extend(mandi_zone_08.MANDIS_MANDI_ZONE_08)
NATIONAL_APMC_MANDI_REGISTRY.extend(mandi_zone_09.MANDIS_MANDI_ZONE_09)
NATIONAL_APMC_MANDI_REGISTRY.extend(mandi_zone_10.MANDIS_MANDI_ZONE_10)
