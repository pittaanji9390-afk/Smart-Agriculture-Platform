"""Gene Bank Subpackage"""
from typing import Dict, Any, List
from . import gene_batch_01
from . import gene_batch_02
from . import gene_batch_03
from . import gene_batch_04
from . import gene_batch_05
from . import gene_batch_06
from . import gene_batch_07
from . import gene_batch_08
from . import gene_batch_09
from . import gene_batch_10

NATIONAL_CROP_GENE_BANK_REGISTRY: List[Dict[str, Any]] = []
NATIONAL_CROP_GENE_BANK_REGISTRY.extend(gene_batch_01.GENES_GENE_BATCH_01)
NATIONAL_CROP_GENE_BANK_REGISTRY.extend(gene_batch_02.GENES_GENE_BATCH_02)
NATIONAL_CROP_GENE_BANK_REGISTRY.extend(gene_batch_03.GENES_GENE_BATCH_03)
NATIONAL_CROP_GENE_BANK_REGISTRY.extend(gene_batch_04.GENES_GENE_BATCH_04)
NATIONAL_CROP_GENE_BANK_REGISTRY.extend(gene_batch_05.GENES_GENE_BATCH_05)
NATIONAL_CROP_GENE_BANK_REGISTRY.extend(gene_batch_06.GENES_GENE_BATCH_06)
NATIONAL_CROP_GENE_BANK_REGISTRY.extend(gene_batch_07.GENES_GENE_BATCH_07)
NATIONAL_CROP_GENE_BANK_REGISTRY.extend(gene_batch_08.GENES_GENE_BATCH_08)
NATIONAL_CROP_GENE_BANK_REGISTRY.extend(gene_batch_09.GENES_GENE_BATCH_09)
NATIONAL_CROP_GENE_BANK_REGISTRY.extend(gene_batch_10.GENES_GENE_BATCH_10)
