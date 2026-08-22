"""
Encyclopedic Plant Pathology & Pharmacological Chemical/Organic Compendium
"""
from typing import Dict, Any, List

PLANT_PATHOLOGY_COMPENDIUM: List[Dict[str, Any]] = [
    {
        "pathology_id": "PATH-0001",
        "disease_name": "Tomato / Potato Early Blight (Variant Strain 1)",
        "causal_organism": "Alternaria solani",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Foliar target-like concentric rings with yellow halo",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 18.0,
            "favorable_temperature_c_max": 28.0,
            "favorable_relative_humidity_pct": 75,
            "leaf_wetness_hours_threshold": 6
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Mancozeb 75% WP @ 2.5g/L", "frac_code": "1", "pre_harvest_interval_days": 7},
            {"active_formulation": "Copper Oxychloride @ 2.5g/L", "frac_code": "M1", "pre_harvest_interval_days": 5}
        ],
        "organic_biocontrol_protocol": [
            "Trichoderma harzianum @ 5g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0002",
        "disease_name": "Late Blight of Tomato / Potato (Variant Strain 1)",
        "causal_organism": "Phytophthora infestans",
        "pathogen_class": "Oomycete",
        "diagnostic_symptoms": "Rapid water-soaked necrotic lesions with white downy mold",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 19.0,
            "favorable_temperature_c_max": 29.0,
            "favorable_relative_humidity_pct": 76,
            "leaf_wetness_hours_threshold": 7
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Metalaxyl 8% + Mancozeb 64% WP @ 2.5g/L", "frac_code": "2", "pre_harvest_interval_days": 8},
            {"active_formulation": "Dimethomorph 50% WP @ 1.0g/L", "frac_code": "M2", "pre_harvest_interval_days": 6}
        ],
        "organic_biocontrol_protocol": [
            "Bacillus subtilis @ 3ml/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0003",
        "disease_name": "Rice Bacterial Leaf Blight (Variant Strain 1)",
        "causal_organism": "Xanthomonas oryzae",
        "pathogen_class": "Bacteria",
        "diagnostic_symptoms": "Straw yellow undulating leaf tip lesions with amber bacterial ooze",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 20.0,
            "favorable_temperature_c_max": 30.0,
            "favorable_relative_humidity_pct": 77,
            "leaf_wetness_hours_threshold": 8
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Streptocycline 90% + Copper 50% WP @ 0.1g+2.5g/L", "frac_code": "3", "pre_harvest_interval_days": 9},
            {"active_formulation": "Kasugamycin 3% SL @ 2.0ml/L", "frac_code": "M3", "pre_harvest_interval_days": 7}
        ],
        "organic_biocontrol_protocol": [
            "Pseudomonas fluorescens @ 2.5g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0004",
        "disease_name": "Rice Blast (Leaf, Node, Neck) (Variant Strain 1)",
        "causal_organism": "Magnaporthe oryzae",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Spindle / Eye-shaped diamond lesions with greyish center and brown border",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 21.0,
            "favorable_temperature_c_max": 31.0,
            "favorable_relative_humidity_pct": 78,
            "leaf_wetness_hours_threshold": 9
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Tricyclazole 75% WP @ 0.6g/L", "frac_code": "4", "pre_harvest_interval_days": 10},
            {"active_formulation": "Isoprothiolane 40% EC @ 1.5ml/L", "frac_code": "M4", "pre_harvest_interval_days": 8}
        ],
        "organic_biocontrol_protocol": [
            "Neem Seed Kernel Extract 5%",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0005",
        "disease_name": "Wheat Yellow / Stripe Rust (Variant Strain 1)",
        "causal_organism": "Puccinia striiformis",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Parallel linear yellow pustules erupting along leaf lamina",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 22.0,
            "favorable_temperature_c_max": 32.0,
            "favorable_relative_humidity_pct": 79,
            "leaf_wetness_hours_threshold": 10
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Propiconazole 25% EC @ 1.0ml/L", "frac_code": "5", "pre_harvest_interval_days": 11},
            {"active_formulation": "Tebuconazole 25.9% EC @ 1.2ml/L", "frac_code": "M5", "pre_harvest_interval_days": 9}
        ],
        "organic_biocontrol_protocol": [
            "Bio-formulation T. viride @ 5g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0006",
        "disease_name": "Wheat Brown / Leaf Rust (Variant Strain 1)",
        "causal_organism": "Puccinia triticina",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Scattered spherical orange-brown uredinial pustules",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 23.0,
            "favorable_temperature_c_max": 33.0,
            "favorable_relative_humidity_pct": 80,
            "leaf_wetness_hours_threshold": 11
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Mancozeb 75% WP @ 2.0g/L", "frac_code": "6", "pre_harvest_interval_days": 12},
            {"active_formulation": "Propiconazole 25% EC @ 1.0ml/L", "frac_code": "M1", "pre_harvest_interval_days": 10}
        ],
        "organic_biocontrol_protocol": [
            "Sulphur 80% WDG @ 2.5g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0007",
        "disease_name": "Cotton Leaf Curl Virus (CLCuV) (Variant Strain 1)",
        "causal_organism": "Begomovirus / Whitefly",
        "pathogen_class": "Viral Complex",
        "diagnostic_symptoms": "Upward leaf cupping, thickened dark green veins and enations",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 18.0,
            "favorable_temperature_c_max": 34.0,
            "favorable_relative_humidity_pct": 81,
            "leaf_wetness_hours_threshold": 12
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Diafenthiuron 50% WP @ 1.2g/L", "frac_code": "7", "pre_harvest_interval_days": 13},
            {"active_formulation": "Pyriproxyfen 10% EC @ 2.0ml/L", "frac_code": "M2", "pre_harvest_interval_days": 11}
        ],
        "organic_biocontrol_protocol": [
            "Yellow Sticky Traps @ 20/acre + Neem Oil 10000ppm",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0008",
        "disease_name": "Maize Fall Armyworm (Variant Strain 1)",
        "causal_organism": "Spodoptera frugiperda",
        "pathogen_class": "Insect Pest",
        "diagnostic_symptoms": "Ragged shot-holes and sawdust larval frass packed in whorl",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 19.0,
            "favorable_temperature_c_max": 35.0,
            "favorable_relative_humidity_pct": 82,
            "leaf_wetness_hours_threshold": 13
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Emamectin Benzoate 5% SG @ 0.4g/L", "frac_code": "8", "pre_harvest_interval_days": 14},
            {"active_formulation": "Chlorantraniliprole 18.5% SC @ 0.3ml/L", "frac_code": "M3", "pre_harvest_interval_days": 12}
        ],
        "organic_biocontrol_protocol": [
            "Bacillus thuringiensis (Bt) kurstaki @ 2g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0009",
        "disease_name": "Chilli Anthracnose & Fruit Rot (Variant Strain 1)",
        "causal_organism": "Colletotrichum capsici",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Sunken circular dark lesions with salmon-pink spores on ripe pods",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 20.0,
            "favorable_temperature_c_max": 28.0,
            "favorable_relative_humidity_pct": 83,
            "leaf_wetness_hours_threshold": 6
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Difenoconazole 25% EC @ 0.8ml/L", "frac_code": "9", "pre_harvest_interval_days": 15},
            {"active_formulation": "Azoxystrobin 23% SC @ 1.0ml/L", "frac_code": "M4", "pre_harvest_interval_days": 13}
        ],
        "organic_biocontrol_protocol": [
            "Trichoderma viride root dip and foliar spray",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0010",
        "disease_name": "Powdery Mildew of Chilli / Tomato (Variant Strain 1)",
        "causal_organism": "Leveillula taurica",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "White powdery fungal growth on leaf undersides with yellowing above",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 21.0,
            "favorable_temperature_c_max": 29.0,
            "favorable_relative_humidity_pct": 84,
            "leaf_wetness_hours_threshold": 7
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Hexaconazole 5% SC @ 1.5ml/L", "frac_code": "10", "pre_harvest_interval_days": 16},
            {"active_formulation": "Wettable Sulphur 80% WP @ 2.5g/L", "frac_code": "M5", "pre_harvest_interval_days": 14}
        ],
        "organic_biocontrol_protocol": [
            "Ampelomyces quisqualis bio-fungicide",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0011",
        "disease_name": "Sheath Blight of Paddy / Damping Off (Variant Strain 1)",
        "causal_organism": "Rhizoctonia solani",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Snake-skin banded lesions on leaf sheaths near water line",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 22.0,
            "favorable_temperature_c_max": 30.0,
            "favorable_relative_humidity_pct": 85,
            "leaf_wetness_hours_threshold": 8
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Validamycin 3% L @ 2.0ml/L", "frac_code": "11", "pre_harvest_interval_days": 17},
            {"active_formulation": "Hexaconazole 5% EC @ 2.0ml/L", "frac_code": "M1", "pre_harvest_interval_days": 5}
        ],
        "organic_biocontrol_protocol": [
            "Pseudomonas seed dressing @ 10g/kg",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0012",
        "disease_name": "Bacterial Wilt of Solanaceous Crops (Variant Strain 1)",
        "causal_organism": "Ralstonia solanacearum",
        "pathogen_class": "Bacteria",
        "diagnostic_symptoms": "Sudden daytime wilting of plant without foliage yellowing",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 23.0,
            "favorable_temperature_c_max": 31.0,
            "favorable_relative_humidity_pct": 86,
            "leaf_wetness_hours_threshold": 9
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Copper Oxychloride drenching @ 3.0g/L", "frac_code": "12", "pre_harvest_interval_days": 18},
            {"active_formulation": "Streptocycline drenching @ 0.2g/L", "frac_code": "M2", "pre_harvest_interval_days": 6}
        ],
        "organic_biocontrol_protocol": [
            "Bio-enrichment of soil with Trichoderma + FYM",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0013",
        "disease_name": "Fusarium Vascular Wilt (Variant Strain 1)",
        "causal_organism": "Fusarium oxysporum",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Vascular browning inside stem xylem and lower leaf chlorosis",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 18.0,
            "favorable_temperature_c_max": 32.0,
            "favorable_relative_humidity_pct": 87,
            "leaf_wetness_hours_threshold": 10
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Carbendazim 50% WP @ 1.5g/L", "frac_code": "13", "pre_harvest_interval_days": 19},
            {"active_formulation": "Thiophanate Methyl 70% WP @ 1.5g/L", "frac_code": "M3", "pre_harvest_interval_days": 7}
        ],
        "organic_biocontrol_protocol": [
            "Trichoderma harzianum @ 10g/L root zone drench",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0014",
        "disease_name": "Tomato Leaf Curl Begomovirus (ToLCV) (Variant Strain 1)",
        "causal_organism": "Bemisia tabaci",
        "pathogen_class": "Insect Vector",
        "diagnostic_symptoms": "Severe curling, puckering, reduction in leaf lamina size, stunting",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 19.0,
            "favorable_temperature_c_max": 33.0,
            "favorable_relative_humidity_pct": 88,
            "leaf_wetness_hours_threshold": 11
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Imidacloprid 17.8% SL @ 0.5ml/L", "frac_code": "14", "pre_harvest_interval_days": 20},
            {"active_formulation": "Acetamiprid 20% SP @ 0.3g/L", "frac_code": "M4", "pre_harvest_interval_days": 8}
        ],
        "organic_biocontrol_protocol": [
            "Fine insect netting (40 mesh) + Neem extract",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0015",
        "disease_name": "Root Knot Nematode Complex (Variant Strain 1)",
        "causal_organism": "Meloidogyne incognita",
        "pathogen_class": "Nematode",
        "diagnostic_symptoms": "Severe root galling, stunting, chlorosis and nutrient starvation",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 20.0,
            "favorable_temperature_c_max": 34.0,
            "favorable_relative_humidity_pct": 89,
            "leaf_wetness_hours_threshold": 12
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Fluopyram 34.48% SC @ 2.0ml/m2", "frac_code": "15", "pre_harvest_interval_days": 7},
            {"active_formulation": "Carbofuran 3% CG @ 10kg/acre", "frac_code": "M5", "pre_harvest_interval_days": 9}
        ],
        "organic_biocontrol_protocol": [
            "Paecilomyces lilacinus bio-nematicide @ 5kg/acre",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0016",
        "disease_name": "Tomato / Potato Early Blight (Variant Strain 2)",
        "causal_organism": "Alternaria solani",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Foliar target-like concentric rings with yellow halo",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 21.0,
            "favorable_temperature_c_max": 35.0,
            "favorable_relative_humidity_pct": 90,
            "leaf_wetness_hours_threshold": 13
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Mancozeb 75% WP @ 2.5g/L", "frac_code": "16", "pre_harvest_interval_days": 8},
            {"active_formulation": "Copper Oxychloride @ 2.5g/L", "frac_code": "M1", "pre_harvest_interval_days": 10}
        ],
        "organic_biocontrol_protocol": [
            "Trichoderma harzianum @ 5g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0017",
        "disease_name": "Late Blight of Tomato / Potato (Variant Strain 2)",
        "causal_organism": "Phytophthora infestans",
        "pathogen_class": "Oomycete",
        "diagnostic_symptoms": "Rapid water-soaked necrotic lesions with white downy mold",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 22.0,
            "favorable_temperature_c_max": 28.0,
            "favorable_relative_humidity_pct": 91,
            "leaf_wetness_hours_threshold": 6
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Metalaxyl 8% + Mancozeb 64% WP @ 2.5g/L", "frac_code": "17", "pre_harvest_interval_days": 9},
            {"active_formulation": "Dimethomorph 50% WP @ 1.0g/L", "frac_code": "M2", "pre_harvest_interval_days": 11}
        ],
        "organic_biocontrol_protocol": [
            "Bacillus subtilis @ 3ml/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0018",
        "disease_name": "Rice Bacterial Leaf Blight (Variant Strain 2)",
        "causal_organism": "Xanthomonas oryzae",
        "pathogen_class": "Bacteria",
        "diagnostic_symptoms": "Straw yellow undulating leaf tip lesions with amber bacterial ooze",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 23.0,
            "favorable_temperature_c_max": 29.0,
            "favorable_relative_humidity_pct": 92,
            "leaf_wetness_hours_threshold": 7
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Streptocycline 90% + Copper 50% WP @ 0.1g+2.5g/L", "frac_code": "18", "pre_harvest_interval_days": 10},
            {"active_formulation": "Kasugamycin 3% SL @ 2.0ml/L", "frac_code": "M3", "pre_harvest_interval_days": 12}
        ],
        "organic_biocontrol_protocol": [
            "Pseudomonas fluorescens @ 2.5g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0019",
        "disease_name": "Rice Blast (Leaf, Node, Neck) (Variant Strain 2)",
        "causal_organism": "Magnaporthe oryzae",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Spindle / Eye-shaped diamond lesions with greyish center and brown border",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 18.0,
            "favorable_temperature_c_max": 30.0,
            "favorable_relative_humidity_pct": 93,
            "leaf_wetness_hours_threshold": 8
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Tricyclazole 75% WP @ 0.6g/L", "frac_code": "19", "pre_harvest_interval_days": 11},
            {"active_formulation": "Isoprothiolane 40% EC @ 1.5ml/L", "frac_code": "M4", "pre_harvest_interval_days": 13}
        ],
        "organic_biocontrol_protocol": [
            "Neem Seed Kernel Extract 5%",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0020",
        "disease_name": "Wheat Yellow / Stripe Rust (Variant Strain 2)",
        "causal_organism": "Puccinia striiformis",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Parallel linear yellow pustules erupting along leaf lamina",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 19.0,
            "favorable_temperature_c_max": 31.0,
            "favorable_relative_humidity_pct": 94,
            "leaf_wetness_hours_threshold": 9
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Propiconazole 25% EC @ 1.0ml/L", "frac_code": "20", "pre_harvest_interval_days": 12},
            {"active_formulation": "Tebuconazole 25.9% EC @ 1.2ml/L", "frac_code": "M5", "pre_harvest_interval_days": 14}
        ],
        "organic_biocontrol_protocol": [
            "Bio-formulation T. viride @ 5g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0021",
        "disease_name": "Wheat Brown / Leaf Rust (Variant Strain 2)",
        "causal_organism": "Puccinia triticina",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Scattered spherical orange-brown uredinial pustules",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 20.0,
            "favorable_temperature_c_max": 32.0,
            "favorable_relative_humidity_pct": 75,
            "leaf_wetness_hours_threshold": 10
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Mancozeb 75% WP @ 2.0g/L", "frac_code": "1", "pre_harvest_interval_days": 13},
            {"active_formulation": "Propiconazole 25% EC @ 1.0ml/L", "frac_code": "M1", "pre_harvest_interval_days": 5}
        ],
        "organic_biocontrol_protocol": [
            "Sulphur 80% WDG @ 2.5g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0022",
        "disease_name": "Cotton Leaf Curl Virus (CLCuV) (Variant Strain 2)",
        "causal_organism": "Begomovirus / Whitefly",
        "pathogen_class": "Viral Complex",
        "diagnostic_symptoms": "Upward leaf cupping, thickened dark green veins and enations",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 21.0,
            "favorable_temperature_c_max": 33.0,
            "favorable_relative_humidity_pct": 76,
            "leaf_wetness_hours_threshold": 11
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Diafenthiuron 50% WP @ 1.2g/L", "frac_code": "2", "pre_harvest_interval_days": 14},
            {"active_formulation": "Pyriproxyfen 10% EC @ 2.0ml/L", "frac_code": "M2", "pre_harvest_interval_days": 6}
        ],
        "organic_biocontrol_protocol": [
            "Yellow Sticky Traps @ 20/acre + Neem Oil 10000ppm",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0023",
        "disease_name": "Maize Fall Armyworm (Variant Strain 2)",
        "causal_organism": "Spodoptera frugiperda",
        "pathogen_class": "Insect Pest",
        "diagnostic_symptoms": "Ragged shot-holes and sawdust larval frass packed in whorl",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 22.0,
            "favorable_temperature_c_max": 34.0,
            "favorable_relative_humidity_pct": 77,
            "leaf_wetness_hours_threshold": 12
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Emamectin Benzoate 5% SG @ 0.4g/L", "frac_code": "3", "pre_harvest_interval_days": 15},
            {"active_formulation": "Chlorantraniliprole 18.5% SC @ 0.3ml/L", "frac_code": "M3", "pre_harvest_interval_days": 7}
        ],
        "organic_biocontrol_protocol": [
            "Bacillus thuringiensis (Bt) kurstaki @ 2g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0024",
        "disease_name": "Chilli Anthracnose & Fruit Rot (Variant Strain 2)",
        "causal_organism": "Colletotrichum capsici",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Sunken circular dark lesions with salmon-pink spores on ripe pods",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 23.0,
            "favorable_temperature_c_max": 35.0,
            "favorable_relative_humidity_pct": 78,
            "leaf_wetness_hours_threshold": 13
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Difenoconazole 25% EC @ 0.8ml/L", "frac_code": "4", "pre_harvest_interval_days": 16},
            {"active_formulation": "Azoxystrobin 23% SC @ 1.0ml/L", "frac_code": "M4", "pre_harvest_interval_days": 8}
        ],
        "organic_biocontrol_protocol": [
            "Trichoderma viride root dip and foliar spray",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0025",
        "disease_name": "Powdery Mildew of Chilli / Tomato (Variant Strain 2)",
        "causal_organism": "Leveillula taurica",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "White powdery fungal growth on leaf undersides with yellowing above",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 18.0,
            "favorable_temperature_c_max": 28.0,
            "favorable_relative_humidity_pct": 79,
            "leaf_wetness_hours_threshold": 6
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Hexaconazole 5% SC @ 1.5ml/L", "frac_code": "5", "pre_harvest_interval_days": 17},
            {"active_formulation": "Wettable Sulphur 80% WP @ 2.5g/L", "frac_code": "M5", "pre_harvest_interval_days": 9}
        ],
        "organic_biocontrol_protocol": [
            "Ampelomyces quisqualis bio-fungicide",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0026",
        "disease_name": "Sheath Blight of Paddy / Damping Off (Variant Strain 2)",
        "causal_organism": "Rhizoctonia solani",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Snake-skin banded lesions on leaf sheaths near water line",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 19.0,
            "favorable_temperature_c_max": 29.0,
            "favorable_relative_humidity_pct": 80,
            "leaf_wetness_hours_threshold": 7
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Validamycin 3% L @ 2.0ml/L", "frac_code": "6", "pre_harvest_interval_days": 18},
            {"active_formulation": "Hexaconazole 5% EC @ 2.0ml/L", "frac_code": "M1", "pre_harvest_interval_days": 10}
        ],
        "organic_biocontrol_protocol": [
            "Pseudomonas seed dressing @ 10g/kg",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0027",
        "disease_name": "Bacterial Wilt of Solanaceous Crops (Variant Strain 2)",
        "causal_organism": "Ralstonia solanacearum",
        "pathogen_class": "Bacteria",
        "diagnostic_symptoms": "Sudden daytime wilting of plant without foliage yellowing",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 20.0,
            "favorable_temperature_c_max": 30.0,
            "favorable_relative_humidity_pct": 81,
            "leaf_wetness_hours_threshold": 8
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Copper Oxychloride drenching @ 3.0g/L", "frac_code": "7", "pre_harvest_interval_days": 19},
            {"active_formulation": "Streptocycline drenching @ 0.2g/L", "frac_code": "M2", "pre_harvest_interval_days": 11}
        ],
        "organic_biocontrol_protocol": [
            "Bio-enrichment of soil with Trichoderma + FYM",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0028",
        "disease_name": "Fusarium Vascular Wilt (Variant Strain 2)",
        "causal_organism": "Fusarium oxysporum",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Vascular browning inside stem xylem and lower leaf chlorosis",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 21.0,
            "favorable_temperature_c_max": 31.0,
            "favorable_relative_humidity_pct": 82,
            "leaf_wetness_hours_threshold": 9
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Carbendazim 50% WP @ 1.5g/L", "frac_code": "8", "pre_harvest_interval_days": 20},
            {"active_formulation": "Thiophanate Methyl 70% WP @ 1.5g/L", "frac_code": "M3", "pre_harvest_interval_days": 12}
        ],
        "organic_biocontrol_protocol": [
            "Trichoderma harzianum @ 10g/L root zone drench",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0029",
        "disease_name": "Tomato Leaf Curl Begomovirus (ToLCV) (Variant Strain 2)",
        "causal_organism": "Bemisia tabaci",
        "pathogen_class": "Insect Vector",
        "diagnostic_symptoms": "Severe curling, puckering, reduction in leaf lamina size, stunting",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 22.0,
            "favorable_temperature_c_max": 32.0,
            "favorable_relative_humidity_pct": 83,
            "leaf_wetness_hours_threshold": 10
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Imidacloprid 17.8% SL @ 0.5ml/L", "frac_code": "9", "pre_harvest_interval_days": 7},
            {"active_formulation": "Acetamiprid 20% SP @ 0.3g/L", "frac_code": "M4", "pre_harvest_interval_days": 13}
        ],
        "organic_biocontrol_protocol": [
            "Fine insect netting (40 mesh) + Neem extract",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0030",
        "disease_name": "Root Knot Nematode Complex (Variant Strain 2)",
        "causal_organism": "Meloidogyne incognita",
        "pathogen_class": "Nematode",
        "diagnostic_symptoms": "Severe root galling, stunting, chlorosis and nutrient starvation",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 23.0,
            "favorable_temperature_c_max": 33.0,
            "favorable_relative_humidity_pct": 84,
            "leaf_wetness_hours_threshold": 11
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Fluopyram 34.48% SC @ 2.0ml/m2", "frac_code": "10", "pre_harvest_interval_days": 8},
            {"active_formulation": "Carbofuran 3% CG @ 10kg/acre", "frac_code": "M5", "pre_harvest_interval_days": 14}
        ],
        "organic_biocontrol_protocol": [
            "Paecilomyces lilacinus bio-nematicide @ 5kg/acre",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0031",
        "disease_name": "Tomato / Potato Early Blight (Variant Strain 3)",
        "causal_organism": "Alternaria solani",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Foliar target-like concentric rings with yellow halo",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 18.0,
            "favorable_temperature_c_max": 34.0,
            "favorable_relative_humidity_pct": 85,
            "leaf_wetness_hours_threshold": 12
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Mancozeb 75% WP @ 2.5g/L", "frac_code": "11", "pre_harvest_interval_days": 9},
            {"active_formulation": "Copper Oxychloride @ 2.5g/L", "frac_code": "M1", "pre_harvest_interval_days": 5}
        ],
        "organic_biocontrol_protocol": [
            "Trichoderma harzianum @ 5g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0032",
        "disease_name": "Late Blight of Tomato / Potato (Variant Strain 3)",
        "causal_organism": "Phytophthora infestans",
        "pathogen_class": "Oomycete",
        "diagnostic_symptoms": "Rapid water-soaked necrotic lesions with white downy mold",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 19.0,
            "favorable_temperature_c_max": 35.0,
            "favorable_relative_humidity_pct": 86,
            "leaf_wetness_hours_threshold": 13
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Metalaxyl 8% + Mancozeb 64% WP @ 2.5g/L", "frac_code": "12", "pre_harvest_interval_days": 10},
            {"active_formulation": "Dimethomorph 50% WP @ 1.0g/L", "frac_code": "M2", "pre_harvest_interval_days": 6}
        ],
        "organic_biocontrol_protocol": [
            "Bacillus subtilis @ 3ml/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0033",
        "disease_name": "Rice Bacterial Leaf Blight (Variant Strain 3)",
        "causal_organism": "Xanthomonas oryzae",
        "pathogen_class": "Bacteria",
        "diagnostic_symptoms": "Straw yellow undulating leaf tip lesions with amber bacterial ooze",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 20.0,
            "favorable_temperature_c_max": 28.0,
            "favorable_relative_humidity_pct": 87,
            "leaf_wetness_hours_threshold": 6
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Streptocycline 90% + Copper 50% WP @ 0.1g+2.5g/L", "frac_code": "13", "pre_harvest_interval_days": 11},
            {"active_formulation": "Kasugamycin 3% SL @ 2.0ml/L", "frac_code": "M3", "pre_harvest_interval_days": 7}
        ],
        "organic_biocontrol_protocol": [
            "Pseudomonas fluorescens @ 2.5g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0034",
        "disease_name": "Rice Blast (Leaf, Node, Neck) (Variant Strain 3)",
        "causal_organism": "Magnaporthe oryzae",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Spindle / Eye-shaped diamond lesions with greyish center and brown border",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 21.0,
            "favorable_temperature_c_max": 29.0,
            "favorable_relative_humidity_pct": 88,
            "leaf_wetness_hours_threshold": 7
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Tricyclazole 75% WP @ 0.6g/L", "frac_code": "14", "pre_harvest_interval_days": 12},
            {"active_formulation": "Isoprothiolane 40% EC @ 1.5ml/L", "frac_code": "M4", "pre_harvest_interval_days": 8}
        ],
        "organic_biocontrol_protocol": [
            "Neem Seed Kernel Extract 5%",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0035",
        "disease_name": "Wheat Yellow / Stripe Rust (Variant Strain 3)",
        "causal_organism": "Puccinia striiformis",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Parallel linear yellow pustules erupting along leaf lamina",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 22.0,
            "favorable_temperature_c_max": 30.0,
            "favorable_relative_humidity_pct": 89,
            "leaf_wetness_hours_threshold": 8
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Propiconazole 25% EC @ 1.0ml/L", "frac_code": "15", "pre_harvest_interval_days": 13},
            {"active_formulation": "Tebuconazole 25.9% EC @ 1.2ml/L", "frac_code": "M5", "pre_harvest_interval_days": 9}
        ],
        "organic_biocontrol_protocol": [
            "Bio-formulation T. viride @ 5g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0036",
        "disease_name": "Wheat Brown / Leaf Rust (Variant Strain 3)",
        "causal_organism": "Puccinia triticina",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Scattered spherical orange-brown uredinial pustules",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 23.0,
            "favorable_temperature_c_max": 31.0,
            "favorable_relative_humidity_pct": 90,
            "leaf_wetness_hours_threshold": 9
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Mancozeb 75% WP @ 2.0g/L", "frac_code": "16", "pre_harvest_interval_days": 14},
            {"active_formulation": "Propiconazole 25% EC @ 1.0ml/L", "frac_code": "M1", "pre_harvest_interval_days": 10}
        ],
        "organic_biocontrol_protocol": [
            "Sulphur 80% WDG @ 2.5g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0037",
        "disease_name": "Cotton Leaf Curl Virus (CLCuV) (Variant Strain 3)",
        "causal_organism": "Begomovirus / Whitefly",
        "pathogen_class": "Viral Complex",
        "diagnostic_symptoms": "Upward leaf cupping, thickened dark green veins and enations",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 18.0,
            "favorable_temperature_c_max": 32.0,
            "favorable_relative_humidity_pct": 91,
            "leaf_wetness_hours_threshold": 10
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Diafenthiuron 50% WP @ 1.2g/L", "frac_code": "17", "pre_harvest_interval_days": 15},
            {"active_formulation": "Pyriproxyfen 10% EC @ 2.0ml/L", "frac_code": "M2", "pre_harvest_interval_days": 11}
        ],
        "organic_biocontrol_protocol": [
            "Yellow Sticky Traps @ 20/acre + Neem Oil 10000ppm",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0038",
        "disease_name": "Maize Fall Armyworm (Variant Strain 3)",
        "causal_organism": "Spodoptera frugiperda",
        "pathogen_class": "Insect Pest",
        "diagnostic_symptoms": "Ragged shot-holes and sawdust larval frass packed in whorl",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 19.0,
            "favorable_temperature_c_max": 33.0,
            "favorable_relative_humidity_pct": 92,
            "leaf_wetness_hours_threshold": 11
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Emamectin Benzoate 5% SG @ 0.4g/L", "frac_code": "18", "pre_harvest_interval_days": 16},
            {"active_formulation": "Chlorantraniliprole 18.5% SC @ 0.3ml/L", "frac_code": "M3", "pre_harvest_interval_days": 12}
        ],
        "organic_biocontrol_protocol": [
            "Bacillus thuringiensis (Bt) kurstaki @ 2g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0039",
        "disease_name": "Chilli Anthracnose & Fruit Rot (Variant Strain 3)",
        "causal_organism": "Colletotrichum capsici",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Sunken circular dark lesions with salmon-pink spores on ripe pods",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 20.0,
            "favorable_temperature_c_max": 34.0,
            "favorable_relative_humidity_pct": 93,
            "leaf_wetness_hours_threshold": 12
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Difenoconazole 25% EC @ 0.8ml/L", "frac_code": "19", "pre_harvest_interval_days": 17},
            {"active_formulation": "Azoxystrobin 23% SC @ 1.0ml/L", "frac_code": "M4", "pre_harvest_interval_days": 13}
        ],
        "organic_biocontrol_protocol": [
            "Trichoderma viride root dip and foliar spray",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0040",
        "disease_name": "Powdery Mildew of Chilli / Tomato (Variant Strain 3)",
        "causal_organism": "Leveillula taurica",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "White powdery fungal growth on leaf undersides with yellowing above",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 21.0,
            "favorable_temperature_c_max": 35.0,
            "favorable_relative_humidity_pct": 94,
            "leaf_wetness_hours_threshold": 13
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Hexaconazole 5% SC @ 1.5ml/L", "frac_code": "20", "pre_harvest_interval_days": 18},
            {"active_formulation": "Wettable Sulphur 80% WP @ 2.5g/L", "frac_code": "M5", "pre_harvest_interval_days": 14}
        ],
        "organic_biocontrol_protocol": [
            "Ampelomyces quisqualis bio-fungicide",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0041",
        "disease_name": "Sheath Blight of Paddy / Damping Off (Variant Strain 3)",
        "causal_organism": "Rhizoctonia solani",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Snake-skin banded lesions on leaf sheaths near water line",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 22.0,
            "favorable_temperature_c_max": 28.0,
            "favorable_relative_humidity_pct": 75,
            "leaf_wetness_hours_threshold": 6
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Validamycin 3% L @ 2.0ml/L", "frac_code": "1", "pre_harvest_interval_days": 19},
            {"active_formulation": "Hexaconazole 5% EC @ 2.0ml/L", "frac_code": "M1", "pre_harvest_interval_days": 5}
        ],
        "organic_biocontrol_protocol": [
            "Pseudomonas seed dressing @ 10g/kg",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0042",
        "disease_name": "Bacterial Wilt of Solanaceous Crops (Variant Strain 3)",
        "causal_organism": "Ralstonia solanacearum",
        "pathogen_class": "Bacteria",
        "diagnostic_symptoms": "Sudden daytime wilting of plant without foliage yellowing",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 23.0,
            "favorable_temperature_c_max": 29.0,
            "favorable_relative_humidity_pct": 76,
            "leaf_wetness_hours_threshold": 7
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Copper Oxychloride drenching @ 3.0g/L", "frac_code": "2", "pre_harvest_interval_days": 20},
            {"active_formulation": "Streptocycline drenching @ 0.2g/L", "frac_code": "M2", "pre_harvest_interval_days": 6}
        ],
        "organic_biocontrol_protocol": [
            "Bio-enrichment of soil with Trichoderma + FYM",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0043",
        "disease_name": "Fusarium Vascular Wilt (Variant Strain 3)",
        "causal_organism": "Fusarium oxysporum",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Vascular browning inside stem xylem and lower leaf chlorosis",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 18.0,
            "favorable_temperature_c_max": 30.0,
            "favorable_relative_humidity_pct": 77,
            "leaf_wetness_hours_threshold": 8
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Carbendazim 50% WP @ 1.5g/L", "frac_code": "3", "pre_harvest_interval_days": 7},
            {"active_formulation": "Thiophanate Methyl 70% WP @ 1.5g/L", "frac_code": "M3", "pre_harvest_interval_days": 7}
        ],
        "organic_biocontrol_protocol": [
            "Trichoderma harzianum @ 10g/L root zone drench",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0044",
        "disease_name": "Tomato Leaf Curl Begomovirus (ToLCV) (Variant Strain 3)",
        "causal_organism": "Bemisia tabaci",
        "pathogen_class": "Insect Vector",
        "diagnostic_symptoms": "Severe curling, puckering, reduction in leaf lamina size, stunting",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 19.0,
            "favorable_temperature_c_max": 31.0,
            "favorable_relative_humidity_pct": 78,
            "leaf_wetness_hours_threshold": 9
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Imidacloprid 17.8% SL @ 0.5ml/L", "frac_code": "4", "pre_harvest_interval_days": 8},
            {"active_formulation": "Acetamiprid 20% SP @ 0.3g/L", "frac_code": "M4", "pre_harvest_interval_days": 8}
        ],
        "organic_biocontrol_protocol": [
            "Fine insect netting (40 mesh) + Neem extract",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0045",
        "disease_name": "Root Knot Nematode Complex (Variant Strain 3)",
        "causal_organism": "Meloidogyne incognita",
        "pathogen_class": "Nematode",
        "diagnostic_symptoms": "Severe root galling, stunting, chlorosis and nutrient starvation",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 20.0,
            "favorable_temperature_c_max": 32.0,
            "favorable_relative_humidity_pct": 79,
            "leaf_wetness_hours_threshold": 10
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Fluopyram 34.48% SC @ 2.0ml/m2", "frac_code": "5", "pre_harvest_interval_days": 9},
            {"active_formulation": "Carbofuran 3% CG @ 10kg/acre", "frac_code": "M5", "pre_harvest_interval_days": 9}
        ],
        "organic_biocontrol_protocol": [
            "Paecilomyces lilacinus bio-nematicide @ 5kg/acre",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0046",
        "disease_name": "Tomato / Potato Early Blight (Variant Strain 4)",
        "causal_organism": "Alternaria solani",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Foliar target-like concentric rings with yellow halo",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 21.0,
            "favorable_temperature_c_max": 33.0,
            "favorable_relative_humidity_pct": 80,
            "leaf_wetness_hours_threshold": 11
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Mancozeb 75% WP @ 2.5g/L", "frac_code": "6", "pre_harvest_interval_days": 10},
            {"active_formulation": "Copper Oxychloride @ 2.5g/L", "frac_code": "M1", "pre_harvest_interval_days": 10}
        ],
        "organic_biocontrol_protocol": [
            "Trichoderma harzianum @ 5g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0047",
        "disease_name": "Late Blight of Tomato / Potato (Variant Strain 4)",
        "causal_organism": "Phytophthora infestans",
        "pathogen_class": "Oomycete",
        "diagnostic_symptoms": "Rapid water-soaked necrotic lesions with white downy mold",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 22.0,
            "favorable_temperature_c_max": 34.0,
            "favorable_relative_humidity_pct": 81,
            "leaf_wetness_hours_threshold": 12
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Metalaxyl 8% + Mancozeb 64% WP @ 2.5g/L", "frac_code": "7", "pre_harvest_interval_days": 11},
            {"active_formulation": "Dimethomorph 50% WP @ 1.0g/L", "frac_code": "M2", "pre_harvest_interval_days": 11}
        ],
        "organic_biocontrol_protocol": [
            "Bacillus subtilis @ 3ml/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0048",
        "disease_name": "Rice Bacterial Leaf Blight (Variant Strain 4)",
        "causal_organism": "Xanthomonas oryzae",
        "pathogen_class": "Bacteria",
        "diagnostic_symptoms": "Straw yellow undulating leaf tip lesions with amber bacterial ooze",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 23.0,
            "favorable_temperature_c_max": 35.0,
            "favorable_relative_humidity_pct": 82,
            "leaf_wetness_hours_threshold": 13
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Streptocycline 90% + Copper 50% WP @ 0.1g+2.5g/L", "frac_code": "8", "pre_harvest_interval_days": 12},
            {"active_formulation": "Kasugamycin 3% SL @ 2.0ml/L", "frac_code": "M3", "pre_harvest_interval_days": 12}
        ],
        "organic_biocontrol_protocol": [
            "Pseudomonas fluorescens @ 2.5g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0049",
        "disease_name": "Rice Blast (Leaf, Node, Neck) (Variant Strain 4)",
        "causal_organism": "Magnaporthe oryzae",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Spindle / Eye-shaped diamond lesions with greyish center and brown border",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 18.0,
            "favorable_temperature_c_max": 28.0,
            "favorable_relative_humidity_pct": 83,
            "leaf_wetness_hours_threshold": 6
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Tricyclazole 75% WP @ 0.6g/L", "frac_code": "9", "pre_harvest_interval_days": 13},
            {"active_formulation": "Isoprothiolane 40% EC @ 1.5ml/L", "frac_code": "M4", "pre_harvest_interval_days": 13}
        ],
        "organic_biocontrol_protocol": [
            "Neem Seed Kernel Extract 5%",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0050",
        "disease_name": "Wheat Yellow / Stripe Rust (Variant Strain 4)",
        "causal_organism": "Puccinia striiformis",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Parallel linear yellow pustules erupting along leaf lamina",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 19.0,
            "favorable_temperature_c_max": 29.0,
            "favorable_relative_humidity_pct": 84,
            "leaf_wetness_hours_threshold": 7
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Propiconazole 25% EC @ 1.0ml/L", "frac_code": "10", "pre_harvest_interval_days": 14},
            {"active_formulation": "Tebuconazole 25.9% EC @ 1.2ml/L", "frac_code": "M5", "pre_harvest_interval_days": 14}
        ],
        "organic_biocontrol_protocol": [
            "Bio-formulation T. viride @ 5g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0051",
        "disease_name": "Wheat Brown / Leaf Rust (Variant Strain 4)",
        "causal_organism": "Puccinia triticina",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Scattered spherical orange-brown uredinial pustules",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 20.0,
            "favorable_temperature_c_max": 30.0,
            "favorable_relative_humidity_pct": 85,
            "leaf_wetness_hours_threshold": 8
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Mancozeb 75% WP @ 2.0g/L", "frac_code": "11", "pre_harvest_interval_days": 15},
            {"active_formulation": "Propiconazole 25% EC @ 1.0ml/L", "frac_code": "M1", "pre_harvest_interval_days": 5}
        ],
        "organic_biocontrol_protocol": [
            "Sulphur 80% WDG @ 2.5g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0052",
        "disease_name": "Cotton Leaf Curl Virus (CLCuV) (Variant Strain 4)",
        "causal_organism": "Begomovirus / Whitefly",
        "pathogen_class": "Viral Complex",
        "diagnostic_symptoms": "Upward leaf cupping, thickened dark green veins and enations",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 21.0,
            "favorable_temperature_c_max": 31.0,
            "favorable_relative_humidity_pct": 86,
            "leaf_wetness_hours_threshold": 9
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Diafenthiuron 50% WP @ 1.2g/L", "frac_code": "12", "pre_harvest_interval_days": 16},
            {"active_formulation": "Pyriproxyfen 10% EC @ 2.0ml/L", "frac_code": "M2", "pre_harvest_interval_days": 6}
        ],
        "organic_biocontrol_protocol": [
            "Yellow Sticky Traps @ 20/acre + Neem Oil 10000ppm",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0053",
        "disease_name": "Maize Fall Armyworm (Variant Strain 4)",
        "causal_organism": "Spodoptera frugiperda",
        "pathogen_class": "Insect Pest",
        "diagnostic_symptoms": "Ragged shot-holes and sawdust larval frass packed in whorl",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 22.0,
            "favorable_temperature_c_max": 32.0,
            "favorable_relative_humidity_pct": 87,
            "leaf_wetness_hours_threshold": 10
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Emamectin Benzoate 5% SG @ 0.4g/L", "frac_code": "13", "pre_harvest_interval_days": 17},
            {"active_formulation": "Chlorantraniliprole 18.5% SC @ 0.3ml/L", "frac_code": "M3", "pre_harvest_interval_days": 7}
        ],
        "organic_biocontrol_protocol": [
            "Bacillus thuringiensis (Bt) kurstaki @ 2g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0054",
        "disease_name": "Chilli Anthracnose & Fruit Rot (Variant Strain 4)",
        "causal_organism": "Colletotrichum capsici",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Sunken circular dark lesions with salmon-pink spores on ripe pods",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 23.0,
            "favorable_temperature_c_max": 33.0,
            "favorable_relative_humidity_pct": 88,
            "leaf_wetness_hours_threshold": 11
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Difenoconazole 25% EC @ 0.8ml/L", "frac_code": "14", "pre_harvest_interval_days": 18},
            {"active_formulation": "Azoxystrobin 23% SC @ 1.0ml/L", "frac_code": "M4", "pre_harvest_interval_days": 8}
        ],
        "organic_biocontrol_protocol": [
            "Trichoderma viride root dip and foliar spray",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0055",
        "disease_name": "Powdery Mildew of Chilli / Tomato (Variant Strain 4)",
        "causal_organism": "Leveillula taurica",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "White powdery fungal growth on leaf undersides with yellowing above",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 18.0,
            "favorable_temperature_c_max": 34.0,
            "favorable_relative_humidity_pct": 89,
            "leaf_wetness_hours_threshold": 12
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Hexaconazole 5% SC @ 1.5ml/L", "frac_code": "15", "pre_harvest_interval_days": 19},
            {"active_formulation": "Wettable Sulphur 80% WP @ 2.5g/L", "frac_code": "M5", "pre_harvest_interval_days": 9}
        ],
        "organic_biocontrol_protocol": [
            "Ampelomyces quisqualis bio-fungicide",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0056",
        "disease_name": "Sheath Blight of Paddy / Damping Off (Variant Strain 4)",
        "causal_organism": "Rhizoctonia solani",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Snake-skin banded lesions on leaf sheaths near water line",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 19.0,
            "favorable_temperature_c_max": 35.0,
            "favorable_relative_humidity_pct": 90,
            "leaf_wetness_hours_threshold": 13
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Validamycin 3% L @ 2.0ml/L", "frac_code": "16", "pre_harvest_interval_days": 20},
            {"active_formulation": "Hexaconazole 5% EC @ 2.0ml/L", "frac_code": "M1", "pre_harvest_interval_days": 10}
        ],
        "organic_biocontrol_protocol": [
            "Pseudomonas seed dressing @ 10g/kg",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0057",
        "disease_name": "Bacterial Wilt of Solanaceous Crops (Variant Strain 4)",
        "causal_organism": "Ralstonia solanacearum",
        "pathogen_class": "Bacteria",
        "diagnostic_symptoms": "Sudden daytime wilting of plant without foliage yellowing",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 20.0,
            "favorable_temperature_c_max": 28.0,
            "favorable_relative_humidity_pct": 91,
            "leaf_wetness_hours_threshold": 6
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Copper Oxychloride drenching @ 3.0g/L", "frac_code": "17", "pre_harvest_interval_days": 7},
            {"active_formulation": "Streptocycline drenching @ 0.2g/L", "frac_code": "M2", "pre_harvest_interval_days": 11}
        ],
        "organic_biocontrol_protocol": [
            "Bio-enrichment of soil with Trichoderma + FYM",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0058",
        "disease_name": "Fusarium Vascular Wilt (Variant Strain 4)",
        "causal_organism": "Fusarium oxysporum",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Vascular browning inside stem xylem and lower leaf chlorosis",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 21.0,
            "favorable_temperature_c_max": 29.0,
            "favorable_relative_humidity_pct": 92,
            "leaf_wetness_hours_threshold": 7
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Carbendazim 50% WP @ 1.5g/L", "frac_code": "18", "pre_harvest_interval_days": 8},
            {"active_formulation": "Thiophanate Methyl 70% WP @ 1.5g/L", "frac_code": "M3", "pre_harvest_interval_days": 12}
        ],
        "organic_biocontrol_protocol": [
            "Trichoderma harzianum @ 10g/L root zone drench",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0059",
        "disease_name": "Tomato Leaf Curl Begomovirus (ToLCV) (Variant Strain 4)",
        "causal_organism": "Bemisia tabaci",
        "pathogen_class": "Insect Vector",
        "diagnostic_symptoms": "Severe curling, puckering, reduction in leaf lamina size, stunting",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 22.0,
            "favorable_temperature_c_max": 30.0,
            "favorable_relative_humidity_pct": 93,
            "leaf_wetness_hours_threshold": 8
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Imidacloprid 17.8% SL @ 0.5ml/L", "frac_code": "19", "pre_harvest_interval_days": 9},
            {"active_formulation": "Acetamiprid 20% SP @ 0.3g/L", "frac_code": "M4", "pre_harvest_interval_days": 13}
        ],
        "organic_biocontrol_protocol": [
            "Fine insect netting (40 mesh) + Neem extract",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0060",
        "disease_name": "Root Knot Nematode Complex (Variant Strain 4)",
        "causal_organism": "Meloidogyne incognita",
        "pathogen_class": "Nematode",
        "diagnostic_symptoms": "Severe root galling, stunting, chlorosis and nutrient starvation",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 23.0,
            "favorable_temperature_c_max": 31.0,
            "favorable_relative_humidity_pct": 94,
            "leaf_wetness_hours_threshold": 9
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Fluopyram 34.48% SC @ 2.0ml/m2", "frac_code": "20", "pre_harvest_interval_days": 10},
            {"active_formulation": "Carbofuran 3% CG @ 10kg/acre", "frac_code": "M5", "pre_harvest_interval_days": 14}
        ],
        "organic_biocontrol_protocol": [
            "Paecilomyces lilacinus bio-nematicide @ 5kg/acre",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0061",
        "disease_name": "Tomato / Potato Early Blight (Variant Strain 5)",
        "causal_organism": "Alternaria solani",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Foliar target-like concentric rings with yellow halo",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 18.0,
            "favorable_temperature_c_max": 32.0,
            "favorable_relative_humidity_pct": 75,
            "leaf_wetness_hours_threshold": 10
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Mancozeb 75% WP @ 2.5g/L", "frac_code": "1", "pre_harvest_interval_days": 11},
            {"active_formulation": "Copper Oxychloride @ 2.5g/L", "frac_code": "M1", "pre_harvest_interval_days": 5}
        ],
        "organic_biocontrol_protocol": [
            "Trichoderma harzianum @ 5g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0062",
        "disease_name": "Late Blight of Tomato / Potato (Variant Strain 5)",
        "causal_organism": "Phytophthora infestans",
        "pathogen_class": "Oomycete",
        "diagnostic_symptoms": "Rapid water-soaked necrotic lesions with white downy mold",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 19.0,
            "favorable_temperature_c_max": 33.0,
            "favorable_relative_humidity_pct": 76,
            "leaf_wetness_hours_threshold": 11
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Metalaxyl 8% + Mancozeb 64% WP @ 2.5g/L", "frac_code": "2", "pre_harvest_interval_days": 12},
            {"active_formulation": "Dimethomorph 50% WP @ 1.0g/L", "frac_code": "M2", "pre_harvest_interval_days": 6}
        ],
        "organic_biocontrol_protocol": [
            "Bacillus subtilis @ 3ml/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0063",
        "disease_name": "Rice Bacterial Leaf Blight (Variant Strain 5)",
        "causal_organism": "Xanthomonas oryzae",
        "pathogen_class": "Bacteria",
        "diagnostic_symptoms": "Straw yellow undulating leaf tip lesions with amber bacterial ooze",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 20.0,
            "favorable_temperature_c_max": 34.0,
            "favorable_relative_humidity_pct": 77,
            "leaf_wetness_hours_threshold": 12
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Streptocycline 90% + Copper 50% WP @ 0.1g+2.5g/L", "frac_code": "3", "pre_harvest_interval_days": 13},
            {"active_formulation": "Kasugamycin 3% SL @ 2.0ml/L", "frac_code": "M3", "pre_harvest_interval_days": 7}
        ],
        "organic_biocontrol_protocol": [
            "Pseudomonas fluorescens @ 2.5g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0064",
        "disease_name": "Rice Blast (Leaf, Node, Neck) (Variant Strain 5)",
        "causal_organism": "Magnaporthe oryzae",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Spindle / Eye-shaped diamond lesions with greyish center and brown border",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 21.0,
            "favorable_temperature_c_max": 35.0,
            "favorable_relative_humidity_pct": 78,
            "leaf_wetness_hours_threshold": 13
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Tricyclazole 75% WP @ 0.6g/L", "frac_code": "4", "pre_harvest_interval_days": 14},
            {"active_formulation": "Isoprothiolane 40% EC @ 1.5ml/L", "frac_code": "M4", "pre_harvest_interval_days": 8}
        ],
        "organic_biocontrol_protocol": [
            "Neem Seed Kernel Extract 5%",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0065",
        "disease_name": "Wheat Yellow / Stripe Rust (Variant Strain 5)",
        "causal_organism": "Puccinia striiformis",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Parallel linear yellow pustules erupting along leaf lamina",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 22.0,
            "favorable_temperature_c_max": 28.0,
            "favorable_relative_humidity_pct": 79,
            "leaf_wetness_hours_threshold": 6
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Propiconazole 25% EC @ 1.0ml/L", "frac_code": "5", "pre_harvest_interval_days": 15},
            {"active_formulation": "Tebuconazole 25.9% EC @ 1.2ml/L", "frac_code": "M5", "pre_harvest_interval_days": 9}
        ],
        "organic_biocontrol_protocol": [
            "Bio-formulation T. viride @ 5g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0066",
        "disease_name": "Wheat Brown / Leaf Rust (Variant Strain 5)",
        "causal_organism": "Puccinia triticina",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Scattered spherical orange-brown uredinial pustules",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 23.0,
            "favorable_temperature_c_max": 29.0,
            "favorable_relative_humidity_pct": 80,
            "leaf_wetness_hours_threshold": 7
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Mancozeb 75% WP @ 2.0g/L", "frac_code": "6", "pre_harvest_interval_days": 16},
            {"active_formulation": "Propiconazole 25% EC @ 1.0ml/L", "frac_code": "M1", "pre_harvest_interval_days": 10}
        ],
        "organic_biocontrol_protocol": [
            "Sulphur 80% WDG @ 2.5g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0067",
        "disease_name": "Cotton Leaf Curl Virus (CLCuV) (Variant Strain 5)",
        "causal_organism": "Begomovirus / Whitefly",
        "pathogen_class": "Viral Complex",
        "diagnostic_symptoms": "Upward leaf cupping, thickened dark green veins and enations",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 18.0,
            "favorable_temperature_c_max": 30.0,
            "favorable_relative_humidity_pct": 81,
            "leaf_wetness_hours_threshold": 8
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Diafenthiuron 50% WP @ 1.2g/L", "frac_code": "7", "pre_harvest_interval_days": 17},
            {"active_formulation": "Pyriproxyfen 10% EC @ 2.0ml/L", "frac_code": "M2", "pre_harvest_interval_days": 11}
        ],
        "organic_biocontrol_protocol": [
            "Yellow Sticky Traps @ 20/acre + Neem Oil 10000ppm",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0068",
        "disease_name": "Maize Fall Armyworm (Variant Strain 5)",
        "causal_organism": "Spodoptera frugiperda",
        "pathogen_class": "Insect Pest",
        "diagnostic_symptoms": "Ragged shot-holes and sawdust larval frass packed in whorl",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 19.0,
            "favorable_temperature_c_max": 31.0,
            "favorable_relative_humidity_pct": 82,
            "leaf_wetness_hours_threshold": 9
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Emamectin Benzoate 5% SG @ 0.4g/L", "frac_code": "8", "pre_harvest_interval_days": 18},
            {"active_formulation": "Chlorantraniliprole 18.5% SC @ 0.3ml/L", "frac_code": "M3", "pre_harvest_interval_days": 12}
        ],
        "organic_biocontrol_protocol": [
            "Bacillus thuringiensis (Bt) kurstaki @ 2g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0069",
        "disease_name": "Chilli Anthracnose & Fruit Rot (Variant Strain 5)",
        "causal_organism": "Colletotrichum capsici",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Sunken circular dark lesions with salmon-pink spores on ripe pods",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 20.0,
            "favorable_temperature_c_max": 32.0,
            "favorable_relative_humidity_pct": 83,
            "leaf_wetness_hours_threshold": 10
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Difenoconazole 25% EC @ 0.8ml/L", "frac_code": "9", "pre_harvest_interval_days": 19},
            {"active_formulation": "Azoxystrobin 23% SC @ 1.0ml/L", "frac_code": "M4", "pre_harvest_interval_days": 13}
        ],
        "organic_biocontrol_protocol": [
            "Trichoderma viride root dip and foliar spray",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0070",
        "disease_name": "Powdery Mildew of Chilli / Tomato (Variant Strain 5)",
        "causal_organism": "Leveillula taurica",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "White powdery fungal growth on leaf undersides with yellowing above",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 21.0,
            "favorable_temperature_c_max": 33.0,
            "favorable_relative_humidity_pct": 84,
            "leaf_wetness_hours_threshold": 11
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Hexaconazole 5% SC @ 1.5ml/L", "frac_code": "10", "pre_harvest_interval_days": 20},
            {"active_formulation": "Wettable Sulphur 80% WP @ 2.5g/L", "frac_code": "M5", "pre_harvest_interval_days": 14}
        ],
        "organic_biocontrol_protocol": [
            "Ampelomyces quisqualis bio-fungicide",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0071",
        "disease_name": "Sheath Blight of Paddy / Damping Off (Variant Strain 5)",
        "causal_organism": "Rhizoctonia solani",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Snake-skin banded lesions on leaf sheaths near water line",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 22.0,
            "favorable_temperature_c_max": 34.0,
            "favorable_relative_humidity_pct": 85,
            "leaf_wetness_hours_threshold": 12
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Validamycin 3% L @ 2.0ml/L", "frac_code": "11", "pre_harvest_interval_days": 7},
            {"active_formulation": "Hexaconazole 5% EC @ 2.0ml/L", "frac_code": "M1", "pre_harvest_interval_days": 5}
        ],
        "organic_biocontrol_protocol": [
            "Pseudomonas seed dressing @ 10g/kg",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0072",
        "disease_name": "Bacterial Wilt of Solanaceous Crops (Variant Strain 5)",
        "causal_organism": "Ralstonia solanacearum",
        "pathogen_class": "Bacteria",
        "diagnostic_symptoms": "Sudden daytime wilting of plant without foliage yellowing",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 23.0,
            "favorable_temperature_c_max": 35.0,
            "favorable_relative_humidity_pct": 86,
            "leaf_wetness_hours_threshold": 13
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Copper Oxychloride drenching @ 3.0g/L", "frac_code": "12", "pre_harvest_interval_days": 8},
            {"active_formulation": "Streptocycline drenching @ 0.2g/L", "frac_code": "M2", "pre_harvest_interval_days": 6}
        ],
        "organic_biocontrol_protocol": [
            "Bio-enrichment of soil with Trichoderma + FYM",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0073",
        "disease_name": "Fusarium Vascular Wilt (Variant Strain 5)",
        "causal_organism": "Fusarium oxysporum",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Vascular browning inside stem xylem and lower leaf chlorosis",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 18.0,
            "favorable_temperature_c_max": 28.0,
            "favorable_relative_humidity_pct": 87,
            "leaf_wetness_hours_threshold": 6
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Carbendazim 50% WP @ 1.5g/L", "frac_code": "13", "pre_harvest_interval_days": 9},
            {"active_formulation": "Thiophanate Methyl 70% WP @ 1.5g/L", "frac_code": "M3", "pre_harvest_interval_days": 7}
        ],
        "organic_biocontrol_protocol": [
            "Trichoderma harzianum @ 10g/L root zone drench",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0074",
        "disease_name": "Tomato Leaf Curl Begomovirus (ToLCV) (Variant Strain 5)",
        "causal_organism": "Bemisia tabaci",
        "pathogen_class": "Insect Vector",
        "diagnostic_symptoms": "Severe curling, puckering, reduction in leaf lamina size, stunting",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 19.0,
            "favorable_temperature_c_max": 29.0,
            "favorable_relative_humidity_pct": 88,
            "leaf_wetness_hours_threshold": 7
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Imidacloprid 17.8% SL @ 0.5ml/L", "frac_code": "14", "pre_harvest_interval_days": 10},
            {"active_formulation": "Acetamiprid 20% SP @ 0.3g/L", "frac_code": "M4", "pre_harvest_interval_days": 8}
        ],
        "organic_biocontrol_protocol": [
            "Fine insect netting (40 mesh) + Neem extract",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0075",
        "disease_name": "Root Knot Nematode Complex (Variant Strain 5)",
        "causal_organism": "Meloidogyne incognita",
        "pathogen_class": "Nematode",
        "diagnostic_symptoms": "Severe root galling, stunting, chlorosis and nutrient starvation",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 20.0,
            "favorable_temperature_c_max": 30.0,
            "favorable_relative_humidity_pct": 89,
            "leaf_wetness_hours_threshold": 8
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Fluopyram 34.48% SC @ 2.0ml/m2", "frac_code": "15", "pre_harvest_interval_days": 11},
            {"active_formulation": "Carbofuran 3% CG @ 10kg/acre", "frac_code": "M5", "pre_harvest_interval_days": 9}
        ],
        "organic_biocontrol_protocol": [
            "Paecilomyces lilacinus bio-nematicide @ 5kg/acre",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0076",
        "disease_name": "Tomato / Potato Early Blight (Variant Strain 6)",
        "causal_organism": "Alternaria solani",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Foliar target-like concentric rings with yellow halo",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 21.0,
            "favorable_temperature_c_max": 31.0,
            "favorable_relative_humidity_pct": 90,
            "leaf_wetness_hours_threshold": 9
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Mancozeb 75% WP @ 2.5g/L", "frac_code": "16", "pre_harvest_interval_days": 12},
            {"active_formulation": "Copper Oxychloride @ 2.5g/L", "frac_code": "M1", "pre_harvest_interval_days": 10}
        ],
        "organic_biocontrol_protocol": [
            "Trichoderma harzianum @ 5g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0077",
        "disease_name": "Late Blight of Tomato / Potato (Variant Strain 6)",
        "causal_organism": "Phytophthora infestans",
        "pathogen_class": "Oomycete",
        "diagnostic_symptoms": "Rapid water-soaked necrotic lesions with white downy mold",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 22.0,
            "favorable_temperature_c_max": 32.0,
            "favorable_relative_humidity_pct": 91,
            "leaf_wetness_hours_threshold": 10
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Metalaxyl 8% + Mancozeb 64% WP @ 2.5g/L", "frac_code": "17", "pre_harvest_interval_days": 13},
            {"active_formulation": "Dimethomorph 50% WP @ 1.0g/L", "frac_code": "M2", "pre_harvest_interval_days": 11}
        ],
        "organic_biocontrol_protocol": [
            "Bacillus subtilis @ 3ml/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0078",
        "disease_name": "Rice Bacterial Leaf Blight (Variant Strain 6)",
        "causal_organism": "Xanthomonas oryzae",
        "pathogen_class": "Bacteria",
        "diagnostic_symptoms": "Straw yellow undulating leaf tip lesions with amber bacterial ooze",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 23.0,
            "favorable_temperature_c_max": 33.0,
            "favorable_relative_humidity_pct": 92,
            "leaf_wetness_hours_threshold": 11
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Streptocycline 90% + Copper 50% WP @ 0.1g+2.5g/L", "frac_code": "18", "pre_harvest_interval_days": 14},
            {"active_formulation": "Kasugamycin 3% SL @ 2.0ml/L", "frac_code": "M3", "pre_harvest_interval_days": 12}
        ],
        "organic_biocontrol_protocol": [
            "Pseudomonas fluorescens @ 2.5g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0079",
        "disease_name": "Rice Blast (Leaf, Node, Neck) (Variant Strain 6)",
        "causal_organism": "Magnaporthe oryzae",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Spindle / Eye-shaped diamond lesions with greyish center and brown border",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 18.0,
            "favorable_temperature_c_max": 34.0,
            "favorable_relative_humidity_pct": 93,
            "leaf_wetness_hours_threshold": 12
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Tricyclazole 75% WP @ 0.6g/L", "frac_code": "19", "pre_harvest_interval_days": 15},
            {"active_formulation": "Isoprothiolane 40% EC @ 1.5ml/L", "frac_code": "M4", "pre_harvest_interval_days": 13}
        ],
        "organic_biocontrol_protocol": [
            "Neem Seed Kernel Extract 5%",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0080",
        "disease_name": "Wheat Yellow / Stripe Rust (Variant Strain 6)",
        "causal_organism": "Puccinia striiformis",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Parallel linear yellow pustules erupting along leaf lamina",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 19.0,
            "favorable_temperature_c_max": 35.0,
            "favorable_relative_humidity_pct": 94,
            "leaf_wetness_hours_threshold": 13
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Propiconazole 25% EC @ 1.0ml/L", "frac_code": "20", "pre_harvest_interval_days": 16},
            {"active_formulation": "Tebuconazole 25.9% EC @ 1.2ml/L", "frac_code": "M5", "pre_harvest_interval_days": 14}
        ],
        "organic_biocontrol_protocol": [
            "Bio-formulation T. viride @ 5g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0081",
        "disease_name": "Wheat Brown / Leaf Rust (Variant Strain 6)",
        "causal_organism": "Puccinia triticina",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Scattered spherical orange-brown uredinial pustules",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 20.0,
            "favorable_temperature_c_max": 28.0,
            "favorable_relative_humidity_pct": 75,
            "leaf_wetness_hours_threshold": 6
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Mancozeb 75% WP @ 2.0g/L", "frac_code": "1", "pre_harvest_interval_days": 17},
            {"active_formulation": "Propiconazole 25% EC @ 1.0ml/L", "frac_code": "M1", "pre_harvest_interval_days": 5}
        ],
        "organic_biocontrol_protocol": [
            "Sulphur 80% WDG @ 2.5g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0082",
        "disease_name": "Cotton Leaf Curl Virus (CLCuV) (Variant Strain 6)",
        "causal_organism": "Begomovirus / Whitefly",
        "pathogen_class": "Viral Complex",
        "diagnostic_symptoms": "Upward leaf cupping, thickened dark green veins and enations",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 21.0,
            "favorable_temperature_c_max": 29.0,
            "favorable_relative_humidity_pct": 76,
            "leaf_wetness_hours_threshold": 7
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Diafenthiuron 50% WP @ 1.2g/L", "frac_code": "2", "pre_harvest_interval_days": 18},
            {"active_formulation": "Pyriproxyfen 10% EC @ 2.0ml/L", "frac_code": "M2", "pre_harvest_interval_days": 6}
        ],
        "organic_biocontrol_protocol": [
            "Yellow Sticky Traps @ 20/acre + Neem Oil 10000ppm",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0083",
        "disease_name": "Maize Fall Armyworm (Variant Strain 6)",
        "causal_organism": "Spodoptera frugiperda",
        "pathogen_class": "Insect Pest",
        "diagnostic_symptoms": "Ragged shot-holes and sawdust larval frass packed in whorl",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 22.0,
            "favorable_temperature_c_max": 30.0,
            "favorable_relative_humidity_pct": 77,
            "leaf_wetness_hours_threshold": 8
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Emamectin Benzoate 5% SG @ 0.4g/L", "frac_code": "3", "pre_harvest_interval_days": 19},
            {"active_formulation": "Chlorantraniliprole 18.5% SC @ 0.3ml/L", "frac_code": "M3", "pre_harvest_interval_days": 7}
        ],
        "organic_biocontrol_protocol": [
            "Bacillus thuringiensis (Bt) kurstaki @ 2g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0084",
        "disease_name": "Chilli Anthracnose & Fruit Rot (Variant Strain 6)",
        "causal_organism": "Colletotrichum capsici",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Sunken circular dark lesions with salmon-pink spores on ripe pods",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 23.0,
            "favorable_temperature_c_max": 31.0,
            "favorable_relative_humidity_pct": 78,
            "leaf_wetness_hours_threshold": 9
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Difenoconazole 25% EC @ 0.8ml/L", "frac_code": "4", "pre_harvest_interval_days": 20},
            {"active_formulation": "Azoxystrobin 23% SC @ 1.0ml/L", "frac_code": "M4", "pre_harvest_interval_days": 8}
        ],
        "organic_biocontrol_protocol": [
            "Trichoderma viride root dip and foliar spray",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0085",
        "disease_name": "Powdery Mildew of Chilli / Tomato (Variant Strain 6)",
        "causal_organism": "Leveillula taurica",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "White powdery fungal growth on leaf undersides with yellowing above",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 18.0,
            "favorable_temperature_c_max": 32.0,
            "favorable_relative_humidity_pct": 79,
            "leaf_wetness_hours_threshold": 10
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Hexaconazole 5% SC @ 1.5ml/L", "frac_code": "5", "pre_harvest_interval_days": 7},
            {"active_formulation": "Wettable Sulphur 80% WP @ 2.5g/L", "frac_code": "M5", "pre_harvest_interval_days": 9}
        ],
        "organic_biocontrol_protocol": [
            "Ampelomyces quisqualis bio-fungicide",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0086",
        "disease_name": "Sheath Blight of Paddy / Damping Off (Variant Strain 6)",
        "causal_organism": "Rhizoctonia solani",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Snake-skin banded lesions on leaf sheaths near water line",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 19.0,
            "favorable_temperature_c_max": 33.0,
            "favorable_relative_humidity_pct": 80,
            "leaf_wetness_hours_threshold": 11
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Validamycin 3% L @ 2.0ml/L", "frac_code": "6", "pre_harvest_interval_days": 8},
            {"active_formulation": "Hexaconazole 5% EC @ 2.0ml/L", "frac_code": "M1", "pre_harvest_interval_days": 10}
        ],
        "organic_biocontrol_protocol": [
            "Pseudomonas seed dressing @ 10g/kg",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0087",
        "disease_name": "Bacterial Wilt of Solanaceous Crops (Variant Strain 6)",
        "causal_organism": "Ralstonia solanacearum",
        "pathogen_class": "Bacteria",
        "diagnostic_symptoms": "Sudden daytime wilting of plant without foliage yellowing",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 20.0,
            "favorable_temperature_c_max": 34.0,
            "favorable_relative_humidity_pct": 81,
            "leaf_wetness_hours_threshold": 12
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Copper Oxychloride drenching @ 3.0g/L", "frac_code": "7", "pre_harvest_interval_days": 9},
            {"active_formulation": "Streptocycline drenching @ 0.2g/L", "frac_code": "M2", "pre_harvest_interval_days": 11}
        ],
        "organic_biocontrol_protocol": [
            "Bio-enrichment of soil with Trichoderma + FYM",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0088",
        "disease_name": "Fusarium Vascular Wilt (Variant Strain 6)",
        "causal_organism": "Fusarium oxysporum",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Vascular browning inside stem xylem and lower leaf chlorosis",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 21.0,
            "favorable_temperature_c_max": 35.0,
            "favorable_relative_humidity_pct": 82,
            "leaf_wetness_hours_threshold": 13
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Carbendazim 50% WP @ 1.5g/L", "frac_code": "8", "pre_harvest_interval_days": 10},
            {"active_formulation": "Thiophanate Methyl 70% WP @ 1.5g/L", "frac_code": "M3", "pre_harvest_interval_days": 12}
        ],
        "organic_biocontrol_protocol": [
            "Trichoderma harzianum @ 10g/L root zone drench",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0089",
        "disease_name": "Tomato Leaf Curl Begomovirus (ToLCV) (Variant Strain 6)",
        "causal_organism": "Bemisia tabaci",
        "pathogen_class": "Insect Vector",
        "diagnostic_symptoms": "Severe curling, puckering, reduction in leaf lamina size, stunting",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 22.0,
            "favorable_temperature_c_max": 28.0,
            "favorable_relative_humidity_pct": 83,
            "leaf_wetness_hours_threshold": 6
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Imidacloprid 17.8% SL @ 0.5ml/L", "frac_code": "9", "pre_harvest_interval_days": 11},
            {"active_formulation": "Acetamiprid 20% SP @ 0.3g/L", "frac_code": "M4", "pre_harvest_interval_days": 13}
        ],
        "organic_biocontrol_protocol": [
            "Fine insect netting (40 mesh) + Neem extract",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0090",
        "disease_name": "Root Knot Nematode Complex (Variant Strain 6)",
        "causal_organism": "Meloidogyne incognita",
        "pathogen_class": "Nematode",
        "diagnostic_symptoms": "Severe root galling, stunting, chlorosis and nutrient starvation",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 23.0,
            "favorable_temperature_c_max": 29.0,
            "favorable_relative_humidity_pct": 84,
            "leaf_wetness_hours_threshold": 7
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Fluopyram 34.48% SC @ 2.0ml/m2", "frac_code": "10", "pre_harvest_interval_days": 12},
            {"active_formulation": "Carbofuran 3% CG @ 10kg/acre", "frac_code": "M5", "pre_harvest_interval_days": 14}
        ],
        "organic_biocontrol_protocol": [
            "Paecilomyces lilacinus bio-nematicide @ 5kg/acre",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0091",
        "disease_name": "Tomato / Potato Early Blight (Variant Strain 7)",
        "causal_organism": "Alternaria solani",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Foliar target-like concentric rings with yellow halo",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 18.0,
            "favorable_temperature_c_max": 30.0,
            "favorable_relative_humidity_pct": 85,
            "leaf_wetness_hours_threshold": 8
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Mancozeb 75% WP @ 2.5g/L", "frac_code": "11", "pre_harvest_interval_days": 13},
            {"active_formulation": "Copper Oxychloride @ 2.5g/L", "frac_code": "M1", "pre_harvest_interval_days": 5}
        ],
        "organic_biocontrol_protocol": [
            "Trichoderma harzianum @ 5g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0092",
        "disease_name": "Late Blight of Tomato / Potato (Variant Strain 7)",
        "causal_organism": "Phytophthora infestans",
        "pathogen_class": "Oomycete",
        "diagnostic_symptoms": "Rapid water-soaked necrotic lesions with white downy mold",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 19.0,
            "favorable_temperature_c_max": 31.0,
            "favorable_relative_humidity_pct": 86,
            "leaf_wetness_hours_threshold": 9
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Metalaxyl 8% + Mancozeb 64% WP @ 2.5g/L", "frac_code": "12", "pre_harvest_interval_days": 14},
            {"active_formulation": "Dimethomorph 50% WP @ 1.0g/L", "frac_code": "M2", "pre_harvest_interval_days": 6}
        ],
        "organic_biocontrol_protocol": [
            "Bacillus subtilis @ 3ml/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0093",
        "disease_name": "Rice Bacterial Leaf Blight (Variant Strain 7)",
        "causal_organism": "Xanthomonas oryzae",
        "pathogen_class": "Bacteria",
        "diagnostic_symptoms": "Straw yellow undulating leaf tip lesions with amber bacterial ooze",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 20.0,
            "favorable_temperature_c_max": 32.0,
            "favorable_relative_humidity_pct": 87,
            "leaf_wetness_hours_threshold": 10
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Streptocycline 90% + Copper 50% WP @ 0.1g+2.5g/L", "frac_code": "13", "pre_harvest_interval_days": 15},
            {"active_formulation": "Kasugamycin 3% SL @ 2.0ml/L", "frac_code": "M3", "pre_harvest_interval_days": 7}
        ],
        "organic_biocontrol_protocol": [
            "Pseudomonas fluorescens @ 2.5g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0094",
        "disease_name": "Rice Blast (Leaf, Node, Neck) (Variant Strain 7)",
        "causal_organism": "Magnaporthe oryzae",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Spindle / Eye-shaped diamond lesions with greyish center and brown border",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 21.0,
            "favorable_temperature_c_max": 33.0,
            "favorable_relative_humidity_pct": 88,
            "leaf_wetness_hours_threshold": 11
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Tricyclazole 75% WP @ 0.6g/L", "frac_code": "14", "pre_harvest_interval_days": 16},
            {"active_formulation": "Isoprothiolane 40% EC @ 1.5ml/L", "frac_code": "M4", "pre_harvest_interval_days": 8}
        ],
        "organic_biocontrol_protocol": [
            "Neem Seed Kernel Extract 5%",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0095",
        "disease_name": "Wheat Yellow / Stripe Rust (Variant Strain 7)",
        "causal_organism": "Puccinia striiformis",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Parallel linear yellow pustules erupting along leaf lamina",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 22.0,
            "favorable_temperature_c_max": 34.0,
            "favorable_relative_humidity_pct": 89,
            "leaf_wetness_hours_threshold": 12
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Propiconazole 25% EC @ 1.0ml/L", "frac_code": "15", "pre_harvest_interval_days": 17},
            {"active_formulation": "Tebuconazole 25.9% EC @ 1.2ml/L", "frac_code": "M5", "pre_harvest_interval_days": 9}
        ],
        "organic_biocontrol_protocol": [
            "Bio-formulation T. viride @ 5g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0096",
        "disease_name": "Wheat Brown / Leaf Rust (Variant Strain 7)",
        "causal_organism": "Puccinia triticina",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Scattered spherical orange-brown uredinial pustules",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 23.0,
            "favorable_temperature_c_max": 35.0,
            "favorable_relative_humidity_pct": 90,
            "leaf_wetness_hours_threshold": 13
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Mancozeb 75% WP @ 2.0g/L", "frac_code": "16", "pre_harvest_interval_days": 18},
            {"active_formulation": "Propiconazole 25% EC @ 1.0ml/L", "frac_code": "M1", "pre_harvest_interval_days": 10}
        ],
        "organic_biocontrol_protocol": [
            "Sulphur 80% WDG @ 2.5g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0097",
        "disease_name": "Cotton Leaf Curl Virus (CLCuV) (Variant Strain 7)",
        "causal_organism": "Begomovirus / Whitefly",
        "pathogen_class": "Viral Complex",
        "diagnostic_symptoms": "Upward leaf cupping, thickened dark green veins and enations",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 18.0,
            "favorable_temperature_c_max": 28.0,
            "favorable_relative_humidity_pct": 91,
            "leaf_wetness_hours_threshold": 6
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Diafenthiuron 50% WP @ 1.2g/L", "frac_code": "17", "pre_harvest_interval_days": 19},
            {"active_formulation": "Pyriproxyfen 10% EC @ 2.0ml/L", "frac_code": "M2", "pre_harvest_interval_days": 11}
        ],
        "organic_biocontrol_protocol": [
            "Yellow Sticky Traps @ 20/acre + Neem Oil 10000ppm",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0098",
        "disease_name": "Maize Fall Armyworm (Variant Strain 7)",
        "causal_organism": "Spodoptera frugiperda",
        "pathogen_class": "Insect Pest",
        "diagnostic_symptoms": "Ragged shot-holes and sawdust larval frass packed in whorl",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 19.0,
            "favorable_temperature_c_max": 29.0,
            "favorable_relative_humidity_pct": 92,
            "leaf_wetness_hours_threshold": 7
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Emamectin Benzoate 5% SG @ 0.4g/L", "frac_code": "18", "pre_harvest_interval_days": 20},
            {"active_formulation": "Chlorantraniliprole 18.5% SC @ 0.3ml/L", "frac_code": "M3", "pre_harvest_interval_days": 12}
        ],
        "organic_biocontrol_protocol": [
            "Bacillus thuringiensis (Bt) kurstaki @ 2g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0099",
        "disease_name": "Chilli Anthracnose & Fruit Rot (Variant Strain 7)",
        "causal_organism": "Colletotrichum capsici",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Sunken circular dark lesions with salmon-pink spores on ripe pods",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 20.0,
            "favorable_temperature_c_max": 30.0,
            "favorable_relative_humidity_pct": 93,
            "leaf_wetness_hours_threshold": 8
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Difenoconazole 25% EC @ 0.8ml/L", "frac_code": "19", "pre_harvest_interval_days": 7},
            {"active_formulation": "Azoxystrobin 23% SC @ 1.0ml/L", "frac_code": "M4", "pre_harvest_interval_days": 13}
        ],
        "organic_biocontrol_protocol": [
            "Trichoderma viride root dip and foliar spray",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0100",
        "disease_name": "Powdery Mildew of Chilli / Tomato (Variant Strain 7)",
        "causal_organism": "Leveillula taurica",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "White powdery fungal growth on leaf undersides with yellowing above",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 21.0,
            "favorable_temperature_c_max": 31.0,
            "favorable_relative_humidity_pct": 94,
            "leaf_wetness_hours_threshold": 9
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Hexaconazole 5% SC @ 1.5ml/L", "frac_code": "20", "pre_harvest_interval_days": 8},
            {"active_formulation": "Wettable Sulphur 80% WP @ 2.5g/L", "frac_code": "M5", "pre_harvest_interval_days": 14}
        ],
        "organic_biocontrol_protocol": [
            "Ampelomyces quisqualis bio-fungicide",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0101",
        "disease_name": "Sheath Blight of Paddy / Damping Off (Variant Strain 7)",
        "causal_organism": "Rhizoctonia solani",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Snake-skin banded lesions on leaf sheaths near water line",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 22.0,
            "favorable_temperature_c_max": 32.0,
            "favorable_relative_humidity_pct": 75,
            "leaf_wetness_hours_threshold": 10
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Validamycin 3% L @ 2.0ml/L", "frac_code": "1", "pre_harvest_interval_days": 9},
            {"active_formulation": "Hexaconazole 5% EC @ 2.0ml/L", "frac_code": "M1", "pre_harvest_interval_days": 5}
        ],
        "organic_biocontrol_protocol": [
            "Pseudomonas seed dressing @ 10g/kg",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0102",
        "disease_name": "Bacterial Wilt of Solanaceous Crops (Variant Strain 7)",
        "causal_organism": "Ralstonia solanacearum",
        "pathogen_class": "Bacteria",
        "diagnostic_symptoms": "Sudden daytime wilting of plant without foliage yellowing",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 23.0,
            "favorable_temperature_c_max": 33.0,
            "favorable_relative_humidity_pct": 76,
            "leaf_wetness_hours_threshold": 11
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Copper Oxychloride drenching @ 3.0g/L", "frac_code": "2", "pre_harvest_interval_days": 10},
            {"active_formulation": "Streptocycline drenching @ 0.2g/L", "frac_code": "M2", "pre_harvest_interval_days": 6}
        ],
        "organic_biocontrol_protocol": [
            "Bio-enrichment of soil with Trichoderma + FYM",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0103",
        "disease_name": "Fusarium Vascular Wilt (Variant Strain 7)",
        "causal_organism": "Fusarium oxysporum",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Vascular browning inside stem xylem and lower leaf chlorosis",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 18.0,
            "favorable_temperature_c_max": 34.0,
            "favorable_relative_humidity_pct": 77,
            "leaf_wetness_hours_threshold": 12
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Carbendazim 50% WP @ 1.5g/L", "frac_code": "3", "pre_harvest_interval_days": 11},
            {"active_formulation": "Thiophanate Methyl 70% WP @ 1.5g/L", "frac_code": "M3", "pre_harvest_interval_days": 7}
        ],
        "organic_biocontrol_protocol": [
            "Trichoderma harzianum @ 10g/L root zone drench",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0104",
        "disease_name": "Tomato Leaf Curl Begomovirus (ToLCV) (Variant Strain 7)",
        "causal_organism": "Bemisia tabaci",
        "pathogen_class": "Insect Vector",
        "diagnostic_symptoms": "Severe curling, puckering, reduction in leaf lamina size, stunting",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 19.0,
            "favorable_temperature_c_max": 35.0,
            "favorable_relative_humidity_pct": 78,
            "leaf_wetness_hours_threshold": 13
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Imidacloprid 17.8% SL @ 0.5ml/L", "frac_code": "4", "pre_harvest_interval_days": 12},
            {"active_formulation": "Acetamiprid 20% SP @ 0.3g/L", "frac_code": "M4", "pre_harvest_interval_days": 8}
        ],
        "organic_biocontrol_protocol": [
            "Fine insect netting (40 mesh) + Neem extract",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0105",
        "disease_name": "Root Knot Nematode Complex (Variant Strain 7)",
        "causal_organism": "Meloidogyne incognita",
        "pathogen_class": "Nematode",
        "diagnostic_symptoms": "Severe root galling, stunting, chlorosis and nutrient starvation",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 20.0,
            "favorable_temperature_c_max": 28.0,
            "favorable_relative_humidity_pct": 79,
            "leaf_wetness_hours_threshold": 6
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Fluopyram 34.48% SC @ 2.0ml/m2", "frac_code": "5", "pre_harvest_interval_days": 13},
            {"active_formulation": "Carbofuran 3% CG @ 10kg/acre", "frac_code": "M5", "pre_harvest_interval_days": 9}
        ],
        "organic_biocontrol_protocol": [
            "Paecilomyces lilacinus bio-nematicide @ 5kg/acre",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0106",
        "disease_name": "Tomato / Potato Early Blight (Variant Strain 8)",
        "causal_organism": "Alternaria solani",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Foliar target-like concentric rings with yellow halo",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 21.0,
            "favorable_temperature_c_max": 29.0,
            "favorable_relative_humidity_pct": 80,
            "leaf_wetness_hours_threshold": 7
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Mancozeb 75% WP @ 2.5g/L", "frac_code": "6", "pre_harvest_interval_days": 14},
            {"active_formulation": "Copper Oxychloride @ 2.5g/L", "frac_code": "M1", "pre_harvest_interval_days": 10}
        ],
        "organic_biocontrol_protocol": [
            "Trichoderma harzianum @ 5g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0107",
        "disease_name": "Late Blight of Tomato / Potato (Variant Strain 8)",
        "causal_organism": "Phytophthora infestans",
        "pathogen_class": "Oomycete",
        "diagnostic_symptoms": "Rapid water-soaked necrotic lesions with white downy mold",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 22.0,
            "favorable_temperature_c_max": 30.0,
            "favorable_relative_humidity_pct": 81,
            "leaf_wetness_hours_threshold": 8
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Metalaxyl 8% + Mancozeb 64% WP @ 2.5g/L", "frac_code": "7", "pre_harvest_interval_days": 15},
            {"active_formulation": "Dimethomorph 50% WP @ 1.0g/L", "frac_code": "M2", "pre_harvest_interval_days": 11}
        ],
        "organic_biocontrol_protocol": [
            "Bacillus subtilis @ 3ml/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0108",
        "disease_name": "Rice Bacterial Leaf Blight (Variant Strain 8)",
        "causal_organism": "Xanthomonas oryzae",
        "pathogen_class": "Bacteria",
        "diagnostic_symptoms": "Straw yellow undulating leaf tip lesions with amber bacterial ooze",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 23.0,
            "favorable_temperature_c_max": 31.0,
            "favorable_relative_humidity_pct": 82,
            "leaf_wetness_hours_threshold": 9
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Streptocycline 90% + Copper 50% WP @ 0.1g+2.5g/L", "frac_code": "8", "pre_harvest_interval_days": 16},
            {"active_formulation": "Kasugamycin 3% SL @ 2.0ml/L", "frac_code": "M3", "pre_harvest_interval_days": 12}
        ],
        "organic_biocontrol_protocol": [
            "Pseudomonas fluorescens @ 2.5g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0109",
        "disease_name": "Rice Blast (Leaf, Node, Neck) (Variant Strain 8)",
        "causal_organism": "Magnaporthe oryzae",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Spindle / Eye-shaped diamond lesions with greyish center and brown border",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 18.0,
            "favorable_temperature_c_max": 32.0,
            "favorable_relative_humidity_pct": 83,
            "leaf_wetness_hours_threshold": 10
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Tricyclazole 75% WP @ 0.6g/L", "frac_code": "9", "pre_harvest_interval_days": 17},
            {"active_formulation": "Isoprothiolane 40% EC @ 1.5ml/L", "frac_code": "M4", "pre_harvest_interval_days": 13}
        ],
        "organic_biocontrol_protocol": [
            "Neem Seed Kernel Extract 5%",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0110",
        "disease_name": "Wheat Yellow / Stripe Rust (Variant Strain 8)",
        "causal_organism": "Puccinia striiformis",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Parallel linear yellow pustules erupting along leaf lamina",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 19.0,
            "favorable_temperature_c_max": 33.0,
            "favorable_relative_humidity_pct": 84,
            "leaf_wetness_hours_threshold": 11
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Propiconazole 25% EC @ 1.0ml/L", "frac_code": "10", "pre_harvest_interval_days": 18},
            {"active_formulation": "Tebuconazole 25.9% EC @ 1.2ml/L", "frac_code": "M5", "pre_harvest_interval_days": 14}
        ],
        "organic_biocontrol_protocol": [
            "Bio-formulation T. viride @ 5g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0111",
        "disease_name": "Wheat Brown / Leaf Rust (Variant Strain 8)",
        "causal_organism": "Puccinia triticina",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Scattered spherical orange-brown uredinial pustules",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 20.0,
            "favorable_temperature_c_max": 34.0,
            "favorable_relative_humidity_pct": 85,
            "leaf_wetness_hours_threshold": 12
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Mancozeb 75% WP @ 2.0g/L", "frac_code": "11", "pre_harvest_interval_days": 19},
            {"active_formulation": "Propiconazole 25% EC @ 1.0ml/L", "frac_code": "M1", "pre_harvest_interval_days": 5}
        ],
        "organic_biocontrol_protocol": [
            "Sulphur 80% WDG @ 2.5g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0112",
        "disease_name": "Cotton Leaf Curl Virus (CLCuV) (Variant Strain 8)",
        "causal_organism": "Begomovirus / Whitefly",
        "pathogen_class": "Viral Complex",
        "diagnostic_symptoms": "Upward leaf cupping, thickened dark green veins and enations",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 21.0,
            "favorable_temperature_c_max": 35.0,
            "favorable_relative_humidity_pct": 86,
            "leaf_wetness_hours_threshold": 13
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Diafenthiuron 50% WP @ 1.2g/L", "frac_code": "12", "pre_harvest_interval_days": 20},
            {"active_formulation": "Pyriproxyfen 10% EC @ 2.0ml/L", "frac_code": "M2", "pre_harvest_interval_days": 6}
        ],
        "organic_biocontrol_protocol": [
            "Yellow Sticky Traps @ 20/acre + Neem Oil 10000ppm",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0113",
        "disease_name": "Maize Fall Armyworm (Variant Strain 8)",
        "causal_organism": "Spodoptera frugiperda",
        "pathogen_class": "Insect Pest",
        "diagnostic_symptoms": "Ragged shot-holes and sawdust larval frass packed in whorl",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 22.0,
            "favorable_temperature_c_max": 28.0,
            "favorable_relative_humidity_pct": 87,
            "leaf_wetness_hours_threshold": 6
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Emamectin Benzoate 5% SG @ 0.4g/L", "frac_code": "13", "pre_harvest_interval_days": 7},
            {"active_formulation": "Chlorantraniliprole 18.5% SC @ 0.3ml/L", "frac_code": "M3", "pre_harvest_interval_days": 7}
        ],
        "organic_biocontrol_protocol": [
            "Bacillus thuringiensis (Bt) kurstaki @ 2g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0114",
        "disease_name": "Chilli Anthracnose & Fruit Rot (Variant Strain 8)",
        "causal_organism": "Colletotrichum capsici",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Sunken circular dark lesions with salmon-pink spores on ripe pods",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 23.0,
            "favorable_temperature_c_max": 29.0,
            "favorable_relative_humidity_pct": 88,
            "leaf_wetness_hours_threshold": 7
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Difenoconazole 25% EC @ 0.8ml/L", "frac_code": "14", "pre_harvest_interval_days": 8},
            {"active_formulation": "Azoxystrobin 23% SC @ 1.0ml/L", "frac_code": "M4", "pre_harvest_interval_days": 8}
        ],
        "organic_biocontrol_protocol": [
            "Trichoderma viride root dip and foliar spray",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0115",
        "disease_name": "Powdery Mildew of Chilli / Tomato (Variant Strain 8)",
        "causal_organism": "Leveillula taurica",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "White powdery fungal growth on leaf undersides with yellowing above",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 18.0,
            "favorable_temperature_c_max": 30.0,
            "favorable_relative_humidity_pct": 89,
            "leaf_wetness_hours_threshold": 8
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Hexaconazole 5% SC @ 1.5ml/L", "frac_code": "15", "pre_harvest_interval_days": 9},
            {"active_formulation": "Wettable Sulphur 80% WP @ 2.5g/L", "frac_code": "M5", "pre_harvest_interval_days": 9}
        ],
        "organic_biocontrol_protocol": [
            "Ampelomyces quisqualis bio-fungicide",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0116",
        "disease_name": "Sheath Blight of Paddy / Damping Off (Variant Strain 8)",
        "causal_organism": "Rhizoctonia solani",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Snake-skin banded lesions on leaf sheaths near water line",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 19.0,
            "favorable_temperature_c_max": 31.0,
            "favorable_relative_humidity_pct": 90,
            "leaf_wetness_hours_threshold": 9
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Validamycin 3% L @ 2.0ml/L", "frac_code": "16", "pre_harvest_interval_days": 10},
            {"active_formulation": "Hexaconazole 5% EC @ 2.0ml/L", "frac_code": "M1", "pre_harvest_interval_days": 10}
        ],
        "organic_biocontrol_protocol": [
            "Pseudomonas seed dressing @ 10g/kg",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0117",
        "disease_name": "Bacterial Wilt of Solanaceous Crops (Variant Strain 8)",
        "causal_organism": "Ralstonia solanacearum",
        "pathogen_class": "Bacteria",
        "diagnostic_symptoms": "Sudden daytime wilting of plant without foliage yellowing",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 20.0,
            "favorable_temperature_c_max": 32.0,
            "favorable_relative_humidity_pct": 91,
            "leaf_wetness_hours_threshold": 10
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Copper Oxychloride drenching @ 3.0g/L", "frac_code": "17", "pre_harvest_interval_days": 11},
            {"active_formulation": "Streptocycline drenching @ 0.2g/L", "frac_code": "M2", "pre_harvest_interval_days": 11}
        ],
        "organic_biocontrol_protocol": [
            "Bio-enrichment of soil with Trichoderma + FYM",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0118",
        "disease_name": "Fusarium Vascular Wilt (Variant Strain 8)",
        "causal_organism": "Fusarium oxysporum",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Vascular browning inside stem xylem and lower leaf chlorosis",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 21.0,
            "favorable_temperature_c_max": 33.0,
            "favorable_relative_humidity_pct": 92,
            "leaf_wetness_hours_threshold": 11
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Carbendazim 50% WP @ 1.5g/L", "frac_code": "18", "pre_harvest_interval_days": 12},
            {"active_formulation": "Thiophanate Methyl 70% WP @ 1.5g/L", "frac_code": "M3", "pre_harvest_interval_days": 12}
        ],
        "organic_biocontrol_protocol": [
            "Trichoderma harzianum @ 10g/L root zone drench",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0119",
        "disease_name": "Tomato Leaf Curl Begomovirus (ToLCV) (Variant Strain 8)",
        "causal_organism": "Bemisia tabaci",
        "pathogen_class": "Insect Vector",
        "diagnostic_symptoms": "Severe curling, puckering, reduction in leaf lamina size, stunting",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 22.0,
            "favorable_temperature_c_max": 34.0,
            "favorable_relative_humidity_pct": 93,
            "leaf_wetness_hours_threshold": 12
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Imidacloprid 17.8% SL @ 0.5ml/L", "frac_code": "19", "pre_harvest_interval_days": 13},
            {"active_formulation": "Acetamiprid 20% SP @ 0.3g/L", "frac_code": "M4", "pre_harvest_interval_days": 13}
        ],
        "organic_biocontrol_protocol": [
            "Fine insect netting (40 mesh) + Neem extract",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0120",
        "disease_name": "Root Knot Nematode Complex (Variant Strain 8)",
        "causal_organism": "Meloidogyne incognita",
        "pathogen_class": "Nematode",
        "diagnostic_symptoms": "Severe root galling, stunting, chlorosis and nutrient starvation",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 23.0,
            "favorable_temperature_c_max": 35.0,
            "favorable_relative_humidity_pct": 94,
            "leaf_wetness_hours_threshold": 13
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Fluopyram 34.48% SC @ 2.0ml/m2", "frac_code": "20", "pre_harvest_interval_days": 14},
            {"active_formulation": "Carbofuran 3% CG @ 10kg/acre", "frac_code": "M5", "pre_harvest_interval_days": 14}
        ],
        "organic_biocontrol_protocol": [
            "Paecilomyces lilacinus bio-nematicide @ 5kg/acre",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0121",
        "disease_name": "Tomato / Potato Early Blight (Variant Strain 9)",
        "causal_organism": "Alternaria solani",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Foliar target-like concentric rings with yellow halo",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 18.0,
            "favorable_temperature_c_max": 28.0,
            "favorable_relative_humidity_pct": 75,
            "leaf_wetness_hours_threshold": 6
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Mancozeb 75% WP @ 2.5g/L", "frac_code": "1", "pre_harvest_interval_days": 15},
            {"active_formulation": "Copper Oxychloride @ 2.5g/L", "frac_code": "M1", "pre_harvest_interval_days": 5}
        ],
        "organic_biocontrol_protocol": [
            "Trichoderma harzianum @ 5g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0122",
        "disease_name": "Late Blight of Tomato / Potato (Variant Strain 9)",
        "causal_organism": "Phytophthora infestans",
        "pathogen_class": "Oomycete",
        "diagnostic_symptoms": "Rapid water-soaked necrotic lesions with white downy mold",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 19.0,
            "favorable_temperature_c_max": 29.0,
            "favorable_relative_humidity_pct": 76,
            "leaf_wetness_hours_threshold": 7
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Metalaxyl 8% + Mancozeb 64% WP @ 2.5g/L", "frac_code": "2", "pre_harvest_interval_days": 16},
            {"active_formulation": "Dimethomorph 50% WP @ 1.0g/L", "frac_code": "M2", "pre_harvest_interval_days": 6}
        ],
        "organic_biocontrol_protocol": [
            "Bacillus subtilis @ 3ml/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0123",
        "disease_name": "Rice Bacterial Leaf Blight (Variant Strain 9)",
        "causal_organism": "Xanthomonas oryzae",
        "pathogen_class": "Bacteria",
        "diagnostic_symptoms": "Straw yellow undulating leaf tip lesions with amber bacterial ooze",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 20.0,
            "favorable_temperature_c_max": 30.0,
            "favorable_relative_humidity_pct": 77,
            "leaf_wetness_hours_threshold": 8
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Streptocycline 90% + Copper 50% WP @ 0.1g+2.5g/L", "frac_code": "3", "pre_harvest_interval_days": 17},
            {"active_formulation": "Kasugamycin 3% SL @ 2.0ml/L", "frac_code": "M3", "pre_harvest_interval_days": 7}
        ],
        "organic_biocontrol_protocol": [
            "Pseudomonas fluorescens @ 2.5g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0124",
        "disease_name": "Rice Blast (Leaf, Node, Neck) (Variant Strain 9)",
        "causal_organism": "Magnaporthe oryzae",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Spindle / Eye-shaped diamond lesions with greyish center and brown border",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 21.0,
            "favorable_temperature_c_max": 31.0,
            "favorable_relative_humidity_pct": 78,
            "leaf_wetness_hours_threshold": 9
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Tricyclazole 75% WP @ 0.6g/L", "frac_code": "4", "pre_harvest_interval_days": 18},
            {"active_formulation": "Isoprothiolane 40% EC @ 1.5ml/L", "frac_code": "M4", "pre_harvest_interval_days": 8}
        ],
        "organic_biocontrol_protocol": [
            "Neem Seed Kernel Extract 5%",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0125",
        "disease_name": "Wheat Yellow / Stripe Rust (Variant Strain 9)",
        "causal_organism": "Puccinia striiformis",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Parallel linear yellow pustules erupting along leaf lamina",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 22.0,
            "favorable_temperature_c_max": 32.0,
            "favorable_relative_humidity_pct": 79,
            "leaf_wetness_hours_threshold": 10
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Propiconazole 25% EC @ 1.0ml/L", "frac_code": "5", "pre_harvest_interval_days": 19},
            {"active_formulation": "Tebuconazole 25.9% EC @ 1.2ml/L", "frac_code": "M5", "pre_harvest_interval_days": 9}
        ],
        "organic_biocontrol_protocol": [
            "Bio-formulation T. viride @ 5g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0126",
        "disease_name": "Wheat Brown / Leaf Rust (Variant Strain 9)",
        "causal_organism": "Puccinia triticina",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Scattered spherical orange-brown uredinial pustules",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 23.0,
            "favorable_temperature_c_max": 33.0,
            "favorable_relative_humidity_pct": 80,
            "leaf_wetness_hours_threshold": 11
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Mancozeb 75% WP @ 2.0g/L", "frac_code": "6", "pre_harvest_interval_days": 20},
            {"active_formulation": "Propiconazole 25% EC @ 1.0ml/L", "frac_code": "M1", "pre_harvest_interval_days": 10}
        ],
        "organic_biocontrol_protocol": [
            "Sulphur 80% WDG @ 2.5g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0127",
        "disease_name": "Cotton Leaf Curl Virus (CLCuV) (Variant Strain 9)",
        "causal_organism": "Begomovirus / Whitefly",
        "pathogen_class": "Viral Complex",
        "diagnostic_symptoms": "Upward leaf cupping, thickened dark green veins and enations",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 18.0,
            "favorable_temperature_c_max": 34.0,
            "favorable_relative_humidity_pct": 81,
            "leaf_wetness_hours_threshold": 12
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Diafenthiuron 50% WP @ 1.2g/L", "frac_code": "7", "pre_harvest_interval_days": 7},
            {"active_formulation": "Pyriproxyfen 10% EC @ 2.0ml/L", "frac_code": "M2", "pre_harvest_interval_days": 11}
        ],
        "organic_biocontrol_protocol": [
            "Yellow Sticky Traps @ 20/acre + Neem Oil 10000ppm",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0128",
        "disease_name": "Maize Fall Armyworm (Variant Strain 9)",
        "causal_organism": "Spodoptera frugiperda",
        "pathogen_class": "Insect Pest",
        "diagnostic_symptoms": "Ragged shot-holes and sawdust larval frass packed in whorl",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 19.0,
            "favorable_temperature_c_max": 35.0,
            "favorable_relative_humidity_pct": 82,
            "leaf_wetness_hours_threshold": 13
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Emamectin Benzoate 5% SG @ 0.4g/L", "frac_code": "8", "pre_harvest_interval_days": 8},
            {"active_formulation": "Chlorantraniliprole 18.5% SC @ 0.3ml/L", "frac_code": "M3", "pre_harvest_interval_days": 12}
        ],
        "organic_biocontrol_protocol": [
            "Bacillus thuringiensis (Bt) kurstaki @ 2g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0129",
        "disease_name": "Chilli Anthracnose & Fruit Rot (Variant Strain 9)",
        "causal_organism": "Colletotrichum capsici",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Sunken circular dark lesions with salmon-pink spores on ripe pods",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 20.0,
            "favorable_temperature_c_max": 28.0,
            "favorable_relative_humidity_pct": 83,
            "leaf_wetness_hours_threshold": 6
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Difenoconazole 25% EC @ 0.8ml/L", "frac_code": "9", "pre_harvest_interval_days": 9},
            {"active_formulation": "Azoxystrobin 23% SC @ 1.0ml/L", "frac_code": "M4", "pre_harvest_interval_days": 13}
        ],
        "organic_biocontrol_protocol": [
            "Trichoderma viride root dip and foliar spray",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0130",
        "disease_name": "Powdery Mildew of Chilli / Tomato (Variant Strain 9)",
        "causal_organism": "Leveillula taurica",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "White powdery fungal growth on leaf undersides with yellowing above",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 21.0,
            "favorable_temperature_c_max": 29.0,
            "favorable_relative_humidity_pct": 84,
            "leaf_wetness_hours_threshold": 7
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Hexaconazole 5% SC @ 1.5ml/L", "frac_code": "10", "pre_harvest_interval_days": 10},
            {"active_formulation": "Wettable Sulphur 80% WP @ 2.5g/L", "frac_code": "M5", "pre_harvest_interval_days": 14}
        ],
        "organic_biocontrol_protocol": [
            "Ampelomyces quisqualis bio-fungicide",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0131",
        "disease_name": "Sheath Blight of Paddy / Damping Off (Variant Strain 9)",
        "causal_organism": "Rhizoctonia solani",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Snake-skin banded lesions on leaf sheaths near water line",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 22.0,
            "favorable_temperature_c_max": 30.0,
            "favorable_relative_humidity_pct": 85,
            "leaf_wetness_hours_threshold": 8
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Validamycin 3% L @ 2.0ml/L", "frac_code": "11", "pre_harvest_interval_days": 11},
            {"active_formulation": "Hexaconazole 5% EC @ 2.0ml/L", "frac_code": "M1", "pre_harvest_interval_days": 5}
        ],
        "organic_biocontrol_protocol": [
            "Pseudomonas seed dressing @ 10g/kg",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0132",
        "disease_name": "Bacterial Wilt of Solanaceous Crops (Variant Strain 9)",
        "causal_organism": "Ralstonia solanacearum",
        "pathogen_class": "Bacteria",
        "diagnostic_symptoms": "Sudden daytime wilting of plant without foliage yellowing",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 23.0,
            "favorable_temperature_c_max": 31.0,
            "favorable_relative_humidity_pct": 86,
            "leaf_wetness_hours_threshold": 9
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Copper Oxychloride drenching @ 3.0g/L", "frac_code": "12", "pre_harvest_interval_days": 12},
            {"active_formulation": "Streptocycline drenching @ 0.2g/L", "frac_code": "M2", "pre_harvest_interval_days": 6}
        ],
        "organic_biocontrol_protocol": [
            "Bio-enrichment of soil with Trichoderma + FYM",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0133",
        "disease_name": "Fusarium Vascular Wilt (Variant Strain 9)",
        "causal_organism": "Fusarium oxysporum",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Vascular browning inside stem xylem and lower leaf chlorosis",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 18.0,
            "favorable_temperature_c_max": 32.0,
            "favorable_relative_humidity_pct": 87,
            "leaf_wetness_hours_threshold": 10
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Carbendazim 50% WP @ 1.5g/L", "frac_code": "13", "pre_harvest_interval_days": 13},
            {"active_formulation": "Thiophanate Methyl 70% WP @ 1.5g/L", "frac_code": "M3", "pre_harvest_interval_days": 7}
        ],
        "organic_biocontrol_protocol": [
            "Trichoderma harzianum @ 10g/L root zone drench",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0134",
        "disease_name": "Tomato Leaf Curl Begomovirus (ToLCV) (Variant Strain 9)",
        "causal_organism": "Bemisia tabaci",
        "pathogen_class": "Insect Vector",
        "diagnostic_symptoms": "Severe curling, puckering, reduction in leaf lamina size, stunting",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 19.0,
            "favorable_temperature_c_max": 33.0,
            "favorable_relative_humidity_pct": 88,
            "leaf_wetness_hours_threshold": 11
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Imidacloprid 17.8% SL @ 0.5ml/L", "frac_code": "14", "pre_harvest_interval_days": 14},
            {"active_formulation": "Acetamiprid 20% SP @ 0.3g/L", "frac_code": "M4", "pre_harvest_interval_days": 8}
        ],
        "organic_biocontrol_protocol": [
            "Fine insect netting (40 mesh) + Neem extract",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0135",
        "disease_name": "Root Knot Nematode Complex (Variant Strain 9)",
        "causal_organism": "Meloidogyne incognita",
        "pathogen_class": "Nematode",
        "diagnostic_symptoms": "Severe root galling, stunting, chlorosis and nutrient starvation",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 20.0,
            "favorable_temperature_c_max": 34.0,
            "favorable_relative_humidity_pct": 89,
            "leaf_wetness_hours_threshold": 12
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Fluopyram 34.48% SC @ 2.0ml/m2", "frac_code": "15", "pre_harvest_interval_days": 15},
            {"active_formulation": "Carbofuran 3% CG @ 10kg/acre", "frac_code": "M5", "pre_harvest_interval_days": 9}
        ],
        "organic_biocontrol_protocol": [
            "Paecilomyces lilacinus bio-nematicide @ 5kg/acre",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0136",
        "disease_name": "Tomato / Potato Early Blight (Variant Strain 10)",
        "causal_organism": "Alternaria solani",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Foliar target-like concentric rings with yellow halo",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 21.0,
            "favorable_temperature_c_max": 35.0,
            "favorable_relative_humidity_pct": 90,
            "leaf_wetness_hours_threshold": 13
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Mancozeb 75% WP @ 2.5g/L", "frac_code": "16", "pre_harvest_interval_days": 16},
            {"active_formulation": "Copper Oxychloride @ 2.5g/L", "frac_code": "M1", "pre_harvest_interval_days": 10}
        ],
        "organic_biocontrol_protocol": [
            "Trichoderma harzianum @ 5g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0137",
        "disease_name": "Late Blight of Tomato / Potato (Variant Strain 10)",
        "causal_organism": "Phytophthora infestans",
        "pathogen_class": "Oomycete",
        "diagnostic_symptoms": "Rapid water-soaked necrotic lesions with white downy mold",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 22.0,
            "favorable_temperature_c_max": 28.0,
            "favorable_relative_humidity_pct": 91,
            "leaf_wetness_hours_threshold": 6
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Metalaxyl 8% + Mancozeb 64% WP @ 2.5g/L", "frac_code": "17", "pre_harvest_interval_days": 17},
            {"active_formulation": "Dimethomorph 50% WP @ 1.0g/L", "frac_code": "M2", "pre_harvest_interval_days": 11}
        ],
        "organic_biocontrol_protocol": [
            "Bacillus subtilis @ 3ml/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0138",
        "disease_name": "Rice Bacterial Leaf Blight (Variant Strain 10)",
        "causal_organism": "Xanthomonas oryzae",
        "pathogen_class": "Bacteria",
        "diagnostic_symptoms": "Straw yellow undulating leaf tip lesions with amber bacterial ooze",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 23.0,
            "favorable_temperature_c_max": 29.0,
            "favorable_relative_humidity_pct": 92,
            "leaf_wetness_hours_threshold": 7
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Streptocycline 90% + Copper 50% WP @ 0.1g+2.5g/L", "frac_code": "18", "pre_harvest_interval_days": 18},
            {"active_formulation": "Kasugamycin 3% SL @ 2.0ml/L", "frac_code": "M3", "pre_harvest_interval_days": 12}
        ],
        "organic_biocontrol_protocol": [
            "Pseudomonas fluorescens @ 2.5g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0139",
        "disease_name": "Rice Blast (Leaf, Node, Neck) (Variant Strain 10)",
        "causal_organism": "Magnaporthe oryzae",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Spindle / Eye-shaped diamond lesions with greyish center and brown border",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 18.0,
            "favorable_temperature_c_max": 30.0,
            "favorable_relative_humidity_pct": 93,
            "leaf_wetness_hours_threshold": 8
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Tricyclazole 75% WP @ 0.6g/L", "frac_code": "19", "pre_harvest_interval_days": 19},
            {"active_formulation": "Isoprothiolane 40% EC @ 1.5ml/L", "frac_code": "M4", "pre_harvest_interval_days": 13}
        ],
        "organic_biocontrol_protocol": [
            "Neem Seed Kernel Extract 5%",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0140",
        "disease_name": "Wheat Yellow / Stripe Rust (Variant Strain 10)",
        "causal_organism": "Puccinia striiformis",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Parallel linear yellow pustules erupting along leaf lamina",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 19.0,
            "favorable_temperature_c_max": 31.0,
            "favorable_relative_humidity_pct": 94,
            "leaf_wetness_hours_threshold": 9
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Propiconazole 25% EC @ 1.0ml/L", "frac_code": "20", "pre_harvest_interval_days": 20},
            {"active_formulation": "Tebuconazole 25.9% EC @ 1.2ml/L", "frac_code": "M5", "pre_harvest_interval_days": 14}
        ],
        "organic_biocontrol_protocol": [
            "Bio-formulation T. viride @ 5g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0141",
        "disease_name": "Wheat Brown / Leaf Rust (Variant Strain 10)",
        "causal_organism": "Puccinia triticina",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Scattered spherical orange-brown uredinial pustules",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 20.0,
            "favorable_temperature_c_max": 32.0,
            "favorable_relative_humidity_pct": 75,
            "leaf_wetness_hours_threshold": 10
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Mancozeb 75% WP @ 2.0g/L", "frac_code": "1", "pre_harvest_interval_days": 7},
            {"active_formulation": "Propiconazole 25% EC @ 1.0ml/L", "frac_code": "M1", "pre_harvest_interval_days": 5}
        ],
        "organic_biocontrol_protocol": [
            "Sulphur 80% WDG @ 2.5g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0142",
        "disease_name": "Cotton Leaf Curl Virus (CLCuV) (Variant Strain 10)",
        "causal_organism": "Begomovirus / Whitefly",
        "pathogen_class": "Viral Complex",
        "diagnostic_symptoms": "Upward leaf cupping, thickened dark green veins and enations",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 21.0,
            "favorable_temperature_c_max": 33.0,
            "favorable_relative_humidity_pct": 76,
            "leaf_wetness_hours_threshold": 11
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Diafenthiuron 50% WP @ 1.2g/L", "frac_code": "2", "pre_harvest_interval_days": 8},
            {"active_formulation": "Pyriproxyfen 10% EC @ 2.0ml/L", "frac_code": "M2", "pre_harvest_interval_days": 6}
        ],
        "organic_biocontrol_protocol": [
            "Yellow Sticky Traps @ 20/acre + Neem Oil 10000ppm",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0143",
        "disease_name": "Maize Fall Armyworm (Variant Strain 10)",
        "causal_organism": "Spodoptera frugiperda",
        "pathogen_class": "Insect Pest",
        "diagnostic_symptoms": "Ragged shot-holes and sawdust larval frass packed in whorl",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 22.0,
            "favorable_temperature_c_max": 34.0,
            "favorable_relative_humidity_pct": 77,
            "leaf_wetness_hours_threshold": 12
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Emamectin Benzoate 5% SG @ 0.4g/L", "frac_code": "3", "pre_harvest_interval_days": 9},
            {"active_formulation": "Chlorantraniliprole 18.5% SC @ 0.3ml/L", "frac_code": "M3", "pre_harvest_interval_days": 7}
        ],
        "organic_biocontrol_protocol": [
            "Bacillus thuringiensis (Bt) kurstaki @ 2g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0144",
        "disease_name": "Chilli Anthracnose & Fruit Rot (Variant Strain 10)",
        "causal_organism": "Colletotrichum capsici",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Sunken circular dark lesions with salmon-pink spores on ripe pods",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 23.0,
            "favorable_temperature_c_max": 35.0,
            "favorable_relative_humidity_pct": 78,
            "leaf_wetness_hours_threshold": 13
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Difenoconazole 25% EC @ 0.8ml/L", "frac_code": "4", "pre_harvest_interval_days": 10},
            {"active_formulation": "Azoxystrobin 23% SC @ 1.0ml/L", "frac_code": "M4", "pre_harvest_interval_days": 8}
        ],
        "organic_biocontrol_protocol": [
            "Trichoderma viride root dip and foliar spray",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0145",
        "disease_name": "Powdery Mildew of Chilli / Tomato (Variant Strain 10)",
        "causal_organism": "Leveillula taurica",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "White powdery fungal growth on leaf undersides with yellowing above",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 18.0,
            "favorable_temperature_c_max": 28.0,
            "favorable_relative_humidity_pct": 79,
            "leaf_wetness_hours_threshold": 6
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Hexaconazole 5% SC @ 1.5ml/L", "frac_code": "5", "pre_harvest_interval_days": 11},
            {"active_formulation": "Wettable Sulphur 80% WP @ 2.5g/L", "frac_code": "M5", "pre_harvest_interval_days": 9}
        ],
        "organic_biocontrol_protocol": [
            "Ampelomyces quisqualis bio-fungicide",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0146",
        "disease_name": "Sheath Blight of Paddy / Damping Off (Variant Strain 10)",
        "causal_organism": "Rhizoctonia solani",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Snake-skin banded lesions on leaf sheaths near water line",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 19.0,
            "favorable_temperature_c_max": 29.0,
            "favorable_relative_humidity_pct": 80,
            "leaf_wetness_hours_threshold": 7
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Validamycin 3% L @ 2.0ml/L", "frac_code": "6", "pre_harvest_interval_days": 12},
            {"active_formulation": "Hexaconazole 5% EC @ 2.0ml/L", "frac_code": "M1", "pre_harvest_interval_days": 10}
        ],
        "organic_biocontrol_protocol": [
            "Pseudomonas seed dressing @ 10g/kg",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0147",
        "disease_name": "Bacterial Wilt of Solanaceous Crops (Variant Strain 10)",
        "causal_organism": "Ralstonia solanacearum",
        "pathogen_class": "Bacteria",
        "diagnostic_symptoms": "Sudden daytime wilting of plant without foliage yellowing",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 20.0,
            "favorable_temperature_c_max": 30.0,
            "favorable_relative_humidity_pct": 81,
            "leaf_wetness_hours_threshold": 8
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Copper Oxychloride drenching @ 3.0g/L", "frac_code": "7", "pre_harvest_interval_days": 13},
            {"active_formulation": "Streptocycline drenching @ 0.2g/L", "frac_code": "M2", "pre_harvest_interval_days": 11}
        ],
        "organic_biocontrol_protocol": [
            "Bio-enrichment of soil with Trichoderma + FYM",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0148",
        "disease_name": "Fusarium Vascular Wilt (Variant Strain 10)",
        "causal_organism": "Fusarium oxysporum",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Vascular browning inside stem xylem and lower leaf chlorosis",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 21.0,
            "favorable_temperature_c_max": 31.0,
            "favorable_relative_humidity_pct": 82,
            "leaf_wetness_hours_threshold": 9
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Carbendazim 50% WP @ 1.5g/L", "frac_code": "8", "pre_harvest_interval_days": 14},
            {"active_formulation": "Thiophanate Methyl 70% WP @ 1.5g/L", "frac_code": "M3", "pre_harvest_interval_days": 12}
        ],
        "organic_biocontrol_protocol": [
            "Trichoderma harzianum @ 10g/L root zone drench",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0149",
        "disease_name": "Tomato Leaf Curl Begomovirus (ToLCV) (Variant Strain 10)",
        "causal_organism": "Bemisia tabaci",
        "pathogen_class": "Insect Vector",
        "diagnostic_symptoms": "Severe curling, puckering, reduction in leaf lamina size, stunting",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 22.0,
            "favorable_temperature_c_max": 32.0,
            "favorable_relative_humidity_pct": 83,
            "leaf_wetness_hours_threshold": 10
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Imidacloprid 17.8% SL @ 0.5ml/L", "frac_code": "9", "pre_harvest_interval_days": 15},
            {"active_formulation": "Acetamiprid 20% SP @ 0.3g/L", "frac_code": "M4", "pre_harvest_interval_days": 13}
        ],
        "organic_biocontrol_protocol": [
            "Fine insect netting (40 mesh) + Neem extract",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0150",
        "disease_name": "Root Knot Nematode Complex (Variant Strain 10)",
        "causal_organism": "Meloidogyne incognita",
        "pathogen_class": "Nematode",
        "diagnostic_symptoms": "Severe root galling, stunting, chlorosis and nutrient starvation",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 23.0,
            "favorable_temperature_c_max": 33.0,
            "favorable_relative_humidity_pct": 84,
            "leaf_wetness_hours_threshold": 11
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Fluopyram 34.48% SC @ 2.0ml/m2", "frac_code": "10", "pre_harvest_interval_days": 16},
            {"active_formulation": "Carbofuran 3% CG @ 10kg/acre", "frac_code": "M5", "pre_harvest_interval_days": 14}
        ],
        "organic_biocontrol_protocol": [
            "Paecilomyces lilacinus bio-nematicide @ 5kg/acre",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0151",
        "disease_name": "Tomato / Potato Early Blight (Variant Strain 11)",
        "causal_organism": "Alternaria solani",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Foliar target-like concentric rings with yellow halo",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 18.0,
            "favorable_temperature_c_max": 34.0,
            "favorable_relative_humidity_pct": 85,
            "leaf_wetness_hours_threshold": 12
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Mancozeb 75% WP @ 2.5g/L", "frac_code": "11", "pre_harvest_interval_days": 17},
            {"active_formulation": "Copper Oxychloride @ 2.5g/L", "frac_code": "M1", "pre_harvest_interval_days": 5}
        ],
        "organic_biocontrol_protocol": [
            "Trichoderma harzianum @ 5g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0152",
        "disease_name": "Late Blight of Tomato / Potato (Variant Strain 11)",
        "causal_organism": "Phytophthora infestans",
        "pathogen_class": "Oomycete",
        "diagnostic_symptoms": "Rapid water-soaked necrotic lesions with white downy mold",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 19.0,
            "favorable_temperature_c_max": 35.0,
            "favorable_relative_humidity_pct": 86,
            "leaf_wetness_hours_threshold": 13
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Metalaxyl 8% + Mancozeb 64% WP @ 2.5g/L", "frac_code": "12", "pre_harvest_interval_days": 18},
            {"active_formulation": "Dimethomorph 50% WP @ 1.0g/L", "frac_code": "M2", "pre_harvest_interval_days": 6}
        ],
        "organic_biocontrol_protocol": [
            "Bacillus subtilis @ 3ml/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0153",
        "disease_name": "Rice Bacterial Leaf Blight (Variant Strain 11)",
        "causal_organism": "Xanthomonas oryzae",
        "pathogen_class": "Bacteria",
        "diagnostic_symptoms": "Straw yellow undulating leaf tip lesions with amber bacterial ooze",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 20.0,
            "favorable_temperature_c_max": 28.0,
            "favorable_relative_humidity_pct": 87,
            "leaf_wetness_hours_threshold": 6
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Streptocycline 90% + Copper 50% WP @ 0.1g+2.5g/L", "frac_code": "13", "pre_harvest_interval_days": 19},
            {"active_formulation": "Kasugamycin 3% SL @ 2.0ml/L", "frac_code": "M3", "pre_harvest_interval_days": 7}
        ],
        "organic_biocontrol_protocol": [
            "Pseudomonas fluorescens @ 2.5g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0154",
        "disease_name": "Rice Blast (Leaf, Node, Neck) (Variant Strain 11)",
        "causal_organism": "Magnaporthe oryzae",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Spindle / Eye-shaped diamond lesions with greyish center and brown border",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 21.0,
            "favorable_temperature_c_max": 29.0,
            "favorable_relative_humidity_pct": 88,
            "leaf_wetness_hours_threshold": 7
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Tricyclazole 75% WP @ 0.6g/L", "frac_code": "14", "pre_harvest_interval_days": 20},
            {"active_formulation": "Isoprothiolane 40% EC @ 1.5ml/L", "frac_code": "M4", "pre_harvest_interval_days": 8}
        ],
        "organic_biocontrol_protocol": [
            "Neem Seed Kernel Extract 5%",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0155",
        "disease_name": "Wheat Yellow / Stripe Rust (Variant Strain 11)",
        "causal_organism": "Puccinia striiformis",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Parallel linear yellow pustules erupting along leaf lamina",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 22.0,
            "favorable_temperature_c_max": 30.0,
            "favorable_relative_humidity_pct": 89,
            "leaf_wetness_hours_threshold": 8
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Propiconazole 25% EC @ 1.0ml/L", "frac_code": "15", "pre_harvest_interval_days": 7},
            {"active_formulation": "Tebuconazole 25.9% EC @ 1.2ml/L", "frac_code": "M5", "pre_harvest_interval_days": 9}
        ],
        "organic_biocontrol_protocol": [
            "Bio-formulation T. viride @ 5g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0156",
        "disease_name": "Wheat Brown / Leaf Rust (Variant Strain 11)",
        "causal_organism": "Puccinia triticina",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Scattered spherical orange-brown uredinial pustules",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 23.0,
            "favorable_temperature_c_max": 31.0,
            "favorable_relative_humidity_pct": 90,
            "leaf_wetness_hours_threshold": 9
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Mancozeb 75% WP @ 2.0g/L", "frac_code": "16", "pre_harvest_interval_days": 8},
            {"active_formulation": "Propiconazole 25% EC @ 1.0ml/L", "frac_code": "M1", "pre_harvest_interval_days": 10}
        ],
        "organic_biocontrol_protocol": [
            "Sulphur 80% WDG @ 2.5g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0157",
        "disease_name": "Cotton Leaf Curl Virus (CLCuV) (Variant Strain 11)",
        "causal_organism": "Begomovirus / Whitefly",
        "pathogen_class": "Viral Complex",
        "diagnostic_symptoms": "Upward leaf cupping, thickened dark green veins and enations",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 18.0,
            "favorable_temperature_c_max": 32.0,
            "favorable_relative_humidity_pct": 91,
            "leaf_wetness_hours_threshold": 10
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Diafenthiuron 50% WP @ 1.2g/L", "frac_code": "17", "pre_harvest_interval_days": 9},
            {"active_formulation": "Pyriproxyfen 10% EC @ 2.0ml/L", "frac_code": "M2", "pre_harvest_interval_days": 11}
        ],
        "organic_biocontrol_protocol": [
            "Yellow Sticky Traps @ 20/acre + Neem Oil 10000ppm",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0158",
        "disease_name": "Maize Fall Armyworm (Variant Strain 11)",
        "causal_organism": "Spodoptera frugiperda",
        "pathogen_class": "Insect Pest",
        "diagnostic_symptoms": "Ragged shot-holes and sawdust larval frass packed in whorl",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 19.0,
            "favorable_temperature_c_max": 33.0,
            "favorable_relative_humidity_pct": 92,
            "leaf_wetness_hours_threshold": 11
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Emamectin Benzoate 5% SG @ 0.4g/L", "frac_code": "18", "pre_harvest_interval_days": 10},
            {"active_formulation": "Chlorantraniliprole 18.5% SC @ 0.3ml/L", "frac_code": "M3", "pre_harvest_interval_days": 12}
        ],
        "organic_biocontrol_protocol": [
            "Bacillus thuringiensis (Bt) kurstaki @ 2g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0159",
        "disease_name": "Chilli Anthracnose & Fruit Rot (Variant Strain 11)",
        "causal_organism": "Colletotrichum capsici",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Sunken circular dark lesions with salmon-pink spores on ripe pods",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 20.0,
            "favorable_temperature_c_max": 34.0,
            "favorable_relative_humidity_pct": 93,
            "leaf_wetness_hours_threshold": 12
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Difenoconazole 25% EC @ 0.8ml/L", "frac_code": "19", "pre_harvest_interval_days": 11},
            {"active_formulation": "Azoxystrobin 23% SC @ 1.0ml/L", "frac_code": "M4", "pre_harvest_interval_days": 13}
        ],
        "organic_biocontrol_protocol": [
            "Trichoderma viride root dip and foliar spray",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0160",
        "disease_name": "Powdery Mildew of Chilli / Tomato (Variant Strain 11)",
        "causal_organism": "Leveillula taurica",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "White powdery fungal growth on leaf undersides with yellowing above",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 21.0,
            "favorable_temperature_c_max": 35.0,
            "favorable_relative_humidity_pct": 94,
            "leaf_wetness_hours_threshold": 13
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Hexaconazole 5% SC @ 1.5ml/L", "frac_code": "20", "pre_harvest_interval_days": 12},
            {"active_formulation": "Wettable Sulphur 80% WP @ 2.5g/L", "frac_code": "M5", "pre_harvest_interval_days": 14}
        ],
        "organic_biocontrol_protocol": [
            "Ampelomyces quisqualis bio-fungicide",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0161",
        "disease_name": "Sheath Blight of Paddy / Damping Off (Variant Strain 11)",
        "causal_organism": "Rhizoctonia solani",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Snake-skin banded lesions on leaf sheaths near water line",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 22.0,
            "favorable_temperature_c_max": 28.0,
            "favorable_relative_humidity_pct": 75,
            "leaf_wetness_hours_threshold": 6
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Validamycin 3% L @ 2.0ml/L", "frac_code": "1", "pre_harvest_interval_days": 13},
            {"active_formulation": "Hexaconazole 5% EC @ 2.0ml/L", "frac_code": "M1", "pre_harvest_interval_days": 5}
        ],
        "organic_biocontrol_protocol": [
            "Pseudomonas seed dressing @ 10g/kg",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0162",
        "disease_name": "Bacterial Wilt of Solanaceous Crops (Variant Strain 11)",
        "causal_organism": "Ralstonia solanacearum",
        "pathogen_class": "Bacteria",
        "diagnostic_symptoms": "Sudden daytime wilting of plant without foliage yellowing",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 23.0,
            "favorable_temperature_c_max": 29.0,
            "favorable_relative_humidity_pct": 76,
            "leaf_wetness_hours_threshold": 7
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Copper Oxychloride drenching @ 3.0g/L", "frac_code": "2", "pre_harvest_interval_days": 14},
            {"active_formulation": "Streptocycline drenching @ 0.2g/L", "frac_code": "M2", "pre_harvest_interval_days": 6}
        ],
        "organic_biocontrol_protocol": [
            "Bio-enrichment of soil with Trichoderma + FYM",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0163",
        "disease_name": "Fusarium Vascular Wilt (Variant Strain 11)",
        "causal_organism": "Fusarium oxysporum",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Vascular browning inside stem xylem and lower leaf chlorosis",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 18.0,
            "favorable_temperature_c_max": 30.0,
            "favorable_relative_humidity_pct": 77,
            "leaf_wetness_hours_threshold": 8
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Carbendazim 50% WP @ 1.5g/L", "frac_code": "3", "pre_harvest_interval_days": 15},
            {"active_formulation": "Thiophanate Methyl 70% WP @ 1.5g/L", "frac_code": "M3", "pre_harvest_interval_days": 7}
        ],
        "organic_biocontrol_protocol": [
            "Trichoderma harzianum @ 10g/L root zone drench",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0164",
        "disease_name": "Tomato Leaf Curl Begomovirus (ToLCV) (Variant Strain 11)",
        "causal_organism": "Bemisia tabaci",
        "pathogen_class": "Insect Vector",
        "diagnostic_symptoms": "Severe curling, puckering, reduction in leaf lamina size, stunting",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 19.0,
            "favorable_temperature_c_max": 31.0,
            "favorable_relative_humidity_pct": 78,
            "leaf_wetness_hours_threshold": 9
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Imidacloprid 17.8% SL @ 0.5ml/L", "frac_code": "4", "pre_harvest_interval_days": 16},
            {"active_formulation": "Acetamiprid 20% SP @ 0.3g/L", "frac_code": "M4", "pre_harvest_interval_days": 8}
        ],
        "organic_biocontrol_protocol": [
            "Fine insect netting (40 mesh) + Neem extract",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0165",
        "disease_name": "Root Knot Nematode Complex (Variant Strain 11)",
        "causal_organism": "Meloidogyne incognita",
        "pathogen_class": "Nematode",
        "diagnostic_symptoms": "Severe root galling, stunting, chlorosis and nutrient starvation",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 20.0,
            "favorable_temperature_c_max": 32.0,
            "favorable_relative_humidity_pct": 79,
            "leaf_wetness_hours_threshold": 10
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Fluopyram 34.48% SC @ 2.0ml/m2", "frac_code": "5", "pre_harvest_interval_days": 17},
            {"active_formulation": "Carbofuran 3% CG @ 10kg/acre", "frac_code": "M5", "pre_harvest_interval_days": 9}
        ],
        "organic_biocontrol_protocol": [
            "Paecilomyces lilacinus bio-nematicide @ 5kg/acre",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0166",
        "disease_name": "Tomato / Potato Early Blight (Variant Strain 12)",
        "causal_organism": "Alternaria solani",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Foliar target-like concentric rings with yellow halo",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 21.0,
            "favorable_temperature_c_max": 33.0,
            "favorable_relative_humidity_pct": 80,
            "leaf_wetness_hours_threshold": 11
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Mancozeb 75% WP @ 2.5g/L", "frac_code": "6", "pre_harvest_interval_days": 18},
            {"active_formulation": "Copper Oxychloride @ 2.5g/L", "frac_code": "M1", "pre_harvest_interval_days": 10}
        ],
        "organic_biocontrol_protocol": [
            "Trichoderma harzianum @ 5g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0167",
        "disease_name": "Late Blight of Tomato / Potato (Variant Strain 12)",
        "causal_organism": "Phytophthora infestans",
        "pathogen_class": "Oomycete",
        "diagnostic_symptoms": "Rapid water-soaked necrotic lesions with white downy mold",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 22.0,
            "favorable_temperature_c_max": 34.0,
            "favorable_relative_humidity_pct": 81,
            "leaf_wetness_hours_threshold": 12
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Metalaxyl 8% + Mancozeb 64% WP @ 2.5g/L", "frac_code": "7", "pre_harvest_interval_days": 19},
            {"active_formulation": "Dimethomorph 50% WP @ 1.0g/L", "frac_code": "M2", "pre_harvest_interval_days": 11}
        ],
        "organic_biocontrol_protocol": [
            "Bacillus subtilis @ 3ml/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0168",
        "disease_name": "Rice Bacterial Leaf Blight (Variant Strain 12)",
        "causal_organism": "Xanthomonas oryzae",
        "pathogen_class": "Bacteria",
        "diagnostic_symptoms": "Straw yellow undulating leaf tip lesions with amber bacterial ooze",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 23.0,
            "favorable_temperature_c_max": 35.0,
            "favorable_relative_humidity_pct": 82,
            "leaf_wetness_hours_threshold": 13
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Streptocycline 90% + Copper 50% WP @ 0.1g+2.5g/L", "frac_code": "8", "pre_harvest_interval_days": 20},
            {"active_formulation": "Kasugamycin 3% SL @ 2.0ml/L", "frac_code": "M3", "pre_harvest_interval_days": 12}
        ],
        "organic_biocontrol_protocol": [
            "Pseudomonas fluorescens @ 2.5g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0169",
        "disease_name": "Rice Blast (Leaf, Node, Neck) (Variant Strain 12)",
        "causal_organism": "Magnaporthe oryzae",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Spindle / Eye-shaped diamond lesions with greyish center and brown border",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 18.0,
            "favorable_temperature_c_max": 28.0,
            "favorable_relative_humidity_pct": 83,
            "leaf_wetness_hours_threshold": 6
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Tricyclazole 75% WP @ 0.6g/L", "frac_code": "9", "pre_harvest_interval_days": 7},
            {"active_formulation": "Isoprothiolane 40% EC @ 1.5ml/L", "frac_code": "M4", "pre_harvest_interval_days": 13}
        ],
        "organic_biocontrol_protocol": [
            "Neem Seed Kernel Extract 5%",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0170",
        "disease_name": "Wheat Yellow / Stripe Rust (Variant Strain 12)",
        "causal_organism": "Puccinia striiformis",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Parallel linear yellow pustules erupting along leaf lamina",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 19.0,
            "favorable_temperature_c_max": 29.0,
            "favorable_relative_humidity_pct": 84,
            "leaf_wetness_hours_threshold": 7
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Propiconazole 25% EC @ 1.0ml/L", "frac_code": "10", "pre_harvest_interval_days": 8},
            {"active_formulation": "Tebuconazole 25.9% EC @ 1.2ml/L", "frac_code": "M5", "pre_harvest_interval_days": 14}
        ],
        "organic_biocontrol_protocol": [
            "Bio-formulation T. viride @ 5g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0171",
        "disease_name": "Wheat Brown / Leaf Rust (Variant Strain 12)",
        "causal_organism": "Puccinia triticina",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Scattered spherical orange-brown uredinial pustules",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 20.0,
            "favorable_temperature_c_max": 30.0,
            "favorable_relative_humidity_pct": 85,
            "leaf_wetness_hours_threshold": 8
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Mancozeb 75% WP @ 2.0g/L", "frac_code": "11", "pre_harvest_interval_days": 9},
            {"active_formulation": "Propiconazole 25% EC @ 1.0ml/L", "frac_code": "M1", "pre_harvest_interval_days": 5}
        ],
        "organic_biocontrol_protocol": [
            "Sulphur 80% WDG @ 2.5g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0172",
        "disease_name": "Cotton Leaf Curl Virus (CLCuV) (Variant Strain 12)",
        "causal_organism": "Begomovirus / Whitefly",
        "pathogen_class": "Viral Complex",
        "diagnostic_symptoms": "Upward leaf cupping, thickened dark green veins and enations",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 21.0,
            "favorable_temperature_c_max": 31.0,
            "favorable_relative_humidity_pct": 86,
            "leaf_wetness_hours_threshold": 9
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Diafenthiuron 50% WP @ 1.2g/L", "frac_code": "12", "pre_harvest_interval_days": 10},
            {"active_formulation": "Pyriproxyfen 10% EC @ 2.0ml/L", "frac_code": "M2", "pre_harvest_interval_days": 6}
        ],
        "organic_biocontrol_protocol": [
            "Yellow Sticky Traps @ 20/acre + Neem Oil 10000ppm",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0173",
        "disease_name": "Maize Fall Armyworm (Variant Strain 12)",
        "causal_organism": "Spodoptera frugiperda",
        "pathogen_class": "Insect Pest",
        "diagnostic_symptoms": "Ragged shot-holes and sawdust larval frass packed in whorl",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 22.0,
            "favorable_temperature_c_max": 32.0,
            "favorable_relative_humidity_pct": 87,
            "leaf_wetness_hours_threshold": 10
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Emamectin Benzoate 5% SG @ 0.4g/L", "frac_code": "13", "pre_harvest_interval_days": 11},
            {"active_formulation": "Chlorantraniliprole 18.5% SC @ 0.3ml/L", "frac_code": "M3", "pre_harvest_interval_days": 7}
        ],
        "organic_biocontrol_protocol": [
            "Bacillus thuringiensis (Bt) kurstaki @ 2g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0174",
        "disease_name": "Chilli Anthracnose & Fruit Rot (Variant Strain 12)",
        "causal_organism": "Colletotrichum capsici",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Sunken circular dark lesions with salmon-pink spores on ripe pods",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 23.0,
            "favorable_temperature_c_max": 33.0,
            "favorable_relative_humidity_pct": 88,
            "leaf_wetness_hours_threshold": 11
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Difenoconazole 25% EC @ 0.8ml/L", "frac_code": "14", "pre_harvest_interval_days": 12},
            {"active_formulation": "Azoxystrobin 23% SC @ 1.0ml/L", "frac_code": "M4", "pre_harvest_interval_days": 8}
        ],
        "organic_biocontrol_protocol": [
            "Trichoderma viride root dip and foliar spray",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0175",
        "disease_name": "Powdery Mildew of Chilli / Tomato (Variant Strain 12)",
        "causal_organism": "Leveillula taurica",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "White powdery fungal growth on leaf undersides with yellowing above",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 18.0,
            "favorable_temperature_c_max": 34.0,
            "favorable_relative_humidity_pct": 89,
            "leaf_wetness_hours_threshold": 12
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Hexaconazole 5% SC @ 1.5ml/L", "frac_code": "15", "pre_harvest_interval_days": 13},
            {"active_formulation": "Wettable Sulphur 80% WP @ 2.5g/L", "frac_code": "M5", "pre_harvest_interval_days": 9}
        ],
        "organic_biocontrol_protocol": [
            "Ampelomyces quisqualis bio-fungicide",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0176",
        "disease_name": "Sheath Blight of Paddy / Damping Off (Variant Strain 12)",
        "causal_organism": "Rhizoctonia solani",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Snake-skin banded lesions on leaf sheaths near water line",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 19.0,
            "favorable_temperature_c_max": 35.0,
            "favorable_relative_humidity_pct": 90,
            "leaf_wetness_hours_threshold": 13
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Validamycin 3% L @ 2.0ml/L", "frac_code": "16", "pre_harvest_interval_days": 14},
            {"active_formulation": "Hexaconazole 5% EC @ 2.0ml/L", "frac_code": "M1", "pre_harvest_interval_days": 10}
        ],
        "organic_biocontrol_protocol": [
            "Pseudomonas seed dressing @ 10g/kg",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0177",
        "disease_name": "Bacterial Wilt of Solanaceous Crops (Variant Strain 12)",
        "causal_organism": "Ralstonia solanacearum",
        "pathogen_class": "Bacteria",
        "diagnostic_symptoms": "Sudden daytime wilting of plant without foliage yellowing",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 20.0,
            "favorable_temperature_c_max": 28.0,
            "favorable_relative_humidity_pct": 91,
            "leaf_wetness_hours_threshold": 6
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Copper Oxychloride drenching @ 3.0g/L", "frac_code": "17", "pre_harvest_interval_days": 15},
            {"active_formulation": "Streptocycline drenching @ 0.2g/L", "frac_code": "M2", "pre_harvest_interval_days": 11}
        ],
        "organic_biocontrol_protocol": [
            "Bio-enrichment of soil with Trichoderma + FYM",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0178",
        "disease_name": "Fusarium Vascular Wilt (Variant Strain 12)",
        "causal_organism": "Fusarium oxysporum",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Vascular browning inside stem xylem and lower leaf chlorosis",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 21.0,
            "favorable_temperature_c_max": 29.0,
            "favorable_relative_humidity_pct": 92,
            "leaf_wetness_hours_threshold": 7
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Carbendazim 50% WP @ 1.5g/L", "frac_code": "18", "pre_harvest_interval_days": 16},
            {"active_formulation": "Thiophanate Methyl 70% WP @ 1.5g/L", "frac_code": "M3", "pre_harvest_interval_days": 12}
        ],
        "organic_biocontrol_protocol": [
            "Trichoderma harzianum @ 10g/L root zone drench",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0179",
        "disease_name": "Tomato Leaf Curl Begomovirus (ToLCV) (Variant Strain 12)",
        "causal_organism": "Bemisia tabaci",
        "pathogen_class": "Insect Vector",
        "diagnostic_symptoms": "Severe curling, puckering, reduction in leaf lamina size, stunting",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 22.0,
            "favorable_temperature_c_max": 30.0,
            "favorable_relative_humidity_pct": 93,
            "leaf_wetness_hours_threshold": 8
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Imidacloprid 17.8% SL @ 0.5ml/L", "frac_code": "19", "pre_harvest_interval_days": 17},
            {"active_formulation": "Acetamiprid 20% SP @ 0.3g/L", "frac_code": "M4", "pre_harvest_interval_days": 13}
        ],
        "organic_biocontrol_protocol": [
            "Fine insect netting (40 mesh) + Neem extract",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0180",
        "disease_name": "Root Knot Nematode Complex (Variant Strain 12)",
        "causal_organism": "Meloidogyne incognita",
        "pathogen_class": "Nematode",
        "diagnostic_symptoms": "Severe root galling, stunting, chlorosis and nutrient starvation",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 23.0,
            "favorable_temperature_c_max": 31.0,
            "favorable_relative_humidity_pct": 94,
            "leaf_wetness_hours_threshold": 9
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Fluopyram 34.48% SC @ 2.0ml/m2", "frac_code": "20", "pre_harvest_interval_days": 18},
            {"active_formulation": "Carbofuran 3% CG @ 10kg/acre", "frac_code": "M5", "pre_harvest_interval_days": 14}
        ],
        "organic_biocontrol_protocol": [
            "Paecilomyces lilacinus bio-nematicide @ 5kg/acre",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0181",
        "disease_name": "Tomato / Potato Early Blight (Variant Strain 13)",
        "causal_organism": "Alternaria solani",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Foliar target-like concentric rings with yellow halo",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 18.0,
            "favorable_temperature_c_max": 32.0,
            "favorable_relative_humidity_pct": 75,
            "leaf_wetness_hours_threshold": 10
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Mancozeb 75% WP @ 2.5g/L", "frac_code": "1", "pre_harvest_interval_days": 19},
            {"active_formulation": "Copper Oxychloride @ 2.5g/L", "frac_code": "M1", "pre_harvest_interval_days": 5}
        ],
        "organic_biocontrol_protocol": [
            "Trichoderma harzianum @ 5g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0182",
        "disease_name": "Late Blight of Tomato / Potato (Variant Strain 13)",
        "causal_organism": "Phytophthora infestans",
        "pathogen_class": "Oomycete",
        "diagnostic_symptoms": "Rapid water-soaked necrotic lesions with white downy mold",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 19.0,
            "favorable_temperature_c_max": 33.0,
            "favorable_relative_humidity_pct": 76,
            "leaf_wetness_hours_threshold": 11
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Metalaxyl 8% + Mancozeb 64% WP @ 2.5g/L", "frac_code": "2", "pre_harvest_interval_days": 20},
            {"active_formulation": "Dimethomorph 50% WP @ 1.0g/L", "frac_code": "M2", "pre_harvest_interval_days": 6}
        ],
        "organic_biocontrol_protocol": [
            "Bacillus subtilis @ 3ml/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0183",
        "disease_name": "Rice Bacterial Leaf Blight (Variant Strain 13)",
        "causal_organism": "Xanthomonas oryzae",
        "pathogen_class": "Bacteria",
        "diagnostic_symptoms": "Straw yellow undulating leaf tip lesions with amber bacterial ooze",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 20.0,
            "favorable_temperature_c_max": 34.0,
            "favorable_relative_humidity_pct": 77,
            "leaf_wetness_hours_threshold": 12
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Streptocycline 90% + Copper 50% WP @ 0.1g+2.5g/L", "frac_code": "3", "pre_harvest_interval_days": 7},
            {"active_formulation": "Kasugamycin 3% SL @ 2.0ml/L", "frac_code": "M3", "pre_harvest_interval_days": 7}
        ],
        "organic_biocontrol_protocol": [
            "Pseudomonas fluorescens @ 2.5g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0184",
        "disease_name": "Rice Blast (Leaf, Node, Neck) (Variant Strain 13)",
        "causal_organism": "Magnaporthe oryzae",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Spindle / Eye-shaped diamond lesions with greyish center and brown border",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 21.0,
            "favorable_temperature_c_max": 35.0,
            "favorable_relative_humidity_pct": 78,
            "leaf_wetness_hours_threshold": 13
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Tricyclazole 75% WP @ 0.6g/L", "frac_code": "4", "pre_harvest_interval_days": 8},
            {"active_formulation": "Isoprothiolane 40% EC @ 1.5ml/L", "frac_code": "M4", "pre_harvest_interval_days": 8}
        ],
        "organic_biocontrol_protocol": [
            "Neem Seed Kernel Extract 5%",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0185",
        "disease_name": "Wheat Yellow / Stripe Rust (Variant Strain 13)",
        "causal_organism": "Puccinia striiformis",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Parallel linear yellow pustules erupting along leaf lamina",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 22.0,
            "favorable_temperature_c_max": 28.0,
            "favorable_relative_humidity_pct": 79,
            "leaf_wetness_hours_threshold": 6
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Propiconazole 25% EC @ 1.0ml/L", "frac_code": "5", "pre_harvest_interval_days": 9},
            {"active_formulation": "Tebuconazole 25.9% EC @ 1.2ml/L", "frac_code": "M5", "pre_harvest_interval_days": 9}
        ],
        "organic_biocontrol_protocol": [
            "Bio-formulation T. viride @ 5g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0186",
        "disease_name": "Wheat Brown / Leaf Rust (Variant Strain 13)",
        "causal_organism": "Puccinia triticina",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Scattered spherical orange-brown uredinial pustules",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 23.0,
            "favorable_temperature_c_max": 29.0,
            "favorable_relative_humidity_pct": 80,
            "leaf_wetness_hours_threshold": 7
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Mancozeb 75% WP @ 2.0g/L", "frac_code": "6", "pre_harvest_interval_days": 10},
            {"active_formulation": "Propiconazole 25% EC @ 1.0ml/L", "frac_code": "M1", "pre_harvest_interval_days": 10}
        ],
        "organic_biocontrol_protocol": [
            "Sulphur 80% WDG @ 2.5g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0187",
        "disease_name": "Cotton Leaf Curl Virus (CLCuV) (Variant Strain 13)",
        "causal_organism": "Begomovirus / Whitefly",
        "pathogen_class": "Viral Complex",
        "diagnostic_symptoms": "Upward leaf cupping, thickened dark green veins and enations",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 18.0,
            "favorable_temperature_c_max": 30.0,
            "favorable_relative_humidity_pct": 81,
            "leaf_wetness_hours_threshold": 8
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Diafenthiuron 50% WP @ 1.2g/L", "frac_code": "7", "pre_harvest_interval_days": 11},
            {"active_formulation": "Pyriproxyfen 10% EC @ 2.0ml/L", "frac_code": "M2", "pre_harvest_interval_days": 11}
        ],
        "organic_biocontrol_protocol": [
            "Yellow Sticky Traps @ 20/acre + Neem Oil 10000ppm",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0188",
        "disease_name": "Maize Fall Armyworm (Variant Strain 13)",
        "causal_organism": "Spodoptera frugiperda",
        "pathogen_class": "Insect Pest",
        "diagnostic_symptoms": "Ragged shot-holes and sawdust larval frass packed in whorl",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 19.0,
            "favorable_temperature_c_max": 31.0,
            "favorable_relative_humidity_pct": 82,
            "leaf_wetness_hours_threshold": 9
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Emamectin Benzoate 5% SG @ 0.4g/L", "frac_code": "8", "pre_harvest_interval_days": 12},
            {"active_formulation": "Chlorantraniliprole 18.5% SC @ 0.3ml/L", "frac_code": "M3", "pre_harvest_interval_days": 12}
        ],
        "organic_biocontrol_protocol": [
            "Bacillus thuringiensis (Bt) kurstaki @ 2g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0189",
        "disease_name": "Chilli Anthracnose & Fruit Rot (Variant Strain 13)",
        "causal_organism": "Colletotrichum capsici",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Sunken circular dark lesions with salmon-pink spores on ripe pods",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 20.0,
            "favorable_temperature_c_max": 32.0,
            "favorable_relative_humidity_pct": 83,
            "leaf_wetness_hours_threshold": 10
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Difenoconazole 25% EC @ 0.8ml/L", "frac_code": "9", "pre_harvest_interval_days": 13},
            {"active_formulation": "Azoxystrobin 23% SC @ 1.0ml/L", "frac_code": "M4", "pre_harvest_interval_days": 13}
        ],
        "organic_biocontrol_protocol": [
            "Trichoderma viride root dip and foliar spray",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0190",
        "disease_name": "Powdery Mildew of Chilli / Tomato (Variant Strain 13)",
        "causal_organism": "Leveillula taurica",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "White powdery fungal growth on leaf undersides with yellowing above",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 21.0,
            "favorable_temperature_c_max": 33.0,
            "favorable_relative_humidity_pct": 84,
            "leaf_wetness_hours_threshold": 11
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Hexaconazole 5% SC @ 1.5ml/L", "frac_code": "10", "pre_harvest_interval_days": 14},
            {"active_formulation": "Wettable Sulphur 80% WP @ 2.5g/L", "frac_code": "M5", "pre_harvest_interval_days": 14}
        ],
        "organic_biocontrol_protocol": [
            "Ampelomyces quisqualis bio-fungicide",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0191",
        "disease_name": "Sheath Blight of Paddy / Damping Off (Variant Strain 13)",
        "causal_organism": "Rhizoctonia solani",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Snake-skin banded lesions on leaf sheaths near water line",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 22.0,
            "favorable_temperature_c_max": 34.0,
            "favorable_relative_humidity_pct": 85,
            "leaf_wetness_hours_threshold": 12
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Validamycin 3% L @ 2.0ml/L", "frac_code": "11", "pre_harvest_interval_days": 15},
            {"active_formulation": "Hexaconazole 5% EC @ 2.0ml/L", "frac_code": "M1", "pre_harvest_interval_days": 5}
        ],
        "organic_biocontrol_protocol": [
            "Pseudomonas seed dressing @ 10g/kg",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0192",
        "disease_name": "Bacterial Wilt of Solanaceous Crops (Variant Strain 13)",
        "causal_organism": "Ralstonia solanacearum",
        "pathogen_class": "Bacteria",
        "diagnostic_symptoms": "Sudden daytime wilting of plant without foliage yellowing",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 23.0,
            "favorable_temperature_c_max": 35.0,
            "favorable_relative_humidity_pct": 86,
            "leaf_wetness_hours_threshold": 13
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Copper Oxychloride drenching @ 3.0g/L", "frac_code": "12", "pre_harvest_interval_days": 16},
            {"active_formulation": "Streptocycline drenching @ 0.2g/L", "frac_code": "M2", "pre_harvest_interval_days": 6}
        ],
        "organic_biocontrol_protocol": [
            "Bio-enrichment of soil with Trichoderma + FYM",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0193",
        "disease_name": "Fusarium Vascular Wilt (Variant Strain 13)",
        "causal_organism": "Fusarium oxysporum",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Vascular browning inside stem xylem and lower leaf chlorosis",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 18.0,
            "favorable_temperature_c_max": 28.0,
            "favorable_relative_humidity_pct": 87,
            "leaf_wetness_hours_threshold": 6
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Carbendazim 50% WP @ 1.5g/L", "frac_code": "13", "pre_harvest_interval_days": 17},
            {"active_formulation": "Thiophanate Methyl 70% WP @ 1.5g/L", "frac_code": "M3", "pre_harvest_interval_days": 7}
        ],
        "organic_biocontrol_protocol": [
            "Trichoderma harzianum @ 10g/L root zone drench",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0194",
        "disease_name": "Tomato Leaf Curl Begomovirus (ToLCV) (Variant Strain 13)",
        "causal_organism": "Bemisia tabaci",
        "pathogen_class": "Insect Vector",
        "diagnostic_symptoms": "Severe curling, puckering, reduction in leaf lamina size, stunting",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 19.0,
            "favorable_temperature_c_max": 29.0,
            "favorable_relative_humidity_pct": 88,
            "leaf_wetness_hours_threshold": 7
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Imidacloprid 17.8% SL @ 0.5ml/L", "frac_code": "14", "pre_harvest_interval_days": 18},
            {"active_formulation": "Acetamiprid 20% SP @ 0.3g/L", "frac_code": "M4", "pre_harvest_interval_days": 8}
        ],
        "organic_biocontrol_protocol": [
            "Fine insect netting (40 mesh) + Neem extract",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0195",
        "disease_name": "Root Knot Nematode Complex (Variant Strain 13)",
        "causal_organism": "Meloidogyne incognita",
        "pathogen_class": "Nematode",
        "diagnostic_symptoms": "Severe root galling, stunting, chlorosis and nutrient starvation",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 20.0,
            "favorable_temperature_c_max": 30.0,
            "favorable_relative_humidity_pct": 89,
            "leaf_wetness_hours_threshold": 8
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Fluopyram 34.48% SC @ 2.0ml/m2", "frac_code": "15", "pre_harvest_interval_days": 19},
            {"active_formulation": "Carbofuran 3% CG @ 10kg/acre", "frac_code": "M5", "pre_harvest_interval_days": 9}
        ],
        "organic_biocontrol_protocol": [
            "Paecilomyces lilacinus bio-nematicide @ 5kg/acre",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0196",
        "disease_name": "Tomato / Potato Early Blight (Variant Strain 14)",
        "causal_organism": "Alternaria solani",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Foliar target-like concentric rings with yellow halo",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 21.0,
            "favorable_temperature_c_max": 31.0,
            "favorable_relative_humidity_pct": 90,
            "leaf_wetness_hours_threshold": 9
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Mancozeb 75% WP @ 2.5g/L", "frac_code": "16", "pre_harvest_interval_days": 20},
            {"active_formulation": "Copper Oxychloride @ 2.5g/L", "frac_code": "M1", "pre_harvest_interval_days": 10}
        ],
        "organic_biocontrol_protocol": [
            "Trichoderma harzianum @ 5g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0197",
        "disease_name": "Late Blight of Tomato / Potato (Variant Strain 14)",
        "causal_organism": "Phytophthora infestans",
        "pathogen_class": "Oomycete",
        "diagnostic_symptoms": "Rapid water-soaked necrotic lesions with white downy mold",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 22.0,
            "favorable_temperature_c_max": 32.0,
            "favorable_relative_humidity_pct": 91,
            "leaf_wetness_hours_threshold": 10
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Metalaxyl 8% + Mancozeb 64% WP @ 2.5g/L", "frac_code": "17", "pre_harvest_interval_days": 7},
            {"active_formulation": "Dimethomorph 50% WP @ 1.0g/L", "frac_code": "M2", "pre_harvest_interval_days": 11}
        ],
        "organic_biocontrol_protocol": [
            "Bacillus subtilis @ 3ml/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0198",
        "disease_name": "Rice Bacterial Leaf Blight (Variant Strain 14)",
        "causal_organism": "Xanthomonas oryzae",
        "pathogen_class": "Bacteria",
        "diagnostic_symptoms": "Straw yellow undulating leaf tip lesions with amber bacterial ooze",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 23.0,
            "favorable_temperature_c_max": 33.0,
            "favorable_relative_humidity_pct": 92,
            "leaf_wetness_hours_threshold": 11
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Streptocycline 90% + Copper 50% WP @ 0.1g+2.5g/L", "frac_code": "18", "pre_harvest_interval_days": 8},
            {"active_formulation": "Kasugamycin 3% SL @ 2.0ml/L", "frac_code": "M3", "pre_harvest_interval_days": 12}
        ],
        "organic_biocontrol_protocol": [
            "Pseudomonas fluorescens @ 2.5g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0199",
        "disease_name": "Rice Blast (Leaf, Node, Neck) (Variant Strain 14)",
        "causal_organism": "Magnaporthe oryzae",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Spindle / Eye-shaped diamond lesions with greyish center and brown border",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 18.0,
            "favorable_temperature_c_max": 34.0,
            "favorable_relative_humidity_pct": 93,
            "leaf_wetness_hours_threshold": 12
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Tricyclazole 75% WP @ 0.6g/L", "frac_code": "19", "pre_harvest_interval_days": 9},
            {"active_formulation": "Isoprothiolane 40% EC @ 1.5ml/L", "frac_code": "M4", "pre_harvest_interval_days": 13}
        ],
        "organic_biocontrol_protocol": [
            "Neem Seed Kernel Extract 5%",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
    {
        "pathology_id": "PATH-0200",
        "disease_name": "Wheat Yellow / Stripe Rust (Variant Strain 14)",
        "causal_organism": "Puccinia striiformis",
        "pathogen_class": "Fungus",
        "diagnostic_symptoms": "Parallel linear yellow pustules erupting along leaf lamina",
        "epidemiology_triggers": {
            "favorable_temperature_c_min": 19.0,
            "favorable_temperature_c_max": 35.0,
            "favorable_relative_humidity_pct": 94,
            "leaf_wetness_hours_threshold": 13
        },
        "chemical_intervention_protocol": [
            {"active_formulation": "Propiconazole 25% EC @ 1.0ml/L", "frac_code": "20", "pre_harvest_interval_days": 10},
            {"active_formulation": "Tebuconazole 25.9% EC @ 1.2ml/L", "frac_code": "M5", "pre_harvest_interval_days": 14}
        ],
        "organic_biocontrol_protocol": [
            "Bio-formulation T. viride @ 5g/L",
            "Foliar spray with Panchagavya 3% + Neem oil 5ml/L at 10-day intervals",
            "Soil incorporation of enriched Vermicompost with Pseudomonas fluorescens"
        ],
        "integrated_cultural_practices": [
            "Sanitize pruning tools with 10% Sodium Hypochlorite",
            "Ensure wide crop row spacing to maximize solar penetration and air circulation",
            "Destroy and burn all infected crop residues immediately post-harvest"
        ]
    },
]
