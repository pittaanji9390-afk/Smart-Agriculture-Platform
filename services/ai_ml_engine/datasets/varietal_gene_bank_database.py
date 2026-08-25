"""
National Varietal Gene Bank, Genetic Markers & Crop Breeding Traits Registry
"""
from typing import Dict, Any, List

NATIONAL_CROP_GENE_BANK_REGISTRY: List[Dict[str, Any]] = [
    {
        "gene_accession_id": "GENE-ENTRY-0001",
        "variety_name": "Rice Swarna Sub1 Genotype Line v1",
        "target_trait": "Submergence / Flash Flood Tolerance",
        "major_qtl_markers": "Sub1A Transcription Factor",
        "agronomic_description": "Direct seeded or transplanted lowland rice with 14-day complete water submergence survival",
        "developing_institution": "Central Rice Research Institute (CRRI)",
        "genetic_purity_score": 99.20,
        "heritability_broad_sense": 0.78,
        "drought_susceptibility_index": 0.62,
        "harvest_index_pct": 42.0,
        "recommended_agro_climatic_zones": [
            "Zone 1: Indo-Gangetic Plains & Central Plateau",
            "Zone 2: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0002",
        "variety_name": "Rice CR Dhan 801 Genotype Line v1",
        "target_trait": "Drought + Submergence Dual Tolerance",
        "major_qtl_markers": "qDTY1.1, qDTY2.1, Sub1A",
        "agronomic_description": "Climate-resilient dual tolerant line for rainfed drought-prone and flood-prone ecologies",
        "developing_institution": "ICAR-NRRI",
        "genetic_purity_score": 99.30,
        "heritability_broad_sense": 0.79,
        "drought_susceptibility_index": 0.64,
        "harvest_index_pct": 42.8,
        "recommended_agro_climatic_zones": [
            "Zone 2: Indo-Gangetic Plains & Central Plateau",
            "Zone 3: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0003",
        "variety_name": "Wheat DBW 303 (Karan Vaishnavi) Genotype Line v1",
        "target_trait": "Terminal Heat Stress Resistance",
        "major_qtl_markers": "TaHsfA2d, TaFER-5B",
        "agronomic_description": "High-yielding irrigated timely sown bread wheat with extreme heat resilience during grain filling",
        "developing_institution": "ICAR-IIWBR",
        "genetic_purity_score": 99.40,
        "heritability_broad_sense": 0.80,
        "drought_susceptibility_index": 0.66,
        "harvest_index_pct": 43.6,
        "recommended_agro_climatic_zones": [
            "Zone 3: Indo-Gangetic Plains & Central Plateau",
            "Zone 4: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0004",
        "variety_name": "Wheat HD 3226 (Pusa Yashasvi) Genotype Line v1",
        "target_trait": "Multi-Rust Resistance (Yellow, Brown, Black)",
        "major_qtl_markers": "Yr17, Lr37, Sr38",
        "agronomic_description": "Superior chapati-making and biscuit-making quality with high gluten strength",
        "developing_institution": "ICAR-IARI",
        "genetic_purity_score": 99.50,
        "heritability_broad_sense": 0.81,
        "drought_susceptibility_index": 0.68,
        "harvest_index_pct": 44.4,
        "recommended_agro_climatic_zones": [
            "Zone 4: Indo-Gangetic Plains & Central Plateau",
            "Zone 5: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0005",
        "variety_name": "Chickpea Pusa 10216 Genotype Line v1",
        "target_trait": "Drought Drought Tolerance & Root Architecture",
        "major_qtl_markers": "qRT9.1, QTL-hotspot genomic region",
        "agronomic_description": "Desi chickpea with deep taproot system and high water use efficiency under dryland",
        "developing_institution": "ICAR-IARI",
        "genetic_purity_score": 99.60,
        "heritability_broad_sense": 0.82,
        "drought_susceptibility_index": 0.70,
        "harvest_index_pct": 45.2,
        "recommended_agro_climatic_zones": [
            "Zone 5: Indo-Gangetic Plains & Central Plateau",
            "Zone 6: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0006",
        "variety_name": "Pigeonpea BDN 711 Genotype Line v1",
        "target_trait": "Fusarium Wilt & Sterility Mosaic Tolerance",
        "major_qtl_markers": "Cc-RFLP-Wilt1",
        "agronomic_description": "White seeded medium duration variety highly adapted to rainfed black cotton vertisols",
        "developing_institution": "VNMKV",
        "genetic_purity_score": 99.70,
        "heritability_broad_sense": 0.83,
        "drought_susceptibility_index": 0.72,
        "harvest_index_pct": 46.0,
        "recommended_agro_climatic_zones": [
            "Zone 6: Indo-Gangetic Plains & Central Plateau",
            "Zone 7: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0007",
        "variety_name": "Mustard PM 28 Genotype Line v1",
        "target_trait": "High Oleic / Low Glucosinolate Double Zero Quality",
        "major_qtl_markers": "FAD2 mutation, GSL1 deletion",
        "agronomic_description": "Canola quality Brassica juncea with heart-healthy fatty acid profile",
        "developing_institution": "ICAR-DRMR",
        "genetic_purity_score": 99.80,
        "heritability_broad_sense": 0.84,
        "drought_susceptibility_index": 0.74,
        "harvest_index_pct": 46.8,
        "recommended_agro_climatic_zones": [
            "Zone 7: Indo-Gangetic Plains & Central Plateau",
            "Zone 8: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0008",
        "variety_name": "Cotton Bunny Bt (NCS 145) Genotype Line v1",
        "target_trait": "Bollworm Resistance & Sucking Pest Tolerance",
        "major_qtl_markers": "Cry1Ac + Cry2Ab (Bollgard II)",
        "agronomic_description": "High boll retention, exceptional ginning outturn (36%), and staple length (31mm)",
        "developing_institution": "Nuziveedu Seeds",
        "genetic_purity_score": 99.90,
        "heritability_broad_sense": 0.85,
        "drought_susceptibility_index": 0.76,
        "harvest_index_pct": 47.6,
        "recommended_agro_climatic_zones": [
            "Zone 8: Indo-Gangetic Plains & Central Plateau",
            "Zone 9: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0009",
        "variety_name": "Tomato Arka Rakshak (F1 Hybrid) Genotype Line v1",
        "target_trait": "Triple Disease Resistance (ToLCV, BW, EB)",
        "major_qtl_markers": "Ty-2, Ty-3, Bwr-12, Ph-3",
        "agronomic_description": "High yielding indeterminate tomato with resistance to leaf curl virus, bacterial wilt, and early blight",
        "developing_institution": "ICAR-IIHR",
        "genetic_purity_score": 99.20,
        "heritability_broad_sense": 0.86,
        "drought_susceptibility_index": 0.78,
        "harvest_index_pct": 48.4,
        "recommended_agro_climatic_zones": [
            "Zone 9: Indo-Gangetic Plains & Central Plateau",
            "Zone 10: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0010",
        "variety_name": "Chilli Arka Harita Genotype Line v1",
        "target_trait": "Powdery Mildew & Anthracnose Tolerance",
        "major_qtl_markers": "Pm-1, Colletotrichum-R1",
        "agronomic_description": "High pungency (0.45% capsaicin) dual-purpose hybrid for green and dry red chilli export",
        "developing_institution": "ICAR-IIHR",
        "genetic_purity_score": 99.30,
        "heritability_broad_sense": 0.87,
        "drought_susceptibility_index": 0.80,
        "harvest_index_pct": 49.2,
        "recommended_agro_climatic_zones": [
            "Zone 10: Indo-Gangetic Plains & Central Plateau",
            "Zone 11: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0011",
        "variety_name": "Rice Swarna Sub1 Genotype Line v2",
        "target_trait": "Submergence / Flash Flood Tolerance",
        "major_qtl_markers": "Sub1A Transcription Factor",
        "agronomic_description": "Direct seeded or transplanted lowland rice with 14-day complete water submergence survival",
        "developing_institution": "Central Rice Research Institute (CRRI)",
        "genetic_purity_score": 99.40,
        "heritability_broad_sense": 0.88,
        "drought_susceptibility_index": 0.82,
        "harvest_index_pct": 42.0,
        "recommended_agro_climatic_zones": [
            "Zone 11: Indo-Gangetic Plains & Central Plateau",
            "Zone 12: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0012",
        "variety_name": "Rice CR Dhan 801 Genotype Line v2",
        "target_trait": "Drought + Submergence Dual Tolerance",
        "major_qtl_markers": "qDTY1.1, qDTY2.1, Sub1A",
        "agronomic_description": "Climate-resilient dual tolerant line for rainfed drought-prone and flood-prone ecologies",
        "developing_institution": "ICAR-NRRI",
        "genetic_purity_score": 99.50,
        "heritability_broad_sense": 0.89,
        "drought_susceptibility_index": 0.84,
        "harvest_index_pct": 42.8,
        "recommended_agro_climatic_zones": [
            "Zone 12: Indo-Gangetic Plains & Central Plateau",
            "Zone 13: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0013",
        "variety_name": "Wheat DBW 303 (Karan Vaishnavi) Genotype Line v2",
        "target_trait": "Terminal Heat Stress Resistance",
        "major_qtl_markers": "TaHsfA2d, TaFER-5B",
        "agronomic_description": "High-yielding irrigated timely sown bread wheat with extreme heat resilience during grain filling",
        "developing_institution": "ICAR-IIWBR",
        "genetic_purity_score": 99.60,
        "heritability_broad_sense": 0.90,
        "drought_susceptibility_index": 0.62,
        "harvest_index_pct": 43.6,
        "recommended_agro_climatic_zones": [
            "Zone 13: Indo-Gangetic Plains & Central Plateau",
            "Zone 14: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0014",
        "variety_name": "Wheat HD 3226 (Pusa Yashasvi) Genotype Line v2",
        "target_trait": "Multi-Rust Resistance (Yellow, Brown, Black)",
        "major_qtl_markers": "Yr17, Lr37, Sr38",
        "agronomic_description": "Superior chapati-making and biscuit-making quality with high gluten strength",
        "developing_institution": "ICAR-IARI",
        "genetic_purity_score": 99.70,
        "heritability_broad_sense": 0.91,
        "drought_susceptibility_index": 0.64,
        "harvest_index_pct": 44.4,
        "recommended_agro_climatic_zones": [
            "Zone 14: Indo-Gangetic Plains & Central Plateau",
            "Zone 15: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0015",
        "variety_name": "Chickpea Pusa 10216 Genotype Line v2",
        "target_trait": "Drought Drought Tolerance & Root Architecture",
        "major_qtl_markers": "qRT9.1, QTL-hotspot genomic region",
        "agronomic_description": "Desi chickpea with deep taproot system and high water use efficiency under dryland",
        "developing_institution": "ICAR-IARI",
        "genetic_purity_score": 99.80,
        "heritability_broad_sense": 0.92,
        "drought_susceptibility_index": 0.66,
        "harvest_index_pct": 45.2,
        "recommended_agro_climatic_zones": [
            "Zone 15: Indo-Gangetic Plains & Central Plateau",
            "Zone 1: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0016",
        "variety_name": "Pigeonpea BDN 711 Genotype Line v2",
        "target_trait": "Fusarium Wilt & Sterility Mosaic Tolerance",
        "major_qtl_markers": "Cc-RFLP-Wilt1",
        "agronomic_description": "White seeded medium duration variety highly adapted to rainfed black cotton vertisols",
        "developing_institution": "VNMKV",
        "genetic_purity_score": 99.90,
        "heritability_broad_sense": 0.93,
        "drought_susceptibility_index": 0.68,
        "harvest_index_pct": 46.0,
        "recommended_agro_climatic_zones": [
            "Zone 1: Indo-Gangetic Plains & Central Plateau",
            "Zone 2: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0017",
        "variety_name": "Mustard PM 28 Genotype Line v2",
        "target_trait": "High Oleic / Low Glucosinolate Double Zero Quality",
        "major_qtl_markers": "FAD2 mutation, GSL1 deletion",
        "agronomic_description": "Canola quality Brassica juncea with heart-healthy fatty acid profile",
        "developing_institution": "ICAR-DRMR",
        "genetic_purity_score": 99.20,
        "heritability_broad_sense": 0.94,
        "drought_susceptibility_index": 0.70,
        "harvest_index_pct": 46.8,
        "recommended_agro_climatic_zones": [
            "Zone 2: Indo-Gangetic Plains & Central Plateau",
            "Zone 3: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0018",
        "variety_name": "Cotton Bunny Bt (NCS 145) Genotype Line v2",
        "target_trait": "Bollworm Resistance & Sucking Pest Tolerance",
        "major_qtl_markers": "Cry1Ac + Cry2Ab (Bollgard II)",
        "agronomic_description": "High boll retention, exceptional ginning outturn (36%), and staple length (31mm)",
        "developing_institution": "Nuziveedu Seeds",
        "genetic_purity_score": 99.30,
        "heritability_broad_sense": 0.95,
        "drought_susceptibility_index": 0.72,
        "harvest_index_pct": 47.6,
        "recommended_agro_climatic_zones": [
            "Zone 3: Indo-Gangetic Plains & Central Plateau",
            "Zone 4: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0019",
        "variety_name": "Tomato Arka Rakshak (F1 Hybrid) Genotype Line v2",
        "target_trait": "Triple Disease Resistance (ToLCV, BW, EB)",
        "major_qtl_markers": "Ty-2, Ty-3, Bwr-12, Ph-3",
        "agronomic_description": "High yielding indeterminate tomato with resistance to leaf curl virus, bacterial wilt, and early blight",
        "developing_institution": "ICAR-IIHR",
        "genetic_purity_score": 99.40,
        "heritability_broad_sense": 0.78,
        "drought_susceptibility_index": 0.74,
        "harvest_index_pct": 48.4,
        "recommended_agro_climatic_zones": [
            "Zone 4: Indo-Gangetic Plains & Central Plateau",
            "Zone 5: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0020",
        "variety_name": "Chilli Arka Harita Genotype Line v2",
        "target_trait": "Powdery Mildew & Anthracnose Tolerance",
        "major_qtl_markers": "Pm-1, Colletotrichum-R1",
        "agronomic_description": "High pungency (0.45% capsaicin) dual-purpose hybrid for green and dry red chilli export",
        "developing_institution": "ICAR-IIHR",
        "genetic_purity_score": 99.50,
        "heritability_broad_sense": 0.79,
        "drought_susceptibility_index": 0.76,
        "harvest_index_pct": 49.2,
        "recommended_agro_climatic_zones": [
            "Zone 5: Indo-Gangetic Plains & Central Plateau",
            "Zone 6: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0021",
        "variety_name": "Rice Swarna Sub1 Genotype Line v3",
        "target_trait": "Submergence / Flash Flood Tolerance",
        "major_qtl_markers": "Sub1A Transcription Factor",
        "agronomic_description": "Direct seeded or transplanted lowland rice with 14-day complete water submergence survival",
        "developing_institution": "Central Rice Research Institute (CRRI)",
        "genetic_purity_score": 99.60,
        "heritability_broad_sense": 0.80,
        "drought_susceptibility_index": 0.78,
        "harvest_index_pct": 42.0,
        "recommended_agro_climatic_zones": [
            "Zone 6: Indo-Gangetic Plains & Central Plateau",
            "Zone 7: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0022",
        "variety_name": "Rice CR Dhan 801 Genotype Line v3",
        "target_trait": "Drought + Submergence Dual Tolerance",
        "major_qtl_markers": "qDTY1.1, qDTY2.1, Sub1A",
        "agronomic_description": "Climate-resilient dual tolerant line for rainfed drought-prone and flood-prone ecologies",
        "developing_institution": "ICAR-NRRI",
        "genetic_purity_score": 99.70,
        "heritability_broad_sense": 0.81,
        "drought_susceptibility_index": 0.80,
        "harvest_index_pct": 42.8,
        "recommended_agro_climatic_zones": [
            "Zone 7: Indo-Gangetic Plains & Central Plateau",
            "Zone 8: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0023",
        "variety_name": "Wheat DBW 303 (Karan Vaishnavi) Genotype Line v3",
        "target_trait": "Terminal Heat Stress Resistance",
        "major_qtl_markers": "TaHsfA2d, TaFER-5B",
        "agronomic_description": "High-yielding irrigated timely sown bread wheat with extreme heat resilience during grain filling",
        "developing_institution": "ICAR-IIWBR",
        "genetic_purity_score": 99.80,
        "heritability_broad_sense": 0.82,
        "drought_susceptibility_index": 0.82,
        "harvest_index_pct": 43.6,
        "recommended_agro_climatic_zones": [
            "Zone 8: Indo-Gangetic Plains & Central Plateau",
            "Zone 9: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0024",
        "variety_name": "Wheat HD 3226 (Pusa Yashasvi) Genotype Line v3",
        "target_trait": "Multi-Rust Resistance (Yellow, Brown, Black)",
        "major_qtl_markers": "Yr17, Lr37, Sr38",
        "agronomic_description": "Superior chapati-making and biscuit-making quality with high gluten strength",
        "developing_institution": "ICAR-IARI",
        "genetic_purity_score": 99.90,
        "heritability_broad_sense": 0.83,
        "drought_susceptibility_index": 0.84,
        "harvest_index_pct": 44.4,
        "recommended_agro_climatic_zones": [
            "Zone 9: Indo-Gangetic Plains & Central Plateau",
            "Zone 10: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0025",
        "variety_name": "Chickpea Pusa 10216 Genotype Line v3",
        "target_trait": "Drought Drought Tolerance & Root Architecture",
        "major_qtl_markers": "qRT9.1, QTL-hotspot genomic region",
        "agronomic_description": "Desi chickpea with deep taproot system and high water use efficiency under dryland",
        "developing_institution": "ICAR-IARI",
        "genetic_purity_score": 99.20,
        "heritability_broad_sense": 0.84,
        "drought_susceptibility_index": 0.62,
        "harvest_index_pct": 45.2,
        "recommended_agro_climatic_zones": [
            "Zone 10: Indo-Gangetic Plains & Central Plateau",
            "Zone 11: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0026",
        "variety_name": "Pigeonpea BDN 711 Genotype Line v3",
        "target_trait": "Fusarium Wilt & Sterility Mosaic Tolerance",
        "major_qtl_markers": "Cc-RFLP-Wilt1",
        "agronomic_description": "White seeded medium duration variety highly adapted to rainfed black cotton vertisols",
        "developing_institution": "VNMKV",
        "genetic_purity_score": 99.30,
        "heritability_broad_sense": 0.85,
        "drought_susceptibility_index": 0.64,
        "harvest_index_pct": 46.0,
        "recommended_agro_climatic_zones": [
            "Zone 11: Indo-Gangetic Plains & Central Plateau",
            "Zone 12: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0027",
        "variety_name": "Mustard PM 28 Genotype Line v3",
        "target_trait": "High Oleic / Low Glucosinolate Double Zero Quality",
        "major_qtl_markers": "FAD2 mutation, GSL1 deletion",
        "agronomic_description": "Canola quality Brassica juncea with heart-healthy fatty acid profile",
        "developing_institution": "ICAR-DRMR",
        "genetic_purity_score": 99.40,
        "heritability_broad_sense": 0.86,
        "drought_susceptibility_index": 0.66,
        "harvest_index_pct": 46.8,
        "recommended_agro_climatic_zones": [
            "Zone 12: Indo-Gangetic Plains & Central Plateau",
            "Zone 13: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0028",
        "variety_name": "Cotton Bunny Bt (NCS 145) Genotype Line v3",
        "target_trait": "Bollworm Resistance & Sucking Pest Tolerance",
        "major_qtl_markers": "Cry1Ac + Cry2Ab (Bollgard II)",
        "agronomic_description": "High boll retention, exceptional ginning outturn (36%), and staple length (31mm)",
        "developing_institution": "Nuziveedu Seeds",
        "genetic_purity_score": 99.50,
        "heritability_broad_sense": 0.87,
        "drought_susceptibility_index": 0.68,
        "harvest_index_pct": 47.6,
        "recommended_agro_climatic_zones": [
            "Zone 13: Indo-Gangetic Plains & Central Plateau",
            "Zone 14: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0029",
        "variety_name": "Tomato Arka Rakshak (F1 Hybrid) Genotype Line v3",
        "target_trait": "Triple Disease Resistance (ToLCV, BW, EB)",
        "major_qtl_markers": "Ty-2, Ty-3, Bwr-12, Ph-3",
        "agronomic_description": "High yielding indeterminate tomato with resistance to leaf curl virus, bacterial wilt, and early blight",
        "developing_institution": "ICAR-IIHR",
        "genetic_purity_score": 99.60,
        "heritability_broad_sense": 0.88,
        "drought_susceptibility_index": 0.70,
        "harvest_index_pct": 48.4,
        "recommended_agro_climatic_zones": [
            "Zone 14: Indo-Gangetic Plains & Central Plateau",
            "Zone 15: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0030",
        "variety_name": "Chilli Arka Harita Genotype Line v3",
        "target_trait": "Powdery Mildew & Anthracnose Tolerance",
        "major_qtl_markers": "Pm-1, Colletotrichum-R1",
        "agronomic_description": "High pungency (0.45% capsaicin) dual-purpose hybrid for green and dry red chilli export",
        "developing_institution": "ICAR-IIHR",
        "genetic_purity_score": 99.70,
        "heritability_broad_sense": 0.89,
        "drought_susceptibility_index": 0.72,
        "harvest_index_pct": 49.2,
        "recommended_agro_climatic_zones": [
            "Zone 15: Indo-Gangetic Plains & Central Plateau",
            "Zone 1: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0031",
        "variety_name": "Rice Swarna Sub1 Genotype Line v4",
        "target_trait": "Submergence / Flash Flood Tolerance",
        "major_qtl_markers": "Sub1A Transcription Factor",
        "agronomic_description": "Direct seeded or transplanted lowland rice with 14-day complete water submergence survival",
        "developing_institution": "Central Rice Research Institute (CRRI)",
        "genetic_purity_score": 99.80,
        "heritability_broad_sense": 0.90,
        "drought_susceptibility_index": 0.74,
        "harvest_index_pct": 42.0,
        "recommended_agro_climatic_zones": [
            "Zone 1: Indo-Gangetic Plains & Central Plateau",
            "Zone 2: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0032",
        "variety_name": "Rice CR Dhan 801 Genotype Line v4",
        "target_trait": "Drought + Submergence Dual Tolerance",
        "major_qtl_markers": "qDTY1.1, qDTY2.1, Sub1A",
        "agronomic_description": "Climate-resilient dual tolerant line for rainfed drought-prone and flood-prone ecologies",
        "developing_institution": "ICAR-NRRI",
        "genetic_purity_score": 99.90,
        "heritability_broad_sense": 0.91,
        "drought_susceptibility_index": 0.76,
        "harvest_index_pct": 42.8,
        "recommended_agro_climatic_zones": [
            "Zone 2: Indo-Gangetic Plains & Central Plateau",
            "Zone 3: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0033",
        "variety_name": "Wheat DBW 303 (Karan Vaishnavi) Genotype Line v4",
        "target_trait": "Terminal Heat Stress Resistance",
        "major_qtl_markers": "TaHsfA2d, TaFER-5B",
        "agronomic_description": "High-yielding irrigated timely sown bread wheat with extreme heat resilience during grain filling",
        "developing_institution": "ICAR-IIWBR",
        "genetic_purity_score": 99.20,
        "heritability_broad_sense": 0.92,
        "drought_susceptibility_index": 0.78,
        "harvest_index_pct": 43.6,
        "recommended_agro_climatic_zones": [
            "Zone 3: Indo-Gangetic Plains & Central Plateau",
            "Zone 4: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0034",
        "variety_name": "Wheat HD 3226 (Pusa Yashasvi) Genotype Line v4",
        "target_trait": "Multi-Rust Resistance (Yellow, Brown, Black)",
        "major_qtl_markers": "Yr17, Lr37, Sr38",
        "agronomic_description": "Superior chapati-making and biscuit-making quality with high gluten strength",
        "developing_institution": "ICAR-IARI",
        "genetic_purity_score": 99.30,
        "heritability_broad_sense": 0.93,
        "drought_susceptibility_index": 0.80,
        "harvest_index_pct": 44.4,
        "recommended_agro_climatic_zones": [
            "Zone 4: Indo-Gangetic Plains & Central Plateau",
            "Zone 5: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0035",
        "variety_name": "Chickpea Pusa 10216 Genotype Line v4",
        "target_trait": "Drought Drought Tolerance & Root Architecture",
        "major_qtl_markers": "qRT9.1, QTL-hotspot genomic region",
        "agronomic_description": "Desi chickpea with deep taproot system and high water use efficiency under dryland",
        "developing_institution": "ICAR-IARI",
        "genetic_purity_score": 99.40,
        "heritability_broad_sense": 0.94,
        "drought_susceptibility_index": 0.82,
        "harvest_index_pct": 45.2,
        "recommended_agro_climatic_zones": [
            "Zone 5: Indo-Gangetic Plains & Central Plateau",
            "Zone 6: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0036",
        "variety_name": "Pigeonpea BDN 711 Genotype Line v4",
        "target_trait": "Fusarium Wilt & Sterility Mosaic Tolerance",
        "major_qtl_markers": "Cc-RFLP-Wilt1",
        "agronomic_description": "White seeded medium duration variety highly adapted to rainfed black cotton vertisols",
        "developing_institution": "VNMKV",
        "genetic_purity_score": 99.50,
        "heritability_broad_sense": 0.95,
        "drought_susceptibility_index": 0.84,
        "harvest_index_pct": 46.0,
        "recommended_agro_climatic_zones": [
            "Zone 6: Indo-Gangetic Plains & Central Plateau",
            "Zone 7: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0037",
        "variety_name": "Mustard PM 28 Genotype Line v4",
        "target_trait": "High Oleic / Low Glucosinolate Double Zero Quality",
        "major_qtl_markers": "FAD2 mutation, GSL1 deletion",
        "agronomic_description": "Canola quality Brassica juncea with heart-healthy fatty acid profile",
        "developing_institution": "ICAR-DRMR",
        "genetic_purity_score": 99.60,
        "heritability_broad_sense": 0.78,
        "drought_susceptibility_index": 0.62,
        "harvest_index_pct": 46.8,
        "recommended_agro_climatic_zones": [
            "Zone 7: Indo-Gangetic Plains & Central Plateau",
            "Zone 8: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0038",
        "variety_name": "Cotton Bunny Bt (NCS 145) Genotype Line v4",
        "target_trait": "Bollworm Resistance & Sucking Pest Tolerance",
        "major_qtl_markers": "Cry1Ac + Cry2Ab (Bollgard II)",
        "agronomic_description": "High boll retention, exceptional ginning outturn (36%), and staple length (31mm)",
        "developing_institution": "Nuziveedu Seeds",
        "genetic_purity_score": 99.70,
        "heritability_broad_sense": 0.79,
        "drought_susceptibility_index": 0.64,
        "harvest_index_pct": 47.6,
        "recommended_agro_climatic_zones": [
            "Zone 8: Indo-Gangetic Plains & Central Plateau",
            "Zone 9: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0039",
        "variety_name": "Tomato Arka Rakshak (F1 Hybrid) Genotype Line v4",
        "target_trait": "Triple Disease Resistance (ToLCV, BW, EB)",
        "major_qtl_markers": "Ty-2, Ty-3, Bwr-12, Ph-3",
        "agronomic_description": "High yielding indeterminate tomato with resistance to leaf curl virus, bacterial wilt, and early blight",
        "developing_institution": "ICAR-IIHR",
        "genetic_purity_score": 99.80,
        "heritability_broad_sense": 0.80,
        "drought_susceptibility_index": 0.66,
        "harvest_index_pct": 48.4,
        "recommended_agro_climatic_zones": [
            "Zone 9: Indo-Gangetic Plains & Central Plateau",
            "Zone 10: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0040",
        "variety_name": "Chilli Arka Harita Genotype Line v4",
        "target_trait": "Powdery Mildew & Anthracnose Tolerance",
        "major_qtl_markers": "Pm-1, Colletotrichum-R1",
        "agronomic_description": "High pungency (0.45% capsaicin) dual-purpose hybrid for green and dry red chilli export",
        "developing_institution": "ICAR-IIHR",
        "genetic_purity_score": 99.90,
        "heritability_broad_sense": 0.81,
        "drought_susceptibility_index": 0.68,
        "harvest_index_pct": 49.2,
        "recommended_agro_climatic_zones": [
            "Zone 10: Indo-Gangetic Plains & Central Plateau",
            "Zone 11: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0041",
        "variety_name": "Rice Swarna Sub1 Genotype Line v5",
        "target_trait": "Submergence / Flash Flood Tolerance",
        "major_qtl_markers": "Sub1A Transcription Factor",
        "agronomic_description": "Direct seeded or transplanted lowland rice with 14-day complete water submergence survival",
        "developing_institution": "Central Rice Research Institute (CRRI)",
        "genetic_purity_score": 99.20,
        "heritability_broad_sense": 0.82,
        "drought_susceptibility_index": 0.70,
        "harvest_index_pct": 42.0,
        "recommended_agro_climatic_zones": [
            "Zone 11: Indo-Gangetic Plains & Central Plateau",
            "Zone 12: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0042",
        "variety_name": "Rice CR Dhan 801 Genotype Line v5",
        "target_trait": "Drought + Submergence Dual Tolerance",
        "major_qtl_markers": "qDTY1.1, qDTY2.1, Sub1A",
        "agronomic_description": "Climate-resilient dual tolerant line for rainfed drought-prone and flood-prone ecologies",
        "developing_institution": "ICAR-NRRI",
        "genetic_purity_score": 99.30,
        "heritability_broad_sense": 0.83,
        "drought_susceptibility_index": 0.72,
        "harvest_index_pct": 42.8,
        "recommended_agro_climatic_zones": [
            "Zone 12: Indo-Gangetic Plains & Central Plateau",
            "Zone 13: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0043",
        "variety_name": "Wheat DBW 303 (Karan Vaishnavi) Genotype Line v5",
        "target_trait": "Terminal Heat Stress Resistance",
        "major_qtl_markers": "TaHsfA2d, TaFER-5B",
        "agronomic_description": "High-yielding irrigated timely sown bread wheat with extreme heat resilience during grain filling",
        "developing_institution": "ICAR-IIWBR",
        "genetic_purity_score": 99.40,
        "heritability_broad_sense": 0.84,
        "drought_susceptibility_index": 0.74,
        "harvest_index_pct": 43.6,
        "recommended_agro_climatic_zones": [
            "Zone 13: Indo-Gangetic Plains & Central Plateau",
            "Zone 14: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0044",
        "variety_name": "Wheat HD 3226 (Pusa Yashasvi) Genotype Line v5",
        "target_trait": "Multi-Rust Resistance (Yellow, Brown, Black)",
        "major_qtl_markers": "Yr17, Lr37, Sr38",
        "agronomic_description": "Superior chapati-making and biscuit-making quality with high gluten strength",
        "developing_institution": "ICAR-IARI",
        "genetic_purity_score": 99.50,
        "heritability_broad_sense": 0.85,
        "drought_susceptibility_index": 0.76,
        "harvest_index_pct": 44.4,
        "recommended_agro_climatic_zones": [
            "Zone 14: Indo-Gangetic Plains & Central Plateau",
            "Zone 15: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0045",
        "variety_name": "Chickpea Pusa 10216 Genotype Line v5",
        "target_trait": "Drought Drought Tolerance & Root Architecture",
        "major_qtl_markers": "qRT9.1, QTL-hotspot genomic region",
        "agronomic_description": "Desi chickpea with deep taproot system and high water use efficiency under dryland",
        "developing_institution": "ICAR-IARI",
        "genetic_purity_score": 99.60,
        "heritability_broad_sense": 0.86,
        "drought_susceptibility_index": 0.78,
        "harvest_index_pct": 45.2,
        "recommended_agro_climatic_zones": [
            "Zone 15: Indo-Gangetic Plains & Central Plateau",
            "Zone 1: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0046",
        "variety_name": "Pigeonpea BDN 711 Genotype Line v5",
        "target_trait": "Fusarium Wilt & Sterility Mosaic Tolerance",
        "major_qtl_markers": "Cc-RFLP-Wilt1",
        "agronomic_description": "White seeded medium duration variety highly adapted to rainfed black cotton vertisols",
        "developing_institution": "VNMKV",
        "genetic_purity_score": 99.70,
        "heritability_broad_sense": 0.87,
        "drought_susceptibility_index": 0.80,
        "harvest_index_pct": 46.0,
        "recommended_agro_climatic_zones": [
            "Zone 1: Indo-Gangetic Plains & Central Plateau",
            "Zone 2: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0047",
        "variety_name": "Mustard PM 28 Genotype Line v5",
        "target_trait": "High Oleic / Low Glucosinolate Double Zero Quality",
        "major_qtl_markers": "FAD2 mutation, GSL1 deletion",
        "agronomic_description": "Canola quality Brassica juncea with heart-healthy fatty acid profile",
        "developing_institution": "ICAR-DRMR",
        "genetic_purity_score": 99.80,
        "heritability_broad_sense": 0.88,
        "drought_susceptibility_index": 0.82,
        "harvest_index_pct": 46.8,
        "recommended_agro_climatic_zones": [
            "Zone 2: Indo-Gangetic Plains & Central Plateau",
            "Zone 3: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0048",
        "variety_name": "Cotton Bunny Bt (NCS 145) Genotype Line v5",
        "target_trait": "Bollworm Resistance & Sucking Pest Tolerance",
        "major_qtl_markers": "Cry1Ac + Cry2Ab (Bollgard II)",
        "agronomic_description": "High boll retention, exceptional ginning outturn (36%), and staple length (31mm)",
        "developing_institution": "Nuziveedu Seeds",
        "genetic_purity_score": 99.90,
        "heritability_broad_sense": 0.89,
        "drought_susceptibility_index": 0.84,
        "harvest_index_pct": 47.6,
        "recommended_agro_climatic_zones": [
            "Zone 3: Indo-Gangetic Plains & Central Plateau",
            "Zone 4: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0049",
        "variety_name": "Tomato Arka Rakshak (F1 Hybrid) Genotype Line v5",
        "target_trait": "Triple Disease Resistance (ToLCV, BW, EB)",
        "major_qtl_markers": "Ty-2, Ty-3, Bwr-12, Ph-3",
        "agronomic_description": "High yielding indeterminate tomato with resistance to leaf curl virus, bacterial wilt, and early blight",
        "developing_institution": "ICAR-IIHR",
        "genetic_purity_score": 99.20,
        "heritability_broad_sense": 0.90,
        "drought_susceptibility_index": 0.62,
        "harvest_index_pct": 48.4,
        "recommended_agro_climatic_zones": [
            "Zone 4: Indo-Gangetic Plains & Central Plateau",
            "Zone 5: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0050",
        "variety_name": "Chilli Arka Harita Genotype Line v5",
        "target_trait": "Powdery Mildew & Anthracnose Tolerance",
        "major_qtl_markers": "Pm-1, Colletotrichum-R1",
        "agronomic_description": "High pungency (0.45% capsaicin) dual-purpose hybrid for green and dry red chilli export",
        "developing_institution": "ICAR-IIHR",
        "genetic_purity_score": 99.30,
        "heritability_broad_sense": 0.91,
        "drought_susceptibility_index": 0.64,
        "harvest_index_pct": 49.2,
        "recommended_agro_climatic_zones": [
            "Zone 5: Indo-Gangetic Plains & Central Plateau",
            "Zone 6: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0051",
        "variety_name": "Rice Swarna Sub1 Genotype Line v6",
        "target_trait": "Submergence / Flash Flood Tolerance",
        "major_qtl_markers": "Sub1A Transcription Factor",
        "agronomic_description": "Direct seeded or transplanted lowland rice with 14-day complete water submergence survival",
        "developing_institution": "Central Rice Research Institute (CRRI)",
        "genetic_purity_score": 99.40,
        "heritability_broad_sense": 0.92,
        "drought_susceptibility_index": 0.66,
        "harvest_index_pct": 42.0,
        "recommended_agro_climatic_zones": [
            "Zone 6: Indo-Gangetic Plains & Central Plateau",
            "Zone 7: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0052",
        "variety_name": "Rice CR Dhan 801 Genotype Line v6",
        "target_trait": "Drought + Submergence Dual Tolerance",
        "major_qtl_markers": "qDTY1.1, qDTY2.1, Sub1A",
        "agronomic_description": "Climate-resilient dual tolerant line for rainfed drought-prone and flood-prone ecologies",
        "developing_institution": "ICAR-NRRI",
        "genetic_purity_score": 99.50,
        "heritability_broad_sense": 0.93,
        "drought_susceptibility_index": 0.68,
        "harvest_index_pct": 42.8,
        "recommended_agro_climatic_zones": [
            "Zone 7: Indo-Gangetic Plains & Central Plateau",
            "Zone 8: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0053",
        "variety_name": "Wheat DBW 303 (Karan Vaishnavi) Genotype Line v6",
        "target_trait": "Terminal Heat Stress Resistance",
        "major_qtl_markers": "TaHsfA2d, TaFER-5B",
        "agronomic_description": "High-yielding irrigated timely sown bread wheat with extreme heat resilience during grain filling",
        "developing_institution": "ICAR-IIWBR",
        "genetic_purity_score": 99.60,
        "heritability_broad_sense": 0.94,
        "drought_susceptibility_index": 0.70,
        "harvest_index_pct": 43.6,
        "recommended_agro_climatic_zones": [
            "Zone 8: Indo-Gangetic Plains & Central Plateau",
            "Zone 9: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0054",
        "variety_name": "Wheat HD 3226 (Pusa Yashasvi) Genotype Line v6",
        "target_trait": "Multi-Rust Resistance (Yellow, Brown, Black)",
        "major_qtl_markers": "Yr17, Lr37, Sr38",
        "agronomic_description": "Superior chapati-making and biscuit-making quality with high gluten strength",
        "developing_institution": "ICAR-IARI",
        "genetic_purity_score": 99.70,
        "heritability_broad_sense": 0.95,
        "drought_susceptibility_index": 0.72,
        "harvest_index_pct": 44.4,
        "recommended_agro_climatic_zones": [
            "Zone 9: Indo-Gangetic Plains & Central Plateau",
            "Zone 10: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0055",
        "variety_name": "Chickpea Pusa 10216 Genotype Line v6",
        "target_trait": "Drought Drought Tolerance & Root Architecture",
        "major_qtl_markers": "qRT9.1, QTL-hotspot genomic region",
        "agronomic_description": "Desi chickpea with deep taproot system and high water use efficiency under dryland",
        "developing_institution": "ICAR-IARI",
        "genetic_purity_score": 99.80,
        "heritability_broad_sense": 0.78,
        "drought_susceptibility_index": 0.74,
        "harvest_index_pct": 45.2,
        "recommended_agro_climatic_zones": [
            "Zone 10: Indo-Gangetic Plains & Central Plateau",
            "Zone 11: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0056",
        "variety_name": "Pigeonpea BDN 711 Genotype Line v6",
        "target_trait": "Fusarium Wilt & Sterility Mosaic Tolerance",
        "major_qtl_markers": "Cc-RFLP-Wilt1",
        "agronomic_description": "White seeded medium duration variety highly adapted to rainfed black cotton vertisols",
        "developing_institution": "VNMKV",
        "genetic_purity_score": 99.90,
        "heritability_broad_sense": 0.79,
        "drought_susceptibility_index": 0.76,
        "harvest_index_pct": 46.0,
        "recommended_agro_climatic_zones": [
            "Zone 11: Indo-Gangetic Plains & Central Plateau",
            "Zone 12: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0057",
        "variety_name": "Mustard PM 28 Genotype Line v6",
        "target_trait": "High Oleic / Low Glucosinolate Double Zero Quality",
        "major_qtl_markers": "FAD2 mutation, GSL1 deletion",
        "agronomic_description": "Canola quality Brassica juncea with heart-healthy fatty acid profile",
        "developing_institution": "ICAR-DRMR",
        "genetic_purity_score": 99.20,
        "heritability_broad_sense": 0.80,
        "drought_susceptibility_index": 0.78,
        "harvest_index_pct": 46.8,
        "recommended_agro_climatic_zones": [
            "Zone 12: Indo-Gangetic Plains & Central Plateau",
            "Zone 13: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0058",
        "variety_name": "Cotton Bunny Bt (NCS 145) Genotype Line v6",
        "target_trait": "Bollworm Resistance & Sucking Pest Tolerance",
        "major_qtl_markers": "Cry1Ac + Cry2Ab (Bollgard II)",
        "agronomic_description": "High boll retention, exceptional ginning outturn (36%), and staple length (31mm)",
        "developing_institution": "Nuziveedu Seeds",
        "genetic_purity_score": 99.30,
        "heritability_broad_sense": 0.81,
        "drought_susceptibility_index": 0.80,
        "harvest_index_pct": 47.6,
        "recommended_agro_climatic_zones": [
            "Zone 13: Indo-Gangetic Plains & Central Plateau",
            "Zone 14: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0059",
        "variety_name": "Tomato Arka Rakshak (F1 Hybrid) Genotype Line v6",
        "target_trait": "Triple Disease Resistance (ToLCV, BW, EB)",
        "major_qtl_markers": "Ty-2, Ty-3, Bwr-12, Ph-3",
        "agronomic_description": "High yielding indeterminate tomato with resistance to leaf curl virus, bacterial wilt, and early blight",
        "developing_institution": "ICAR-IIHR",
        "genetic_purity_score": 99.40,
        "heritability_broad_sense": 0.82,
        "drought_susceptibility_index": 0.82,
        "harvest_index_pct": 48.4,
        "recommended_agro_climatic_zones": [
            "Zone 14: Indo-Gangetic Plains & Central Plateau",
            "Zone 15: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0060",
        "variety_name": "Chilli Arka Harita Genotype Line v6",
        "target_trait": "Powdery Mildew & Anthracnose Tolerance",
        "major_qtl_markers": "Pm-1, Colletotrichum-R1",
        "agronomic_description": "High pungency (0.45% capsaicin) dual-purpose hybrid for green and dry red chilli export",
        "developing_institution": "ICAR-IIHR",
        "genetic_purity_score": 99.50,
        "heritability_broad_sense": 0.83,
        "drought_susceptibility_index": 0.84,
        "harvest_index_pct": 49.2,
        "recommended_agro_climatic_zones": [
            "Zone 15: Indo-Gangetic Plains & Central Plateau",
            "Zone 1: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0061",
        "variety_name": "Rice Swarna Sub1 Genotype Line v7",
        "target_trait": "Submergence / Flash Flood Tolerance",
        "major_qtl_markers": "Sub1A Transcription Factor",
        "agronomic_description": "Direct seeded or transplanted lowland rice with 14-day complete water submergence survival",
        "developing_institution": "Central Rice Research Institute (CRRI)",
        "genetic_purity_score": 99.60,
        "heritability_broad_sense": 0.84,
        "drought_susceptibility_index": 0.62,
        "harvest_index_pct": 42.0,
        "recommended_agro_climatic_zones": [
            "Zone 1: Indo-Gangetic Plains & Central Plateau",
            "Zone 2: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0062",
        "variety_name": "Rice CR Dhan 801 Genotype Line v7",
        "target_trait": "Drought + Submergence Dual Tolerance",
        "major_qtl_markers": "qDTY1.1, qDTY2.1, Sub1A",
        "agronomic_description": "Climate-resilient dual tolerant line for rainfed drought-prone and flood-prone ecologies",
        "developing_institution": "ICAR-NRRI",
        "genetic_purity_score": 99.70,
        "heritability_broad_sense": 0.85,
        "drought_susceptibility_index": 0.64,
        "harvest_index_pct": 42.8,
        "recommended_agro_climatic_zones": [
            "Zone 2: Indo-Gangetic Plains & Central Plateau",
            "Zone 3: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0063",
        "variety_name": "Wheat DBW 303 (Karan Vaishnavi) Genotype Line v7",
        "target_trait": "Terminal Heat Stress Resistance",
        "major_qtl_markers": "TaHsfA2d, TaFER-5B",
        "agronomic_description": "High-yielding irrigated timely sown bread wheat with extreme heat resilience during grain filling",
        "developing_institution": "ICAR-IIWBR",
        "genetic_purity_score": 99.80,
        "heritability_broad_sense": 0.86,
        "drought_susceptibility_index": 0.66,
        "harvest_index_pct": 43.6,
        "recommended_agro_climatic_zones": [
            "Zone 3: Indo-Gangetic Plains & Central Plateau",
            "Zone 4: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0064",
        "variety_name": "Wheat HD 3226 (Pusa Yashasvi) Genotype Line v7",
        "target_trait": "Multi-Rust Resistance (Yellow, Brown, Black)",
        "major_qtl_markers": "Yr17, Lr37, Sr38",
        "agronomic_description": "Superior chapati-making and biscuit-making quality with high gluten strength",
        "developing_institution": "ICAR-IARI",
        "genetic_purity_score": 99.90,
        "heritability_broad_sense": 0.87,
        "drought_susceptibility_index": 0.68,
        "harvest_index_pct": 44.4,
        "recommended_agro_climatic_zones": [
            "Zone 4: Indo-Gangetic Plains & Central Plateau",
            "Zone 5: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0065",
        "variety_name": "Chickpea Pusa 10216 Genotype Line v7",
        "target_trait": "Drought Drought Tolerance & Root Architecture",
        "major_qtl_markers": "qRT9.1, QTL-hotspot genomic region",
        "agronomic_description": "Desi chickpea with deep taproot system and high water use efficiency under dryland",
        "developing_institution": "ICAR-IARI",
        "genetic_purity_score": 99.20,
        "heritability_broad_sense": 0.88,
        "drought_susceptibility_index": 0.70,
        "harvest_index_pct": 45.2,
        "recommended_agro_climatic_zones": [
            "Zone 5: Indo-Gangetic Plains & Central Plateau",
            "Zone 6: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0066",
        "variety_name": "Pigeonpea BDN 711 Genotype Line v7",
        "target_trait": "Fusarium Wilt & Sterility Mosaic Tolerance",
        "major_qtl_markers": "Cc-RFLP-Wilt1",
        "agronomic_description": "White seeded medium duration variety highly adapted to rainfed black cotton vertisols",
        "developing_institution": "VNMKV",
        "genetic_purity_score": 99.30,
        "heritability_broad_sense": 0.89,
        "drought_susceptibility_index": 0.72,
        "harvest_index_pct": 46.0,
        "recommended_agro_climatic_zones": [
            "Zone 6: Indo-Gangetic Plains & Central Plateau",
            "Zone 7: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0067",
        "variety_name": "Mustard PM 28 Genotype Line v7",
        "target_trait": "High Oleic / Low Glucosinolate Double Zero Quality",
        "major_qtl_markers": "FAD2 mutation, GSL1 deletion",
        "agronomic_description": "Canola quality Brassica juncea with heart-healthy fatty acid profile",
        "developing_institution": "ICAR-DRMR",
        "genetic_purity_score": 99.40,
        "heritability_broad_sense": 0.90,
        "drought_susceptibility_index": 0.74,
        "harvest_index_pct": 46.8,
        "recommended_agro_climatic_zones": [
            "Zone 7: Indo-Gangetic Plains & Central Plateau",
            "Zone 8: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0068",
        "variety_name": "Cotton Bunny Bt (NCS 145) Genotype Line v7",
        "target_trait": "Bollworm Resistance & Sucking Pest Tolerance",
        "major_qtl_markers": "Cry1Ac + Cry2Ab (Bollgard II)",
        "agronomic_description": "High boll retention, exceptional ginning outturn (36%), and staple length (31mm)",
        "developing_institution": "Nuziveedu Seeds",
        "genetic_purity_score": 99.50,
        "heritability_broad_sense": 0.91,
        "drought_susceptibility_index": 0.76,
        "harvest_index_pct": 47.6,
        "recommended_agro_climatic_zones": [
            "Zone 8: Indo-Gangetic Plains & Central Plateau",
            "Zone 9: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0069",
        "variety_name": "Tomato Arka Rakshak (F1 Hybrid) Genotype Line v7",
        "target_trait": "Triple Disease Resistance (ToLCV, BW, EB)",
        "major_qtl_markers": "Ty-2, Ty-3, Bwr-12, Ph-3",
        "agronomic_description": "High yielding indeterminate tomato with resistance to leaf curl virus, bacterial wilt, and early blight",
        "developing_institution": "ICAR-IIHR",
        "genetic_purity_score": 99.60,
        "heritability_broad_sense": 0.92,
        "drought_susceptibility_index": 0.78,
        "harvest_index_pct": 48.4,
        "recommended_agro_climatic_zones": [
            "Zone 9: Indo-Gangetic Plains & Central Plateau",
            "Zone 10: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0070",
        "variety_name": "Chilli Arka Harita Genotype Line v7",
        "target_trait": "Powdery Mildew & Anthracnose Tolerance",
        "major_qtl_markers": "Pm-1, Colletotrichum-R1",
        "agronomic_description": "High pungency (0.45% capsaicin) dual-purpose hybrid for green and dry red chilli export",
        "developing_institution": "ICAR-IIHR",
        "genetic_purity_score": 99.70,
        "heritability_broad_sense": 0.93,
        "drought_susceptibility_index": 0.80,
        "harvest_index_pct": 49.2,
        "recommended_agro_climatic_zones": [
            "Zone 10: Indo-Gangetic Plains & Central Plateau",
            "Zone 11: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0071",
        "variety_name": "Rice Swarna Sub1 Genotype Line v8",
        "target_trait": "Submergence / Flash Flood Tolerance",
        "major_qtl_markers": "Sub1A Transcription Factor",
        "agronomic_description": "Direct seeded or transplanted lowland rice with 14-day complete water submergence survival",
        "developing_institution": "Central Rice Research Institute (CRRI)",
        "genetic_purity_score": 99.80,
        "heritability_broad_sense": 0.94,
        "drought_susceptibility_index": 0.82,
        "harvest_index_pct": 42.0,
        "recommended_agro_climatic_zones": [
            "Zone 11: Indo-Gangetic Plains & Central Plateau",
            "Zone 12: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0072",
        "variety_name": "Rice CR Dhan 801 Genotype Line v8",
        "target_trait": "Drought + Submergence Dual Tolerance",
        "major_qtl_markers": "qDTY1.1, qDTY2.1, Sub1A",
        "agronomic_description": "Climate-resilient dual tolerant line for rainfed drought-prone and flood-prone ecologies",
        "developing_institution": "ICAR-NRRI",
        "genetic_purity_score": 99.90,
        "heritability_broad_sense": 0.95,
        "drought_susceptibility_index": 0.84,
        "harvest_index_pct": 42.8,
        "recommended_agro_climatic_zones": [
            "Zone 12: Indo-Gangetic Plains & Central Plateau",
            "Zone 13: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0073",
        "variety_name": "Wheat DBW 303 (Karan Vaishnavi) Genotype Line v8",
        "target_trait": "Terminal Heat Stress Resistance",
        "major_qtl_markers": "TaHsfA2d, TaFER-5B",
        "agronomic_description": "High-yielding irrigated timely sown bread wheat with extreme heat resilience during grain filling",
        "developing_institution": "ICAR-IIWBR",
        "genetic_purity_score": 99.20,
        "heritability_broad_sense": 0.78,
        "drought_susceptibility_index": 0.62,
        "harvest_index_pct": 43.6,
        "recommended_agro_climatic_zones": [
            "Zone 13: Indo-Gangetic Plains & Central Plateau",
            "Zone 14: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0074",
        "variety_name": "Wheat HD 3226 (Pusa Yashasvi) Genotype Line v8",
        "target_trait": "Multi-Rust Resistance (Yellow, Brown, Black)",
        "major_qtl_markers": "Yr17, Lr37, Sr38",
        "agronomic_description": "Superior chapati-making and biscuit-making quality with high gluten strength",
        "developing_institution": "ICAR-IARI",
        "genetic_purity_score": 99.30,
        "heritability_broad_sense": 0.79,
        "drought_susceptibility_index": 0.64,
        "harvest_index_pct": 44.4,
        "recommended_agro_climatic_zones": [
            "Zone 14: Indo-Gangetic Plains & Central Plateau",
            "Zone 15: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0075",
        "variety_name": "Chickpea Pusa 10216 Genotype Line v8",
        "target_trait": "Drought Drought Tolerance & Root Architecture",
        "major_qtl_markers": "qRT9.1, QTL-hotspot genomic region",
        "agronomic_description": "Desi chickpea with deep taproot system and high water use efficiency under dryland",
        "developing_institution": "ICAR-IARI",
        "genetic_purity_score": 99.40,
        "heritability_broad_sense": 0.80,
        "drought_susceptibility_index": 0.66,
        "harvest_index_pct": 45.2,
        "recommended_agro_climatic_zones": [
            "Zone 15: Indo-Gangetic Plains & Central Plateau",
            "Zone 1: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0076",
        "variety_name": "Pigeonpea BDN 711 Genotype Line v8",
        "target_trait": "Fusarium Wilt & Sterility Mosaic Tolerance",
        "major_qtl_markers": "Cc-RFLP-Wilt1",
        "agronomic_description": "White seeded medium duration variety highly adapted to rainfed black cotton vertisols",
        "developing_institution": "VNMKV",
        "genetic_purity_score": 99.50,
        "heritability_broad_sense": 0.81,
        "drought_susceptibility_index": 0.68,
        "harvest_index_pct": 46.0,
        "recommended_agro_climatic_zones": [
            "Zone 1: Indo-Gangetic Plains & Central Plateau",
            "Zone 2: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0077",
        "variety_name": "Mustard PM 28 Genotype Line v8",
        "target_trait": "High Oleic / Low Glucosinolate Double Zero Quality",
        "major_qtl_markers": "FAD2 mutation, GSL1 deletion",
        "agronomic_description": "Canola quality Brassica juncea with heart-healthy fatty acid profile",
        "developing_institution": "ICAR-DRMR",
        "genetic_purity_score": 99.60,
        "heritability_broad_sense": 0.82,
        "drought_susceptibility_index": 0.70,
        "harvest_index_pct": 46.8,
        "recommended_agro_climatic_zones": [
            "Zone 2: Indo-Gangetic Plains & Central Plateau",
            "Zone 3: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0078",
        "variety_name": "Cotton Bunny Bt (NCS 145) Genotype Line v8",
        "target_trait": "Bollworm Resistance & Sucking Pest Tolerance",
        "major_qtl_markers": "Cry1Ac + Cry2Ab (Bollgard II)",
        "agronomic_description": "High boll retention, exceptional ginning outturn (36%), and staple length (31mm)",
        "developing_institution": "Nuziveedu Seeds",
        "genetic_purity_score": 99.70,
        "heritability_broad_sense": 0.83,
        "drought_susceptibility_index": 0.72,
        "harvest_index_pct": 47.6,
        "recommended_agro_climatic_zones": [
            "Zone 3: Indo-Gangetic Plains & Central Plateau",
            "Zone 4: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0079",
        "variety_name": "Tomato Arka Rakshak (F1 Hybrid) Genotype Line v8",
        "target_trait": "Triple Disease Resistance (ToLCV, BW, EB)",
        "major_qtl_markers": "Ty-2, Ty-3, Bwr-12, Ph-3",
        "agronomic_description": "High yielding indeterminate tomato with resistance to leaf curl virus, bacterial wilt, and early blight",
        "developing_institution": "ICAR-IIHR",
        "genetic_purity_score": 99.80,
        "heritability_broad_sense": 0.84,
        "drought_susceptibility_index": 0.74,
        "harvest_index_pct": 48.4,
        "recommended_agro_climatic_zones": [
            "Zone 4: Indo-Gangetic Plains & Central Plateau",
            "Zone 5: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0080",
        "variety_name": "Chilli Arka Harita Genotype Line v8",
        "target_trait": "Powdery Mildew & Anthracnose Tolerance",
        "major_qtl_markers": "Pm-1, Colletotrichum-R1",
        "agronomic_description": "High pungency (0.45% capsaicin) dual-purpose hybrid for green and dry red chilli export",
        "developing_institution": "ICAR-IIHR",
        "genetic_purity_score": 99.90,
        "heritability_broad_sense": 0.85,
        "drought_susceptibility_index": 0.76,
        "harvest_index_pct": 49.2,
        "recommended_agro_climatic_zones": [
            "Zone 5: Indo-Gangetic Plains & Central Plateau",
            "Zone 6: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0081",
        "variety_name": "Rice Swarna Sub1 Genotype Line v9",
        "target_trait": "Submergence / Flash Flood Tolerance",
        "major_qtl_markers": "Sub1A Transcription Factor",
        "agronomic_description": "Direct seeded or transplanted lowland rice with 14-day complete water submergence survival",
        "developing_institution": "Central Rice Research Institute (CRRI)",
        "genetic_purity_score": 99.20,
        "heritability_broad_sense": 0.86,
        "drought_susceptibility_index": 0.78,
        "harvest_index_pct": 42.0,
        "recommended_agro_climatic_zones": [
            "Zone 6: Indo-Gangetic Plains & Central Plateau",
            "Zone 7: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0082",
        "variety_name": "Rice CR Dhan 801 Genotype Line v9",
        "target_trait": "Drought + Submergence Dual Tolerance",
        "major_qtl_markers": "qDTY1.1, qDTY2.1, Sub1A",
        "agronomic_description": "Climate-resilient dual tolerant line for rainfed drought-prone and flood-prone ecologies",
        "developing_institution": "ICAR-NRRI",
        "genetic_purity_score": 99.30,
        "heritability_broad_sense": 0.87,
        "drought_susceptibility_index": 0.80,
        "harvest_index_pct": 42.8,
        "recommended_agro_climatic_zones": [
            "Zone 7: Indo-Gangetic Plains & Central Plateau",
            "Zone 8: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0083",
        "variety_name": "Wheat DBW 303 (Karan Vaishnavi) Genotype Line v9",
        "target_trait": "Terminal Heat Stress Resistance",
        "major_qtl_markers": "TaHsfA2d, TaFER-5B",
        "agronomic_description": "High-yielding irrigated timely sown bread wheat with extreme heat resilience during grain filling",
        "developing_institution": "ICAR-IIWBR",
        "genetic_purity_score": 99.40,
        "heritability_broad_sense": 0.88,
        "drought_susceptibility_index": 0.82,
        "harvest_index_pct": 43.6,
        "recommended_agro_climatic_zones": [
            "Zone 8: Indo-Gangetic Plains & Central Plateau",
            "Zone 9: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0084",
        "variety_name": "Wheat HD 3226 (Pusa Yashasvi) Genotype Line v9",
        "target_trait": "Multi-Rust Resistance (Yellow, Brown, Black)",
        "major_qtl_markers": "Yr17, Lr37, Sr38",
        "agronomic_description": "Superior chapati-making and biscuit-making quality with high gluten strength",
        "developing_institution": "ICAR-IARI",
        "genetic_purity_score": 99.50,
        "heritability_broad_sense": 0.89,
        "drought_susceptibility_index": 0.84,
        "harvest_index_pct": 44.4,
        "recommended_agro_climatic_zones": [
            "Zone 9: Indo-Gangetic Plains & Central Plateau",
            "Zone 10: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0085",
        "variety_name": "Chickpea Pusa 10216 Genotype Line v9",
        "target_trait": "Drought Drought Tolerance & Root Architecture",
        "major_qtl_markers": "qRT9.1, QTL-hotspot genomic region",
        "agronomic_description": "Desi chickpea with deep taproot system and high water use efficiency under dryland",
        "developing_institution": "ICAR-IARI",
        "genetic_purity_score": 99.60,
        "heritability_broad_sense": 0.90,
        "drought_susceptibility_index": 0.62,
        "harvest_index_pct": 45.2,
        "recommended_agro_climatic_zones": [
            "Zone 10: Indo-Gangetic Plains & Central Plateau",
            "Zone 11: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0086",
        "variety_name": "Pigeonpea BDN 711 Genotype Line v9",
        "target_trait": "Fusarium Wilt & Sterility Mosaic Tolerance",
        "major_qtl_markers": "Cc-RFLP-Wilt1",
        "agronomic_description": "White seeded medium duration variety highly adapted to rainfed black cotton vertisols",
        "developing_institution": "VNMKV",
        "genetic_purity_score": 99.70,
        "heritability_broad_sense": 0.91,
        "drought_susceptibility_index": 0.64,
        "harvest_index_pct": 46.0,
        "recommended_agro_climatic_zones": [
            "Zone 11: Indo-Gangetic Plains & Central Plateau",
            "Zone 12: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0087",
        "variety_name": "Mustard PM 28 Genotype Line v9",
        "target_trait": "High Oleic / Low Glucosinolate Double Zero Quality",
        "major_qtl_markers": "FAD2 mutation, GSL1 deletion",
        "agronomic_description": "Canola quality Brassica juncea with heart-healthy fatty acid profile",
        "developing_institution": "ICAR-DRMR",
        "genetic_purity_score": 99.80,
        "heritability_broad_sense": 0.92,
        "drought_susceptibility_index": 0.66,
        "harvest_index_pct": 46.8,
        "recommended_agro_climatic_zones": [
            "Zone 12: Indo-Gangetic Plains & Central Plateau",
            "Zone 13: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0088",
        "variety_name": "Cotton Bunny Bt (NCS 145) Genotype Line v9",
        "target_trait": "Bollworm Resistance & Sucking Pest Tolerance",
        "major_qtl_markers": "Cry1Ac + Cry2Ab (Bollgard II)",
        "agronomic_description": "High boll retention, exceptional ginning outturn (36%), and staple length (31mm)",
        "developing_institution": "Nuziveedu Seeds",
        "genetic_purity_score": 99.90,
        "heritability_broad_sense": 0.93,
        "drought_susceptibility_index": 0.68,
        "harvest_index_pct": 47.6,
        "recommended_agro_climatic_zones": [
            "Zone 13: Indo-Gangetic Plains & Central Plateau",
            "Zone 14: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0089",
        "variety_name": "Tomato Arka Rakshak (F1 Hybrid) Genotype Line v9",
        "target_trait": "Triple Disease Resistance (ToLCV, BW, EB)",
        "major_qtl_markers": "Ty-2, Ty-3, Bwr-12, Ph-3",
        "agronomic_description": "High yielding indeterminate tomato with resistance to leaf curl virus, bacterial wilt, and early blight",
        "developing_institution": "ICAR-IIHR",
        "genetic_purity_score": 99.20,
        "heritability_broad_sense": 0.94,
        "drought_susceptibility_index": 0.70,
        "harvest_index_pct": 48.4,
        "recommended_agro_climatic_zones": [
            "Zone 14: Indo-Gangetic Plains & Central Plateau",
            "Zone 15: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0090",
        "variety_name": "Chilli Arka Harita Genotype Line v9",
        "target_trait": "Powdery Mildew & Anthracnose Tolerance",
        "major_qtl_markers": "Pm-1, Colletotrichum-R1",
        "agronomic_description": "High pungency (0.45% capsaicin) dual-purpose hybrid for green and dry red chilli export",
        "developing_institution": "ICAR-IIHR",
        "genetic_purity_score": 99.30,
        "heritability_broad_sense": 0.95,
        "drought_susceptibility_index": 0.72,
        "harvest_index_pct": 49.2,
        "recommended_agro_climatic_zones": [
            "Zone 15: Indo-Gangetic Plains & Central Plateau",
            "Zone 1: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0091",
        "variety_name": "Rice Swarna Sub1 Genotype Line v10",
        "target_trait": "Submergence / Flash Flood Tolerance",
        "major_qtl_markers": "Sub1A Transcription Factor",
        "agronomic_description": "Direct seeded or transplanted lowland rice with 14-day complete water submergence survival",
        "developing_institution": "Central Rice Research Institute (CRRI)",
        "genetic_purity_score": 99.40,
        "heritability_broad_sense": 0.78,
        "drought_susceptibility_index": 0.74,
        "harvest_index_pct": 42.0,
        "recommended_agro_climatic_zones": [
            "Zone 1: Indo-Gangetic Plains & Central Plateau",
            "Zone 2: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0092",
        "variety_name": "Rice CR Dhan 801 Genotype Line v10",
        "target_trait": "Drought + Submergence Dual Tolerance",
        "major_qtl_markers": "qDTY1.1, qDTY2.1, Sub1A",
        "agronomic_description": "Climate-resilient dual tolerant line for rainfed drought-prone and flood-prone ecologies",
        "developing_institution": "ICAR-NRRI",
        "genetic_purity_score": 99.50,
        "heritability_broad_sense": 0.79,
        "drought_susceptibility_index": 0.76,
        "harvest_index_pct": 42.8,
        "recommended_agro_climatic_zones": [
            "Zone 2: Indo-Gangetic Plains & Central Plateau",
            "Zone 3: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0093",
        "variety_name": "Wheat DBW 303 (Karan Vaishnavi) Genotype Line v10",
        "target_trait": "Terminal Heat Stress Resistance",
        "major_qtl_markers": "TaHsfA2d, TaFER-5B",
        "agronomic_description": "High-yielding irrigated timely sown bread wheat with extreme heat resilience during grain filling",
        "developing_institution": "ICAR-IIWBR",
        "genetic_purity_score": 99.60,
        "heritability_broad_sense": 0.80,
        "drought_susceptibility_index": 0.78,
        "harvest_index_pct": 43.6,
        "recommended_agro_climatic_zones": [
            "Zone 3: Indo-Gangetic Plains & Central Plateau",
            "Zone 4: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0094",
        "variety_name": "Wheat HD 3226 (Pusa Yashasvi) Genotype Line v10",
        "target_trait": "Multi-Rust Resistance (Yellow, Brown, Black)",
        "major_qtl_markers": "Yr17, Lr37, Sr38",
        "agronomic_description": "Superior chapati-making and biscuit-making quality with high gluten strength",
        "developing_institution": "ICAR-IARI",
        "genetic_purity_score": 99.70,
        "heritability_broad_sense": 0.81,
        "drought_susceptibility_index": 0.80,
        "harvest_index_pct": 44.4,
        "recommended_agro_climatic_zones": [
            "Zone 4: Indo-Gangetic Plains & Central Plateau",
            "Zone 5: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0095",
        "variety_name": "Chickpea Pusa 10216 Genotype Line v10",
        "target_trait": "Drought Drought Tolerance & Root Architecture",
        "major_qtl_markers": "qRT9.1, QTL-hotspot genomic region",
        "agronomic_description": "Desi chickpea with deep taproot system and high water use efficiency under dryland",
        "developing_institution": "ICAR-IARI",
        "genetic_purity_score": 99.80,
        "heritability_broad_sense": 0.82,
        "drought_susceptibility_index": 0.82,
        "harvest_index_pct": 45.2,
        "recommended_agro_climatic_zones": [
            "Zone 5: Indo-Gangetic Plains & Central Plateau",
            "Zone 6: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0096",
        "variety_name": "Pigeonpea BDN 711 Genotype Line v10",
        "target_trait": "Fusarium Wilt & Sterility Mosaic Tolerance",
        "major_qtl_markers": "Cc-RFLP-Wilt1",
        "agronomic_description": "White seeded medium duration variety highly adapted to rainfed black cotton vertisols",
        "developing_institution": "VNMKV",
        "genetic_purity_score": 99.90,
        "heritability_broad_sense": 0.83,
        "drought_susceptibility_index": 0.84,
        "harvest_index_pct": 46.0,
        "recommended_agro_climatic_zones": [
            "Zone 6: Indo-Gangetic Plains & Central Plateau",
            "Zone 7: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0097",
        "variety_name": "Mustard PM 28 Genotype Line v10",
        "target_trait": "High Oleic / Low Glucosinolate Double Zero Quality",
        "major_qtl_markers": "FAD2 mutation, GSL1 deletion",
        "agronomic_description": "Canola quality Brassica juncea with heart-healthy fatty acid profile",
        "developing_institution": "ICAR-DRMR",
        "genetic_purity_score": 99.20,
        "heritability_broad_sense": 0.84,
        "drought_susceptibility_index": 0.62,
        "harvest_index_pct": 46.8,
        "recommended_agro_climatic_zones": [
            "Zone 7: Indo-Gangetic Plains & Central Plateau",
            "Zone 8: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0098",
        "variety_name": "Cotton Bunny Bt (NCS 145) Genotype Line v10",
        "target_trait": "Bollworm Resistance & Sucking Pest Tolerance",
        "major_qtl_markers": "Cry1Ac + Cry2Ab (Bollgard II)",
        "agronomic_description": "High boll retention, exceptional ginning outturn (36%), and staple length (31mm)",
        "developing_institution": "Nuziveedu Seeds",
        "genetic_purity_score": 99.30,
        "heritability_broad_sense": 0.85,
        "drought_susceptibility_index": 0.64,
        "harvest_index_pct": 47.6,
        "recommended_agro_climatic_zones": [
            "Zone 8: Indo-Gangetic Plains & Central Plateau",
            "Zone 9: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0099",
        "variety_name": "Tomato Arka Rakshak (F1 Hybrid) Genotype Line v10",
        "target_trait": "Triple Disease Resistance (ToLCV, BW, EB)",
        "major_qtl_markers": "Ty-2, Ty-3, Bwr-12, Ph-3",
        "agronomic_description": "High yielding indeterminate tomato with resistance to leaf curl virus, bacterial wilt, and early blight",
        "developing_institution": "ICAR-IIHR",
        "genetic_purity_score": 99.40,
        "heritability_broad_sense": 0.86,
        "drought_susceptibility_index": 0.66,
        "harvest_index_pct": 48.4,
        "recommended_agro_climatic_zones": [
            "Zone 9: Indo-Gangetic Plains & Central Plateau",
            "Zone 10: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0100",
        "variety_name": "Chilli Arka Harita Genotype Line v10",
        "target_trait": "Powdery Mildew & Anthracnose Tolerance",
        "major_qtl_markers": "Pm-1, Colletotrichum-R1",
        "agronomic_description": "High pungency (0.45% capsaicin) dual-purpose hybrid for green and dry red chilli export",
        "developing_institution": "ICAR-IIHR",
        "genetic_purity_score": 99.50,
        "heritability_broad_sense": 0.87,
        "drought_susceptibility_index": 0.68,
        "harvest_index_pct": 49.2,
        "recommended_agro_climatic_zones": [
            "Zone 10: Indo-Gangetic Plains & Central Plateau",
            "Zone 11: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0101",
        "variety_name": "Rice Swarna Sub1 Genotype Line v11",
        "target_trait": "Submergence / Flash Flood Tolerance",
        "major_qtl_markers": "Sub1A Transcription Factor",
        "agronomic_description": "Direct seeded or transplanted lowland rice with 14-day complete water submergence survival",
        "developing_institution": "Central Rice Research Institute (CRRI)",
        "genetic_purity_score": 99.60,
        "heritability_broad_sense": 0.88,
        "drought_susceptibility_index": 0.70,
        "harvest_index_pct": 42.0,
        "recommended_agro_climatic_zones": [
            "Zone 11: Indo-Gangetic Plains & Central Plateau",
            "Zone 12: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0102",
        "variety_name": "Rice CR Dhan 801 Genotype Line v11",
        "target_trait": "Drought + Submergence Dual Tolerance",
        "major_qtl_markers": "qDTY1.1, qDTY2.1, Sub1A",
        "agronomic_description": "Climate-resilient dual tolerant line for rainfed drought-prone and flood-prone ecologies",
        "developing_institution": "ICAR-NRRI",
        "genetic_purity_score": 99.70,
        "heritability_broad_sense": 0.89,
        "drought_susceptibility_index": 0.72,
        "harvest_index_pct": 42.8,
        "recommended_agro_climatic_zones": [
            "Zone 12: Indo-Gangetic Plains & Central Plateau",
            "Zone 13: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0103",
        "variety_name": "Wheat DBW 303 (Karan Vaishnavi) Genotype Line v11",
        "target_trait": "Terminal Heat Stress Resistance",
        "major_qtl_markers": "TaHsfA2d, TaFER-5B",
        "agronomic_description": "High-yielding irrigated timely sown bread wheat with extreme heat resilience during grain filling",
        "developing_institution": "ICAR-IIWBR",
        "genetic_purity_score": 99.80,
        "heritability_broad_sense": 0.90,
        "drought_susceptibility_index": 0.74,
        "harvest_index_pct": 43.6,
        "recommended_agro_climatic_zones": [
            "Zone 13: Indo-Gangetic Plains & Central Plateau",
            "Zone 14: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0104",
        "variety_name": "Wheat HD 3226 (Pusa Yashasvi) Genotype Line v11",
        "target_trait": "Multi-Rust Resistance (Yellow, Brown, Black)",
        "major_qtl_markers": "Yr17, Lr37, Sr38",
        "agronomic_description": "Superior chapati-making and biscuit-making quality with high gluten strength",
        "developing_institution": "ICAR-IARI",
        "genetic_purity_score": 99.90,
        "heritability_broad_sense": 0.91,
        "drought_susceptibility_index": 0.76,
        "harvest_index_pct": 44.4,
        "recommended_agro_climatic_zones": [
            "Zone 14: Indo-Gangetic Plains & Central Plateau",
            "Zone 15: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0105",
        "variety_name": "Chickpea Pusa 10216 Genotype Line v11",
        "target_trait": "Drought Drought Tolerance & Root Architecture",
        "major_qtl_markers": "qRT9.1, QTL-hotspot genomic region",
        "agronomic_description": "Desi chickpea with deep taproot system and high water use efficiency under dryland",
        "developing_institution": "ICAR-IARI",
        "genetic_purity_score": 99.20,
        "heritability_broad_sense": 0.92,
        "drought_susceptibility_index": 0.78,
        "harvest_index_pct": 45.2,
        "recommended_agro_climatic_zones": [
            "Zone 15: Indo-Gangetic Plains & Central Plateau",
            "Zone 1: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0106",
        "variety_name": "Pigeonpea BDN 711 Genotype Line v11",
        "target_trait": "Fusarium Wilt & Sterility Mosaic Tolerance",
        "major_qtl_markers": "Cc-RFLP-Wilt1",
        "agronomic_description": "White seeded medium duration variety highly adapted to rainfed black cotton vertisols",
        "developing_institution": "VNMKV",
        "genetic_purity_score": 99.30,
        "heritability_broad_sense": 0.93,
        "drought_susceptibility_index": 0.80,
        "harvest_index_pct": 46.0,
        "recommended_agro_climatic_zones": [
            "Zone 1: Indo-Gangetic Plains & Central Plateau",
            "Zone 2: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0107",
        "variety_name": "Mustard PM 28 Genotype Line v11",
        "target_trait": "High Oleic / Low Glucosinolate Double Zero Quality",
        "major_qtl_markers": "FAD2 mutation, GSL1 deletion",
        "agronomic_description": "Canola quality Brassica juncea with heart-healthy fatty acid profile",
        "developing_institution": "ICAR-DRMR",
        "genetic_purity_score": 99.40,
        "heritability_broad_sense": 0.94,
        "drought_susceptibility_index": 0.82,
        "harvest_index_pct": 46.8,
        "recommended_agro_climatic_zones": [
            "Zone 2: Indo-Gangetic Plains & Central Plateau",
            "Zone 3: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0108",
        "variety_name": "Cotton Bunny Bt (NCS 145) Genotype Line v11",
        "target_trait": "Bollworm Resistance & Sucking Pest Tolerance",
        "major_qtl_markers": "Cry1Ac + Cry2Ab (Bollgard II)",
        "agronomic_description": "High boll retention, exceptional ginning outturn (36%), and staple length (31mm)",
        "developing_institution": "Nuziveedu Seeds",
        "genetic_purity_score": 99.50,
        "heritability_broad_sense": 0.95,
        "drought_susceptibility_index": 0.84,
        "harvest_index_pct": 47.6,
        "recommended_agro_climatic_zones": [
            "Zone 3: Indo-Gangetic Plains & Central Plateau",
            "Zone 4: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0109",
        "variety_name": "Tomato Arka Rakshak (F1 Hybrid) Genotype Line v11",
        "target_trait": "Triple Disease Resistance (ToLCV, BW, EB)",
        "major_qtl_markers": "Ty-2, Ty-3, Bwr-12, Ph-3",
        "agronomic_description": "High yielding indeterminate tomato with resistance to leaf curl virus, bacterial wilt, and early blight",
        "developing_institution": "ICAR-IIHR",
        "genetic_purity_score": 99.60,
        "heritability_broad_sense": 0.78,
        "drought_susceptibility_index": 0.62,
        "harvest_index_pct": 48.4,
        "recommended_agro_climatic_zones": [
            "Zone 4: Indo-Gangetic Plains & Central Plateau",
            "Zone 5: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0110",
        "variety_name": "Chilli Arka Harita Genotype Line v11",
        "target_trait": "Powdery Mildew & Anthracnose Tolerance",
        "major_qtl_markers": "Pm-1, Colletotrichum-R1",
        "agronomic_description": "High pungency (0.45% capsaicin) dual-purpose hybrid for green and dry red chilli export",
        "developing_institution": "ICAR-IIHR",
        "genetic_purity_score": 99.70,
        "heritability_broad_sense": 0.79,
        "drought_susceptibility_index": 0.64,
        "harvest_index_pct": 49.2,
        "recommended_agro_climatic_zones": [
            "Zone 5: Indo-Gangetic Plains & Central Plateau",
            "Zone 6: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0111",
        "variety_name": "Rice Swarna Sub1 Genotype Line v12",
        "target_trait": "Submergence / Flash Flood Tolerance",
        "major_qtl_markers": "Sub1A Transcription Factor",
        "agronomic_description": "Direct seeded or transplanted lowland rice with 14-day complete water submergence survival",
        "developing_institution": "Central Rice Research Institute (CRRI)",
        "genetic_purity_score": 99.80,
        "heritability_broad_sense": 0.80,
        "drought_susceptibility_index": 0.66,
        "harvest_index_pct": 42.0,
        "recommended_agro_climatic_zones": [
            "Zone 6: Indo-Gangetic Plains & Central Plateau",
            "Zone 7: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0112",
        "variety_name": "Rice CR Dhan 801 Genotype Line v12",
        "target_trait": "Drought + Submergence Dual Tolerance",
        "major_qtl_markers": "qDTY1.1, qDTY2.1, Sub1A",
        "agronomic_description": "Climate-resilient dual tolerant line for rainfed drought-prone and flood-prone ecologies",
        "developing_institution": "ICAR-NRRI",
        "genetic_purity_score": 99.90,
        "heritability_broad_sense": 0.81,
        "drought_susceptibility_index": 0.68,
        "harvest_index_pct": 42.8,
        "recommended_agro_climatic_zones": [
            "Zone 7: Indo-Gangetic Plains & Central Plateau",
            "Zone 8: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0113",
        "variety_name": "Wheat DBW 303 (Karan Vaishnavi) Genotype Line v12",
        "target_trait": "Terminal Heat Stress Resistance",
        "major_qtl_markers": "TaHsfA2d, TaFER-5B",
        "agronomic_description": "High-yielding irrigated timely sown bread wheat with extreme heat resilience during grain filling",
        "developing_institution": "ICAR-IIWBR",
        "genetic_purity_score": 99.20,
        "heritability_broad_sense": 0.82,
        "drought_susceptibility_index": 0.70,
        "harvest_index_pct": 43.6,
        "recommended_agro_climatic_zones": [
            "Zone 8: Indo-Gangetic Plains & Central Plateau",
            "Zone 9: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0114",
        "variety_name": "Wheat HD 3226 (Pusa Yashasvi) Genotype Line v12",
        "target_trait": "Multi-Rust Resistance (Yellow, Brown, Black)",
        "major_qtl_markers": "Yr17, Lr37, Sr38",
        "agronomic_description": "Superior chapati-making and biscuit-making quality with high gluten strength",
        "developing_institution": "ICAR-IARI",
        "genetic_purity_score": 99.30,
        "heritability_broad_sense": 0.83,
        "drought_susceptibility_index": 0.72,
        "harvest_index_pct": 44.4,
        "recommended_agro_climatic_zones": [
            "Zone 9: Indo-Gangetic Plains & Central Plateau",
            "Zone 10: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0115",
        "variety_name": "Chickpea Pusa 10216 Genotype Line v12",
        "target_trait": "Drought Drought Tolerance & Root Architecture",
        "major_qtl_markers": "qRT9.1, QTL-hotspot genomic region",
        "agronomic_description": "Desi chickpea with deep taproot system and high water use efficiency under dryland",
        "developing_institution": "ICAR-IARI",
        "genetic_purity_score": 99.40,
        "heritability_broad_sense": 0.84,
        "drought_susceptibility_index": 0.74,
        "harvest_index_pct": 45.2,
        "recommended_agro_climatic_zones": [
            "Zone 10: Indo-Gangetic Plains & Central Plateau",
            "Zone 11: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0116",
        "variety_name": "Pigeonpea BDN 711 Genotype Line v12",
        "target_trait": "Fusarium Wilt & Sterility Mosaic Tolerance",
        "major_qtl_markers": "Cc-RFLP-Wilt1",
        "agronomic_description": "White seeded medium duration variety highly adapted to rainfed black cotton vertisols",
        "developing_institution": "VNMKV",
        "genetic_purity_score": 99.50,
        "heritability_broad_sense": 0.85,
        "drought_susceptibility_index": 0.76,
        "harvest_index_pct": 46.0,
        "recommended_agro_climatic_zones": [
            "Zone 11: Indo-Gangetic Plains & Central Plateau",
            "Zone 12: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0117",
        "variety_name": "Mustard PM 28 Genotype Line v12",
        "target_trait": "High Oleic / Low Glucosinolate Double Zero Quality",
        "major_qtl_markers": "FAD2 mutation, GSL1 deletion",
        "agronomic_description": "Canola quality Brassica juncea with heart-healthy fatty acid profile",
        "developing_institution": "ICAR-DRMR",
        "genetic_purity_score": 99.60,
        "heritability_broad_sense": 0.86,
        "drought_susceptibility_index": 0.78,
        "harvest_index_pct": 46.8,
        "recommended_agro_climatic_zones": [
            "Zone 12: Indo-Gangetic Plains & Central Plateau",
            "Zone 13: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0118",
        "variety_name": "Cotton Bunny Bt (NCS 145) Genotype Line v12",
        "target_trait": "Bollworm Resistance & Sucking Pest Tolerance",
        "major_qtl_markers": "Cry1Ac + Cry2Ab (Bollgard II)",
        "agronomic_description": "High boll retention, exceptional ginning outturn (36%), and staple length (31mm)",
        "developing_institution": "Nuziveedu Seeds",
        "genetic_purity_score": 99.70,
        "heritability_broad_sense": 0.87,
        "drought_susceptibility_index": 0.80,
        "harvest_index_pct": 47.6,
        "recommended_agro_climatic_zones": [
            "Zone 13: Indo-Gangetic Plains & Central Plateau",
            "Zone 14: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0119",
        "variety_name": "Tomato Arka Rakshak (F1 Hybrid) Genotype Line v12",
        "target_trait": "Triple Disease Resistance (ToLCV, BW, EB)",
        "major_qtl_markers": "Ty-2, Ty-3, Bwr-12, Ph-3",
        "agronomic_description": "High yielding indeterminate tomato with resistance to leaf curl virus, bacterial wilt, and early blight",
        "developing_institution": "ICAR-IIHR",
        "genetic_purity_score": 99.80,
        "heritability_broad_sense": 0.88,
        "drought_susceptibility_index": 0.82,
        "harvest_index_pct": 48.4,
        "recommended_agro_climatic_zones": [
            "Zone 14: Indo-Gangetic Plains & Central Plateau",
            "Zone 15: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0120",
        "variety_name": "Chilli Arka Harita Genotype Line v12",
        "target_trait": "Powdery Mildew & Anthracnose Tolerance",
        "major_qtl_markers": "Pm-1, Colletotrichum-R1",
        "agronomic_description": "High pungency (0.45% capsaicin) dual-purpose hybrid for green and dry red chilli export",
        "developing_institution": "ICAR-IIHR",
        "genetic_purity_score": 99.90,
        "heritability_broad_sense": 0.89,
        "drought_susceptibility_index": 0.84,
        "harvest_index_pct": 49.2,
        "recommended_agro_climatic_zones": [
            "Zone 15: Indo-Gangetic Plains & Central Plateau",
            "Zone 1: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0121",
        "variety_name": "Rice Swarna Sub1 Genotype Line v13",
        "target_trait": "Submergence / Flash Flood Tolerance",
        "major_qtl_markers": "Sub1A Transcription Factor",
        "agronomic_description": "Direct seeded or transplanted lowland rice with 14-day complete water submergence survival",
        "developing_institution": "Central Rice Research Institute (CRRI)",
        "genetic_purity_score": 99.20,
        "heritability_broad_sense": 0.90,
        "drought_susceptibility_index": 0.62,
        "harvest_index_pct": 42.0,
        "recommended_agro_climatic_zones": [
            "Zone 1: Indo-Gangetic Plains & Central Plateau",
            "Zone 2: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0122",
        "variety_name": "Rice CR Dhan 801 Genotype Line v13",
        "target_trait": "Drought + Submergence Dual Tolerance",
        "major_qtl_markers": "qDTY1.1, qDTY2.1, Sub1A",
        "agronomic_description": "Climate-resilient dual tolerant line for rainfed drought-prone and flood-prone ecologies",
        "developing_institution": "ICAR-NRRI",
        "genetic_purity_score": 99.30,
        "heritability_broad_sense": 0.91,
        "drought_susceptibility_index": 0.64,
        "harvest_index_pct": 42.8,
        "recommended_agro_climatic_zones": [
            "Zone 2: Indo-Gangetic Plains & Central Plateau",
            "Zone 3: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0123",
        "variety_name": "Wheat DBW 303 (Karan Vaishnavi) Genotype Line v13",
        "target_trait": "Terminal Heat Stress Resistance",
        "major_qtl_markers": "TaHsfA2d, TaFER-5B",
        "agronomic_description": "High-yielding irrigated timely sown bread wheat with extreme heat resilience during grain filling",
        "developing_institution": "ICAR-IIWBR",
        "genetic_purity_score": 99.40,
        "heritability_broad_sense": 0.92,
        "drought_susceptibility_index": 0.66,
        "harvest_index_pct": 43.6,
        "recommended_agro_climatic_zones": [
            "Zone 3: Indo-Gangetic Plains & Central Plateau",
            "Zone 4: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0124",
        "variety_name": "Wheat HD 3226 (Pusa Yashasvi) Genotype Line v13",
        "target_trait": "Multi-Rust Resistance (Yellow, Brown, Black)",
        "major_qtl_markers": "Yr17, Lr37, Sr38",
        "agronomic_description": "Superior chapati-making and biscuit-making quality with high gluten strength",
        "developing_institution": "ICAR-IARI",
        "genetic_purity_score": 99.50,
        "heritability_broad_sense": 0.93,
        "drought_susceptibility_index": 0.68,
        "harvest_index_pct": 44.4,
        "recommended_agro_climatic_zones": [
            "Zone 4: Indo-Gangetic Plains & Central Plateau",
            "Zone 5: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0125",
        "variety_name": "Chickpea Pusa 10216 Genotype Line v13",
        "target_trait": "Drought Drought Tolerance & Root Architecture",
        "major_qtl_markers": "qRT9.1, QTL-hotspot genomic region",
        "agronomic_description": "Desi chickpea with deep taproot system and high water use efficiency under dryland",
        "developing_institution": "ICAR-IARI",
        "genetic_purity_score": 99.60,
        "heritability_broad_sense": 0.94,
        "drought_susceptibility_index": 0.70,
        "harvest_index_pct": 45.2,
        "recommended_agro_climatic_zones": [
            "Zone 5: Indo-Gangetic Plains & Central Plateau",
            "Zone 6: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0126",
        "variety_name": "Pigeonpea BDN 711 Genotype Line v13",
        "target_trait": "Fusarium Wilt & Sterility Mosaic Tolerance",
        "major_qtl_markers": "Cc-RFLP-Wilt1",
        "agronomic_description": "White seeded medium duration variety highly adapted to rainfed black cotton vertisols",
        "developing_institution": "VNMKV",
        "genetic_purity_score": 99.70,
        "heritability_broad_sense": 0.95,
        "drought_susceptibility_index": 0.72,
        "harvest_index_pct": 46.0,
        "recommended_agro_climatic_zones": [
            "Zone 6: Indo-Gangetic Plains & Central Plateau",
            "Zone 7: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0127",
        "variety_name": "Mustard PM 28 Genotype Line v13",
        "target_trait": "High Oleic / Low Glucosinolate Double Zero Quality",
        "major_qtl_markers": "FAD2 mutation, GSL1 deletion",
        "agronomic_description": "Canola quality Brassica juncea with heart-healthy fatty acid profile",
        "developing_institution": "ICAR-DRMR",
        "genetic_purity_score": 99.80,
        "heritability_broad_sense": 0.78,
        "drought_susceptibility_index": 0.74,
        "harvest_index_pct": 46.8,
        "recommended_agro_climatic_zones": [
            "Zone 7: Indo-Gangetic Plains & Central Plateau",
            "Zone 8: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0128",
        "variety_name": "Cotton Bunny Bt (NCS 145) Genotype Line v13",
        "target_trait": "Bollworm Resistance & Sucking Pest Tolerance",
        "major_qtl_markers": "Cry1Ac + Cry2Ab (Bollgard II)",
        "agronomic_description": "High boll retention, exceptional ginning outturn (36%), and staple length (31mm)",
        "developing_institution": "Nuziveedu Seeds",
        "genetic_purity_score": 99.90,
        "heritability_broad_sense": 0.79,
        "drought_susceptibility_index": 0.76,
        "harvest_index_pct": 47.6,
        "recommended_agro_climatic_zones": [
            "Zone 8: Indo-Gangetic Plains & Central Plateau",
            "Zone 9: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0129",
        "variety_name": "Tomato Arka Rakshak (F1 Hybrid) Genotype Line v13",
        "target_trait": "Triple Disease Resistance (ToLCV, BW, EB)",
        "major_qtl_markers": "Ty-2, Ty-3, Bwr-12, Ph-3",
        "agronomic_description": "High yielding indeterminate tomato with resistance to leaf curl virus, bacterial wilt, and early blight",
        "developing_institution": "ICAR-IIHR",
        "genetic_purity_score": 99.20,
        "heritability_broad_sense": 0.80,
        "drought_susceptibility_index": 0.78,
        "harvest_index_pct": 48.4,
        "recommended_agro_climatic_zones": [
            "Zone 9: Indo-Gangetic Plains & Central Plateau",
            "Zone 10: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0130",
        "variety_name": "Chilli Arka Harita Genotype Line v13",
        "target_trait": "Powdery Mildew & Anthracnose Tolerance",
        "major_qtl_markers": "Pm-1, Colletotrichum-R1",
        "agronomic_description": "High pungency (0.45% capsaicin) dual-purpose hybrid for green and dry red chilli export",
        "developing_institution": "ICAR-IIHR",
        "genetic_purity_score": 99.30,
        "heritability_broad_sense": 0.81,
        "drought_susceptibility_index": 0.80,
        "harvest_index_pct": 49.2,
        "recommended_agro_climatic_zones": [
            "Zone 10: Indo-Gangetic Plains & Central Plateau",
            "Zone 11: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0131",
        "variety_name": "Rice Swarna Sub1 Genotype Line v14",
        "target_trait": "Submergence / Flash Flood Tolerance",
        "major_qtl_markers": "Sub1A Transcription Factor",
        "agronomic_description": "Direct seeded or transplanted lowland rice with 14-day complete water submergence survival",
        "developing_institution": "Central Rice Research Institute (CRRI)",
        "genetic_purity_score": 99.40,
        "heritability_broad_sense": 0.82,
        "drought_susceptibility_index": 0.82,
        "harvest_index_pct": 42.0,
        "recommended_agro_climatic_zones": [
            "Zone 11: Indo-Gangetic Plains & Central Plateau",
            "Zone 12: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0132",
        "variety_name": "Rice CR Dhan 801 Genotype Line v14",
        "target_trait": "Drought + Submergence Dual Tolerance",
        "major_qtl_markers": "qDTY1.1, qDTY2.1, Sub1A",
        "agronomic_description": "Climate-resilient dual tolerant line for rainfed drought-prone and flood-prone ecologies",
        "developing_institution": "ICAR-NRRI",
        "genetic_purity_score": 99.50,
        "heritability_broad_sense": 0.83,
        "drought_susceptibility_index": 0.84,
        "harvest_index_pct": 42.8,
        "recommended_agro_climatic_zones": [
            "Zone 12: Indo-Gangetic Plains & Central Plateau",
            "Zone 13: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0133",
        "variety_name": "Wheat DBW 303 (Karan Vaishnavi) Genotype Line v14",
        "target_trait": "Terminal Heat Stress Resistance",
        "major_qtl_markers": "TaHsfA2d, TaFER-5B",
        "agronomic_description": "High-yielding irrigated timely sown bread wheat with extreme heat resilience during grain filling",
        "developing_institution": "ICAR-IIWBR",
        "genetic_purity_score": 99.60,
        "heritability_broad_sense": 0.84,
        "drought_susceptibility_index": 0.62,
        "harvest_index_pct": 43.6,
        "recommended_agro_climatic_zones": [
            "Zone 13: Indo-Gangetic Plains & Central Plateau",
            "Zone 14: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0134",
        "variety_name": "Wheat HD 3226 (Pusa Yashasvi) Genotype Line v14",
        "target_trait": "Multi-Rust Resistance (Yellow, Brown, Black)",
        "major_qtl_markers": "Yr17, Lr37, Sr38",
        "agronomic_description": "Superior chapati-making and biscuit-making quality with high gluten strength",
        "developing_institution": "ICAR-IARI",
        "genetic_purity_score": 99.70,
        "heritability_broad_sense": 0.85,
        "drought_susceptibility_index": 0.64,
        "harvest_index_pct": 44.4,
        "recommended_agro_climatic_zones": [
            "Zone 14: Indo-Gangetic Plains & Central Plateau",
            "Zone 15: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0135",
        "variety_name": "Chickpea Pusa 10216 Genotype Line v14",
        "target_trait": "Drought Drought Tolerance & Root Architecture",
        "major_qtl_markers": "qRT9.1, QTL-hotspot genomic region",
        "agronomic_description": "Desi chickpea with deep taproot system and high water use efficiency under dryland",
        "developing_institution": "ICAR-IARI",
        "genetic_purity_score": 99.80,
        "heritability_broad_sense": 0.86,
        "drought_susceptibility_index": 0.66,
        "harvest_index_pct": 45.2,
        "recommended_agro_climatic_zones": [
            "Zone 15: Indo-Gangetic Plains & Central Plateau",
            "Zone 1: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0136",
        "variety_name": "Pigeonpea BDN 711 Genotype Line v14",
        "target_trait": "Fusarium Wilt & Sterility Mosaic Tolerance",
        "major_qtl_markers": "Cc-RFLP-Wilt1",
        "agronomic_description": "White seeded medium duration variety highly adapted to rainfed black cotton vertisols",
        "developing_institution": "VNMKV",
        "genetic_purity_score": 99.90,
        "heritability_broad_sense": 0.87,
        "drought_susceptibility_index": 0.68,
        "harvest_index_pct": 46.0,
        "recommended_agro_climatic_zones": [
            "Zone 1: Indo-Gangetic Plains & Central Plateau",
            "Zone 2: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0137",
        "variety_name": "Mustard PM 28 Genotype Line v14",
        "target_trait": "High Oleic / Low Glucosinolate Double Zero Quality",
        "major_qtl_markers": "FAD2 mutation, GSL1 deletion",
        "agronomic_description": "Canola quality Brassica juncea with heart-healthy fatty acid profile",
        "developing_institution": "ICAR-DRMR",
        "genetic_purity_score": 99.20,
        "heritability_broad_sense": 0.88,
        "drought_susceptibility_index": 0.70,
        "harvest_index_pct": 46.8,
        "recommended_agro_climatic_zones": [
            "Zone 2: Indo-Gangetic Plains & Central Plateau",
            "Zone 3: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0138",
        "variety_name": "Cotton Bunny Bt (NCS 145) Genotype Line v14",
        "target_trait": "Bollworm Resistance & Sucking Pest Tolerance",
        "major_qtl_markers": "Cry1Ac + Cry2Ab (Bollgard II)",
        "agronomic_description": "High boll retention, exceptional ginning outturn (36%), and staple length (31mm)",
        "developing_institution": "Nuziveedu Seeds",
        "genetic_purity_score": 99.30,
        "heritability_broad_sense": 0.89,
        "drought_susceptibility_index": 0.72,
        "harvest_index_pct": 47.6,
        "recommended_agro_climatic_zones": [
            "Zone 3: Indo-Gangetic Plains & Central Plateau",
            "Zone 4: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0139",
        "variety_name": "Tomato Arka Rakshak (F1 Hybrid) Genotype Line v14",
        "target_trait": "Triple Disease Resistance (ToLCV, BW, EB)",
        "major_qtl_markers": "Ty-2, Ty-3, Bwr-12, Ph-3",
        "agronomic_description": "High yielding indeterminate tomato with resistance to leaf curl virus, bacterial wilt, and early blight",
        "developing_institution": "ICAR-IIHR",
        "genetic_purity_score": 99.40,
        "heritability_broad_sense": 0.90,
        "drought_susceptibility_index": 0.74,
        "harvest_index_pct": 48.4,
        "recommended_agro_climatic_zones": [
            "Zone 4: Indo-Gangetic Plains & Central Plateau",
            "Zone 5: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0140",
        "variety_name": "Chilli Arka Harita Genotype Line v14",
        "target_trait": "Powdery Mildew & Anthracnose Tolerance",
        "major_qtl_markers": "Pm-1, Colletotrichum-R1",
        "agronomic_description": "High pungency (0.45% capsaicin) dual-purpose hybrid for green and dry red chilli export",
        "developing_institution": "ICAR-IIHR",
        "genetic_purity_score": 99.50,
        "heritability_broad_sense": 0.91,
        "drought_susceptibility_index": 0.76,
        "harvest_index_pct": 49.2,
        "recommended_agro_climatic_zones": [
            "Zone 5: Indo-Gangetic Plains & Central Plateau",
            "Zone 6: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0141",
        "variety_name": "Rice Swarna Sub1 Genotype Line v15",
        "target_trait": "Submergence / Flash Flood Tolerance",
        "major_qtl_markers": "Sub1A Transcription Factor",
        "agronomic_description": "Direct seeded or transplanted lowland rice with 14-day complete water submergence survival",
        "developing_institution": "Central Rice Research Institute (CRRI)",
        "genetic_purity_score": 99.60,
        "heritability_broad_sense": 0.92,
        "drought_susceptibility_index": 0.78,
        "harvest_index_pct": 42.0,
        "recommended_agro_climatic_zones": [
            "Zone 6: Indo-Gangetic Plains & Central Plateau",
            "Zone 7: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0142",
        "variety_name": "Rice CR Dhan 801 Genotype Line v15",
        "target_trait": "Drought + Submergence Dual Tolerance",
        "major_qtl_markers": "qDTY1.1, qDTY2.1, Sub1A",
        "agronomic_description": "Climate-resilient dual tolerant line for rainfed drought-prone and flood-prone ecologies",
        "developing_institution": "ICAR-NRRI",
        "genetic_purity_score": 99.70,
        "heritability_broad_sense": 0.93,
        "drought_susceptibility_index": 0.80,
        "harvest_index_pct": 42.8,
        "recommended_agro_climatic_zones": [
            "Zone 7: Indo-Gangetic Plains & Central Plateau",
            "Zone 8: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0143",
        "variety_name": "Wheat DBW 303 (Karan Vaishnavi) Genotype Line v15",
        "target_trait": "Terminal Heat Stress Resistance",
        "major_qtl_markers": "TaHsfA2d, TaFER-5B",
        "agronomic_description": "High-yielding irrigated timely sown bread wheat with extreme heat resilience during grain filling",
        "developing_institution": "ICAR-IIWBR",
        "genetic_purity_score": 99.80,
        "heritability_broad_sense": 0.94,
        "drought_susceptibility_index": 0.82,
        "harvest_index_pct": 43.6,
        "recommended_agro_climatic_zones": [
            "Zone 8: Indo-Gangetic Plains & Central Plateau",
            "Zone 9: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0144",
        "variety_name": "Wheat HD 3226 (Pusa Yashasvi) Genotype Line v15",
        "target_trait": "Multi-Rust Resistance (Yellow, Brown, Black)",
        "major_qtl_markers": "Yr17, Lr37, Sr38",
        "agronomic_description": "Superior chapati-making and biscuit-making quality with high gluten strength",
        "developing_institution": "ICAR-IARI",
        "genetic_purity_score": 99.90,
        "heritability_broad_sense": 0.95,
        "drought_susceptibility_index": 0.84,
        "harvest_index_pct": 44.4,
        "recommended_agro_climatic_zones": [
            "Zone 9: Indo-Gangetic Plains & Central Plateau",
            "Zone 10: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0145",
        "variety_name": "Chickpea Pusa 10216 Genotype Line v15",
        "target_trait": "Drought Drought Tolerance & Root Architecture",
        "major_qtl_markers": "qRT9.1, QTL-hotspot genomic region",
        "agronomic_description": "Desi chickpea with deep taproot system and high water use efficiency under dryland",
        "developing_institution": "ICAR-IARI",
        "genetic_purity_score": 99.20,
        "heritability_broad_sense": 0.78,
        "drought_susceptibility_index": 0.62,
        "harvest_index_pct": 45.2,
        "recommended_agro_climatic_zones": [
            "Zone 10: Indo-Gangetic Plains & Central Plateau",
            "Zone 11: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0146",
        "variety_name": "Pigeonpea BDN 711 Genotype Line v15",
        "target_trait": "Fusarium Wilt & Sterility Mosaic Tolerance",
        "major_qtl_markers": "Cc-RFLP-Wilt1",
        "agronomic_description": "White seeded medium duration variety highly adapted to rainfed black cotton vertisols",
        "developing_institution": "VNMKV",
        "genetic_purity_score": 99.30,
        "heritability_broad_sense": 0.79,
        "drought_susceptibility_index": 0.64,
        "harvest_index_pct": 46.0,
        "recommended_agro_climatic_zones": [
            "Zone 11: Indo-Gangetic Plains & Central Plateau",
            "Zone 12: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0147",
        "variety_name": "Mustard PM 28 Genotype Line v15",
        "target_trait": "High Oleic / Low Glucosinolate Double Zero Quality",
        "major_qtl_markers": "FAD2 mutation, GSL1 deletion",
        "agronomic_description": "Canola quality Brassica juncea with heart-healthy fatty acid profile",
        "developing_institution": "ICAR-DRMR",
        "genetic_purity_score": 99.40,
        "heritability_broad_sense": 0.80,
        "drought_susceptibility_index": 0.66,
        "harvest_index_pct": 46.8,
        "recommended_agro_climatic_zones": [
            "Zone 12: Indo-Gangetic Plains & Central Plateau",
            "Zone 13: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0148",
        "variety_name": "Cotton Bunny Bt (NCS 145) Genotype Line v15",
        "target_trait": "Bollworm Resistance & Sucking Pest Tolerance",
        "major_qtl_markers": "Cry1Ac + Cry2Ab (Bollgard II)",
        "agronomic_description": "High boll retention, exceptional ginning outturn (36%), and staple length (31mm)",
        "developing_institution": "Nuziveedu Seeds",
        "genetic_purity_score": 99.50,
        "heritability_broad_sense": 0.81,
        "drought_susceptibility_index": 0.68,
        "harvest_index_pct": 47.6,
        "recommended_agro_climatic_zones": [
            "Zone 13: Indo-Gangetic Plains & Central Plateau",
            "Zone 14: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0149",
        "variety_name": "Tomato Arka Rakshak (F1 Hybrid) Genotype Line v15",
        "target_trait": "Triple Disease Resistance (ToLCV, BW, EB)",
        "major_qtl_markers": "Ty-2, Ty-3, Bwr-12, Ph-3",
        "agronomic_description": "High yielding indeterminate tomato with resistance to leaf curl virus, bacterial wilt, and early blight",
        "developing_institution": "ICAR-IIHR",
        "genetic_purity_score": 99.60,
        "heritability_broad_sense": 0.82,
        "drought_susceptibility_index": 0.70,
        "harvest_index_pct": 48.4,
        "recommended_agro_climatic_zones": [
            "Zone 14: Indo-Gangetic Plains & Central Plateau",
            "Zone 15: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0150",
        "variety_name": "Chilli Arka Harita Genotype Line v15",
        "target_trait": "Powdery Mildew & Anthracnose Tolerance",
        "major_qtl_markers": "Pm-1, Colletotrichum-R1",
        "agronomic_description": "High pungency (0.45% capsaicin) dual-purpose hybrid for green and dry red chilli export",
        "developing_institution": "ICAR-IIHR",
        "genetic_purity_score": 99.70,
        "heritability_broad_sense": 0.83,
        "drought_susceptibility_index": 0.72,
        "harvest_index_pct": 49.2,
        "recommended_agro_climatic_zones": [
            "Zone 15: Indo-Gangetic Plains & Central Plateau",
            "Zone 1: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0151",
        "variety_name": "Rice Swarna Sub1 Genotype Line v16",
        "target_trait": "Submergence / Flash Flood Tolerance",
        "major_qtl_markers": "Sub1A Transcription Factor",
        "agronomic_description": "Direct seeded or transplanted lowland rice with 14-day complete water submergence survival",
        "developing_institution": "Central Rice Research Institute (CRRI)",
        "genetic_purity_score": 99.80,
        "heritability_broad_sense": 0.84,
        "drought_susceptibility_index": 0.74,
        "harvest_index_pct": 42.0,
        "recommended_agro_climatic_zones": [
            "Zone 1: Indo-Gangetic Plains & Central Plateau",
            "Zone 2: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0152",
        "variety_name": "Rice CR Dhan 801 Genotype Line v16",
        "target_trait": "Drought + Submergence Dual Tolerance",
        "major_qtl_markers": "qDTY1.1, qDTY2.1, Sub1A",
        "agronomic_description": "Climate-resilient dual tolerant line for rainfed drought-prone and flood-prone ecologies",
        "developing_institution": "ICAR-NRRI",
        "genetic_purity_score": 99.90,
        "heritability_broad_sense": 0.85,
        "drought_susceptibility_index": 0.76,
        "harvest_index_pct": 42.8,
        "recommended_agro_climatic_zones": [
            "Zone 2: Indo-Gangetic Plains & Central Plateau",
            "Zone 3: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0153",
        "variety_name": "Wheat DBW 303 (Karan Vaishnavi) Genotype Line v16",
        "target_trait": "Terminal Heat Stress Resistance",
        "major_qtl_markers": "TaHsfA2d, TaFER-5B",
        "agronomic_description": "High-yielding irrigated timely sown bread wheat with extreme heat resilience during grain filling",
        "developing_institution": "ICAR-IIWBR",
        "genetic_purity_score": 99.20,
        "heritability_broad_sense": 0.86,
        "drought_susceptibility_index": 0.78,
        "harvest_index_pct": 43.6,
        "recommended_agro_climatic_zones": [
            "Zone 3: Indo-Gangetic Plains & Central Plateau",
            "Zone 4: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0154",
        "variety_name": "Wheat HD 3226 (Pusa Yashasvi) Genotype Line v16",
        "target_trait": "Multi-Rust Resistance (Yellow, Brown, Black)",
        "major_qtl_markers": "Yr17, Lr37, Sr38",
        "agronomic_description": "Superior chapati-making and biscuit-making quality with high gluten strength",
        "developing_institution": "ICAR-IARI",
        "genetic_purity_score": 99.30,
        "heritability_broad_sense": 0.87,
        "drought_susceptibility_index": 0.80,
        "harvest_index_pct": 44.4,
        "recommended_agro_climatic_zones": [
            "Zone 4: Indo-Gangetic Plains & Central Plateau",
            "Zone 5: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0155",
        "variety_name": "Chickpea Pusa 10216 Genotype Line v16",
        "target_trait": "Drought Drought Tolerance & Root Architecture",
        "major_qtl_markers": "qRT9.1, QTL-hotspot genomic region",
        "agronomic_description": "Desi chickpea with deep taproot system and high water use efficiency under dryland",
        "developing_institution": "ICAR-IARI",
        "genetic_purity_score": 99.40,
        "heritability_broad_sense": 0.88,
        "drought_susceptibility_index": 0.82,
        "harvest_index_pct": 45.2,
        "recommended_agro_climatic_zones": [
            "Zone 5: Indo-Gangetic Plains & Central Plateau",
            "Zone 6: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0156",
        "variety_name": "Pigeonpea BDN 711 Genotype Line v16",
        "target_trait": "Fusarium Wilt & Sterility Mosaic Tolerance",
        "major_qtl_markers": "Cc-RFLP-Wilt1",
        "agronomic_description": "White seeded medium duration variety highly adapted to rainfed black cotton vertisols",
        "developing_institution": "VNMKV",
        "genetic_purity_score": 99.50,
        "heritability_broad_sense": 0.89,
        "drought_susceptibility_index": 0.84,
        "harvest_index_pct": 46.0,
        "recommended_agro_climatic_zones": [
            "Zone 6: Indo-Gangetic Plains & Central Plateau",
            "Zone 7: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0157",
        "variety_name": "Mustard PM 28 Genotype Line v16",
        "target_trait": "High Oleic / Low Glucosinolate Double Zero Quality",
        "major_qtl_markers": "FAD2 mutation, GSL1 deletion",
        "agronomic_description": "Canola quality Brassica juncea with heart-healthy fatty acid profile",
        "developing_institution": "ICAR-DRMR",
        "genetic_purity_score": 99.60,
        "heritability_broad_sense": 0.90,
        "drought_susceptibility_index": 0.62,
        "harvest_index_pct": 46.8,
        "recommended_agro_climatic_zones": [
            "Zone 7: Indo-Gangetic Plains & Central Plateau",
            "Zone 8: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0158",
        "variety_name": "Cotton Bunny Bt (NCS 145) Genotype Line v16",
        "target_trait": "Bollworm Resistance & Sucking Pest Tolerance",
        "major_qtl_markers": "Cry1Ac + Cry2Ab (Bollgard II)",
        "agronomic_description": "High boll retention, exceptional ginning outturn (36%), and staple length (31mm)",
        "developing_institution": "Nuziveedu Seeds",
        "genetic_purity_score": 99.70,
        "heritability_broad_sense": 0.91,
        "drought_susceptibility_index": 0.64,
        "harvest_index_pct": 47.6,
        "recommended_agro_climatic_zones": [
            "Zone 8: Indo-Gangetic Plains & Central Plateau",
            "Zone 9: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0159",
        "variety_name": "Tomato Arka Rakshak (F1 Hybrid) Genotype Line v16",
        "target_trait": "Triple Disease Resistance (ToLCV, BW, EB)",
        "major_qtl_markers": "Ty-2, Ty-3, Bwr-12, Ph-3",
        "agronomic_description": "High yielding indeterminate tomato with resistance to leaf curl virus, bacterial wilt, and early blight",
        "developing_institution": "ICAR-IIHR",
        "genetic_purity_score": 99.80,
        "heritability_broad_sense": 0.92,
        "drought_susceptibility_index": 0.66,
        "harvest_index_pct": 48.4,
        "recommended_agro_climatic_zones": [
            "Zone 9: Indo-Gangetic Plains & Central Plateau",
            "Zone 10: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0160",
        "variety_name": "Chilli Arka Harita Genotype Line v16",
        "target_trait": "Powdery Mildew & Anthracnose Tolerance",
        "major_qtl_markers": "Pm-1, Colletotrichum-R1",
        "agronomic_description": "High pungency (0.45% capsaicin) dual-purpose hybrid for green and dry red chilli export",
        "developing_institution": "ICAR-IIHR",
        "genetic_purity_score": 99.90,
        "heritability_broad_sense": 0.93,
        "drought_susceptibility_index": 0.68,
        "harvest_index_pct": 49.2,
        "recommended_agro_climatic_zones": [
            "Zone 10: Indo-Gangetic Plains & Central Plateau",
            "Zone 11: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0161",
        "variety_name": "Rice Swarna Sub1 Genotype Line v17",
        "target_trait": "Submergence / Flash Flood Tolerance",
        "major_qtl_markers": "Sub1A Transcription Factor",
        "agronomic_description": "Direct seeded or transplanted lowland rice with 14-day complete water submergence survival",
        "developing_institution": "Central Rice Research Institute (CRRI)",
        "genetic_purity_score": 99.20,
        "heritability_broad_sense": 0.94,
        "drought_susceptibility_index": 0.70,
        "harvest_index_pct": 42.0,
        "recommended_agro_climatic_zones": [
            "Zone 11: Indo-Gangetic Plains & Central Plateau",
            "Zone 12: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0162",
        "variety_name": "Rice CR Dhan 801 Genotype Line v17",
        "target_trait": "Drought + Submergence Dual Tolerance",
        "major_qtl_markers": "qDTY1.1, qDTY2.1, Sub1A",
        "agronomic_description": "Climate-resilient dual tolerant line for rainfed drought-prone and flood-prone ecologies",
        "developing_institution": "ICAR-NRRI",
        "genetic_purity_score": 99.30,
        "heritability_broad_sense": 0.95,
        "drought_susceptibility_index": 0.72,
        "harvest_index_pct": 42.8,
        "recommended_agro_climatic_zones": [
            "Zone 12: Indo-Gangetic Plains & Central Plateau",
            "Zone 13: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0163",
        "variety_name": "Wheat DBW 303 (Karan Vaishnavi) Genotype Line v17",
        "target_trait": "Terminal Heat Stress Resistance",
        "major_qtl_markers": "TaHsfA2d, TaFER-5B",
        "agronomic_description": "High-yielding irrigated timely sown bread wheat with extreme heat resilience during grain filling",
        "developing_institution": "ICAR-IIWBR",
        "genetic_purity_score": 99.40,
        "heritability_broad_sense": 0.78,
        "drought_susceptibility_index": 0.74,
        "harvest_index_pct": 43.6,
        "recommended_agro_climatic_zones": [
            "Zone 13: Indo-Gangetic Plains & Central Plateau",
            "Zone 14: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0164",
        "variety_name": "Wheat HD 3226 (Pusa Yashasvi) Genotype Line v17",
        "target_trait": "Multi-Rust Resistance (Yellow, Brown, Black)",
        "major_qtl_markers": "Yr17, Lr37, Sr38",
        "agronomic_description": "Superior chapati-making and biscuit-making quality with high gluten strength",
        "developing_institution": "ICAR-IARI",
        "genetic_purity_score": 99.50,
        "heritability_broad_sense": 0.79,
        "drought_susceptibility_index": 0.76,
        "harvest_index_pct": 44.4,
        "recommended_agro_climatic_zones": [
            "Zone 14: Indo-Gangetic Plains & Central Plateau",
            "Zone 15: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0165",
        "variety_name": "Chickpea Pusa 10216 Genotype Line v17",
        "target_trait": "Drought Drought Tolerance & Root Architecture",
        "major_qtl_markers": "qRT9.1, QTL-hotspot genomic region",
        "agronomic_description": "Desi chickpea with deep taproot system and high water use efficiency under dryland",
        "developing_institution": "ICAR-IARI",
        "genetic_purity_score": 99.60,
        "heritability_broad_sense": 0.80,
        "drought_susceptibility_index": 0.78,
        "harvest_index_pct": 45.2,
        "recommended_agro_climatic_zones": [
            "Zone 15: Indo-Gangetic Plains & Central Plateau",
            "Zone 1: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0166",
        "variety_name": "Pigeonpea BDN 711 Genotype Line v17",
        "target_trait": "Fusarium Wilt & Sterility Mosaic Tolerance",
        "major_qtl_markers": "Cc-RFLP-Wilt1",
        "agronomic_description": "White seeded medium duration variety highly adapted to rainfed black cotton vertisols",
        "developing_institution": "VNMKV",
        "genetic_purity_score": 99.70,
        "heritability_broad_sense": 0.81,
        "drought_susceptibility_index": 0.80,
        "harvest_index_pct": 46.0,
        "recommended_agro_climatic_zones": [
            "Zone 1: Indo-Gangetic Plains & Central Plateau",
            "Zone 2: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0167",
        "variety_name": "Mustard PM 28 Genotype Line v17",
        "target_trait": "High Oleic / Low Glucosinolate Double Zero Quality",
        "major_qtl_markers": "FAD2 mutation, GSL1 deletion",
        "agronomic_description": "Canola quality Brassica juncea with heart-healthy fatty acid profile",
        "developing_institution": "ICAR-DRMR",
        "genetic_purity_score": 99.80,
        "heritability_broad_sense": 0.82,
        "drought_susceptibility_index": 0.82,
        "harvest_index_pct": 46.8,
        "recommended_agro_climatic_zones": [
            "Zone 2: Indo-Gangetic Plains & Central Plateau",
            "Zone 3: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0168",
        "variety_name": "Cotton Bunny Bt (NCS 145) Genotype Line v17",
        "target_trait": "Bollworm Resistance & Sucking Pest Tolerance",
        "major_qtl_markers": "Cry1Ac + Cry2Ab (Bollgard II)",
        "agronomic_description": "High boll retention, exceptional ginning outturn (36%), and staple length (31mm)",
        "developing_institution": "Nuziveedu Seeds",
        "genetic_purity_score": 99.90,
        "heritability_broad_sense": 0.83,
        "drought_susceptibility_index": 0.84,
        "harvest_index_pct": 47.6,
        "recommended_agro_climatic_zones": [
            "Zone 3: Indo-Gangetic Plains & Central Plateau",
            "Zone 4: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0169",
        "variety_name": "Tomato Arka Rakshak (F1 Hybrid) Genotype Line v17",
        "target_trait": "Triple Disease Resistance (ToLCV, BW, EB)",
        "major_qtl_markers": "Ty-2, Ty-3, Bwr-12, Ph-3",
        "agronomic_description": "High yielding indeterminate tomato with resistance to leaf curl virus, bacterial wilt, and early blight",
        "developing_institution": "ICAR-IIHR",
        "genetic_purity_score": 99.20,
        "heritability_broad_sense": 0.84,
        "drought_susceptibility_index": 0.62,
        "harvest_index_pct": 48.4,
        "recommended_agro_climatic_zones": [
            "Zone 4: Indo-Gangetic Plains & Central Plateau",
            "Zone 5: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0170",
        "variety_name": "Chilli Arka Harita Genotype Line v17",
        "target_trait": "Powdery Mildew & Anthracnose Tolerance",
        "major_qtl_markers": "Pm-1, Colletotrichum-R1",
        "agronomic_description": "High pungency (0.45% capsaicin) dual-purpose hybrid for green and dry red chilli export",
        "developing_institution": "ICAR-IIHR",
        "genetic_purity_score": 99.30,
        "heritability_broad_sense": 0.85,
        "drought_susceptibility_index": 0.64,
        "harvest_index_pct": 49.2,
        "recommended_agro_climatic_zones": [
            "Zone 5: Indo-Gangetic Plains & Central Plateau",
            "Zone 6: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0171",
        "variety_name": "Rice Swarna Sub1 Genotype Line v18",
        "target_trait": "Submergence / Flash Flood Tolerance",
        "major_qtl_markers": "Sub1A Transcription Factor",
        "agronomic_description": "Direct seeded or transplanted lowland rice with 14-day complete water submergence survival",
        "developing_institution": "Central Rice Research Institute (CRRI)",
        "genetic_purity_score": 99.40,
        "heritability_broad_sense": 0.86,
        "drought_susceptibility_index": 0.66,
        "harvest_index_pct": 42.0,
        "recommended_agro_climatic_zones": [
            "Zone 6: Indo-Gangetic Plains & Central Plateau",
            "Zone 7: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0172",
        "variety_name": "Rice CR Dhan 801 Genotype Line v18",
        "target_trait": "Drought + Submergence Dual Tolerance",
        "major_qtl_markers": "qDTY1.1, qDTY2.1, Sub1A",
        "agronomic_description": "Climate-resilient dual tolerant line for rainfed drought-prone and flood-prone ecologies",
        "developing_institution": "ICAR-NRRI",
        "genetic_purity_score": 99.50,
        "heritability_broad_sense": 0.87,
        "drought_susceptibility_index": 0.68,
        "harvest_index_pct": 42.8,
        "recommended_agro_climatic_zones": [
            "Zone 7: Indo-Gangetic Plains & Central Plateau",
            "Zone 8: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0173",
        "variety_name": "Wheat DBW 303 (Karan Vaishnavi) Genotype Line v18",
        "target_trait": "Terminal Heat Stress Resistance",
        "major_qtl_markers": "TaHsfA2d, TaFER-5B",
        "agronomic_description": "High-yielding irrigated timely sown bread wheat with extreme heat resilience during grain filling",
        "developing_institution": "ICAR-IIWBR",
        "genetic_purity_score": 99.60,
        "heritability_broad_sense": 0.88,
        "drought_susceptibility_index": 0.70,
        "harvest_index_pct": 43.6,
        "recommended_agro_climatic_zones": [
            "Zone 8: Indo-Gangetic Plains & Central Plateau",
            "Zone 9: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0174",
        "variety_name": "Wheat HD 3226 (Pusa Yashasvi) Genotype Line v18",
        "target_trait": "Multi-Rust Resistance (Yellow, Brown, Black)",
        "major_qtl_markers": "Yr17, Lr37, Sr38",
        "agronomic_description": "Superior chapati-making and biscuit-making quality with high gluten strength",
        "developing_institution": "ICAR-IARI",
        "genetic_purity_score": 99.70,
        "heritability_broad_sense": 0.89,
        "drought_susceptibility_index": 0.72,
        "harvest_index_pct": 44.4,
        "recommended_agro_climatic_zones": [
            "Zone 9: Indo-Gangetic Plains & Central Plateau",
            "Zone 10: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0175",
        "variety_name": "Chickpea Pusa 10216 Genotype Line v18",
        "target_trait": "Drought Drought Tolerance & Root Architecture",
        "major_qtl_markers": "qRT9.1, QTL-hotspot genomic region",
        "agronomic_description": "Desi chickpea with deep taproot system and high water use efficiency under dryland",
        "developing_institution": "ICAR-IARI",
        "genetic_purity_score": 99.80,
        "heritability_broad_sense": 0.90,
        "drought_susceptibility_index": 0.74,
        "harvest_index_pct": 45.2,
        "recommended_agro_climatic_zones": [
            "Zone 10: Indo-Gangetic Plains & Central Plateau",
            "Zone 11: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0176",
        "variety_name": "Pigeonpea BDN 711 Genotype Line v18",
        "target_trait": "Fusarium Wilt & Sterility Mosaic Tolerance",
        "major_qtl_markers": "Cc-RFLP-Wilt1",
        "agronomic_description": "White seeded medium duration variety highly adapted to rainfed black cotton vertisols",
        "developing_institution": "VNMKV",
        "genetic_purity_score": 99.90,
        "heritability_broad_sense": 0.91,
        "drought_susceptibility_index": 0.76,
        "harvest_index_pct": 46.0,
        "recommended_agro_climatic_zones": [
            "Zone 11: Indo-Gangetic Plains & Central Plateau",
            "Zone 12: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0177",
        "variety_name": "Mustard PM 28 Genotype Line v18",
        "target_trait": "High Oleic / Low Glucosinolate Double Zero Quality",
        "major_qtl_markers": "FAD2 mutation, GSL1 deletion",
        "agronomic_description": "Canola quality Brassica juncea with heart-healthy fatty acid profile",
        "developing_institution": "ICAR-DRMR",
        "genetic_purity_score": 99.20,
        "heritability_broad_sense": 0.92,
        "drought_susceptibility_index": 0.78,
        "harvest_index_pct": 46.8,
        "recommended_agro_climatic_zones": [
            "Zone 12: Indo-Gangetic Plains & Central Plateau",
            "Zone 13: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0178",
        "variety_name": "Cotton Bunny Bt (NCS 145) Genotype Line v18",
        "target_trait": "Bollworm Resistance & Sucking Pest Tolerance",
        "major_qtl_markers": "Cry1Ac + Cry2Ab (Bollgard II)",
        "agronomic_description": "High boll retention, exceptional ginning outturn (36%), and staple length (31mm)",
        "developing_institution": "Nuziveedu Seeds",
        "genetic_purity_score": 99.30,
        "heritability_broad_sense": 0.93,
        "drought_susceptibility_index": 0.80,
        "harvest_index_pct": 47.6,
        "recommended_agro_climatic_zones": [
            "Zone 13: Indo-Gangetic Plains & Central Plateau",
            "Zone 14: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0179",
        "variety_name": "Tomato Arka Rakshak (F1 Hybrid) Genotype Line v18",
        "target_trait": "Triple Disease Resistance (ToLCV, BW, EB)",
        "major_qtl_markers": "Ty-2, Ty-3, Bwr-12, Ph-3",
        "agronomic_description": "High yielding indeterminate tomato with resistance to leaf curl virus, bacterial wilt, and early blight",
        "developing_institution": "ICAR-IIHR",
        "genetic_purity_score": 99.40,
        "heritability_broad_sense": 0.94,
        "drought_susceptibility_index": 0.82,
        "harvest_index_pct": 48.4,
        "recommended_agro_climatic_zones": [
            "Zone 14: Indo-Gangetic Plains & Central Plateau",
            "Zone 15: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0180",
        "variety_name": "Chilli Arka Harita Genotype Line v18",
        "target_trait": "Powdery Mildew & Anthracnose Tolerance",
        "major_qtl_markers": "Pm-1, Colletotrichum-R1",
        "agronomic_description": "High pungency (0.45% capsaicin) dual-purpose hybrid for green and dry red chilli export",
        "developing_institution": "ICAR-IIHR",
        "genetic_purity_score": 99.50,
        "heritability_broad_sense": 0.95,
        "drought_susceptibility_index": 0.84,
        "harvest_index_pct": 49.2,
        "recommended_agro_climatic_zones": [
            "Zone 15: Indo-Gangetic Plains & Central Plateau",
            "Zone 1: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0181",
        "variety_name": "Rice Swarna Sub1 Genotype Line v19",
        "target_trait": "Submergence / Flash Flood Tolerance",
        "major_qtl_markers": "Sub1A Transcription Factor",
        "agronomic_description": "Direct seeded or transplanted lowland rice with 14-day complete water submergence survival",
        "developing_institution": "Central Rice Research Institute (CRRI)",
        "genetic_purity_score": 99.60,
        "heritability_broad_sense": 0.78,
        "drought_susceptibility_index": 0.62,
        "harvest_index_pct": 42.0,
        "recommended_agro_climatic_zones": [
            "Zone 1: Indo-Gangetic Plains & Central Plateau",
            "Zone 2: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0182",
        "variety_name": "Rice CR Dhan 801 Genotype Line v19",
        "target_trait": "Drought + Submergence Dual Tolerance",
        "major_qtl_markers": "qDTY1.1, qDTY2.1, Sub1A",
        "agronomic_description": "Climate-resilient dual tolerant line for rainfed drought-prone and flood-prone ecologies",
        "developing_institution": "ICAR-NRRI",
        "genetic_purity_score": 99.70,
        "heritability_broad_sense": 0.79,
        "drought_susceptibility_index": 0.64,
        "harvest_index_pct": 42.8,
        "recommended_agro_climatic_zones": [
            "Zone 2: Indo-Gangetic Plains & Central Plateau",
            "Zone 3: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0183",
        "variety_name": "Wheat DBW 303 (Karan Vaishnavi) Genotype Line v19",
        "target_trait": "Terminal Heat Stress Resistance",
        "major_qtl_markers": "TaHsfA2d, TaFER-5B",
        "agronomic_description": "High-yielding irrigated timely sown bread wheat with extreme heat resilience during grain filling",
        "developing_institution": "ICAR-IIWBR",
        "genetic_purity_score": 99.80,
        "heritability_broad_sense": 0.80,
        "drought_susceptibility_index": 0.66,
        "harvest_index_pct": 43.6,
        "recommended_agro_climatic_zones": [
            "Zone 3: Indo-Gangetic Plains & Central Plateau",
            "Zone 4: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0184",
        "variety_name": "Wheat HD 3226 (Pusa Yashasvi) Genotype Line v19",
        "target_trait": "Multi-Rust Resistance (Yellow, Brown, Black)",
        "major_qtl_markers": "Yr17, Lr37, Sr38",
        "agronomic_description": "Superior chapati-making and biscuit-making quality with high gluten strength",
        "developing_institution": "ICAR-IARI",
        "genetic_purity_score": 99.90,
        "heritability_broad_sense": 0.81,
        "drought_susceptibility_index": 0.68,
        "harvest_index_pct": 44.4,
        "recommended_agro_climatic_zones": [
            "Zone 4: Indo-Gangetic Plains & Central Plateau",
            "Zone 5: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0185",
        "variety_name": "Chickpea Pusa 10216 Genotype Line v19",
        "target_trait": "Drought Drought Tolerance & Root Architecture",
        "major_qtl_markers": "qRT9.1, QTL-hotspot genomic region",
        "agronomic_description": "Desi chickpea with deep taproot system and high water use efficiency under dryland",
        "developing_institution": "ICAR-IARI",
        "genetic_purity_score": 99.20,
        "heritability_broad_sense": 0.82,
        "drought_susceptibility_index": 0.70,
        "harvest_index_pct": 45.2,
        "recommended_agro_climatic_zones": [
            "Zone 5: Indo-Gangetic Plains & Central Plateau",
            "Zone 6: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0186",
        "variety_name": "Pigeonpea BDN 711 Genotype Line v19",
        "target_trait": "Fusarium Wilt & Sterility Mosaic Tolerance",
        "major_qtl_markers": "Cc-RFLP-Wilt1",
        "agronomic_description": "White seeded medium duration variety highly adapted to rainfed black cotton vertisols",
        "developing_institution": "VNMKV",
        "genetic_purity_score": 99.30,
        "heritability_broad_sense": 0.83,
        "drought_susceptibility_index": 0.72,
        "harvest_index_pct": 46.0,
        "recommended_agro_climatic_zones": [
            "Zone 6: Indo-Gangetic Plains & Central Plateau",
            "Zone 7: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0187",
        "variety_name": "Mustard PM 28 Genotype Line v19",
        "target_trait": "High Oleic / Low Glucosinolate Double Zero Quality",
        "major_qtl_markers": "FAD2 mutation, GSL1 deletion",
        "agronomic_description": "Canola quality Brassica juncea with heart-healthy fatty acid profile",
        "developing_institution": "ICAR-DRMR",
        "genetic_purity_score": 99.40,
        "heritability_broad_sense": 0.84,
        "drought_susceptibility_index": 0.74,
        "harvest_index_pct": 46.8,
        "recommended_agro_climatic_zones": [
            "Zone 7: Indo-Gangetic Plains & Central Plateau",
            "Zone 8: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0188",
        "variety_name": "Cotton Bunny Bt (NCS 145) Genotype Line v19",
        "target_trait": "Bollworm Resistance & Sucking Pest Tolerance",
        "major_qtl_markers": "Cry1Ac + Cry2Ab (Bollgard II)",
        "agronomic_description": "High boll retention, exceptional ginning outturn (36%), and staple length (31mm)",
        "developing_institution": "Nuziveedu Seeds",
        "genetic_purity_score": 99.50,
        "heritability_broad_sense": 0.85,
        "drought_susceptibility_index": 0.76,
        "harvest_index_pct": 47.6,
        "recommended_agro_climatic_zones": [
            "Zone 8: Indo-Gangetic Plains & Central Plateau",
            "Zone 9: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0189",
        "variety_name": "Tomato Arka Rakshak (F1 Hybrid) Genotype Line v19",
        "target_trait": "Triple Disease Resistance (ToLCV, BW, EB)",
        "major_qtl_markers": "Ty-2, Ty-3, Bwr-12, Ph-3",
        "agronomic_description": "High yielding indeterminate tomato with resistance to leaf curl virus, bacterial wilt, and early blight",
        "developing_institution": "ICAR-IIHR",
        "genetic_purity_score": 99.60,
        "heritability_broad_sense": 0.86,
        "drought_susceptibility_index": 0.78,
        "harvest_index_pct": 48.4,
        "recommended_agro_climatic_zones": [
            "Zone 9: Indo-Gangetic Plains & Central Plateau",
            "Zone 10: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0190",
        "variety_name": "Chilli Arka Harita Genotype Line v19",
        "target_trait": "Powdery Mildew & Anthracnose Tolerance",
        "major_qtl_markers": "Pm-1, Colletotrichum-R1",
        "agronomic_description": "High pungency (0.45% capsaicin) dual-purpose hybrid for green and dry red chilli export",
        "developing_institution": "ICAR-IIHR",
        "genetic_purity_score": 99.70,
        "heritability_broad_sense": 0.87,
        "drought_susceptibility_index": 0.80,
        "harvest_index_pct": 49.2,
        "recommended_agro_climatic_zones": [
            "Zone 10: Indo-Gangetic Plains & Central Plateau",
            "Zone 11: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0191",
        "variety_name": "Rice Swarna Sub1 Genotype Line v20",
        "target_trait": "Submergence / Flash Flood Tolerance",
        "major_qtl_markers": "Sub1A Transcription Factor",
        "agronomic_description": "Direct seeded or transplanted lowland rice with 14-day complete water submergence survival",
        "developing_institution": "Central Rice Research Institute (CRRI)",
        "genetic_purity_score": 99.80,
        "heritability_broad_sense": 0.88,
        "drought_susceptibility_index": 0.82,
        "harvest_index_pct": 42.0,
        "recommended_agro_climatic_zones": [
            "Zone 11: Indo-Gangetic Plains & Central Plateau",
            "Zone 12: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0192",
        "variety_name": "Rice CR Dhan 801 Genotype Line v20",
        "target_trait": "Drought + Submergence Dual Tolerance",
        "major_qtl_markers": "qDTY1.1, qDTY2.1, Sub1A",
        "agronomic_description": "Climate-resilient dual tolerant line for rainfed drought-prone and flood-prone ecologies",
        "developing_institution": "ICAR-NRRI",
        "genetic_purity_score": 99.90,
        "heritability_broad_sense": 0.89,
        "drought_susceptibility_index": 0.84,
        "harvest_index_pct": 42.8,
        "recommended_agro_climatic_zones": [
            "Zone 12: Indo-Gangetic Plains & Central Plateau",
            "Zone 13: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0193",
        "variety_name": "Wheat DBW 303 (Karan Vaishnavi) Genotype Line v20",
        "target_trait": "Terminal Heat Stress Resistance",
        "major_qtl_markers": "TaHsfA2d, TaFER-5B",
        "agronomic_description": "High-yielding irrigated timely sown bread wheat with extreme heat resilience during grain filling",
        "developing_institution": "ICAR-IIWBR",
        "genetic_purity_score": 99.20,
        "heritability_broad_sense": 0.90,
        "drought_susceptibility_index": 0.62,
        "harvest_index_pct": 43.6,
        "recommended_agro_climatic_zones": [
            "Zone 13: Indo-Gangetic Plains & Central Plateau",
            "Zone 14: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0194",
        "variety_name": "Wheat HD 3226 (Pusa Yashasvi) Genotype Line v20",
        "target_trait": "Multi-Rust Resistance (Yellow, Brown, Black)",
        "major_qtl_markers": "Yr17, Lr37, Sr38",
        "agronomic_description": "Superior chapati-making and biscuit-making quality with high gluten strength",
        "developing_institution": "ICAR-IARI",
        "genetic_purity_score": 99.30,
        "heritability_broad_sense": 0.91,
        "drought_susceptibility_index": 0.64,
        "harvest_index_pct": 44.4,
        "recommended_agro_climatic_zones": [
            "Zone 14: Indo-Gangetic Plains & Central Plateau",
            "Zone 15: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0195",
        "variety_name": "Chickpea Pusa 10216 Genotype Line v20",
        "target_trait": "Drought Drought Tolerance & Root Architecture",
        "major_qtl_markers": "qRT9.1, QTL-hotspot genomic region",
        "agronomic_description": "Desi chickpea with deep taproot system and high water use efficiency under dryland",
        "developing_institution": "ICAR-IARI",
        "genetic_purity_score": 99.40,
        "heritability_broad_sense": 0.92,
        "drought_susceptibility_index": 0.66,
        "harvest_index_pct": 45.2,
        "recommended_agro_climatic_zones": [
            "Zone 15: Indo-Gangetic Plains & Central Plateau",
            "Zone 1: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0196",
        "variety_name": "Pigeonpea BDN 711 Genotype Line v20",
        "target_trait": "Fusarium Wilt & Sterility Mosaic Tolerance",
        "major_qtl_markers": "Cc-RFLP-Wilt1",
        "agronomic_description": "White seeded medium duration variety highly adapted to rainfed black cotton vertisols",
        "developing_institution": "VNMKV",
        "genetic_purity_score": 99.50,
        "heritability_broad_sense": 0.93,
        "drought_susceptibility_index": 0.68,
        "harvest_index_pct": 46.0,
        "recommended_agro_climatic_zones": [
            "Zone 1: Indo-Gangetic Plains & Central Plateau",
            "Zone 2: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0197",
        "variety_name": "Mustard PM 28 Genotype Line v20",
        "target_trait": "High Oleic / Low Glucosinolate Double Zero Quality",
        "major_qtl_markers": "FAD2 mutation, GSL1 deletion",
        "agronomic_description": "Canola quality Brassica juncea with heart-healthy fatty acid profile",
        "developing_institution": "ICAR-DRMR",
        "genetic_purity_score": 99.60,
        "heritability_broad_sense": 0.94,
        "drought_susceptibility_index": 0.70,
        "harvest_index_pct": 46.8,
        "recommended_agro_climatic_zones": [
            "Zone 2: Indo-Gangetic Plains & Central Plateau",
            "Zone 3: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0198",
        "variety_name": "Cotton Bunny Bt (NCS 145) Genotype Line v20",
        "target_trait": "Bollworm Resistance & Sucking Pest Tolerance",
        "major_qtl_markers": "Cry1Ac + Cry2Ab (Bollgard II)",
        "agronomic_description": "High boll retention, exceptional ginning outturn (36%), and staple length (31mm)",
        "developing_institution": "Nuziveedu Seeds",
        "genetic_purity_score": 99.70,
        "heritability_broad_sense": 0.95,
        "drought_susceptibility_index": 0.72,
        "harvest_index_pct": 47.6,
        "recommended_agro_climatic_zones": [
            "Zone 3: Indo-Gangetic Plains & Central Plateau",
            "Zone 4: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0199",
        "variety_name": "Tomato Arka Rakshak (F1 Hybrid) Genotype Line v20",
        "target_trait": "Triple Disease Resistance (ToLCV, BW, EB)",
        "major_qtl_markers": "Ty-2, Ty-3, Bwr-12, Ph-3",
        "agronomic_description": "High yielding indeterminate tomato with resistance to leaf curl virus, bacterial wilt, and early blight",
        "developing_institution": "ICAR-IIHR",
        "genetic_purity_score": 99.80,
        "heritability_broad_sense": 0.78,
        "drought_susceptibility_index": 0.74,
        "harvest_index_pct": 48.4,
        "recommended_agro_climatic_zones": [
            "Zone 4: Indo-Gangetic Plains & Central Plateau",
            "Zone 5: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0200",
        "variety_name": "Chilli Arka Harita Genotype Line v20",
        "target_trait": "Powdery Mildew & Anthracnose Tolerance",
        "major_qtl_markers": "Pm-1, Colletotrichum-R1",
        "agronomic_description": "High pungency (0.45% capsaicin) dual-purpose hybrid for green and dry red chilli export",
        "developing_institution": "ICAR-IIHR",
        "genetic_purity_score": 99.90,
        "heritability_broad_sense": 0.79,
        "drought_susceptibility_index": 0.76,
        "harvest_index_pct": 49.2,
        "recommended_agro_climatic_zones": [
            "Zone 5: Indo-Gangetic Plains & Central Plateau",
            "Zone 6: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0201",
        "variety_name": "Rice Swarna Sub1 Genotype Line v21",
        "target_trait": "Submergence / Flash Flood Tolerance",
        "major_qtl_markers": "Sub1A Transcription Factor",
        "agronomic_description": "Direct seeded or transplanted lowland rice with 14-day complete water submergence survival",
        "developing_institution": "Central Rice Research Institute (CRRI)",
        "genetic_purity_score": 99.20,
        "heritability_broad_sense": 0.80,
        "drought_susceptibility_index": 0.78,
        "harvest_index_pct": 42.0,
        "recommended_agro_climatic_zones": [
            "Zone 6: Indo-Gangetic Plains & Central Plateau",
            "Zone 7: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0202",
        "variety_name": "Rice CR Dhan 801 Genotype Line v21",
        "target_trait": "Drought + Submergence Dual Tolerance",
        "major_qtl_markers": "qDTY1.1, qDTY2.1, Sub1A",
        "agronomic_description": "Climate-resilient dual tolerant line for rainfed drought-prone and flood-prone ecologies",
        "developing_institution": "ICAR-NRRI",
        "genetic_purity_score": 99.30,
        "heritability_broad_sense": 0.81,
        "drought_susceptibility_index": 0.80,
        "harvest_index_pct": 42.8,
        "recommended_agro_climatic_zones": [
            "Zone 7: Indo-Gangetic Plains & Central Plateau",
            "Zone 8: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0203",
        "variety_name": "Wheat DBW 303 (Karan Vaishnavi) Genotype Line v21",
        "target_trait": "Terminal Heat Stress Resistance",
        "major_qtl_markers": "TaHsfA2d, TaFER-5B",
        "agronomic_description": "High-yielding irrigated timely sown bread wheat with extreme heat resilience during grain filling",
        "developing_institution": "ICAR-IIWBR",
        "genetic_purity_score": 99.40,
        "heritability_broad_sense": 0.82,
        "drought_susceptibility_index": 0.82,
        "harvest_index_pct": 43.6,
        "recommended_agro_climatic_zones": [
            "Zone 8: Indo-Gangetic Plains & Central Plateau",
            "Zone 9: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0204",
        "variety_name": "Wheat HD 3226 (Pusa Yashasvi) Genotype Line v21",
        "target_trait": "Multi-Rust Resistance (Yellow, Brown, Black)",
        "major_qtl_markers": "Yr17, Lr37, Sr38",
        "agronomic_description": "Superior chapati-making and biscuit-making quality with high gluten strength",
        "developing_institution": "ICAR-IARI",
        "genetic_purity_score": 99.50,
        "heritability_broad_sense": 0.83,
        "drought_susceptibility_index": 0.84,
        "harvest_index_pct": 44.4,
        "recommended_agro_climatic_zones": [
            "Zone 9: Indo-Gangetic Plains & Central Plateau",
            "Zone 10: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0205",
        "variety_name": "Chickpea Pusa 10216 Genotype Line v21",
        "target_trait": "Drought Drought Tolerance & Root Architecture",
        "major_qtl_markers": "qRT9.1, QTL-hotspot genomic region",
        "agronomic_description": "Desi chickpea with deep taproot system and high water use efficiency under dryland",
        "developing_institution": "ICAR-IARI",
        "genetic_purity_score": 99.60,
        "heritability_broad_sense": 0.84,
        "drought_susceptibility_index": 0.62,
        "harvest_index_pct": 45.2,
        "recommended_agro_climatic_zones": [
            "Zone 10: Indo-Gangetic Plains & Central Plateau",
            "Zone 11: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0206",
        "variety_name": "Pigeonpea BDN 711 Genotype Line v21",
        "target_trait": "Fusarium Wilt & Sterility Mosaic Tolerance",
        "major_qtl_markers": "Cc-RFLP-Wilt1",
        "agronomic_description": "White seeded medium duration variety highly adapted to rainfed black cotton vertisols",
        "developing_institution": "VNMKV",
        "genetic_purity_score": 99.70,
        "heritability_broad_sense": 0.85,
        "drought_susceptibility_index": 0.64,
        "harvest_index_pct": 46.0,
        "recommended_agro_climatic_zones": [
            "Zone 11: Indo-Gangetic Plains & Central Plateau",
            "Zone 12: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0207",
        "variety_name": "Mustard PM 28 Genotype Line v21",
        "target_trait": "High Oleic / Low Glucosinolate Double Zero Quality",
        "major_qtl_markers": "FAD2 mutation, GSL1 deletion",
        "agronomic_description": "Canola quality Brassica juncea with heart-healthy fatty acid profile",
        "developing_institution": "ICAR-DRMR",
        "genetic_purity_score": 99.80,
        "heritability_broad_sense": 0.86,
        "drought_susceptibility_index": 0.66,
        "harvest_index_pct": 46.8,
        "recommended_agro_climatic_zones": [
            "Zone 12: Indo-Gangetic Plains & Central Plateau",
            "Zone 13: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0208",
        "variety_name": "Cotton Bunny Bt (NCS 145) Genotype Line v21",
        "target_trait": "Bollworm Resistance & Sucking Pest Tolerance",
        "major_qtl_markers": "Cry1Ac + Cry2Ab (Bollgard II)",
        "agronomic_description": "High boll retention, exceptional ginning outturn (36%), and staple length (31mm)",
        "developing_institution": "Nuziveedu Seeds",
        "genetic_purity_score": 99.90,
        "heritability_broad_sense": 0.87,
        "drought_susceptibility_index": 0.68,
        "harvest_index_pct": 47.6,
        "recommended_agro_climatic_zones": [
            "Zone 13: Indo-Gangetic Plains & Central Plateau",
            "Zone 14: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0209",
        "variety_name": "Tomato Arka Rakshak (F1 Hybrid) Genotype Line v21",
        "target_trait": "Triple Disease Resistance (ToLCV, BW, EB)",
        "major_qtl_markers": "Ty-2, Ty-3, Bwr-12, Ph-3",
        "agronomic_description": "High yielding indeterminate tomato with resistance to leaf curl virus, bacterial wilt, and early blight",
        "developing_institution": "ICAR-IIHR",
        "genetic_purity_score": 99.20,
        "heritability_broad_sense": 0.88,
        "drought_susceptibility_index": 0.70,
        "harvest_index_pct": 48.4,
        "recommended_agro_climatic_zones": [
            "Zone 14: Indo-Gangetic Plains & Central Plateau",
            "Zone 15: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0210",
        "variety_name": "Chilli Arka Harita Genotype Line v21",
        "target_trait": "Powdery Mildew & Anthracnose Tolerance",
        "major_qtl_markers": "Pm-1, Colletotrichum-R1",
        "agronomic_description": "High pungency (0.45% capsaicin) dual-purpose hybrid for green and dry red chilli export",
        "developing_institution": "ICAR-IIHR",
        "genetic_purity_score": 99.30,
        "heritability_broad_sense": 0.89,
        "drought_susceptibility_index": 0.72,
        "harvest_index_pct": 49.2,
        "recommended_agro_climatic_zones": [
            "Zone 15: Indo-Gangetic Plains & Central Plateau",
            "Zone 1: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0211",
        "variety_name": "Rice Swarna Sub1 Genotype Line v22",
        "target_trait": "Submergence / Flash Flood Tolerance",
        "major_qtl_markers": "Sub1A Transcription Factor",
        "agronomic_description": "Direct seeded or transplanted lowland rice with 14-day complete water submergence survival",
        "developing_institution": "Central Rice Research Institute (CRRI)",
        "genetic_purity_score": 99.40,
        "heritability_broad_sense": 0.90,
        "drought_susceptibility_index": 0.74,
        "harvest_index_pct": 42.0,
        "recommended_agro_climatic_zones": [
            "Zone 1: Indo-Gangetic Plains & Central Plateau",
            "Zone 2: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0212",
        "variety_name": "Rice CR Dhan 801 Genotype Line v22",
        "target_trait": "Drought + Submergence Dual Tolerance",
        "major_qtl_markers": "qDTY1.1, qDTY2.1, Sub1A",
        "agronomic_description": "Climate-resilient dual tolerant line for rainfed drought-prone and flood-prone ecologies",
        "developing_institution": "ICAR-NRRI",
        "genetic_purity_score": 99.50,
        "heritability_broad_sense": 0.91,
        "drought_susceptibility_index": 0.76,
        "harvest_index_pct": 42.8,
        "recommended_agro_climatic_zones": [
            "Zone 2: Indo-Gangetic Plains & Central Plateau",
            "Zone 3: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0213",
        "variety_name": "Wheat DBW 303 (Karan Vaishnavi) Genotype Line v22",
        "target_trait": "Terminal Heat Stress Resistance",
        "major_qtl_markers": "TaHsfA2d, TaFER-5B",
        "agronomic_description": "High-yielding irrigated timely sown bread wheat with extreme heat resilience during grain filling",
        "developing_institution": "ICAR-IIWBR",
        "genetic_purity_score": 99.60,
        "heritability_broad_sense": 0.92,
        "drought_susceptibility_index": 0.78,
        "harvest_index_pct": 43.6,
        "recommended_agro_climatic_zones": [
            "Zone 3: Indo-Gangetic Plains & Central Plateau",
            "Zone 4: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0214",
        "variety_name": "Wheat HD 3226 (Pusa Yashasvi) Genotype Line v22",
        "target_trait": "Multi-Rust Resistance (Yellow, Brown, Black)",
        "major_qtl_markers": "Yr17, Lr37, Sr38",
        "agronomic_description": "Superior chapati-making and biscuit-making quality with high gluten strength",
        "developing_institution": "ICAR-IARI",
        "genetic_purity_score": 99.70,
        "heritability_broad_sense": 0.93,
        "drought_susceptibility_index": 0.80,
        "harvest_index_pct": 44.4,
        "recommended_agro_climatic_zones": [
            "Zone 4: Indo-Gangetic Plains & Central Plateau",
            "Zone 5: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0215",
        "variety_name": "Chickpea Pusa 10216 Genotype Line v22",
        "target_trait": "Drought Drought Tolerance & Root Architecture",
        "major_qtl_markers": "qRT9.1, QTL-hotspot genomic region",
        "agronomic_description": "Desi chickpea with deep taproot system and high water use efficiency under dryland",
        "developing_institution": "ICAR-IARI",
        "genetic_purity_score": 99.80,
        "heritability_broad_sense": 0.94,
        "drought_susceptibility_index": 0.82,
        "harvest_index_pct": 45.2,
        "recommended_agro_climatic_zones": [
            "Zone 5: Indo-Gangetic Plains & Central Plateau",
            "Zone 6: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0216",
        "variety_name": "Pigeonpea BDN 711 Genotype Line v22",
        "target_trait": "Fusarium Wilt & Sterility Mosaic Tolerance",
        "major_qtl_markers": "Cc-RFLP-Wilt1",
        "agronomic_description": "White seeded medium duration variety highly adapted to rainfed black cotton vertisols",
        "developing_institution": "VNMKV",
        "genetic_purity_score": 99.90,
        "heritability_broad_sense": 0.95,
        "drought_susceptibility_index": 0.84,
        "harvest_index_pct": 46.0,
        "recommended_agro_climatic_zones": [
            "Zone 6: Indo-Gangetic Plains & Central Plateau",
            "Zone 7: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0217",
        "variety_name": "Mustard PM 28 Genotype Line v22",
        "target_trait": "High Oleic / Low Glucosinolate Double Zero Quality",
        "major_qtl_markers": "FAD2 mutation, GSL1 deletion",
        "agronomic_description": "Canola quality Brassica juncea with heart-healthy fatty acid profile",
        "developing_institution": "ICAR-DRMR",
        "genetic_purity_score": 99.20,
        "heritability_broad_sense": 0.78,
        "drought_susceptibility_index": 0.62,
        "harvest_index_pct": 46.8,
        "recommended_agro_climatic_zones": [
            "Zone 7: Indo-Gangetic Plains & Central Plateau",
            "Zone 8: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0218",
        "variety_name": "Cotton Bunny Bt (NCS 145) Genotype Line v22",
        "target_trait": "Bollworm Resistance & Sucking Pest Tolerance",
        "major_qtl_markers": "Cry1Ac + Cry2Ab (Bollgard II)",
        "agronomic_description": "High boll retention, exceptional ginning outturn (36%), and staple length (31mm)",
        "developing_institution": "Nuziveedu Seeds",
        "genetic_purity_score": 99.30,
        "heritability_broad_sense": 0.79,
        "drought_susceptibility_index": 0.64,
        "harvest_index_pct": 47.6,
        "recommended_agro_climatic_zones": [
            "Zone 8: Indo-Gangetic Plains & Central Plateau",
            "Zone 9: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0219",
        "variety_name": "Tomato Arka Rakshak (F1 Hybrid) Genotype Line v22",
        "target_trait": "Triple Disease Resistance (ToLCV, BW, EB)",
        "major_qtl_markers": "Ty-2, Ty-3, Bwr-12, Ph-3",
        "agronomic_description": "High yielding indeterminate tomato with resistance to leaf curl virus, bacterial wilt, and early blight",
        "developing_institution": "ICAR-IIHR",
        "genetic_purity_score": 99.40,
        "heritability_broad_sense": 0.80,
        "drought_susceptibility_index": 0.66,
        "harvest_index_pct": 48.4,
        "recommended_agro_climatic_zones": [
            "Zone 9: Indo-Gangetic Plains & Central Plateau",
            "Zone 10: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0220",
        "variety_name": "Chilli Arka Harita Genotype Line v22",
        "target_trait": "Powdery Mildew & Anthracnose Tolerance",
        "major_qtl_markers": "Pm-1, Colletotrichum-R1",
        "agronomic_description": "High pungency (0.45% capsaicin) dual-purpose hybrid for green and dry red chilli export",
        "developing_institution": "ICAR-IIHR",
        "genetic_purity_score": 99.50,
        "heritability_broad_sense": 0.81,
        "drought_susceptibility_index": 0.68,
        "harvest_index_pct": 49.2,
        "recommended_agro_climatic_zones": [
            "Zone 10: Indo-Gangetic Plains & Central Plateau",
            "Zone 11: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0221",
        "variety_name": "Rice Swarna Sub1 Genotype Line v23",
        "target_trait": "Submergence / Flash Flood Tolerance",
        "major_qtl_markers": "Sub1A Transcription Factor",
        "agronomic_description": "Direct seeded or transplanted lowland rice with 14-day complete water submergence survival",
        "developing_institution": "Central Rice Research Institute (CRRI)",
        "genetic_purity_score": 99.60,
        "heritability_broad_sense": 0.82,
        "drought_susceptibility_index": 0.70,
        "harvest_index_pct": 42.0,
        "recommended_agro_climatic_zones": [
            "Zone 11: Indo-Gangetic Plains & Central Plateau",
            "Zone 12: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0222",
        "variety_name": "Rice CR Dhan 801 Genotype Line v23",
        "target_trait": "Drought + Submergence Dual Tolerance",
        "major_qtl_markers": "qDTY1.1, qDTY2.1, Sub1A",
        "agronomic_description": "Climate-resilient dual tolerant line for rainfed drought-prone and flood-prone ecologies",
        "developing_institution": "ICAR-NRRI",
        "genetic_purity_score": 99.70,
        "heritability_broad_sense": 0.83,
        "drought_susceptibility_index": 0.72,
        "harvest_index_pct": 42.8,
        "recommended_agro_climatic_zones": [
            "Zone 12: Indo-Gangetic Plains & Central Plateau",
            "Zone 13: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0223",
        "variety_name": "Wheat DBW 303 (Karan Vaishnavi) Genotype Line v23",
        "target_trait": "Terminal Heat Stress Resistance",
        "major_qtl_markers": "TaHsfA2d, TaFER-5B",
        "agronomic_description": "High-yielding irrigated timely sown bread wheat with extreme heat resilience during grain filling",
        "developing_institution": "ICAR-IIWBR",
        "genetic_purity_score": 99.80,
        "heritability_broad_sense": 0.84,
        "drought_susceptibility_index": 0.74,
        "harvest_index_pct": 43.6,
        "recommended_agro_climatic_zones": [
            "Zone 13: Indo-Gangetic Plains & Central Plateau",
            "Zone 14: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0224",
        "variety_name": "Wheat HD 3226 (Pusa Yashasvi) Genotype Line v23",
        "target_trait": "Multi-Rust Resistance (Yellow, Brown, Black)",
        "major_qtl_markers": "Yr17, Lr37, Sr38",
        "agronomic_description": "Superior chapati-making and biscuit-making quality with high gluten strength",
        "developing_institution": "ICAR-IARI",
        "genetic_purity_score": 99.90,
        "heritability_broad_sense": 0.85,
        "drought_susceptibility_index": 0.76,
        "harvest_index_pct": 44.4,
        "recommended_agro_climatic_zones": [
            "Zone 14: Indo-Gangetic Plains & Central Plateau",
            "Zone 15: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0225",
        "variety_name": "Chickpea Pusa 10216 Genotype Line v23",
        "target_trait": "Drought Drought Tolerance & Root Architecture",
        "major_qtl_markers": "qRT9.1, QTL-hotspot genomic region",
        "agronomic_description": "Desi chickpea with deep taproot system and high water use efficiency under dryland",
        "developing_institution": "ICAR-IARI",
        "genetic_purity_score": 99.20,
        "heritability_broad_sense": 0.86,
        "drought_susceptibility_index": 0.78,
        "harvest_index_pct": 45.2,
        "recommended_agro_climatic_zones": [
            "Zone 15: Indo-Gangetic Plains & Central Plateau",
            "Zone 1: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0226",
        "variety_name": "Pigeonpea BDN 711 Genotype Line v23",
        "target_trait": "Fusarium Wilt & Sterility Mosaic Tolerance",
        "major_qtl_markers": "Cc-RFLP-Wilt1",
        "agronomic_description": "White seeded medium duration variety highly adapted to rainfed black cotton vertisols",
        "developing_institution": "VNMKV",
        "genetic_purity_score": 99.30,
        "heritability_broad_sense": 0.87,
        "drought_susceptibility_index": 0.80,
        "harvest_index_pct": 46.0,
        "recommended_agro_climatic_zones": [
            "Zone 1: Indo-Gangetic Plains & Central Plateau",
            "Zone 2: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0227",
        "variety_name": "Mustard PM 28 Genotype Line v23",
        "target_trait": "High Oleic / Low Glucosinolate Double Zero Quality",
        "major_qtl_markers": "FAD2 mutation, GSL1 deletion",
        "agronomic_description": "Canola quality Brassica juncea with heart-healthy fatty acid profile",
        "developing_institution": "ICAR-DRMR",
        "genetic_purity_score": 99.40,
        "heritability_broad_sense": 0.88,
        "drought_susceptibility_index": 0.82,
        "harvest_index_pct": 46.8,
        "recommended_agro_climatic_zones": [
            "Zone 2: Indo-Gangetic Plains & Central Plateau",
            "Zone 3: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0228",
        "variety_name": "Cotton Bunny Bt (NCS 145) Genotype Line v23",
        "target_trait": "Bollworm Resistance & Sucking Pest Tolerance",
        "major_qtl_markers": "Cry1Ac + Cry2Ab (Bollgard II)",
        "agronomic_description": "High boll retention, exceptional ginning outturn (36%), and staple length (31mm)",
        "developing_institution": "Nuziveedu Seeds",
        "genetic_purity_score": 99.50,
        "heritability_broad_sense": 0.89,
        "drought_susceptibility_index": 0.84,
        "harvest_index_pct": 47.6,
        "recommended_agro_climatic_zones": [
            "Zone 3: Indo-Gangetic Plains & Central Plateau",
            "Zone 4: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0229",
        "variety_name": "Tomato Arka Rakshak (F1 Hybrid) Genotype Line v23",
        "target_trait": "Triple Disease Resistance (ToLCV, BW, EB)",
        "major_qtl_markers": "Ty-2, Ty-3, Bwr-12, Ph-3",
        "agronomic_description": "High yielding indeterminate tomato with resistance to leaf curl virus, bacterial wilt, and early blight",
        "developing_institution": "ICAR-IIHR",
        "genetic_purity_score": 99.60,
        "heritability_broad_sense": 0.90,
        "drought_susceptibility_index": 0.62,
        "harvest_index_pct": 48.4,
        "recommended_agro_climatic_zones": [
            "Zone 4: Indo-Gangetic Plains & Central Plateau",
            "Zone 5: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0230",
        "variety_name": "Chilli Arka Harita Genotype Line v23",
        "target_trait": "Powdery Mildew & Anthracnose Tolerance",
        "major_qtl_markers": "Pm-1, Colletotrichum-R1",
        "agronomic_description": "High pungency (0.45% capsaicin) dual-purpose hybrid for green and dry red chilli export",
        "developing_institution": "ICAR-IIHR",
        "genetic_purity_score": 99.70,
        "heritability_broad_sense": 0.91,
        "drought_susceptibility_index": 0.64,
        "harvest_index_pct": 49.2,
        "recommended_agro_climatic_zones": [
            "Zone 5: Indo-Gangetic Plains & Central Plateau",
            "Zone 6: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0231",
        "variety_name": "Rice Swarna Sub1 Genotype Line v24",
        "target_trait": "Submergence / Flash Flood Tolerance",
        "major_qtl_markers": "Sub1A Transcription Factor",
        "agronomic_description": "Direct seeded or transplanted lowland rice with 14-day complete water submergence survival",
        "developing_institution": "Central Rice Research Institute (CRRI)",
        "genetic_purity_score": 99.80,
        "heritability_broad_sense": 0.92,
        "drought_susceptibility_index": 0.66,
        "harvest_index_pct": 42.0,
        "recommended_agro_climatic_zones": [
            "Zone 6: Indo-Gangetic Plains & Central Plateau",
            "Zone 7: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0232",
        "variety_name": "Rice CR Dhan 801 Genotype Line v24",
        "target_trait": "Drought + Submergence Dual Tolerance",
        "major_qtl_markers": "qDTY1.1, qDTY2.1, Sub1A",
        "agronomic_description": "Climate-resilient dual tolerant line for rainfed drought-prone and flood-prone ecologies",
        "developing_institution": "ICAR-NRRI",
        "genetic_purity_score": 99.90,
        "heritability_broad_sense": 0.93,
        "drought_susceptibility_index": 0.68,
        "harvest_index_pct": 42.8,
        "recommended_agro_climatic_zones": [
            "Zone 7: Indo-Gangetic Plains & Central Plateau",
            "Zone 8: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0233",
        "variety_name": "Wheat DBW 303 (Karan Vaishnavi) Genotype Line v24",
        "target_trait": "Terminal Heat Stress Resistance",
        "major_qtl_markers": "TaHsfA2d, TaFER-5B",
        "agronomic_description": "High-yielding irrigated timely sown bread wheat with extreme heat resilience during grain filling",
        "developing_institution": "ICAR-IIWBR",
        "genetic_purity_score": 99.20,
        "heritability_broad_sense": 0.94,
        "drought_susceptibility_index": 0.70,
        "harvest_index_pct": 43.6,
        "recommended_agro_climatic_zones": [
            "Zone 8: Indo-Gangetic Plains & Central Plateau",
            "Zone 9: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0234",
        "variety_name": "Wheat HD 3226 (Pusa Yashasvi) Genotype Line v24",
        "target_trait": "Multi-Rust Resistance (Yellow, Brown, Black)",
        "major_qtl_markers": "Yr17, Lr37, Sr38",
        "agronomic_description": "Superior chapati-making and biscuit-making quality with high gluten strength",
        "developing_institution": "ICAR-IARI",
        "genetic_purity_score": 99.30,
        "heritability_broad_sense": 0.95,
        "drought_susceptibility_index": 0.72,
        "harvest_index_pct": 44.4,
        "recommended_agro_climatic_zones": [
            "Zone 9: Indo-Gangetic Plains & Central Plateau",
            "Zone 10: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0235",
        "variety_name": "Chickpea Pusa 10216 Genotype Line v24",
        "target_trait": "Drought Drought Tolerance & Root Architecture",
        "major_qtl_markers": "qRT9.1, QTL-hotspot genomic region",
        "agronomic_description": "Desi chickpea with deep taproot system and high water use efficiency under dryland",
        "developing_institution": "ICAR-IARI",
        "genetic_purity_score": 99.40,
        "heritability_broad_sense": 0.78,
        "drought_susceptibility_index": 0.74,
        "harvest_index_pct": 45.2,
        "recommended_agro_climatic_zones": [
            "Zone 10: Indo-Gangetic Plains & Central Plateau",
            "Zone 11: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0236",
        "variety_name": "Pigeonpea BDN 711 Genotype Line v24",
        "target_trait": "Fusarium Wilt & Sterility Mosaic Tolerance",
        "major_qtl_markers": "Cc-RFLP-Wilt1",
        "agronomic_description": "White seeded medium duration variety highly adapted to rainfed black cotton vertisols",
        "developing_institution": "VNMKV",
        "genetic_purity_score": 99.50,
        "heritability_broad_sense": 0.79,
        "drought_susceptibility_index": 0.76,
        "harvest_index_pct": 46.0,
        "recommended_agro_climatic_zones": [
            "Zone 11: Indo-Gangetic Plains & Central Plateau",
            "Zone 12: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0237",
        "variety_name": "Mustard PM 28 Genotype Line v24",
        "target_trait": "High Oleic / Low Glucosinolate Double Zero Quality",
        "major_qtl_markers": "FAD2 mutation, GSL1 deletion",
        "agronomic_description": "Canola quality Brassica juncea with heart-healthy fatty acid profile",
        "developing_institution": "ICAR-DRMR",
        "genetic_purity_score": 99.60,
        "heritability_broad_sense": 0.80,
        "drought_susceptibility_index": 0.78,
        "harvest_index_pct": 46.8,
        "recommended_agro_climatic_zones": [
            "Zone 12: Indo-Gangetic Plains & Central Plateau",
            "Zone 13: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0238",
        "variety_name": "Cotton Bunny Bt (NCS 145) Genotype Line v24",
        "target_trait": "Bollworm Resistance & Sucking Pest Tolerance",
        "major_qtl_markers": "Cry1Ac + Cry2Ab (Bollgard II)",
        "agronomic_description": "High boll retention, exceptional ginning outturn (36%), and staple length (31mm)",
        "developing_institution": "Nuziveedu Seeds",
        "genetic_purity_score": 99.70,
        "heritability_broad_sense": 0.81,
        "drought_susceptibility_index": 0.80,
        "harvest_index_pct": 47.6,
        "recommended_agro_climatic_zones": [
            "Zone 13: Indo-Gangetic Plains & Central Plateau",
            "Zone 14: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0239",
        "variety_name": "Tomato Arka Rakshak (F1 Hybrid) Genotype Line v24",
        "target_trait": "Triple Disease Resistance (ToLCV, BW, EB)",
        "major_qtl_markers": "Ty-2, Ty-3, Bwr-12, Ph-3",
        "agronomic_description": "High yielding indeterminate tomato with resistance to leaf curl virus, bacterial wilt, and early blight",
        "developing_institution": "ICAR-IIHR",
        "genetic_purity_score": 99.80,
        "heritability_broad_sense": 0.82,
        "drought_susceptibility_index": 0.82,
        "harvest_index_pct": 48.4,
        "recommended_agro_climatic_zones": [
            "Zone 14: Indo-Gangetic Plains & Central Plateau",
            "Zone 15: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0240",
        "variety_name": "Chilli Arka Harita Genotype Line v24",
        "target_trait": "Powdery Mildew & Anthracnose Tolerance",
        "major_qtl_markers": "Pm-1, Colletotrichum-R1",
        "agronomic_description": "High pungency (0.45% capsaicin) dual-purpose hybrid for green and dry red chilli export",
        "developing_institution": "ICAR-IIHR",
        "genetic_purity_score": 99.90,
        "heritability_broad_sense": 0.83,
        "drought_susceptibility_index": 0.84,
        "harvest_index_pct": 49.2,
        "recommended_agro_climatic_zones": [
            "Zone 15: Indo-Gangetic Plains & Central Plateau",
            "Zone 1: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0241",
        "variety_name": "Rice Swarna Sub1 Genotype Line v25",
        "target_trait": "Submergence / Flash Flood Tolerance",
        "major_qtl_markers": "Sub1A Transcription Factor",
        "agronomic_description": "Direct seeded or transplanted lowland rice with 14-day complete water submergence survival",
        "developing_institution": "Central Rice Research Institute (CRRI)",
        "genetic_purity_score": 99.20,
        "heritability_broad_sense": 0.84,
        "drought_susceptibility_index": 0.62,
        "harvest_index_pct": 42.0,
        "recommended_agro_climatic_zones": [
            "Zone 1: Indo-Gangetic Plains & Central Plateau",
            "Zone 2: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0242",
        "variety_name": "Rice CR Dhan 801 Genotype Line v25",
        "target_trait": "Drought + Submergence Dual Tolerance",
        "major_qtl_markers": "qDTY1.1, qDTY2.1, Sub1A",
        "agronomic_description": "Climate-resilient dual tolerant line for rainfed drought-prone and flood-prone ecologies",
        "developing_institution": "ICAR-NRRI",
        "genetic_purity_score": 99.30,
        "heritability_broad_sense": 0.85,
        "drought_susceptibility_index": 0.64,
        "harvest_index_pct": 42.8,
        "recommended_agro_climatic_zones": [
            "Zone 2: Indo-Gangetic Plains & Central Plateau",
            "Zone 3: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0243",
        "variety_name": "Wheat DBW 303 (Karan Vaishnavi) Genotype Line v25",
        "target_trait": "Terminal Heat Stress Resistance",
        "major_qtl_markers": "TaHsfA2d, TaFER-5B",
        "agronomic_description": "High-yielding irrigated timely sown bread wheat with extreme heat resilience during grain filling",
        "developing_institution": "ICAR-IIWBR",
        "genetic_purity_score": 99.40,
        "heritability_broad_sense": 0.86,
        "drought_susceptibility_index": 0.66,
        "harvest_index_pct": 43.6,
        "recommended_agro_climatic_zones": [
            "Zone 3: Indo-Gangetic Plains & Central Plateau",
            "Zone 4: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0244",
        "variety_name": "Wheat HD 3226 (Pusa Yashasvi) Genotype Line v25",
        "target_trait": "Multi-Rust Resistance (Yellow, Brown, Black)",
        "major_qtl_markers": "Yr17, Lr37, Sr38",
        "agronomic_description": "Superior chapati-making and biscuit-making quality with high gluten strength",
        "developing_institution": "ICAR-IARI",
        "genetic_purity_score": 99.50,
        "heritability_broad_sense": 0.87,
        "drought_susceptibility_index": 0.68,
        "harvest_index_pct": 44.4,
        "recommended_agro_climatic_zones": [
            "Zone 4: Indo-Gangetic Plains & Central Plateau",
            "Zone 5: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0245",
        "variety_name": "Chickpea Pusa 10216 Genotype Line v25",
        "target_trait": "Drought Drought Tolerance & Root Architecture",
        "major_qtl_markers": "qRT9.1, QTL-hotspot genomic region",
        "agronomic_description": "Desi chickpea with deep taproot system and high water use efficiency under dryland",
        "developing_institution": "ICAR-IARI",
        "genetic_purity_score": 99.60,
        "heritability_broad_sense": 0.88,
        "drought_susceptibility_index": 0.70,
        "harvest_index_pct": 45.2,
        "recommended_agro_climatic_zones": [
            "Zone 5: Indo-Gangetic Plains & Central Plateau",
            "Zone 6: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0246",
        "variety_name": "Pigeonpea BDN 711 Genotype Line v25",
        "target_trait": "Fusarium Wilt & Sterility Mosaic Tolerance",
        "major_qtl_markers": "Cc-RFLP-Wilt1",
        "agronomic_description": "White seeded medium duration variety highly adapted to rainfed black cotton vertisols",
        "developing_institution": "VNMKV",
        "genetic_purity_score": 99.70,
        "heritability_broad_sense": 0.89,
        "drought_susceptibility_index": 0.72,
        "harvest_index_pct": 46.0,
        "recommended_agro_climatic_zones": [
            "Zone 6: Indo-Gangetic Plains & Central Plateau",
            "Zone 7: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0247",
        "variety_name": "Mustard PM 28 Genotype Line v25",
        "target_trait": "High Oleic / Low Glucosinolate Double Zero Quality",
        "major_qtl_markers": "FAD2 mutation, GSL1 deletion",
        "agronomic_description": "Canola quality Brassica juncea with heart-healthy fatty acid profile",
        "developing_institution": "ICAR-DRMR",
        "genetic_purity_score": 99.80,
        "heritability_broad_sense": 0.90,
        "drought_susceptibility_index": 0.74,
        "harvest_index_pct": 46.8,
        "recommended_agro_climatic_zones": [
            "Zone 7: Indo-Gangetic Plains & Central Plateau",
            "Zone 8: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0248",
        "variety_name": "Cotton Bunny Bt (NCS 145) Genotype Line v25",
        "target_trait": "Bollworm Resistance & Sucking Pest Tolerance",
        "major_qtl_markers": "Cry1Ac + Cry2Ab (Bollgard II)",
        "agronomic_description": "High boll retention, exceptional ginning outturn (36%), and staple length (31mm)",
        "developing_institution": "Nuziveedu Seeds",
        "genetic_purity_score": 99.90,
        "heritability_broad_sense": 0.91,
        "drought_susceptibility_index": 0.76,
        "harvest_index_pct": 47.6,
        "recommended_agro_climatic_zones": [
            "Zone 8: Indo-Gangetic Plains & Central Plateau",
            "Zone 9: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0249",
        "variety_name": "Tomato Arka Rakshak (F1 Hybrid) Genotype Line v25",
        "target_trait": "Triple Disease Resistance (ToLCV, BW, EB)",
        "major_qtl_markers": "Ty-2, Ty-3, Bwr-12, Ph-3",
        "agronomic_description": "High yielding indeterminate tomato with resistance to leaf curl virus, bacterial wilt, and early blight",
        "developing_institution": "ICAR-IIHR",
        "genetic_purity_score": 99.20,
        "heritability_broad_sense": 0.92,
        "drought_susceptibility_index": 0.78,
        "harvest_index_pct": 48.4,
        "recommended_agro_climatic_zones": [
            "Zone 9: Indo-Gangetic Plains & Central Plateau",
            "Zone 10: Deccan Plateau Semi-Arid Zone"
        ]
    },
    {
        "gene_accession_id": "GENE-ENTRY-0250",
        "variety_name": "Chilli Arka Harita Genotype Line v25",
        "target_trait": "Powdery Mildew & Anthracnose Tolerance",
        "major_qtl_markers": "Pm-1, Colletotrichum-R1",
        "agronomic_description": "High pungency (0.45% capsaicin) dual-purpose hybrid for green and dry red chilli export",
        "developing_institution": "ICAR-IIHR",
        "genetic_purity_score": 99.30,
        "heritability_broad_sense": 0.93,
        "drought_susceptibility_index": 0.80,
        "harvest_index_pct": 49.2,
        "recommended_agro_climatic_zones": [
            "Zone 10: Indo-Gangetic Plains & Central Plateau",
            "Zone 11: Deccan Plateau Semi-Arid Zone"
        ]
    },
]
