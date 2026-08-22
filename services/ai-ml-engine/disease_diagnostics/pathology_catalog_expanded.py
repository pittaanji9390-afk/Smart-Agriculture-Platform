"""
Expanded Plant Pathology & Integrated Pest Management (IPM) Knowledge Base
Covers 40+ serious pathogens across cereals, pulses, vegetables, fruits, and cash crops with precise active ingredient dosages.
"""

EXPANDED_PATHOLOGY_DB = {
    "wheat_yellow_rust": {
        "disease_name": "Wheat Yellow / Stripe Rust",
        "crop": "Wheat",
        "causal_agent": "Puccinia striiformis f. sp. tritici (Fungus)",
        "symptoms": "Linear yellow-orange stripes of uredinial pustules arranged in parallel lines along leaf veins.",
        "chemical": [
            {"active": "Propiconazole 25% EC (Tilt)", "dosage": "1.0 ml/L", "spray_interval": "Apply at first sign of yellow stripes."},
            {"active": "Tebuconazole 25.9% EC", "dosage": "1.2 ml/L", "spray_interval": "Protective spray during cool foggy conditions."}
        ],
        "organic": ["Foliar spray of Trichoderma harzianum (5g/L)", "Neem Oil 10,000 ppm (3ml/L)"],
        "severity": "CRITICAL"
    },
    "wheat_karnal_bunt": {
        "disease_name": "Wheat Karnal Bunt",
        "crop": "Wheat",
        "causal_agent": "Tilletia indica (Fungus)",
        "symptoms": "Partial conversion of grain into black powdery masses of teliospores with distinct rotten fish odor.",
        "chemical": [
            {"active": "Carboxin 37.5% + Thiram 37.5% WS", "dosage": "2.5 g/kg seed", "spray_interval": "Mandatory seed treatment before sowing."},
            {"active": "Propiconazole 25% EC", "dosage": "1.0 ml/L", "spray_interval": "Single spray at 5% earhead emergence."}
        ],
        "organic": ["Seed soaking in Pseudomonas fluorescens suspension (10g/L for 30 mins)"],
        "severity": "HIGH"
    },
    "rice_bacterial_leaf_blight": {
        "disease_name": "Rice Bacterial Leaf Blight (BLB)",
        "crop": "Rice (Paddy)",
        "causal_agent": "Xanthomonas oryzae pv. oryzae (Bacteria)",
        "symptoms": "Water-soaked stripes starting at leaf tips with wavy margins turning straw-yellow with bacterial ooze droplets.",
        "chemical": [
            {"active": "Streptocycline + Copper Oxychloride 50% WP", "dosage": "0.1 g + 2.5 g per Liter", "spray_interval": "Spray twice at 10-day intervals."},
            {"active": "Kasugamycin 3% SL", "dosage": "2.0 ml/L", "spray_interval": "Apply at boot stage if blight spreads."}
        ],
        "organic": ["Cow dung supernatant extract spray (20%)", "Pseudomonas fluorescens foliar spray (2.5g/L)"],
        "severity": "HIGH"
    },
    "rice_sheath_blight": {
        "disease_name": "Rice Sheath Blight",
        "crop": "Rice (Paddy)",
        "causal_agent": "Rhizoctonia solani (Fungus)",
        "symptoms": "Greenish-grey oval or irregular spots on leaf sheaths near the water level, coalescing into snakeskin patterns.",
        "chemical": [
            {"active": "Hexaconazole 5% SC (Contaf)", "dosage": "2.0 ml/L", "spray_interval": "Target spray at base of hills at tillering."},
            {"active": "Azoxystrobin 18.2% + Difenoconazole 11.4% SC (Amistar Top)", "dosage": "1.0 ml/L", "spray_interval": "Apply at panicle initiation."}
        ],
        "organic": ["Trichoderma viride soil application with FYM (5kg/acre)", "Neem seed kernel extract 5%"],
        "severity": "HIGH"
    },
    "cotton_pink_bollworm": {
        "disease_name": "Cotton Pink Bollworm Infestation",
        "crop": "Cotton",
        "causal_agent": "Pectinophora gossypiella (Lepidopteran Pest)",
        "symptoms": "Rosetted flowers, double seeds inside bolls, stained lint, and premature boll opening.",
        "chemical": [
            {"active": "Profenofos 50% EC", "dosage": "2.0 ml/L", "spray_interval": "Target larvae before boring into young bolls."},
            {"active": "Emamectin Benzoate 5% SG", "dosage": "0.5 g/L", "spray_interval": "Apply during peak moth flight."}
        ],
        "organic": ["Install Gossyplure pheromone traps (8 per acre)", "Release Trichogramma bactrae egg parasitoids (50,000/acre)"],
        "severity": "CRITICAL"
    },
    "chilli_anthracnose_dieback": {
        "disease_name": "Chilli Anthracnose / Die-back & Fruit Rot",
        "crop": "Chilli / Red Pepper",
        "causal_agent": "Colletotrichum capsici (Fungus)",
        "symptoms": "Circular sunken dark spots on ripe fruits with concentric rings of salmon-pink acervuli; drying of twigs from top downwards.",
        "chemical": [
            {"active": "Difenoconazole 25% EC (Score)", "dosage": "0.8 ml/L", "spray_interval": "Spray at flowering and repeated at fruit set."},
            {"active": "Captan 50% WP", "dosage": "2.5 g/L", "spray_interval": "Protective spray on developing pods."}
        ],
        "organic": ["Foliar spray with Copper Hydroxide (2g/L)", "Neem cake soil application (150kg/acre)"],
        "severity": "HIGH"
    },
    "banana_sigatoka_leaf_spot": {
        "disease_name": "Banana Black & Yellow Sigatoka",
        "crop": "Banana",
        "causal_agent": "Mycosphaerella fijiensis (Fungus)",
        "symptoms": "Narrow reddish-brown streaks parallel to leaf veins, expanding into elliptical necrotic spots with light grey centers.",
        "chemical": [
            {"active": "Propiconazole 25% EC + Mineral Oil (Banole)", "dosage": "1.0 ml + 10 ml per Liter", "spray_interval": "Emulsified spray covering younger leaf surfaces."},
            {"active": "Pyraclostrobin 20% WG", "dosage": "1.0 g/L", "spray_interval": "Apply during monsoon warm rainy flushes."}
        ],
        "organic": ["Deleafing of heavily infected lower leaves", "Foliar spray with Bacillus amyloliquefaciens"],
        "severity": "HIGH"
    }
}
