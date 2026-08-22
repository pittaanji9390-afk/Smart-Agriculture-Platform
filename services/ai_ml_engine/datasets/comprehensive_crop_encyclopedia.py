"""
Comprehensive Agronomic Crop Dossiers & Cultivation Encyclopedia
"""
from typing import Dict, Any, List

COMPREHENSIVE_CROP_ENCYCLOPEDIA: List[Dict[str, Any]] = [
    {
        "crop_id": "CROP-0001",
        "crop_name": "Rice (Pusa Basmati 1121) - Select Genotype v1",
        "category": "Cereal",
        "growing_duration_days": 140,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 90,
            "phosphorus_kg_ha": 45,
            "potassium_kg_ha": 45,
            "sulfur_kg_ha": 15,
            "zinc_sulfate_kg_ha": 12.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 36,
            "optimum_temperature_c": 29.0,
            "min_ph": 5.5,
            "max_ph": 7.2,
            "min_annual_rainfall_mm": 1600,
            "max_annual_rainfall_mm": 3200
        },
        "production_economics": {
            "potential_yield_kg_acre": 2200,
            "benchmark_mandi_price_rs_qtl": 2400,
            "estimated_cost_cultivation_acre": 12000,
            "gross_return_acre": 52800
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1360.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0002",
        "crop_name": "Rice (Pusa Basmati 1509) - Select Genotype v1",
        "category": "Cereal",
        "growing_duration_days": 120,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 85,
            "phosphorus_kg_ha": 40,
            "potassium_kg_ha": 40,
            "sulfur_kg_ha": 16,
            "zinc_sulfate_kg_ha": 13.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 38,
            "optimum_temperature_c": 30.0,
            "min_ph": 5.5,
            "max_ph": 7.2,
            "min_annual_rainfall_mm": 1400,
            "max_annual_rainfall_mm": 2800
        },
        "production_economics": {
            "potential_yield_kg_acre": 2400,
            "benchmark_mandi_price_rs_qtl": 2500,
            "estimated_cost_cultivation_acre": 13000,
            "gross_return_acre": 60000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1190.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0003",
        "crop_name": "Rice (BPT 5204 / Samba Mahsuri) - Select Genotype v1",
        "category": "Cereal",
        "growing_duration_days": 150,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 100,
            "phosphorus_kg_ha": 50,
            "potassium_kg_ha": 50,
            "sulfur_kg_ha": 17,
            "zinc_sulfate_kg_ha": 14.5
        },
        "climate_envelope": {
            "min_temperature_c": 20,
            "max_temperature_c": 36,
            "optimum_temperature_c": 28.0,
            "min_ph": 6.0,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 1500,
            "max_annual_rainfall_mm": 3000
        },
        "production_economics": {
            "potential_yield_kg_acre": 2600,
            "benchmark_mandi_price_rs_qtl": 2700,
            "estimated_cost_cultivation_acre": 14000,
            "gross_return_acre": 70200
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1275.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0004",
        "crop_name": "Rice (MTU 1010 / Cottondora Sannalu) - Select Genotype v1",
        "category": "Cereal",
        "growing_duration_days": 125,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 18,
            "zinc_sulfate_kg_ha": 15.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 38,
            "optimum_temperature_c": 30.0,
            "min_ph": 5.5,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 1300,
            "max_annual_rainfall_mm": 2600
        },
        "production_economics": {
            "potential_yield_kg_acre": 3100,
            "benchmark_mandi_price_rs_qtl": 2200,
            "estimated_cost_cultivation_acre": 15000,
            "gross_return_acre": 68200
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1105.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0005",
        "crop_name": "Rice (IR 64 High Yield) - Select Genotype v1",
        "category": "Cereal",
        "growing_duration_days": 120,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 19,
            "zinc_sulfate_kg_ha": 16.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 38,
            "optimum_temperature_c": 30.0,
            "min_ph": 5.5,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 1400,
            "max_annual_rainfall_mm": 2800
        },
        "production_economics": {
            "potential_yield_kg_acre": 3200,
            "benchmark_mandi_price_rs_qtl": 2100,
            "estimated_cost_cultivation_acre": 16000,
            "gross_return_acre": 67200
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1190.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0006",
        "crop_name": "Wheat (HD 2967 High Yield) - Select Genotype v1",
        "category": "Cereal",
        "growing_duration_days": 125,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 20,
            "zinc_sulfate_kg_ha": 17.5
        },
        "climate_envelope": {
            "min_temperature_c": 12,
            "max_temperature_c": 25,
            "optimum_temperature_c": 18.5,
            "min_ph": 6.0,
            "max_ph": 7.8,
            "min_annual_rainfall_mm": 450,
            "max_annual_rainfall_mm": 900
        },
        "production_economics": {
            "potential_yield_kg_acre": 2400,
            "benchmark_mandi_price_rs_qtl": 2350,
            "estimated_cost_cultivation_acre": 17000,
            "gross_return_acre": 56400
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 382.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0007",
        "crop_name": "Wheat (HD 3086 Pusa Gautami) - Select Genotype v1",
        "category": "Cereal",
        "growing_duration_days": 120,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 21,
            "zinc_sulfate_kg_ha": 18.5
        },
        "climate_envelope": {
            "min_temperature_c": 12,
            "max_temperature_c": 26,
            "optimum_temperature_c": 19.0,
            "min_ph": 6.0,
            "max_ph": 7.8,
            "min_annual_rainfall_mm": 450,
            "max_annual_rainfall_mm": 900
        },
        "production_economics": {
            "potential_yield_kg_acre": 2500,
            "benchmark_mandi_price_rs_qtl": 2400,
            "estimated_cost_cultivation_acre": 18000,
            "gross_return_acre": 60000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 382.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0008",
        "crop_name": "Wheat (PBW 343 / Shriram 303) - Select Genotype v1",
        "category": "Cereal",
        "growing_duration_days": 130,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 130,
            "phosphorus_kg_ha": 65,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 22,
            "zinc_sulfate_kg_ha": 19.5
        },
        "climate_envelope": {
            "min_temperature_c": 10,
            "max_temperature_c": 24,
            "optimum_temperature_c": 17.0,
            "min_ph": 6.0,
            "max_ph": 7.8,
            "min_annual_rainfall_mm": 450,
            "max_annual_rainfall_mm": 900
        },
        "production_economics": {
            "potential_yield_kg_acre": 2600,
            "benchmark_mandi_price_rs_qtl": 2300,
            "estimated_cost_cultivation_acre": 19000,
            "gross_return_acre": 59800
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 382.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0009",
        "crop_name": "Wheat (DBW 187 Karan Vandana) - Select Genotype v1",
        "category": "Cereal",
        "growing_duration_days": 120,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 130,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 23,
            "zinc_sulfate_kg_ha": 20.5
        },
        "climate_envelope": {
            "min_temperature_c": 12,
            "max_temperature_c": 27,
            "optimum_temperature_c": 19.5,
            "min_ph": 6.0,
            "max_ph": 7.8,
            "min_annual_rainfall_mm": 400,
            "max_annual_rainfall_mm": 800
        },
        "production_economics": {
            "potential_yield_kg_acre": 2700,
            "benchmark_mandi_price_rs_qtl": 2500,
            "estimated_cost_cultivation_acre": 20000,
            "gross_return_acre": 67500
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 340.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0010",
        "crop_name": "Maize (Pioneer P3396 Hybrid) - Select Genotype v1",
        "category": "Cereal",
        "growing_duration_days": 110,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 140,
            "phosphorus_kg_ha": 65,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 24,
            "zinc_sulfate_kg_ha": 21.5
        },
        "climate_envelope": {
            "min_temperature_c": 18,
            "max_temperature_c": 35,
            "optimum_temperature_c": 26.5,
            "min_ph": 5.8,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 600,
            "max_annual_rainfall_mm": 1200
        },
        "production_economics": {
            "potential_yield_kg_acre": 3600,
            "benchmark_mandi_price_rs_qtl": 2150,
            "estimated_cost_cultivation_acre": 21000,
            "gross_return_acre": 77400
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 510.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0011",
        "crop_name": "Maize (Dekalb 9108 Plus) - Select Genotype v1",
        "category": "Cereal",
        "growing_duration_days": 105,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 130,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 55,
            "sulfur_kg_ha": 25,
            "zinc_sulfate_kg_ha": 22.5
        },
        "climate_envelope": {
            "min_temperature_c": 18,
            "max_temperature_c": 35,
            "optimum_temperature_c": 26.5,
            "min_ph": 5.8,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 550,
            "max_annual_rainfall_mm": 1100
        },
        "production_economics": {
            "potential_yield_kg_acre": 3400,
            "benchmark_mandi_price_rs_qtl": 2150,
            "estimated_cost_cultivation_acre": 22000,
            "gross_return_acre": 73100
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 467.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0012",
        "crop_name": "Maize (Syngenta NK 6240) - Select Genotype v1",
        "category": "Cereal",
        "growing_duration_days": 115,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 140,
            "phosphorus_kg_ha": 70,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 26,
            "zinc_sulfate_kg_ha": 23.5
        },
        "climate_envelope": {
            "min_temperature_c": 18,
            "max_temperature_c": 36,
            "optimum_temperature_c": 27.0,
            "min_ph": 5.8,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 600,
            "max_annual_rainfall_mm": 1200
        },
        "production_economics": {
            "potential_yield_kg_acre": 3800,
            "benchmark_mandi_price_rs_qtl": 2150,
            "estimated_cost_cultivation_acre": 23000,
            "gross_return_acre": 81700
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 510.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0013",
        "crop_name": "Sorghum (CSH 16 Grain Hybrid) - Select Genotype v1",
        "category": "Millet",
        "growing_duration_days": 105,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 80,
            "phosphorus_kg_ha": 40,
            "potassium_kg_ha": 40,
            "sulfur_kg_ha": 27,
            "zinc_sulfate_kg_ha": 24.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 38,
            "optimum_temperature_c": 30.0,
            "min_ph": 6.0,
            "max_ph": 8.2,
            "min_annual_rainfall_mm": 450,
            "max_annual_rainfall_mm": 900
        },
        "production_economics": {
            "potential_yield_kg_acre": 1600,
            "benchmark_mandi_price_rs_qtl": 2900,
            "estimated_cost_cultivation_acre": 24000,
            "gross_return_acre": 46400
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 382.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0014",
        "crop_name": "Pearl Millet (HHB 67 Improved) - Select Genotype v1",
        "category": "Millet",
        "growing_duration_days": 70,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 60,
            "phosphorus_kg_ha": 30,
            "potassium_kg_ha": 30,
            "sulfur_kg_ha": 28,
            "zinc_sulfate_kg_ha": 25.5
        },
        "climate_envelope": {
            "min_temperature_c": 25,
            "max_temperature_c": 42,
            "optimum_temperature_c": 33.5,
            "min_ph": 6.5,
            "max_ph": 8.5,
            "min_annual_rainfall_mm": 300,
            "max_annual_rainfall_mm": 600
        },
        "production_economics": {
            "potential_yield_kg_acre": 1200,
            "benchmark_mandi_price_rs_qtl": 2450,
            "estimated_cost_cultivation_acre": 25000,
            "gross_return_acre": 29400
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 255.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0015",
        "crop_name": "Finger Millet (GPU 28 Ragi) - Select Genotype v1",
        "category": "Millet",
        "growing_duration_days": 110,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 60,
            "phosphorus_kg_ha": 40,
            "potassium_kg_ha": 30,
            "sulfur_kg_ha": 29,
            "zinc_sulfate_kg_ha": 26.5
        },
        "climate_envelope": {
            "min_temperature_c": 18,
            "max_temperature_c": 34,
            "optimum_temperature_c": 26.0,
            "min_ph": 5.5,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 500,
            "max_annual_rainfall_mm": 1000
        },
        "production_economics": {
            "potential_yield_kg_acre": 1300,
            "benchmark_mandi_price_rs_qtl": 3800,
            "estimated_cost_cultivation_acre": 26000,
            "gross_return_acre": 49400
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 425.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0016",
        "crop_name": "Chickpea (JG 11 Desi Gram) - Select Genotype v1",
        "category": "Pulse",
        "growing_duration_days": 95,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 20,
            "phosphorus_kg_ha": 50,
            "potassium_kg_ha": 25,
            "sulfur_kg_ha": 30,
            "zinc_sulfate_kg_ha": 12.5
        },
        "climate_envelope": {
            "min_temperature_c": 15,
            "max_temperature_c": 28,
            "optimum_temperature_c": 21.5,
            "min_ph": 6.0,
            "max_ph": 8.0,
            "min_annual_rainfall_mm": 350,
            "max_annual_rainfall_mm": 700
        },
        "production_economics": {
            "potential_yield_kg_acre": 950,
            "benchmark_mandi_price_rs_qtl": 5400,
            "estimated_cost_cultivation_acre": 27000,
            "gross_return_acre": 51300
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 297.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0017",
        "crop_name": "Chickpea (KAK 2 Kabuli) - Select Genotype v1",
        "category": "Pulse",
        "growing_duration_days": 105,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 25,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 30,
            "sulfur_kg_ha": 31,
            "zinc_sulfate_kg_ha": 13.5
        },
        "climate_envelope": {
            "min_temperature_c": 14,
            "max_temperature_c": 27,
            "optimum_temperature_c": 20.5,
            "min_ph": 6.5,
            "max_ph": 8.2,
            "min_annual_rainfall_mm": 350,
            "max_annual_rainfall_mm": 700
        },
        "production_economics": {
            "potential_yield_kg_acre": 1100,
            "benchmark_mandi_price_rs_qtl": 11000,
            "estimated_cost_cultivation_acre": 28000,
            "gross_return_acre": 121000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 297.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0018",
        "crop_name": "Pigeon Pea (ICPL 87119 Asha) - Select Genotype v1",
        "category": "Pulse",
        "growing_duration_days": 170,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 25,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 30,
            "sulfur_kg_ha": 32,
            "zinc_sulfate_kg_ha": 14.5
        },
        "climate_envelope": {
            "min_temperature_c": 20,
            "max_temperature_c": 36,
            "optimum_temperature_c": 28.0,
            "min_ph": 6.5,
            "max_ph": 8.0,
            "min_annual_rainfall_mm": 700,
            "max_annual_rainfall_mm": 1400
        },
        "production_economics": {
            "potential_yield_kg_acre": 900,
            "benchmark_mandi_price_rs_qtl": 7500,
            "estimated_cost_cultivation_acre": 29000,
            "gross_return_acre": 67500
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 595.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0019",
        "crop_name": "Green Gram (IPM 02-3 / Samrat) - Select Genotype v1",
        "category": "Pulse",
        "growing_duration_days": 65,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 15,
            "phosphorus_kg_ha": 40,
            "potassium_kg_ha": 20,
            "sulfur_kg_ha": 33,
            "zinc_sulfate_kg_ha": 15.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 36,
            "optimum_temperature_c": 29.0,
            "min_ph": 6.2,
            "max_ph": 7.8,
            "min_annual_rainfall_mm": 400,
            "max_annual_rainfall_mm": 800
        },
        "production_economics": {
            "potential_yield_kg_acre": 650,
            "benchmark_mandi_price_rs_qtl": 8500,
            "estimated_cost_cultivation_acre": 12000,
            "gross_return_acre": 55250
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 340.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0020",
        "crop_name": "Black Gram (T-9 / PU 31) - Select Genotype v1",
        "category": "Pulse",
        "growing_duration_days": 75,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 15,
            "phosphorus_kg_ha": 40,
            "potassium_kg_ha": 20,
            "sulfur_kg_ha": 34,
            "zinc_sulfate_kg_ha": 16.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 36,
            "optimum_temperature_c": 29.0,
            "min_ph": 6.0,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 450,
            "max_annual_rainfall_mm": 900
        },
        "production_economics": {
            "potential_yield_kg_acre": 700,
            "benchmark_mandi_price_rs_qtl": 7800,
            "estimated_cost_cultivation_acre": 13000,
            "gross_return_acre": 54600
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 382.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0021",
        "crop_name": "Soybean (JS 335 Central Pride) - Select Genotype v1",
        "category": "Oilseed",
        "growing_duration_days": 95,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 30,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 40,
            "sulfur_kg_ha": 35,
            "zinc_sulfate_kg_ha": 17.5
        },
        "climate_envelope": {
            "min_temperature_c": 20,
            "max_temperature_c": 33,
            "optimum_temperature_c": 26.5,
            "min_ph": 6.0,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 700,
            "max_annual_rainfall_mm": 1400
        },
        "production_economics": {
            "potential_yield_kg_acre": 1100,
            "benchmark_mandi_price_rs_qtl": 4700,
            "estimated_cost_cultivation_acre": 14000,
            "gross_return_acre": 51700
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 595.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0022",
        "crop_name": "Soybean (JS 95-60 Short Duration) - Select Genotype v1",
        "category": "Oilseed",
        "growing_duration_days": 85,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 30,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 40,
            "sulfur_kg_ha": 36,
            "zinc_sulfate_kg_ha": 18.5
        },
        "climate_envelope": {
            "min_temperature_c": 20,
            "max_temperature_c": 33,
            "optimum_temperature_c": 26.5,
            "min_ph": 6.0,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 650,
            "max_annual_rainfall_mm": 1300
        },
        "production_economics": {
            "potential_yield_kg_acre": 1000,
            "benchmark_mandi_price_rs_qtl": 4700,
            "estimated_cost_cultivation_acre": 15000,
            "gross_return_acre": 47000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 552.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0023",
        "crop_name": "Groundnut (TAG 24 Semi-Dwarf) - Select Genotype v1",
        "category": "Oilseed",
        "growing_duration_days": 105,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 25,
            "phosphorus_kg_ha": 50,
            "potassium_kg_ha": 40,
            "sulfur_kg_ha": 37,
            "zinc_sulfate_kg_ha": 19.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 34,
            "optimum_temperature_c": 28.0,
            "min_ph": 5.8,
            "max_ph": 7.2,
            "min_annual_rainfall_mm": 500,
            "max_annual_rainfall_mm": 1000
        },
        "production_economics": {
            "potential_yield_kg_acre": 1250,
            "benchmark_mandi_price_rs_qtl": 6800,
            "estimated_cost_cultivation_acre": 16000,
            "gross_return_acre": 85000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 425.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0024",
        "crop_name": "Groundnut (Kadiri 6 Drought Resilient) - Select Genotype v1",
        "category": "Oilseed",
        "growing_duration_days": 115,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 25,
            "phosphorus_kg_ha": 50,
            "potassium_kg_ha": 40,
            "sulfur_kg_ha": 38,
            "zinc_sulfate_kg_ha": 20.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 34,
            "optimum_temperature_c": 28.0,
            "min_ph": 5.8,
            "max_ph": 7.2,
            "min_annual_rainfall_mm": 450,
            "max_annual_rainfall_mm": 900
        },
        "production_economics": {
            "potential_yield_kg_acre": 1200,
            "benchmark_mandi_price_rs_qtl": 6800,
            "estimated_cost_cultivation_acre": 17000,
            "gross_return_acre": 81600
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 382.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0025",
        "crop_name": "Mustard (Pusa Mustard 30 Zero Erucic) - Select Genotype v1",
        "category": "Oilseed",
        "growing_duration_days": 110,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 60,
            "phosphorus_kg_ha": 30,
            "potassium_kg_ha": 30,
            "sulfur_kg_ha": 39,
            "zinc_sulfate_kg_ha": 21.5
        },
        "climate_envelope": {
            "min_temperature_c": 10,
            "max_temperature_c": 25,
            "optimum_temperature_c": 17.5,
            "min_ph": 6.0,
            "max_ph": 7.8,
            "min_annual_rainfall_mm": 350,
            "max_annual_rainfall_mm": 700
        },
        "production_economics": {
            "potential_yield_kg_acre": 950,
            "benchmark_mandi_price_rs_qtl": 5600,
            "estimated_cost_cultivation_acre": 18000,
            "gross_return_acre": 53200
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 297.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0026",
        "crop_name": "Mustard (Giriraj / DRMRIJ 31) - Select Genotype v1",
        "category": "Oilseed",
        "growing_duration_days": 120,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 80,
            "phosphorus_kg_ha": 40,
            "potassium_kg_ha": 35,
            "sulfur_kg_ha": 15,
            "zinc_sulfate_kg_ha": 22.5
        },
        "climate_envelope": {
            "min_temperature_c": 10,
            "max_temperature_c": 25,
            "optimum_temperature_c": 17.5,
            "min_ph": 6.0,
            "max_ph": 7.8,
            "min_annual_rainfall_mm": 400,
            "max_annual_rainfall_mm": 800
        },
        "production_economics": {
            "potential_yield_kg_acre": 1100,
            "benchmark_mandi_price_rs_qtl": 5600,
            "estimated_cost_cultivation_acre": 19000,
            "gross_return_acre": 61600
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 340.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0027",
        "crop_name": "Cotton (RCH 659 BG II Bt) - Select Genotype v1",
        "category": "Fiber",
        "growing_duration_days": 160,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 16,
            "zinc_sulfate_kg_ha": 23.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 38,
            "optimum_temperature_c": 30.0,
            "min_ph": 6.5,
            "max_ph": 8.2,
            "min_annual_rainfall_mm": 650,
            "max_annual_rainfall_mm": 1300
        },
        "production_economics": {
            "potential_yield_kg_acre": 1400,
            "benchmark_mandi_price_rs_qtl": 7500,
            "estimated_cost_cultivation_acre": 20000,
            "gross_return_acre": 105000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 552.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0028",
        "crop_name": "Cotton (Ajeet 155 BG II) - Select Genotype v1",
        "category": "Fiber",
        "growing_duration_days": 165,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 17,
            "zinc_sulfate_kg_ha": 24.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 38,
            "optimum_temperature_c": 30.0,
            "min_ph": 6.5,
            "max_ph": 8.2,
            "min_annual_rainfall_mm": 650,
            "max_annual_rainfall_mm": 1300
        },
        "production_economics": {
            "potential_yield_kg_acre": 1350,
            "benchmark_mandi_price_rs_qtl": 7500,
            "estimated_cost_cultivation_acre": 21000,
            "gross_return_acre": 101250
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 552.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0029",
        "crop_name": "Sugarcane (Co 0238 High Sugar) - Select Genotype v1",
        "category": "Commercial",
        "growing_duration_days": 330,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 220,
            "phosphorus_kg_ha": 80,
            "potassium_kg_ha": 120,
            "sulfur_kg_ha": 18,
            "zinc_sulfate_kg_ha": 25.5
        },
        "climate_envelope": {
            "min_temperature_c": 24,
            "max_temperature_c": 38,
            "optimum_temperature_c": 31.0,
            "min_ph": 6.2,
            "max_ph": 7.8,
            "min_annual_rainfall_mm": 1600,
            "max_annual_rainfall_mm": 3200
        },
        "production_economics": {
            "potential_yield_kg_acre": 42000,
            "benchmark_mandi_price_rs_qtl": 340,
            "estimated_cost_cultivation_acre": 22000,
            "gross_return_acre": 142800
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1360.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0030",
        "crop_name": "Sugarcane (Co 86032 Wonder Cane) - Select Genotype v1",
        "category": "Commercial",
        "growing_duration_days": 340,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 240,
            "phosphorus_kg_ha": 80,
            "potassium_kg_ha": 120,
            "sulfur_kg_ha": 19,
            "zinc_sulfate_kg_ha": 26.5
        },
        "climate_envelope": {
            "min_temperature_c": 24,
            "max_temperature_c": 38,
            "optimum_temperature_c": 31.0,
            "min_ph": 6.2,
            "max_ph": 7.8,
            "min_annual_rainfall_mm": 1600,
            "max_annual_rainfall_mm": 3200
        },
        "production_economics": {
            "potential_yield_kg_acre": 45000,
            "benchmark_mandi_price_rs_qtl": 340,
            "estimated_cost_cultivation_acre": 23000,
            "gross_return_acre": 153000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1360.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0031",
        "crop_name": "Tomato (Seminis Abhinav Hybrid) - Select Genotype v1",
        "category": "Vegetable",
        "growing_duration_days": 105,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 90,
            "sulfur_kg_ha": 20,
            "zinc_sulfate_kg_ha": 12.5
        },
        "climate_envelope": {
            "min_temperature_c": 18,
            "max_temperature_c": 32,
            "optimum_temperature_c": 25.0,
            "min_ph": 6.0,
            "max_ph": 7.2,
            "min_annual_rainfall_mm": 500,
            "max_annual_rainfall_mm": 1000
        },
        "production_economics": {
            "potential_yield_kg_acre": 16000,
            "benchmark_mandi_price_rs_qtl": 2200,
            "estimated_cost_cultivation_acre": 24000,
            "gross_return_acre": 352000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 425.0,
            "preferred_method": "Drip Irrigation with 1.2 LPH emitters"
        }
    },
    {
        "crop_id": "CROP-0032",
        "crop_name": "Tomato (Syngenta TO-1057) - Select Genotype v1",
        "category": "Vegetable",
        "growing_duration_days": 110,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 90,
            "sulfur_kg_ha": 21,
            "zinc_sulfate_kg_ha": 13.5
        },
        "climate_envelope": {
            "min_temperature_c": 18,
            "max_temperature_c": 32,
            "optimum_temperature_c": 25.0,
            "min_ph": 6.0,
            "max_ph": 7.2,
            "min_annual_rainfall_mm": 500,
            "max_annual_rainfall_mm": 1000
        },
        "production_economics": {
            "potential_yield_kg_acre": 17000,
            "benchmark_mandi_price_rs_qtl": 2200,
            "estimated_cost_cultivation_acre": 25000,
            "gross_return_acre": 374000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 425.0,
            "preferred_method": "Drip Irrigation with 1.2 LPH emitters"
        }
    },
    {
        "crop_id": "CROP-0033",
        "crop_name": "Chilli (Syngenta Armoor Hot) - Select Genotype v1",
        "category": "Spice",
        "growing_duration_days": 155,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 80,
            "sulfur_kg_ha": 22,
            "zinc_sulfate_kg_ha": 14.5
        },
        "climate_envelope": {
            "min_temperature_c": 20,
            "max_temperature_c": 35,
            "optimum_temperature_c": 27.5,
            "min_ph": 6.0,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 750,
            "max_annual_rainfall_mm": 1500
        },
        "production_economics": {
            "potential_yield_kg_acre": 2600,
            "benchmark_mandi_price_rs_qtl": 19500,
            "estimated_cost_cultivation_acre": 26000,
            "gross_return_acre": 507000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 637.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0034",
        "crop_name": "Chilli (US 341 Red Teja) - Select Genotype v1",
        "category": "Spice",
        "growing_duration_days": 160,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 80,
            "sulfur_kg_ha": 23,
            "zinc_sulfate_kg_ha": 15.5
        },
        "climate_envelope": {
            "min_temperature_c": 20,
            "max_temperature_c": 35,
            "optimum_temperature_c": 27.5,
            "min_ph": 6.0,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 750,
            "max_annual_rainfall_mm": 1500
        },
        "production_economics": {
            "potential_yield_kg_acre": 2700,
            "benchmark_mandi_price_rs_qtl": 21000,
            "estimated_cost_cultivation_acre": 27000,
            "gross_return_acre": 567000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 637.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0035",
        "crop_name": "Potato (Kufri Jyoti Table Potato) - Select Genotype v1",
        "category": "Vegetable",
        "growing_duration_days": 90,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 100,
            "sulfur_kg_ha": 24,
            "zinc_sulfate_kg_ha": 16.5
        },
        "climate_envelope": {
            "min_temperature_c": 14,
            "max_temperature_c": 24,
            "optimum_temperature_c": 19.0,
            "min_ph": 5.2,
            "max_ph": 6.5,
            "min_annual_rainfall_mm": 500,
            "max_annual_rainfall_mm": 1000
        },
        "production_economics": {
            "potential_yield_kg_acre": 13000,
            "benchmark_mandi_price_rs_qtl": 1500,
            "estimated_cost_cultivation_acre": 28000,
            "gross_return_acre": 195000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 425.0,
            "preferred_method": "Drip Irrigation with 1.2 LPH emitters"
        }
    },
    {
        "crop_id": "CROP-0036",
        "crop_name": "Potato (Kufri Chipsona Processing) - Select Genotype v1",
        "category": "Vegetable",
        "growing_duration_days": 100,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 130,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 110,
            "sulfur_kg_ha": 25,
            "zinc_sulfate_kg_ha": 17.5
        },
        "climate_envelope": {
            "min_temperature_c": 14,
            "max_temperature_c": 24,
            "optimum_temperature_c": 19.0,
            "min_ph": 5.2,
            "max_ph": 6.5,
            "min_annual_rainfall_mm": 500,
            "max_annual_rainfall_mm": 1000
        },
        "production_economics": {
            "potential_yield_kg_acre": 14000,
            "benchmark_mandi_price_rs_qtl": 1800,
            "estimated_cost_cultivation_acre": 29000,
            "gross_return_acre": 252000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 425.0,
            "preferred_method": "Drip Irrigation with 1.2 LPH emitters"
        }
    },
    {
        "crop_id": "CROP-0037",
        "crop_name": "Onion (Bhima Super Red) - Select Genotype v1",
        "category": "Vegetable",
        "growing_duration_days": 125,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 90,
            "phosphorus_kg_ha": 45,
            "potassium_kg_ha": 50,
            "sulfur_kg_ha": 26,
            "zinc_sulfate_kg_ha": 18.5
        },
        "climate_envelope": {
            "min_temperature_c": 13,
            "max_temperature_c": 30,
            "optimum_temperature_c": 21.5,
            "min_ph": 6.0,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 550,
            "max_annual_rainfall_mm": 1100
        },
        "production_economics": {
            "potential_yield_kg_acre": 11500,
            "benchmark_mandi_price_rs_qtl": 2200,
            "estimated_cost_cultivation_acre": 12000,
            "gross_return_acre": 253000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 467.5,
            "preferred_method": "Drip Irrigation with 1.2 LPH emitters"
        }
    },
    {
        "crop_id": "CROP-0038",
        "crop_name": "Garlic (Yamuna Safed G-1) - Select Genotype v1",
        "category": "Spice",
        "growing_duration_days": 140,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 80,
            "phosphorus_kg_ha": 40,
            "potassium_kg_ha": 40,
            "sulfur_kg_ha": 27,
            "zinc_sulfate_kg_ha": 19.5
        },
        "climate_envelope": {
            "min_temperature_c": 12,
            "max_temperature_c": 25,
            "optimum_temperature_c": 18.5,
            "min_ph": 6.0,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 450,
            "max_annual_rainfall_mm": 900
        },
        "production_economics": {
            "potential_yield_kg_acre": 4200,
            "benchmark_mandi_price_rs_qtl": 14000,
            "estimated_cost_cultivation_acre": 13000,
            "gross_return_acre": 588000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 382.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0039",
        "crop_name": "Turmeric (Prathibha IISR) - Select Genotype v1",
        "category": "Spice",
        "growing_duration_days": 225,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 100,
            "phosphorus_kg_ha": 50,
            "potassium_kg_ha": 90,
            "sulfur_kg_ha": 28,
            "zinc_sulfate_kg_ha": 20.5
        },
        "climate_envelope": {
            "min_temperature_c": 20,
            "max_temperature_c": 35,
            "optimum_temperature_c": 27.5,
            "min_ph": 5.5,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 1400,
            "max_annual_rainfall_mm": 2800
        },
        "production_economics": {
            "potential_yield_kg_acre": 9500,
            "benchmark_mandi_price_rs_qtl": 14500,
            "estimated_cost_cultivation_acre": 14000,
            "gross_return_acre": 1377500
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1190.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0040",
        "crop_name": "Ginger (Varada IISR) - Select Genotype v1",
        "category": "Spice",
        "growing_duration_days": 220,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 90,
            "phosphorus_kg_ha": 50,
            "potassium_kg_ha": 90,
            "sulfur_kg_ha": 29,
            "zinc_sulfate_kg_ha": 21.5
        },
        "climate_envelope": {
            "min_temperature_c": 20,
            "max_temperature_c": 32,
            "optimum_temperature_c": 26.0,
            "min_ph": 5.5,
            "max_ph": 6.5,
            "min_annual_rainfall_mm": 1500,
            "max_annual_rainfall_mm": 3000
        },
        "production_economics": {
            "potential_yield_kg_acre": 8500,
            "benchmark_mandi_price_rs_qtl": 9000,
            "estimated_cost_cultivation_acre": 15000,
            "gross_return_acre": 765000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1275.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0041",
        "crop_name": "Rice (Pusa Basmati 1121) - Select Genotype v2",
        "category": "Cereal",
        "growing_duration_days": 140,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 90,
            "phosphorus_kg_ha": 45,
            "potassium_kg_ha": 45,
            "sulfur_kg_ha": 30,
            "zinc_sulfate_kg_ha": 22.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 36,
            "optimum_temperature_c": 29.0,
            "min_ph": 5.5,
            "max_ph": 7.2,
            "min_annual_rainfall_mm": 1600,
            "max_annual_rainfall_mm": 3200
        },
        "production_economics": {
            "potential_yield_kg_acre": 2200,
            "benchmark_mandi_price_rs_qtl": 2400,
            "estimated_cost_cultivation_acre": 16000,
            "gross_return_acre": 52800
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1360.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0042",
        "crop_name": "Rice (Pusa Basmati 1509) - Select Genotype v2",
        "category": "Cereal",
        "growing_duration_days": 120,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 85,
            "phosphorus_kg_ha": 40,
            "potassium_kg_ha": 40,
            "sulfur_kg_ha": 31,
            "zinc_sulfate_kg_ha": 23.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 38,
            "optimum_temperature_c": 30.0,
            "min_ph": 5.5,
            "max_ph": 7.2,
            "min_annual_rainfall_mm": 1400,
            "max_annual_rainfall_mm": 2800
        },
        "production_economics": {
            "potential_yield_kg_acre": 2400,
            "benchmark_mandi_price_rs_qtl": 2500,
            "estimated_cost_cultivation_acre": 17000,
            "gross_return_acre": 60000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1190.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0043",
        "crop_name": "Rice (BPT 5204 / Samba Mahsuri) - Select Genotype v2",
        "category": "Cereal",
        "growing_duration_days": 150,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 100,
            "phosphorus_kg_ha": 50,
            "potassium_kg_ha": 50,
            "sulfur_kg_ha": 32,
            "zinc_sulfate_kg_ha": 24.5
        },
        "climate_envelope": {
            "min_temperature_c": 20,
            "max_temperature_c": 36,
            "optimum_temperature_c": 28.0,
            "min_ph": 6.0,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 1500,
            "max_annual_rainfall_mm": 3000
        },
        "production_economics": {
            "potential_yield_kg_acre": 2600,
            "benchmark_mandi_price_rs_qtl": 2700,
            "estimated_cost_cultivation_acre": 18000,
            "gross_return_acre": 70200
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1275.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0044",
        "crop_name": "Rice (MTU 1010 / Cottondora Sannalu) - Select Genotype v2",
        "category": "Cereal",
        "growing_duration_days": 125,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 33,
            "zinc_sulfate_kg_ha": 25.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 38,
            "optimum_temperature_c": 30.0,
            "min_ph": 5.5,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 1300,
            "max_annual_rainfall_mm": 2600
        },
        "production_economics": {
            "potential_yield_kg_acre": 3100,
            "benchmark_mandi_price_rs_qtl": 2200,
            "estimated_cost_cultivation_acre": 19000,
            "gross_return_acre": 68200
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1105.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0045",
        "crop_name": "Rice (IR 64 High Yield) - Select Genotype v2",
        "category": "Cereal",
        "growing_duration_days": 120,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 34,
            "zinc_sulfate_kg_ha": 26.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 38,
            "optimum_temperature_c": 30.0,
            "min_ph": 5.5,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 1400,
            "max_annual_rainfall_mm": 2800
        },
        "production_economics": {
            "potential_yield_kg_acre": 3200,
            "benchmark_mandi_price_rs_qtl": 2100,
            "estimated_cost_cultivation_acre": 20000,
            "gross_return_acre": 67200
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1190.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0046",
        "crop_name": "Wheat (HD 2967 High Yield) - Select Genotype v2",
        "category": "Cereal",
        "growing_duration_days": 125,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 35,
            "zinc_sulfate_kg_ha": 12.5
        },
        "climate_envelope": {
            "min_temperature_c": 12,
            "max_temperature_c": 25,
            "optimum_temperature_c": 18.5,
            "min_ph": 6.0,
            "max_ph": 7.8,
            "min_annual_rainfall_mm": 450,
            "max_annual_rainfall_mm": 900
        },
        "production_economics": {
            "potential_yield_kg_acre": 2400,
            "benchmark_mandi_price_rs_qtl": 2350,
            "estimated_cost_cultivation_acre": 21000,
            "gross_return_acre": 56400
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 382.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0047",
        "crop_name": "Wheat (HD 3086 Pusa Gautami) - Select Genotype v2",
        "category": "Cereal",
        "growing_duration_days": 120,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 36,
            "zinc_sulfate_kg_ha": 13.5
        },
        "climate_envelope": {
            "min_temperature_c": 12,
            "max_temperature_c": 26,
            "optimum_temperature_c": 19.0,
            "min_ph": 6.0,
            "max_ph": 7.8,
            "min_annual_rainfall_mm": 450,
            "max_annual_rainfall_mm": 900
        },
        "production_economics": {
            "potential_yield_kg_acre": 2500,
            "benchmark_mandi_price_rs_qtl": 2400,
            "estimated_cost_cultivation_acre": 22000,
            "gross_return_acre": 60000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 382.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0048",
        "crop_name": "Wheat (PBW 343 / Shriram 303) - Select Genotype v2",
        "category": "Cereal",
        "growing_duration_days": 130,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 130,
            "phosphorus_kg_ha": 65,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 37,
            "zinc_sulfate_kg_ha": 14.5
        },
        "climate_envelope": {
            "min_temperature_c": 10,
            "max_temperature_c": 24,
            "optimum_temperature_c": 17.0,
            "min_ph": 6.0,
            "max_ph": 7.8,
            "min_annual_rainfall_mm": 450,
            "max_annual_rainfall_mm": 900
        },
        "production_economics": {
            "potential_yield_kg_acre": 2600,
            "benchmark_mandi_price_rs_qtl": 2300,
            "estimated_cost_cultivation_acre": 23000,
            "gross_return_acre": 59800
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 382.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0049",
        "crop_name": "Wheat (DBW 187 Karan Vandana) - Select Genotype v2",
        "category": "Cereal",
        "growing_duration_days": 120,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 130,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 38,
            "zinc_sulfate_kg_ha": 15.5
        },
        "climate_envelope": {
            "min_temperature_c": 12,
            "max_temperature_c": 27,
            "optimum_temperature_c": 19.5,
            "min_ph": 6.0,
            "max_ph": 7.8,
            "min_annual_rainfall_mm": 400,
            "max_annual_rainfall_mm": 800
        },
        "production_economics": {
            "potential_yield_kg_acre": 2700,
            "benchmark_mandi_price_rs_qtl": 2500,
            "estimated_cost_cultivation_acre": 24000,
            "gross_return_acre": 67500
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 340.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0050",
        "crop_name": "Maize (Pioneer P3396 Hybrid) - Select Genotype v2",
        "category": "Cereal",
        "growing_duration_days": 110,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 140,
            "phosphorus_kg_ha": 65,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 39,
            "zinc_sulfate_kg_ha": 16.5
        },
        "climate_envelope": {
            "min_temperature_c": 18,
            "max_temperature_c": 35,
            "optimum_temperature_c": 26.5,
            "min_ph": 5.8,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 600,
            "max_annual_rainfall_mm": 1200
        },
        "production_economics": {
            "potential_yield_kg_acre": 3600,
            "benchmark_mandi_price_rs_qtl": 2150,
            "estimated_cost_cultivation_acre": 25000,
            "gross_return_acre": 77400
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 510.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0051",
        "crop_name": "Maize (Dekalb 9108 Plus) - Select Genotype v2",
        "category": "Cereal",
        "growing_duration_days": 105,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 130,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 55,
            "sulfur_kg_ha": 15,
            "zinc_sulfate_kg_ha": 17.5
        },
        "climate_envelope": {
            "min_temperature_c": 18,
            "max_temperature_c": 35,
            "optimum_temperature_c": 26.5,
            "min_ph": 5.8,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 550,
            "max_annual_rainfall_mm": 1100
        },
        "production_economics": {
            "potential_yield_kg_acre": 3400,
            "benchmark_mandi_price_rs_qtl": 2150,
            "estimated_cost_cultivation_acre": 26000,
            "gross_return_acre": 73100
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 467.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0052",
        "crop_name": "Maize (Syngenta NK 6240) - Select Genotype v2",
        "category": "Cereal",
        "growing_duration_days": 115,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 140,
            "phosphorus_kg_ha": 70,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 16,
            "zinc_sulfate_kg_ha": 18.5
        },
        "climate_envelope": {
            "min_temperature_c": 18,
            "max_temperature_c": 36,
            "optimum_temperature_c": 27.0,
            "min_ph": 5.8,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 600,
            "max_annual_rainfall_mm": 1200
        },
        "production_economics": {
            "potential_yield_kg_acre": 3800,
            "benchmark_mandi_price_rs_qtl": 2150,
            "estimated_cost_cultivation_acre": 27000,
            "gross_return_acre": 81700
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 510.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0053",
        "crop_name": "Sorghum (CSH 16 Grain Hybrid) - Select Genotype v2",
        "category": "Millet",
        "growing_duration_days": 105,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 80,
            "phosphorus_kg_ha": 40,
            "potassium_kg_ha": 40,
            "sulfur_kg_ha": 17,
            "zinc_sulfate_kg_ha": 19.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 38,
            "optimum_temperature_c": 30.0,
            "min_ph": 6.0,
            "max_ph": 8.2,
            "min_annual_rainfall_mm": 450,
            "max_annual_rainfall_mm": 900
        },
        "production_economics": {
            "potential_yield_kg_acre": 1600,
            "benchmark_mandi_price_rs_qtl": 2900,
            "estimated_cost_cultivation_acre": 28000,
            "gross_return_acre": 46400
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 382.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0054",
        "crop_name": "Pearl Millet (HHB 67 Improved) - Select Genotype v2",
        "category": "Millet",
        "growing_duration_days": 70,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 60,
            "phosphorus_kg_ha": 30,
            "potassium_kg_ha": 30,
            "sulfur_kg_ha": 18,
            "zinc_sulfate_kg_ha": 20.5
        },
        "climate_envelope": {
            "min_temperature_c": 25,
            "max_temperature_c": 42,
            "optimum_temperature_c": 33.5,
            "min_ph": 6.5,
            "max_ph": 8.5,
            "min_annual_rainfall_mm": 300,
            "max_annual_rainfall_mm": 600
        },
        "production_economics": {
            "potential_yield_kg_acre": 1200,
            "benchmark_mandi_price_rs_qtl": 2450,
            "estimated_cost_cultivation_acre": 29000,
            "gross_return_acre": 29400
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 255.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0055",
        "crop_name": "Finger Millet (GPU 28 Ragi) - Select Genotype v2",
        "category": "Millet",
        "growing_duration_days": 110,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 60,
            "phosphorus_kg_ha": 40,
            "potassium_kg_ha": 30,
            "sulfur_kg_ha": 19,
            "zinc_sulfate_kg_ha": 21.5
        },
        "climate_envelope": {
            "min_temperature_c": 18,
            "max_temperature_c": 34,
            "optimum_temperature_c": 26.0,
            "min_ph": 5.5,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 500,
            "max_annual_rainfall_mm": 1000
        },
        "production_economics": {
            "potential_yield_kg_acre": 1300,
            "benchmark_mandi_price_rs_qtl": 3800,
            "estimated_cost_cultivation_acre": 12000,
            "gross_return_acre": 49400
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 425.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0056",
        "crop_name": "Chickpea (JG 11 Desi Gram) - Select Genotype v2",
        "category": "Pulse",
        "growing_duration_days": 95,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 20,
            "phosphorus_kg_ha": 50,
            "potassium_kg_ha": 25,
            "sulfur_kg_ha": 20,
            "zinc_sulfate_kg_ha": 22.5
        },
        "climate_envelope": {
            "min_temperature_c": 15,
            "max_temperature_c": 28,
            "optimum_temperature_c": 21.5,
            "min_ph": 6.0,
            "max_ph": 8.0,
            "min_annual_rainfall_mm": 350,
            "max_annual_rainfall_mm": 700
        },
        "production_economics": {
            "potential_yield_kg_acre": 950,
            "benchmark_mandi_price_rs_qtl": 5400,
            "estimated_cost_cultivation_acre": 13000,
            "gross_return_acre": 51300
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 297.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0057",
        "crop_name": "Chickpea (KAK 2 Kabuli) - Select Genotype v2",
        "category": "Pulse",
        "growing_duration_days": 105,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 25,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 30,
            "sulfur_kg_ha": 21,
            "zinc_sulfate_kg_ha": 23.5
        },
        "climate_envelope": {
            "min_temperature_c": 14,
            "max_temperature_c": 27,
            "optimum_temperature_c": 20.5,
            "min_ph": 6.5,
            "max_ph": 8.2,
            "min_annual_rainfall_mm": 350,
            "max_annual_rainfall_mm": 700
        },
        "production_economics": {
            "potential_yield_kg_acre": 1100,
            "benchmark_mandi_price_rs_qtl": 11000,
            "estimated_cost_cultivation_acre": 14000,
            "gross_return_acre": 121000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 297.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0058",
        "crop_name": "Pigeon Pea (ICPL 87119 Asha) - Select Genotype v2",
        "category": "Pulse",
        "growing_duration_days": 170,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 25,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 30,
            "sulfur_kg_ha": 22,
            "zinc_sulfate_kg_ha": 24.5
        },
        "climate_envelope": {
            "min_temperature_c": 20,
            "max_temperature_c": 36,
            "optimum_temperature_c": 28.0,
            "min_ph": 6.5,
            "max_ph": 8.0,
            "min_annual_rainfall_mm": 700,
            "max_annual_rainfall_mm": 1400
        },
        "production_economics": {
            "potential_yield_kg_acre": 900,
            "benchmark_mandi_price_rs_qtl": 7500,
            "estimated_cost_cultivation_acre": 15000,
            "gross_return_acre": 67500
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 595.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0059",
        "crop_name": "Green Gram (IPM 02-3 / Samrat) - Select Genotype v2",
        "category": "Pulse",
        "growing_duration_days": 65,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 15,
            "phosphorus_kg_ha": 40,
            "potassium_kg_ha": 20,
            "sulfur_kg_ha": 23,
            "zinc_sulfate_kg_ha": 25.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 36,
            "optimum_temperature_c": 29.0,
            "min_ph": 6.2,
            "max_ph": 7.8,
            "min_annual_rainfall_mm": 400,
            "max_annual_rainfall_mm": 800
        },
        "production_economics": {
            "potential_yield_kg_acre": 650,
            "benchmark_mandi_price_rs_qtl": 8500,
            "estimated_cost_cultivation_acre": 16000,
            "gross_return_acre": 55250
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 340.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0060",
        "crop_name": "Black Gram (T-9 / PU 31) - Select Genotype v2",
        "category": "Pulse",
        "growing_duration_days": 75,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 15,
            "phosphorus_kg_ha": 40,
            "potassium_kg_ha": 20,
            "sulfur_kg_ha": 24,
            "zinc_sulfate_kg_ha": 26.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 36,
            "optimum_temperature_c": 29.0,
            "min_ph": 6.0,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 450,
            "max_annual_rainfall_mm": 900
        },
        "production_economics": {
            "potential_yield_kg_acre": 700,
            "benchmark_mandi_price_rs_qtl": 7800,
            "estimated_cost_cultivation_acre": 17000,
            "gross_return_acre": 54600
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 382.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0061",
        "crop_name": "Soybean (JS 335 Central Pride) - Select Genotype v2",
        "category": "Oilseed",
        "growing_duration_days": 95,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 30,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 40,
            "sulfur_kg_ha": 25,
            "zinc_sulfate_kg_ha": 12.5
        },
        "climate_envelope": {
            "min_temperature_c": 20,
            "max_temperature_c": 33,
            "optimum_temperature_c": 26.5,
            "min_ph": 6.0,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 700,
            "max_annual_rainfall_mm": 1400
        },
        "production_economics": {
            "potential_yield_kg_acre": 1100,
            "benchmark_mandi_price_rs_qtl": 4700,
            "estimated_cost_cultivation_acre": 18000,
            "gross_return_acre": 51700
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 595.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0062",
        "crop_name": "Soybean (JS 95-60 Short Duration) - Select Genotype v2",
        "category": "Oilseed",
        "growing_duration_days": 85,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 30,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 40,
            "sulfur_kg_ha": 26,
            "zinc_sulfate_kg_ha": 13.5
        },
        "climate_envelope": {
            "min_temperature_c": 20,
            "max_temperature_c": 33,
            "optimum_temperature_c": 26.5,
            "min_ph": 6.0,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 650,
            "max_annual_rainfall_mm": 1300
        },
        "production_economics": {
            "potential_yield_kg_acre": 1000,
            "benchmark_mandi_price_rs_qtl": 4700,
            "estimated_cost_cultivation_acre": 19000,
            "gross_return_acre": 47000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 552.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0063",
        "crop_name": "Groundnut (TAG 24 Semi-Dwarf) - Select Genotype v2",
        "category": "Oilseed",
        "growing_duration_days": 105,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 25,
            "phosphorus_kg_ha": 50,
            "potassium_kg_ha": 40,
            "sulfur_kg_ha": 27,
            "zinc_sulfate_kg_ha": 14.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 34,
            "optimum_temperature_c": 28.0,
            "min_ph": 5.8,
            "max_ph": 7.2,
            "min_annual_rainfall_mm": 500,
            "max_annual_rainfall_mm": 1000
        },
        "production_economics": {
            "potential_yield_kg_acre": 1250,
            "benchmark_mandi_price_rs_qtl": 6800,
            "estimated_cost_cultivation_acre": 20000,
            "gross_return_acre": 85000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 425.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0064",
        "crop_name": "Groundnut (Kadiri 6 Drought Resilient) - Select Genotype v2",
        "category": "Oilseed",
        "growing_duration_days": 115,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 25,
            "phosphorus_kg_ha": 50,
            "potassium_kg_ha": 40,
            "sulfur_kg_ha": 28,
            "zinc_sulfate_kg_ha": 15.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 34,
            "optimum_temperature_c": 28.0,
            "min_ph": 5.8,
            "max_ph": 7.2,
            "min_annual_rainfall_mm": 450,
            "max_annual_rainfall_mm": 900
        },
        "production_economics": {
            "potential_yield_kg_acre": 1200,
            "benchmark_mandi_price_rs_qtl": 6800,
            "estimated_cost_cultivation_acre": 21000,
            "gross_return_acre": 81600
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 382.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0065",
        "crop_name": "Mustard (Pusa Mustard 30 Zero Erucic) - Select Genotype v2",
        "category": "Oilseed",
        "growing_duration_days": 110,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 60,
            "phosphorus_kg_ha": 30,
            "potassium_kg_ha": 30,
            "sulfur_kg_ha": 29,
            "zinc_sulfate_kg_ha": 16.5
        },
        "climate_envelope": {
            "min_temperature_c": 10,
            "max_temperature_c": 25,
            "optimum_temperature_c": 17.5,
            "min_ph": 6.0,
            "max_ph": 7.8,
            "min_annual_rainfall_mm": 350,
            "max_annual_rainfall_mm": 700
        },
        "production_economics": {
            "potential_yield_kg_acre": 950,
            "benchmark_mandi_price_rs_qtl": 5600,
            "estimated_cost_cultivation_acre": 22000,
            "gross_return_acre": 53200
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 297.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0066",
        "crop_name": "Mustard (Giriraj / DRMRIJ 31) - Select Genotype v2",
        "category": "Oilseed",
        "growing_duration_days": 120,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 80,
            "phosphorus_kg_ha": 40,
            "potassium_kg_ha": 35,
            "sulfur_kg_ha": 30,
            "zinc_sulfate_kg_ha": 17.5
        },
        "climate_envelope": {
            "min_temperature_c": 10,
            "max_temperature_c": 25,
            "optimum_temperature_c": 17.5,
            "min_ph": 6.0,
            "max_ph": 7.8,
            "min_annual_rainfall_mm": 400,
            "max_annual_rainfall_mm": 800
        },
        "production_economics": {
            "potential_yield_kg_acre": 1100,
            "benchmark_mandi_price_rs_qtl": 5600,
            "estimated_cost_cultivation_acre": 23000,
            "gross_return_acre": 61600
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 340.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0067",
        "crop_name": "Cotton (RCH 659 BG II Bt) - Select Genotype v2",
        "category": "Fiber",
        "growing_duration_days": 160,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 31,
            "zinc_sulfate_kg_ha": 18.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 38,
            "optimum_temperature_c": 30.0,
            "min_ph": 6.5,
            "max_ph": 8.2,
            "min_annual_rainfall_mm": 650,
            "max_annual_rainfall_mm": 1300
        },
        "production_economics": {
            "potential_yield_kg_acre": 1400,
            "benchmark_mandi_price_rs_qtl": 7500,
            "estimated_cost_cultivation_acre": 24000,
            "gross_return_acre": 105000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 552.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0068",
        "crop_name": "Cotton (Ajeet 155 BG II) - Select Genotype v2",
        "category": "Fiber",
        "growing_duration_days": 165,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 32,
            "zinc_sulfate_kg_ha": 19.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 38,
            "optimum_temperature_c": 30.0,
            "min_ph": 6.5,
            "max_ph": 8.2,
            "min_annual_rainfall_mm": 650,
            "max_annual_rainfall_mm": 1300
        },
        "production_economics": {
            "potential_yield_kg_acre": 1350,
            "benchmark_mandi_price_rs_qtl": 7500,
            "estimated_cost_cultivation_acre": 25000,
            "gross_return_acre": 101250
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 552.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0069",
        "crop_name": "Sugarcane (Co 0238 High Sugar) - Select Genotype v2",
        "category": "Commercial",
        "growing_duration_days": 330,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 220,
            "phosphorus_kg_ha": 80,
            "potassium_kg_ha": 120,
            "sulfur_kg_ha": 33,
            "zinc_sulfate_kg_ha": 20.5
        },
        "climate_envelope": {
            "min_temperature_c": 24,
            "max_temperature_c": 38,
            "optimum_temperature_c": 31.0,
            "min_ph": 6.2,
            "max_ph": 7.8,
            "min_annual_rainfall_mm": 1600,
            "max_annual_rainfall_mm": 3200
        },
        "production_economics": {
            "potential_yield_kg_acre": 42000,
            "benchmark_mandi_price_rs_qtl": 340,
            "estimated_cost_cultivation_acre": 26000,
            "gross_return_acre": 142800
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1360.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0070",
        "crop_name": "Sugarcane (Co 86032 Wonder Cane) - Select Genotype v2",
        "category": "Commercial",
        "growing_duration_days": 340,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 240,
            "phosphorus_kg_ha": 80,
            "potassium_kg_ha": 120,
            "sulfur_kg_ha": 34,
            "zinc_sulfate_kg_ha": 21.5
        },
        "climate_envelope": {
            "min_temperature_c": 24,
            "max_temperature_c": 38,
            "optimum_temperature_c": 31.0,
            "min_ph": 6.2,
            "max_ph": 7.8,
            "min_annual_rainfall_mm": 1600,
            "max_annual_rainfall_mm": 3200
        },
        "production_economics": {
            "potential_yield_kg_acre": 45000,
            "benchmark_mandi_price_rs_qtl": 340,
            "estimated_cost_cultivation_acre": 27000,
            "gross_return_acre": 153000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1360.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0071",
        "crop_name": "Tomato (Seminis Abhinav Hybrid) - Select Genotype v2",
        "category": "Vegetable",
        "growing_duration_days": 105,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 90,
            "sulfur_kg_ha": 35,
            "zinc_sulfate_kg_ha": 22.5
        },
        "climate_envelope": {
            "min_temperature_c": 18,
            "max_temperature_c": 32,
            "optimum_temperature_c": 25.0,
            "min_ph": 6.0,
            "max_ph": 7.2,
            "min_annual_rainfall_mm": 500,
            "max_annual_rainfall_mm": 1000
        },
        "production_economics": {
            "potential_yield_kg_acre": 16000,
            "benchmark_mandi_price_rs_qtl": 2200,
            "estimated_cost_cultivation_acre": 28000,
            "gross_return_acre": 352000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 425.0,
            "preferred_method": "Drip Irrigation with 1.2 LPH emitters"
        }
    },
    {
        "crop_id": "CROP-0072",
        "crop_name": "Tomato (Syngenta TO-1057) - Select Genotype v2",
        "category": "Vegetable",
        "growing_duration_days": 110,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 90,
            "sulfur_kg_ha": 36,
            "zinc_sulfate_kg_ha": 23.5
        },
        "climate_envelope": {
            "min_temperature_c": 18,
            "max_temperature_c": 32,
            "optimum_temperature_c": 25.0,
            "min_ph": 6.0,
            "max_ph": 7.2,
            "min_annual_rainfall_mm": 500,
            "max_annual_rainfall_mm": 1000
        },
        "production_economics": {
            "potential_yield_kg_acre": 17000,
            "benchmark_mandi_price_rs_qtl": 2200,
            "estimated_cost_cultivation_acre": 29000,
            "gross_return_acre": 374000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 425.0,
            "preferred_method": "Drip Irrigation with 1.2 LPH emitters"
        }
    },
    {
        "crop_id": "CROP-0073",
        "crop_name": "Chilli (Syngenta Armoor Hot) - Select Genotype v2",
        "category": "Spice",
        "growing_duration_days": 155,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 80,
            "sulfur_kg_ha": 37,
            "zinc_sulfate_kg_ha": 24.5
        },
        "climate_envelope": {
            "min_temperature_c": 20,
            "max_temperature_c": 35,
            "optimum_temperature_c": 27.5,
            "min_ph": 6.0,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 750,
            "max_annual_rainfall_mm": 1500
        },
        "production_economics": {
            "potential_yield_kg_acre": 2600,
            "benchmark_mandi_price_rs_qtl": 19500,
            "estimated_cost_cultivation_acre": 12000,
            "gross_return_acre": 507000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 637.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0074",
        "crop_name": "Chilli (US 341 Red Teja) - Select Genotype v2",
        "category": "Spice",
        "growing_duration_days": 160,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 80,
            "sulfur_kg_ha": 38,
            "zinc_sulfate_kg_ha": 25.5
        },
        "climate_envelope": {
            "min_temperature_c": 20,
            "max_temperature_c": 35,
            "optimum_temperature_c": 27.5,
            "min_ph": 6.0,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 750,
            "max_annual_rainfall_mm": 1500
        },
        "production_economics": {
            "potential_yield_kg_acre": 2700,
            "benchmark_mandi_price_rs_qtl": 21000,
            "estimated_cost_cultivation_acre": 13000,
            "gross_return_acre": 567000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 637.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0075",
        "crop_name": "Potato (Kufri Jyoti Table Potato) - Select Genotype v2",
        "category": "Vegetable",
        "growing_duration_days": 90,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 100,
            "sulfur_kg_ha": 39,
            "zinc_sulfate_kg_ha": 26.5
        },
        "climate_envelope": {
            "min_temperature_c": 14,
            "max_temperature_c": 24,
            "optimum_temperature_c": 19.0,
            "min_ph": 5.2,
            "max_ph": 6.5,
            "min_annual_rainfall_mm": 500,
            "max_annual_rainfall_mm": 1000
        },
        "production_economics": {
            "potential_yield_kg_acre": 13000,
            "benchmark_mandi_price_rs_qtl": 1500,
            "estimated_cost_cultivation_acre": 14000,
            "gross_return_acre": 195000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 425.0,
            "preferred_method": "Drip Irrigation with 1.2 LPH emitters"
        }
    },
    {
        "crop_id": "CROP-0076",
        "crop_name": "Potato (Kufri Chipsona Processing) - Select Genotype v2",
        "category": "Vegetable",
        "growing_duration_days": 100,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 130,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 110,
            "sulfur_kg_ha": 15,
            "zinc_sulfate_kg_ha": 12.5
        },
        "climate_envelope": {
            "min_temperature_c": 14,
            "max_temperature_c": 24,
            "optimum_temperature_c": 19.0,
            "min_ph": 5.2,
            "max_ph": 6.5,
            "min_annual_rainfall_mm": 500,
            "max_annual_rainfall_mm": 1000
        },
        "production_economics": {
            "potential_yield_kg_acre": 14000,
            "benchmark_mandi_price_rs_qtl": 1800,
            "estimated_cost_cultivation_acre": 15000,
            "gross_return_acre": 252000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 425.0,
            "preferred_method": "Drip Irrigation with 1.2 LPH emitters"
        }
    },
    {
        "crop_id": "CROP-0077",
        "crop_name": "Onion (Bhima Super Red) - Select Genotype v2",
        "category": "Vegetable",
        "growing_duration_days": 125,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 90,
            "phosphorus_kg_ha": 45,
            "potassium_kg_ha": 50,
            "sulfur_kg_ha": 16,
            "zinc_sulfate_kg_ha": 13.5
        },
        "climate_envelope": {
            "min_temperature_c": 13,
            "max_temperature_c": 30,
            "optimum_temperature_c": 21.5,
            "min_ph": 6.0,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 550,
            "max_annual_rainfall_mm": 1100
        },
        "production_economics": {
            "potential_yield_kg_acre": 11500,
            "benchmark_mandi_price_rs_qtl": 2200,
            "estimated_cost_cultivation_acre": 16000,
            "gross_return_acre": 253000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 467.5,
            "preferred_method": "Drip Irrigation with 1.2 LPH emitters"
        }
    },
    {
        "crop_id": "CROP-0078",
        "crop_name": "Garlic (Yamuna Safed G-1) - Select Genotype v2",
        "category": "Spice",
        "growing_duration_days": 140,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 80,
            "phosphorus_kg_ha": 40,
            "potassium_kg_ha": 40,
            "sulfur_kg_ha": 17,
            "zinc_sulfate_kg_ha": 14.5
        },
        "climate_envelope": {
            "min_temperature_c": 12,
            "max_temperature_c": 25,
            "optimum_temperature_c": 18.5,
            "min_ph": 6.0,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 450,
            "max_annual_rainfall_mm": 900
        },
        "production_economics": {
            "potential_yield_kg_acre": 4200,
            "benchmark_mandi_price_rs_qtl": 14000,
            "estimated_cost_cultivation_acre": 17000,
            "gross_return_acre": 588000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 382.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0079",
        "crop_name": "Turmeric (Prathibha IISR) - Select Genotype v2",
        "category": "Spice",
        "growing_duration_days": 225,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 100,
            "phosphorus_kg_ha": 50,
            "potassium_kg_ha": 90,
            "sulfur_kg_ha": 18,
            "zinc_sulfate_kg_ha": 15.5
        },
        "climate_envelope": {
            "min_temperature_c": 20,
            "max_temperature_c": 35,
            "optimum_temperature_c": 27.5,
            "min_ph": 5.5,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 1400,
            "max_annual_rainfall_mm": 2800
        },
        "production_economics": {
            "potential_yield_kg_acre": 9500,
            "benchmark_mandi_price_rs_qtl": 14500,
            "estimated_cost_cultivation_acre": 18000,
            "gross_return_acre": 1377500
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1190.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0080",
        "crop_name": "Ginger (Varada IISR) - Select Genotype v2",
        "category": "Spice",
        "growing_duration_days": 220,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 90,
            "phosphorus_kg_ha": 50,
            "potassium_kg_ha": 90,
            "sulfur_kg_ha": 19,
            "zinc_sulfate_kg_ha": 16.5
        },
        "climate_envelope": {
            "min_temperature_c": 20,
            "max_temperature_c": 32,
            "optimum_temperature_c": 26.0,
            "min_ph": 5.5,
            "max_ph": 6.5,
            "min_annual_rainfall_mm": 1500,
            "max_annual_rainfall_mm": 3000
        },
        "production_economics": {
            "potential_yield_kg_acre": 8500,
            "benchmark_mandi_price_rs_qtl": 9000,
            "estimated_cost_cultivation_acre": 19000,
            "gross_return_acre": 765000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1275.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0081",
        "crop_name": "Rice (Pusa Basmati 1121) - Select Genotype v3",
        "category": "Cereal",
        "growing_duration_days": 140,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 90,
            "phosphorus_kg_ha": 45,
            "potassium_kg_ha": 45,
            "sulfur_kg_ha": 20,
            "zinc_sulfate_kg_ha": 17.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 36,
            "optimum_temperature_c": 29.0,
            "min_ph": 5.5,
            "max_ph": 7.2,
            "min_annual_rainfall_mm": 1600,
            "max_annual_rainfall_mm": 3200
        },
        "production_economics": {
            "potential_yield_kg_acre": 2200,
            "benchmark_mandi_price_rs_qtl": 2400,
            "estimated_cost_cultivation_acre": 20000,
            "gross_return_acre": 52800
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1360.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0082",
        "crop_name": "Rice (Pusa Basmati 1509) - Select Genotype v3",
        "category": "Cereal",
        "growing_duration_days": 120,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 85,
            "phosphorus_kg_ha": 40,
            "potassium_kg_ha": 40,
            "sulfur_kg_ha": 21,
            "zinc_sulfate_kg_ha": 18.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 38,
            "optimum_temperature_c": 30.0,
            "min_ph": 5.5,
            "max_ph": 7.2,
            "min_annual_rainfall_mm": 1400,
            "max_annual_rainfall_mm": 2800
        },
        "production_economics": {
            "potential_yield_kg_acre": 2400,
            "benchmark_mandi_price_rs_qtl": 2500,
            "estimated_cost_cultivation_acre": 21000,
            "gross_return_acre": 60000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1190.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0083",
        "crop_name": "Rice (BPT 5204 / Samba Mahsuri) - Select Genotype v3",
        "category": "Cereal",
        "growing_duration_days": 150,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 100,
            "phosphorus_kg_ha": 50,
            "potassium_kg_ha": 50,
            "sulfur_kg_ha": 22,
            "zinc_sulfate_kg_ha": 19.5
        },
        "climate_envelope": {
            "min_temperature_c": 20,
            "max_temperature_c": 36,
            "optimum_temperature_c": 28.0,
            "min_ph": 6.0,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 1500,
            "max_annual_rainfall_mm": 3000
        },
        "production_economics": {
            "potential_yield_kg_acre": 2600,
            "benchmark_mandi_price_rs_qtl": 2700,
            "estimated_cost_cultivation_acre": 22000,
            "gross_return_acre": 70200
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1275.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0084",
        "crop_name": "Rice (MTU 1010 / Cottondora Sannalu) - Select Genotype v3",
        "category": "Cereal",
        "growing_duration_days": 125,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 23,
            "zinc_sulfate_kg_ha": 20.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 38,
            "optimum_temperature_c": 30.0,
            "min_ph": 5.5,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 1300,
            "max_annual_rainfall_mm": 2600
        },
        "production_economics": {
            "potential_yield_kg_acre": 3100,
            "benchmark_mandi_price_rs_qtl": 2200,
            "estimated_cost_cultivation_acre": 23000,
            "gross_return_acre": 68200
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1105.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0085",
        "crop_name": "Rice (IR 64 High Yield) - Select Genotype v3",
        "category": "Cereal",
        "growing_duration_days": 120,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 24,
            "zinc_sulfate_kg_ha": 21.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 38,
            "optimum_temperature_c": 30.0,
            "min_ph": 5.5,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 1400,
            "max_annual_rainfall_mm": 2800
        },
        "production_economics": {
            "potential_yield_kg_acre": 3200,
            "benchmark_mandi_price_rs_qtl": 2100,
            "estimated_cost_cultivation_acre": 24000,
            "gross_return_acre": 67200
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1190.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0086",
        "crop_name": "Wheat (HD 2967 High Yield) - Select Genotype v3",
        "category": "Cereal",
        "growing_duration_days": 125,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 25,
            "zinc_sulfate_kg_ha": 22.5
        },
        "climate_envelope": {
            "min_temperature_c": 12,
            "max_temperature_c": 25,
            "optimum_temperature_c": 18.5,
            "min_ph": 6.0,
            "max_ph": 7.8,
            "min_annual_rainfall_mm": 450,
            "max_annual_rainfall_mm": 900
        },
        "production_economics": {
            "potential_yield_kg_acre": 2400,
            "benchmark_mandi_price_rs_qtl": 2350,
            "estimated_cost_cultivation_acre": 25000,
            "gross_return_acre": 56400
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 382.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0087",
        "crop_name": "Wheat (HD 3086 Pusa Gautami) - Select Genotype v3",
        "category": "Cereal",
        "growing_duration_days": 120,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 26,
            "zinc_sulfate_kg_ha": 23.5
        },
        "climate_envelope": {
            "min_temperature_c": 12,
            "max_temperature_c": 26,
            "optimum_temperature_c": 19.0,
            "min_ph": 6.0,
            "max_ph": 7.8,
            "min_annual_rainfall_mm": 450,
            "max_annual_rainfall_mm": 900
        },
        "production_economics": {
            "potential_yield_kg_acre": 2500,
            "benchmark_mandi_price_rs_qtl": 2400,
            "estimated_cost_cultivation_acre": 26000,
            "gross_return_acre": 60000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 382.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0088",
        "crop_name": "Wheat (PBW 343 / Shriram 303) - Select Genotype v3",
        "category": "Cereal",
        "growing_duration_days": 130,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 130,
            "phosphorus_kg_ha": 65,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 27,
            "zinc_sulfate_kg_ha": 24.5
        },
        "climate_envelope": {
            "min_temperature_c": 10,
            "max_temperature_c": 24,
            "optimum_temperature_c": 17.0,
            "min_ph": 6.0,
            "max_ph": 7.8,
            "min_annual_rainfall_mm": 450,
            "max_annual_rainfall_mm": 900
        },
        "production_economics": {
            "potential_yield_kg_acre": 2600,
            "benchmark_mandi_price_rs_qtl": 2300,
            "estimated_cost_cultivation_acre": 27000,
            "gross_return_acre": 59800
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 382.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0089",
        "crop_name": "Wheat (DBW 187 Karan Vandana) - Select Genotype v3",
        "category": "Cereal",
        "growing_duration_days": 120,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 130,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 28,
            "zinc_sulfate_kg_ha": 25.5
        },
        "climate_envelope": {
            "min_temperature_c": 12,
            "max_temperature_c": 27,
            "optimum_temperature_c": 19.5,
            "min_ph": 6.0,
            "max_ph": 7.8,
            "min_annual_rainfall_mm": 400,
            "max_annual_rainfall_mm": 800
        },
        "production_economics": {
            "potential_yield_kg_acre": 2700,
            "benchmark_mandi_price_rs_qtl": 2500,
            "estimated_cost_cultivation_acre": 28000,
            "gross_return_acre": 67500
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 340.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0090",
        "crop_name": "Maize (Pioneer P3396 Hybrid) - Select Genotype v3",
        "category": "Cereal",
        "growing_duration_days": 110,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 140,
            "phosphorus_kg_ha": 65,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 29,
            "zinc_sulfate_kg_ha": 26.5
        },
        "climate_envelope": {
            "min_temperature_c": 18,
            "max_temperature_c": 35,
            "optimum_temperature_c": 26.5,
            "min_ph": 5.8,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 600,
            "max_annual_rainfall_mm": 1200
        },
        "production_economics": {
            "potential_yield_kg_acre": 3600,
            "benchmark_mandi_price_rs_qtl": 2150,
            "estimated_cost_cultivation_acre": 29000,
            "gross_return_acre": 77400
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 510.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0091",
        "crop_name": "Maize (Dekalb 9108 Plus) - Select Genotype v3",
        "category": "Cereal",
        "growing_duration_days": 105,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 130,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 55,
            "sulfur_kg_ha": 30,
            "zinc_sulfate_kg_ha": 12.5
        },
        "climate_envelope": {
            "min_temperature_c": 18,
            "max_temperature_c": 35,
            "optimum_temperature_c": 26.5,
            "min_ph": 5.8,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 550,
            "max_annual_rainfall_mm": 1100
        },
        "production_economics": {
            "potential_yield_kg_acre": 3400,
            "benchmark_mandi_price_rs_qtl": 2150,
            "estimated_cost_cultivation_acre": 12000,
            "gross_return_acre": 73100
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 467.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0092",
        "crop_name": "Maize (Syngenta NK 6240) - Select Genotype v3",
        "category": "Cereal",
        "growing_duration_days": 115,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 140,
            "phosphorus_kg_ha": 70,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 31,
            "zinc_sulfate_kg_ha": 13.5
        },
        "climate_envelope": {
            "min_temperature_c": 18,
            "max_temperature_c": 36,
            "optimum_temperature_c": 27.0,
            "min_ph": 5.8,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 600,
            "max_annual_rainfall_mm": 1200
        },
        "production_economics": {
            "potential_yield_kg_acre": 3800,
            "benchmark_mandi_price_rs_qtl": 2150,
            "estimated_cost_cultivation_acre": 13000,
            "gross_return_acre": 81700
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 510.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0093",
        "crop_name": "Sorghum (CSH 16 Grain Hybrid) - Select Genotype v3",
        "category": "Millet",
        "growing_duration_days": 105,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 80,
            "phosphorus_kg_ha": 40,
            "potassium_kg_ha": 40,
            "sulfur_kg_ha": 32,
            "zinc_sulfate_kg_ha": 14.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 38,
            "optimum_temperature_c": 30.0,
            "min_ph": 6.0,
            "max_ph": 8.2,
            "min_annual_rainfall_mm": 450,
            "max_annual_rainfall_mm": 900
        },
        "production_economics": {
            "potential_yield_kg_acre": 1600,
            "benchmark_mandi_price_rs_qtl": 2900,
            "estimated_cost_cultivation_acre": 14000,
            "gross_return_acre": 46400
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 382.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0094",
        "crop_name": "Pearl Millet (HHB 67 Improved) - Select Genotype v3",
        "category": "Millet",
        "growing_duration_days": 70,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 60,
            "phosphorus_kg_ha": 30,
            "potassium_kg_ha": 30,
            "sulfur_kg_ha": 33,
            "zinc_sulfate_kg_ha": 15.5
        },
        "climate_envelope": {
            "min_temperature_c": 25,
            "max_temperature_c": 42,
            "optimum_temperature_c": 33.5,
            "min_ph": 6.5,
            "max_ph": 8.5,
            "min_annual_rainfall_mm": 300,
            "max_annual_rainfall_mm": 600
        },
        "production_economics": {
            "potential_yield_kg_acre": 1200,
            "benchmark_mandi_price_rs_qtl": 2450,
            "estimated_cost_cultivation_acre": 15000,
            "gross_return_acre": 29400
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 255.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0095",
        "crop_name": "Finger Millet (GPU 28 Ragi) - Select Genotype v3",
        "category": "Millet",
        "growing_duration_days": 110,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 60,
            "phosphorus_kg_ha": 40,
            "potassium_kg_ha": 30,
            "sulfur_kg_ha": 34,
            "zinc_sulfate_kg_ha": 16.5
        },
        "climate_envelope": {
            "min_temperature_c": 18,
            "max_temperature_c": 34,
            "optimum_temperature_c": 26.0,
            "min_ph": 5.5,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 500,
            "max_annual_rainfall_mm": 1000
        },
        "production_economics": {
            "potential_yield_kg_acre": 1300,
            "benchmark_mandi_price_rs_qtl": 3800,
            "estimated_cost_cultivation_acre": 16000,
            "gross_return_acre": 49400
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 425.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0096",
        "crop_name": "Chickpea (JG 11 Desi Gram) - Select Genotype v3",
        "category": "Pulse",
        "growing_duration_days": 95,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 20,
            "phosphorus_kg_ha": 50,
            "potassium_kg_ha": 25,
            "sulfur_kg_ha": 35,
            "zinc_sulfate_kg_ha": 17.5
        },
        "climate_envelope": {
            "min_temperature_c": 15,
            "max_temperature_c": 28,
            "optimum_temperature_c": 21.5,
            "min_ph": 6.0,
            "max_ph": 8.0,
            "min_annual_rainfall_mm": 350,
            "max_annual_rainfall_mm": 700
        },
        "production_economics": {
            "potential_yield_kg_acre": 950,
            "benchmark_mandi_price_rs_qtl": 5400,
            "estimated_cost_cultivation_acre": 17000,
            "gross_return_acre": 51300
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 297.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0097",
        "crop_name": "Chickpea (KAK 2 Kabuli) - Select Genotype v3",
        "category": "Pulse",
        "growing_duration_days": 105,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 25,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 30,
            "sulfur_kg_ha": 36,
            "zinc_sulfate_kg_ha": 18.5
        },
        "climate_envelope": {
            "min_temperature_c": 14,
            "max_temperature_c": 27,
            "optimum_temperature_c": 20.5,
            "min_ph": 6.5,
            "max_ph": 8.2,
            "min_annual_rainfall_mm": 350,
            "max_annual_rainfall_mm": 700
        },
        "production_economics": {
            "potential_yield_kg_acre": 1100,
            "benchmark_mandi_price_rs_qtl": 11000,
            "estimated_cost_cultivation_acre": 18000,
            "gross_return_acre": 121000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 297.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0098",
        "crop_name": "Pigeon Pea (ICPL 87119 Asha) - Select Genotype v3",
        "category": "Pulse",
        "growing_duration_days": 170,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 25,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 30,
            "sulfur_kg_ha": 37,
            "zinc_sulfate_kg_ha": 19.5
        },
        "climate_envelope": {
            "min_temperature_c": 20,
            "max_temperature_c": 36,
            "optimum_temperature_c": 28.0,
            "min_ph": 6.5,
            "max_ph": 8.0,
            "min_annual_rainfall_mm": 700,
            "max_annual_rainfall_mm": 1400
        },
        "production_economics": {
            "potential_yield_kg_acre": 900,
            "benchmark_mandi_price_rs_qtl": 7500,
            "estimated_cost_cultivation_acre": 19000,
            "gross_return_acre": 67500
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 595.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0099",
        "crop_name": "Green Gram (IPM 02-3 / Samrat) - Select Genotype v3",
        "category": "Pulse",
        "growing_duration_days": 65,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 15,
            "phosphorus_kg_ha": 40,
            "potassium_kg_ha": 20,
            "sulfur_kg_ha": 38,
            "zinc_sulfate_kg_ha": 20.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 36,
            "optimum_temperature_c": 29.0,
            "min_ph": 6.2,
            "max_ph": 7.8,
            "min_annual_rainfall_mm": 400,
            "max_annual_rainfall_mm": 800
        },
        "production_economics": {
            "potential_yield_kg_acre": 650,
            "benchmark_mandi_price_rs_qtl": 8500,
            "estimated_cost_cultivation_acre": 20000,
            "gross_return_acre": 55250
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 340.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0100",
        "crop_name": "Black Gram (T-9 / PU 31) - Select Genotype v3",
        "category": "Pulse",
        "growing_duration_days": 75,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 15,
            "phosphorus_kg_ha": 40,
            "potassium_kg_ha": 20,
            "sulfur_kg_ha": 39,
            "zinc_sulfate_kg_ha": 21.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 36,
            "optimum_temperature_c": 29.0,
            "min_ph": 6.0,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 450,
            "max_annual_rainfall_mm": 900
        },
        "production_economics": {
            "potential_yield_kg_acre": 700,
            "benchmark_mandi_price_rs_qtl": 7800,
            "estimated_cost_cultivation_acre": 21000,
            "gross_return_acre": 54600
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 382.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0101",
        "crop_name": "Soybean (JS 335 Central Pride) - Select Genotype v3",
        "category": "Oilseed",
        "growing_duration_days": 95,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 30,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 40,
            "sulfur_kg_ha": 15,
            "zinc_sulfate_kg_ha": 22.5
        },
        "climate_envelope": {
            "min_temperature_c": 20,
            "max_temperature_c": 33,
            "optimum_temperature_c": 26.5,
            "min_ph": 6.0,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 700,
            "max_annual_rainfall_mm": 1400
        },
        "production_economics": {
            "potential_yield_kg_acre": 1100,
            "benchmark_mandi_price_rs_qtl": 4700,
            "estimated_cost_cultivation_acre": 22000,
            "gross_return_acre": 51700
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 595.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0102",
        "crop_name": "Soybean (JS 95-60 Short Duration) - Select Genotype v3",
        "category": "Oilseed",
        "growing_duration_days": 85,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 30,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 40,
            "sulfur_kg_ha": 16,
            "zinc_sulfate_kg_ha": 23.5
        },
        "climate_envelope": {
            "min_temperature_c": 20,
            "max_temperature_c": 33,
            "optimum_temperature_c": 26.5,
            "min_ph": 6.0,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 650,
            "max_annual_rainfall_mm": 1300
        },
        "production_economics": {
            "potential_yield_kg_acre": 1000,
            "benchmark_mandi_price_rs_qtl": 4700,
            "estimated_cost_cultivation_acre": 23000,
            "gross_return_acre": 47000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 552.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0103",
        "crop_name": "Groundnut (TAG 24 Semi-Dwarf) - Select Genotype v3",
        "category": "Oilseed",
        "growing_duration_days": 105,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 25,
            "phosphorus_kg_ha": 50,
            "potassium_kg_ha": 40,
            "sulfur_kg_ha": 17,
            "zinc_sulfate_kg_ha": 24.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 34,
            "optimum_temperature_c": 28.0,
            "min_ph": 5.8,
            "max_ph": 7.2,
            "min_annual_rainfall_mm": 500,
            "max_annual_rainfall_mm": 1000
        },
        "production_economics": {
            "potential_yield_kg_acre": 1250,
            "benchmark_mandi_price_rs_qtl": 6800,
            "estimated_cost_cultivation_acre": 24000,
            "gross_return_acre": 85000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 425.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0104",
        "crop_name": "Groundnut (Kadiri 6 Drought Resilient) - Select Genotype v3",
        "category": "Oilseed",
        "growing_duration_days": 115,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 25,
            "phosphorus_kg_ha": 50,
            "potassium_kg_ha": 40,
            "sulfur_kg_ha": 18,
            "zinc_sulfate_kg_ha": 25.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 34,
            "optimum_temperature_c": 28.0,
            "min_ph": 5.8,
            "max_ph": 7.2,
            "min_annual_rainfall_mm": 450,
            "max_annual_rainfall_mm": 900
        },
        "production_economics": {
            "potential_yield_kg_acre": 1200,
            "benchmark_mandi_price_rs_qtl": 6800,
            "estimated_cost_cultivation_acre": 25000,
            "gross_return_acre": 81600
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 382.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0105",
        "crop_name": "Mustard (Pusa Mustard 30 Zero Erucic) - Select Genotype v3",
        "category": "Oilseed",
        "growing_duration_days": 110,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 60,
            "phosphorus_kg_ha": 30,
            "potassium_kg_ha": 30,
            "sulfur_kg_ha": 19,
            "zinc_sulfate_kg_ha": 26.5
        },
        "climate_envelope": {
            "min_temperature_c": 10,
            "max_temperature_c": 25,
            "optimum_temperature_c": 17.5,
            "min_ph": 6.0,
            "max_ph": 7.8,
            "min_annual_rainfall_mm": 350,
            "max_annual_rainfall_mm": 700
        },
        "production_economics": {
            "potential_yield_kg_acre": 950,
            "benchmark_mandi_price_rs_qtl": 5600,
            "estimated_cost_cultivation_acre": 26000,
            "gross_return_acre": 53200
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 297.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0106",
        "crop_name": "Mustard (Giriraj / DRMRIJ 31) - Select Genotype v3",
        "category": "Oilseed",
        "growing_duration_days": 120,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 80,
            "phosphorus_kg_ha": 40,
            "potassium_kg_ha": 35,
            "sulfur_kg_ha": 20,
            "zinc_sulfate_kg_ha": 12.5
        },
        "climate_envelope": {
            "min_temperature_c": 10,
            "max_temperature_c": 25,
            "optimum_temperature_c": 17.5,
            "min_ph": 6.0,
            "max_ph": 7.8,
            "min_annual_rainfall_mm": 400,
            "max_annual_rainfall_mm": 800
        },
        "production_economics": {
            "potential_yield_kg_acre": 1100,
            "benchmark_mandi_price_rs_qtl": 5600,
            "estimated_cost_cultivation_acre": 27000,
            "gross_return_acre": 61600
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 340.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0107",
        "crop_name": "Cotton (RCH 659 BG II Bt) - Select Genotype v3",
        "category": "Fiber",
        "growing_duration_days": 160,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 21,
            "zinc_sulfate_kg_ha": 13.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 38,
            "optimum_temperature_c": 30.0,
            "min_ph": 6.5,
            "max_ph": 8.2,
            "min_annual_rainfall_mm": 650,
            "max_annual_rainfall_mm": 1300
        },
        "production_economics": {
            "potential_yield_kg_acre": 1400,
            "benchmark_mandi_price_rs_qtl": 7500,
            "estimated_cost_cultivation_acre": 28000,
            "gross_return_acre": 105000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 552.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0108",
        "crop_name": "Cotton (Ajeet 155 BG II) - Select Genotype v3",
        "category": "Fiber",
        "growing_duration_days": 165,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 22,
            "zinc_sulfate_kg_ha": 14.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 38,
            "optimum_temperature_c": 30.0,
            "min_ph": 6.5,
            "max_ph": 8.2,
            "min_annual_rainfall_mm": 650,
            "max_annual_rainfall_mm": 1300
        },
        "production_economics": {
            "potential_yield_kg_acre": 1350,
            "benchmark_mandi_price_rs_qtl": 7500,
            "estimated_cost_cultivation_acre": 29000,
            "gross_return_acre": 101250
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 552.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0109",
        "crop_name": "Sugarcane (Co 0238 High Sugar) - Select Genotype v3",
        "category": "Commercial",
        "growing_duration_days": 330,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 220,
            "phosphorus_kg_ha": 80,
            "potassium_kg_ha": 120,
            "sulfur_kg_ha": 23,
            "zinc_sulfate_kg_ha": 15.5
        },
        "climate_envelope": {
            "min_temperature_c": 24,
            "max_temperature_c": 38,
            "optimum_temperature_c": 31.0,
            "min_ph": 6.2,
            "max_ph": 7.8,
            "min_annual_rainfall_mm": 1600,
            "max_annual_rainfall_mm": 3200
        },
        "production_economics": {
            "potential_yield_kg_acre": 42000,
            "benchmark_mandi_price_rs_qtl": 340,
            "estimated_cost_cultivation_acre": 12000,
            "gross_return_acre": 142800
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1360.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0110",
        "crop_name": "Sugarcane (Co 86032 Wonder Cane) - Select Genotype v3",
        "category": "Commercial",
        "growing_duration_days": 340,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 240,
            "phosphorus_kg_ha": 80,
            "potassium_kg_ha": 120,
            "sulfur_kg_ha": 24,
            "zinc_sulfate_kg_ha": 16.5
        },
        "climate_envelope": {
            "min_temperature_c": 24,
            "max_temperature_c": 38,
            "optimum_temperature_c": 31.0,
            "min_ph": 6.2,
            "max_ph": 7.8,
            "min_annual_rainfall_mm": 1600,
            "max_annual_rainfall_mm": 3200
        },
        "production_economics": {
            "potential_yield_kg_acre": 45000,
            "benchmark_mandi_price_rs_qtl": 340,
            "estimated_cost_cultivation_acre": 13000,
            "gross_return_acre": 153000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1360.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0111",
        "crop_name": "Tomato (Seminis Abhinav Hybrid) - Select Genotype v3",
        "category": "Vegetable",
        "growing_duration_days": 105,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 90,
            "sulfur_kg_ha": 25,
            "zinc_sulfate_kg_ha": 17.5
        },
        "climate_envelope": {
            "min_temperature_c": 18,
            "max_temperature_c": 32,
            "optimum_temperature_c": 25.0,
            "min_ph": 6.0,
            "max_ph": 7.2,
            "min_annual_rainfall_mm": 500,
            "max_annual_rainfall_mm": 1000
        },
        "production_economics": {
            "potential_yield_kg_acre": 16000,
            "benchmark_mandi_price_rs_qtl": 2200,
            "estimated_cost_cultivation_acre": 14000,
            "gross_return_acre": 352000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 425.0,
            "preferred_method": "Drip Irrigation with 1.2 LPH emitters"
        }
    },
    {
        "crop_id": "CROP-0112",
        "crop_name": "Tomato (Syngenta TO-1057) - Select Genotype v3",
        "category": "Vegetable",
        "growing_duration_days": 110,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 90,
            "sulfur_kg_ha": 26,
            "zinc_sulfate_kg_ha": 18.5
        },
        "climate_envelope": {
            "min_temperature_c": 18,
            "max_temperature_c": 32,
            "optimum_temperature_c": 25.0,
            "min_ph": 6.0,
            "max_ph": 7.2,
            "min_annual_rainfall_mm": 500,
            "max_annual_rainfall_mm": 1000
        },
        "production_economics": {
            "potential_yield_kg_acre": 17000,
            "benchmark_mandi_price_rs_qtl": 2200,
            "estimated_cost_cultivation_acre": 15000,
            "gross_return_acre": 374000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 425.0,
            "preferred_method": "Drip Irrigation with 1.2 LPH emitters"
        }
    },
    {
        "crop_id": "CROP-0113",
        "crop_name": "Chilli (Syngenta Armoor Hot) - Select Genotype v3",
        "category": "Spice",
        "growing_duration_days": 155,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 80,
            "sulfur_kg_ha": 27,
            "zinc_sulfate_kg_ha": 19.5
        },
        "climate_envelope": {
            "min_temperature_c": 20,
            "max_temperature_c": 35,
            "optimum_temperature_c": 27.5,
            "min_ph": 6.0,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 750,
            "max_annual_rainfall_mm": 1500
        },
        "production_economics": {
            "potential_yield_kg_acre": 2600,
            "benchmark_mandi_price_rs_qtl": 19500,
            "estimated_cost_cultivation_acre": 16000,
            "gross_return_acre": 507000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 637.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0114",
        "crop_name": "Chilli (US 341 Red Teja) - Select Genotype v3",
        "category": "Spice",
        "growing_duration_days": 160,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 80,
            "sulfur_kg_ha": 28,
            "zinc_sulfate_kg_ha": 20.5
        },
        "climate_envelope": {
            "min_temperature_c": 20,
            "max_temperature_c": 35,
            "optimum_temperature_c": 27.5,
            "min_ph": 6.0,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 750,
            "max_annual_rainfall_mm": 1500
        },
        "production_economics": {
            "potential_yield_kg_acre": 2700,
            "benchmark_mandi_price_rs_qtl": 21000,
            "estimated_cost_cultivation_acre": 17000,
            "gross_return_acre": 567000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 637.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0115",
        "crop_name": "Potato (Kufri Jyoti Table Potato) - Select Genotype v3",
        "category": "Vegetable",
        "growing_duration_days": 90,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 100,
            "sulfur_kg_ha": 29,
            "zinc_sulfate_kg_ha": 21.5
        },
        "climate_envelope": {
            "min_temperature_c": 14,
            "max_temperature_c": 24,
            "optimum_temperature_c": 19.0,
            "min_ph": 5.2,
            "max_ph": 6.5,
            "min_annual_rainfall_mm": 500,
            "max_annual_rainfall_mm": 1000
        },
        "production_economics": {
            "potential_yield_kg_acre": 13000,
            "benchmark_mandi_price_rs_qtl": 1500,
            "estimated_cost_cultivation_acre": 18000,
            "gross_return_acre": 195000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 425.0,
            "preferred_method": "Drip Irrigation with 1.2 LPH emitters"
        }
    },
    {
        "crop_id": "CROP-0116",
        "crop_name": "Potato (Kufri Chipsona Processing) - Select Genotype v3",
        "category": "Vegetable",
        "growing_duration_days": 100,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 130,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 110,
            "sulfur_kg_ha": 30,
            "zinc_sulfate_kg_ha": 22.5
        },
        "climate_envelope": {
            "min_temperature_c": 14,
            "max_temperature_c": 24,
            "optimum_temperature_c": 19.0,
            "min_ph": 5.2,
            "max_ph": 6.5,
            "min_annual_rainfall_mm": 500,
            "max_annual_rainfall_mm": 1000
        },
        "production_economics": {
            "potential_yield_kg_acre": 14000,
            "benchmark_mandi_price_rs_qtl": 1800,
            "estimated_cost_cultivation_acre": 19000,
            "gross_return_acre": 252000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 425.0,
            "preferred_method": "Drip Irrigation with 1.2 LPH emitters"
        }
    },
    {
        "crop_id": "CROP-0117",
        "crop_name": "Onion (Bhima Super Red) - Select Genotype v3",
        "category": "Vegetable",
        "growing_duration_days": 125,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 90,
            "phosphorus_kg_ha": 45,
            "potassium_kg_ha": 50,
            "sulfur_kg_ha": 31,
            "zinc_sulfate_kg_ha": 23.5
        },
        "climate_envelope": {
            "min_temperature_c": 13,
            "max_temperature_c": 30,
            "optimum_temperature_c": 21.5,
            "min_ph": 6.0,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 550,
            "max_annual_rainfall_mm": 1100
        },
        "production_economics": {
            "potential_yield_kg_acre": 11500,
            "benchmark_mandi_price_rs_qtl": 2200,
            "estimated_cost_cultivation_acre": 20000,
            "gross_return_acre": 253000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 467.5,
            "preferred_method": "Drip Irrigation with 1.2 LPH emitters"
        }
    },
    {
        "crop_id": "CROP-0118",
        "crop_name": "Garlic (Yamuna Safed G-1) - Select Genotype v3",
        "category": "Spice",
        "growing_duration_days": 140,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 80,
            "phosphorus_kg_ha": 40,
            "potassium_kg_ha": 40,
            "sulfur_kg_ha": 32,
            "zinc_sulfate_kg_ha": 24.5
        },
        "climate_envelope": {
            "min_temperature_c": 12,
            "max_temperature_c": 25,
            "optimum_temperature_c": 18.5,
            "min_ph": 6.0,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 450,
            "max_annual_rainfall_mm": 900
        },
        "production_economics": {
            "potential_yield_kg_acre": 4200,
            "benchmark_mandi_price_rs_qtl": 14000,
            "estimated_cost_cultivation_acre": 21000,
            "gross_return_acre": 588000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 382.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0119",
        "crop_name": "Turmeric (Prathibha IISR) - Select Genotype v3",
        "category": "Spice",
        "growing_duration_days": 225,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 100,
            "phosphorus_kg_ha": 50,
            "potassium_kg_ha": 90,
            "sulfur_kg_ha": 33,
            "zinc_sulfate_kg_ha": 25.5
        },
        "climate_envelope": {
            "min_temperature_c": 20,
            "max_temperature_c": 35,
            "optimum_temperature_c": 27.5,
            "min_ph": 5.5,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 1400,
            "max_annual_rainfall_mm": 2800
        },
        "production_economics": {
            "potential_yield_kg_acre": 9500,
            "benchmark_mandi_price_rs_qtl": 14500,
            "estimated_cost_cultivation_acre": 22000,
            "gross_return_acre": 1377500
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1190.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0120",
        "crop_name": "Ginger (Varada IISR) - Select Genotype v3",
        "category": "Spice",
        "growing_duration_days": 220,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 90,
            "phosphorus_kg_ha": 50,
            "potassium_kg_ha": 90,
            "sulfur_kg_ha": 34,
            "zinc_sulfate_kg_ha": 26.5
        },
        "climate_envelope": {
            "min_temperature_c": 20,
            "max_temperature_c": 32,
            "optimum_temperature_c": 26.0,
            "min_ph": 5.5,
            "max_ph": 6.5,
            "min_annual_rainfall_mm": 1500,
            "max_annual_rainfall_mm": 3000
        },
        "production_economics": {
            "potential_yield_kg_acre": 8500,
            "benchmark_mandi_price_rs_qtl": 9000,
            "estimated_cost_cultivation_acre": 23000,
            "gross_return_acre": 765000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1275.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0121",
        "crop_name": "Rice (Pusa Basmati 1121) - Select Genotype v4",
        "category": "Cereal",
        "growing_duration_days": 140,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 90,
            "phosphorus_kg_ha": 45,
            "potassium_kg_ha": 45,
            "sulfur_kg_ha": 35,
            "zinc_sulfate_kg_ha": 12.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 36,
            "optimum_temperature_c": 29.0,
            "min_ph": 5.5,
            "max_ph": 7.2,
            "min_annual_rainfall_mm": 1600,
            "max_annual_rainfall_mm": 3200
        },
        "production_economics": {
            "potential_yield_kg_acre": 2200,
            "benchmark_mandi_price_rs_qtl": 2400,
            "estimated_cost_cultivation_acre": 24000,
            "gross_return_acre": 52800
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1360.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0122",
        "crop_name": "Rice (Pusa Basmati 1509) - Select Genotype v4",
        "category": "Cereal",
        "growing_duration_days": 120,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 85,
            "phosphorus_kg_ha": 40,
            "potassium_kg_ha": 40,
            "sulfur_kg_ha": 36,
            "zinc_sulfate_kg_ha": 13.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 38,
            "optimum_temperature_c": 30.0,
            "min_ph": 5.5,
            "max_ph": 7.2,
            "min_annual_rainfall_mm": 1400,
            "max_annual_rainfall_mm": 2800
        },
        "production_economics": {
            "potential_yield_kg_acre": 2400,
            "benchmark_mandi_price_rs_qtl": 2500,
            "estimated_cost_cultivation_acre": 25000,
            "gross_return_acre": 60000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1190.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0123",
        "crop_name": "Rice (BPT 5204 / Samba Mahsuri) - Select Genotype v4",
        "category": "Cereal",
        "growing_duration_days": 150,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 100,
            "phosphorus_kg_ha": 50,
            "potassium_kg_ha": 50,
            "sulfur_kg_ha": 37,
            "zinc_sulfate_kg_ha": 14.5
        },
        "climate_envelope": {
            "min_temperature_c": 20,
            "max_temperature_c": 36,
            "optimum_temperature_c": 28.0,
            "min_ph": 6.0,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 1500,
            "max_annual_rainfall_mm": 3000
        },
        "production_economics": {
            "potential_yield_kg_acre": 2600,
            "benchmark_mandi_price_rs_qtl": 2700,
            "estimated_cost_cultivation_acre": 26000,
            "gross_return_acre": 70200
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1275.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0124",
        "crop_name": "Rice (MTU 1010 / Cottondora Sannalu) - Select Genotype v4",
        "category": "Cereal",
        "growing_duration_days": 125,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 38,
            "zinc_sulfate_kg_ha": 15.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 38,
            "optimum_temperature_c": 30.0,
            "min_ph": 5.5,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 1300,
            "max_annual_rainfall_mm": 2600
        },
        "production_economics": {
            "potential_yield_kg_acre": 3100,
            "benchmark_mandi_price_rs_qtl": 2200,
            "estimated_cost_cultivation_acre": 27000,
            "gross_return_acre": 68200
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1105.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0125",
        "crop_name": "Rice (IR 64 High Yield) - Select Genotype v4",
        "category": "Cereal",
        "growing_duration_days": 120,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 39,
            "zinc_sulfate_kg_ha": 16.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 38,
            "optimum_temperature_c": 30.0,
            "min_ph": 5.5,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 1400,
            "max_annual_rainfall_mm": 2800
        },
        "production_economics": {
            "potential_yield_kg_acre": 3200,
            "benchmark_mandi_price_rs_qtl": 2100,
            "estimated_cost_cultivation_acre": 28000,
            "gross_return_acre": 67200
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1190.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0126",
        "crop_name": "Wheat (HD 2967 High Yield) - Select Genotype v4",
        "category": "Cereal",
        "growing_duration_days": 125,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 15,
            "zinc_sulfate_kg_ha": 17.5
        },
        "climate_envelope": {
            "min_temperature_c": 12,
            "max_temperature_c": 25,
            "optimum_temperature_c": 18.5,
            "min_ph": 6.0,
            "max_ph": 7.8,
            "min_annual_rainfall_mm": 450,
            "max_annual_rainfall_mm": 900
        },
        "production_economics": {
            "potential_yield_kg_acre": 2400,
            "benchmark_mandi_price_rs_qtl": 2350,
            "estimated_cost_cultivation_acre": 29000,
            "gross_return_acre": 56400
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 382.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0127",
        "crop_name": "Wheat (HD 3086 Pusa Gautami) - Select Genotype v4",
        "category": "Cereal",
        "growing_duration_days": 120,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 16,
            "zinc_sulfate_kg_ha": 18.5
        },
        "climate_envelope": {
            "min_temperature_c": 12,
            "max_temperature_c": 26,
            "optimum_temperature_c": 19.0,
            "min_ph": 6.0,
            "max_ph": 7.8,
            "min_annual_rainfall_mm": 450,
            "max_annual_rainfall_mm": 900
        },
        "production_economics": {
            "potential_yield_kg_acre": 2500,
            "benchmark_mandi_price_rs_qtl": 2400,
            "estimated_cost_cultivation_acre": 12000,
            "gross_return_acre": 60000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 382.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0128",
        "crop_name": "Wheat (PBW 343 / Shriram 303) - Select Genotype v4",
        "category": "Cereal",
        "growing_duration_days": 130,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 130,
            "phosphorus_kg_ha": 65,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 17,
            "zinc_sulfate_kg_ha": 19.5
        },
        "climate_envelope": {
            "min_temperature_c": 10,
            "max_temperature_c": 24,
            "optimum_temperature_c": 17.0,
            "min_ph": 6.0,
            "max_ph": 7.8,
            "min_annual_rainfall_mm": 450,
            "max_annual_rainfall_mm": 900
        },
        "production_economics": {
            "potential_yield_kg_acre": 2600,
            "benchmark_mandi_price_rs_qtl": 2300,
            "estimated_cost_cultivation_acre": 13000,
            "gross_return_acre": 59800
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 382.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0129",
        "crop_name": "Wheat (DBW 187 Karan Vandana) - Select Genotype v4",
        "category": "Cereal",
        "growing_duration_days": 120,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 130,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 18,
            "zinc_sulfate_kg_ha": 20.5
        },
        "climate_envelope": {
            "min_temperature_c": 12,
            "max_temperature_c": 27,
            "optimum_temperature_c": 19.5,
            "min_ph": 6.0,
            "max_ph": 7.8,
            "min_annual_rainfall_mm": 400,
            "max_annual_rainfall_mm": 800
        },
        "production_economics": {
            "potential_yield_kg_acre": 2700,
            "benchmark_mandi_price_rs_qtl": 2500,
            "estimated_cost_cultivation_acre": 14000,
            "gross_return_acre": 67500
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 340.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0130",
        "crop_name": "Maize (Pioneer P3396 Hybrid) - Select Genotype v4",
        "category": "Cereal",
        "growing_duration_days": 110,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 140,
            "phosphorus_kg_ha": 65,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 19,
            "zinc_sulfate_kg_ha": 21.5
        },
        "climate_envelope": {
            "min_temperature_c": 18,
            "max_temperature_c": 35,
            "optimum_temperature_c": 26.5,
            "min_ph": 5.8,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 600,
            "max_annual_rainfall_mm": 1200
        },
        "production_economics": {
            "potential_yield_kg_acre": 3600,
            "benchmark_mandi_price_rs_qtl": 2150,
            "estimated_cost_cultivation_acre": 15000,
            "gross_return_acre": 77400
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 510.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0131",
        "crop_name": "Maize (Dekalb 9108 Plus) - Select Genotype v4",
        "category": "Cereal",
        "growing_duration_days": 105,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 130,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 55,
            "sulfur_kg_ha": 20,
            "zinc_sulfate_kg_ha": 22.5
        },
        "climate_envelope": {
            "min_temperature_c": 18,
            "max_temperature_c": 35,
            "optimum_temperature_c": 26.5,
            "min_ph": 5.8,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 550,
            "max_annual_rainfall_mm": 1100
        },
        "production_economics": {
            "potential_yield_kg_acre": 3400,
            "benchmark_mandi_price_rs_qtl": 2150,
            "estimated_cost_cultivation_acre": 16000,
            "gross_return_acre": 73100
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 467.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0132",
        "crop_name": "Maize (Syngenta NK 6240) - Select Genotype v4",
        "category": "Cereal",
        "growing_duration_days": 115,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 140,
            "phosphorus_kg_ha": 70,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 21,
            "zinc_sulfate_kg_ha": 23.5
        },
        "climate_envelope": {
            "min_temperature_c": 18,
            "max_temperature_c": 36,
            "optimum_temperature_c": 27.0,
            "min_ph": 5.8,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 600,
            "max_annual_rainfall_mm": 1200
        },
        "production_economics": {
            "potential_yield_kg_acre": 3800,
            "benchmark_mandi_price_rs_qtl": 2150,
            "estimated_cost_cultivation_acre": 17000,
            "gross_return_acre": 81700
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 510.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0133",
        "crop_name": "Sorghum (CSH 16 Grain Hybrid) - Select Genotype v4",
        "category": "Millet",
        "growing_duration_days": 105,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 80,
            "phosphorus_kg_ha": 40,
            "potassium_kg_ha": 40,
            "sulfur_kg_ha": 22,
            "zinc_sulfate_kg_ha": 24.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 38,
            "optimum_temperature_c": 30.0,
            "min_ph": 6.0,
            "max_ph": 8.2,
            "min_annual_rainfall_mm": 450,
            "max_annual_rainfall_mm": 900
        },
        "production_economics": {
            "potential_yield_kg_acre": 1600,
            "benchmark_mandi_price_rs_qtl": 2900,
            "estimated_cost_cultivation_acre": 18000,
            "gross_return_acre": 46400
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 382.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0134",
        "crop_name": "Pearl Millet (HHB 67 Improved) - Select Genotype v4",
        "category": "Millet",
        "growing_duration_days": 70,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 60,
            "phosphorus_kg_ha": 30,
            "potassium_kg_ha": 30,
            "sulfur_kg_ha": 23,
            "zinc_sulfate_kg_ha": 25.5
        },
        "climate_envelope": {
            "min_temperature_c": 25,
            "max_temperature_c": 42,
            "optimum_temperature_c": 33.5,
            "min_ph": 6.5,
            "max_ph": 8.5,
            "min_annual_rainfall_mm": 300,
            "max_annual_rainfall_mm": 600
        },
        "production_economics": {
            "potential_yield_kg_acre": 1200,
            "benchmark_mandi_price_rs_qtl": 2450,
            "estimated_cost_cultivation_acre": 19000,
            "gross_return_acre": 29400
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 255.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0135",
        "crop_name": "Finger Millet (GPU 28 Ragi) - Select Genotype v4",
        "category": "Millet",
        "growing_duration_days": 110,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 60,
            "phosphorus_kg_ha": 40,
            "potassium_kg_ha": 30,
            "sulfur_kg_ha": 24,
            "zinc_sulfate_kg_ha": 26.5
        },
        "climate_envelope": {
            "min_temperature_c": 18,
            "max_temperature_c": 34,
            "optimum_temperature_c": 26.0,
            "min_ph": 5.5,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 500,
            "max_annual_rainfall_mm": 1000
        },
        "production_economics": {
            "potential_yield_kg_acre": 1300,
            "benchmark_mandi_price_rs_qtl": 3800,
            "estimated_cost_cultivation_acre": 20000,
            "gross_return_acre": 49400
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 425.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0136",
        "crop_name": "Chickpea (JG 11 Desi Gram) - Select Genotype v4",
        "category": "Pulse",
        "growing_duration_days": 95,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 20,
            "phosphorus_kg_ha": 50,
            "potassium_kg_ha": 25,
            "sulfur_kg_ha": 25,
            "zinc_sulfate_kg_ha": 12.5
        },
        "climate_envelope": {
            "min_temperature_c": 15,
            "max_temperature_c": 28,
            "optimum_temperature_c": 21.5,
            "min_ph": 6.0,
            "max_ph": 8.0,
            "min_annual_rainfall_mm": 350,
            "max_annual_rainfall_mm": 700
        },
        "production_economics": {
            "potential_yield_kg_acre": 950,
            "benchmark_mandi_price_rs_qtl": 5400,
            "estimated_cost_cultivation_acre": 21000,
            "gross_return_acre": 51300
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 297.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0137",
        "crop_name": "Chickpea (KAK 2 Kabuli) - Select Genotype v4",
        "category": "Pulse",
        "growing_duration_days": 105,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 25,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 30,
            "sulfur_kg_ha": 26,
            "zinc_sulfate_kg_ha": 13.5
        },
        "climate_envelope": {
            "min_temperature_c": 14,
            "max_temperature_c": 27,
            "optimum_temperature_c": 20.5,
            "min_ph": 6.5,
            "max_ph": 8.2,
            "min_annual_rainfall_mm": 350,
            "max_annual_rainfall_mm": 700
        },
        "production_economics": {
            "potential_yield_kg_acre": 1100,
            "benchmark_mandi_price_rs_qtl": 11000,
            "estimated_cost_cultivation_acre": 22000,
            "gross_return_acre": 121000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 297.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0138",
        "crop_name": "Pigeon Pea (ICPL 87119 Asha) - Select Genotype v4",
        "category": "Pulse",
        "growing_duration_days": 170,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 25,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 30,
            "sulfur_kg_ha": 27,
            "zinc_sulfate_kg_ha": 14.5
        },
        "climate_envelope": {
            "min_temperature_c": 20,
            "max_temperature_c": 36,
            "optimum_temperature_c": 28.0,
            "min_ph": 6.5,
            "max_ph": 8.0,
            "min_annual_rainfall_mm": 700,
            "max_annual_rainfall_mm": 1400
        },
        "production_economics": {
            "potential_yield_kg_acre": 900,
            "benchmark_mandi_price_rs_qtl": 7500,
            "estimated_cost_cultivation_acre": 23000,
            "gross_return_acre": 67500
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 595.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0139",
        "crop_name": "Green Gram (IPM 02-3 / Samrat) - Select Genotype v4",
        "category": "Pulse",
        "growing_duration_days": 65,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 15,
            "phosphorus_kg_ha": 40,
            "potassium_kg_ha": 20,
            "sulfur_kg_ha": 28,
            "zinc_sulfate_kg_ha": 15.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 36,
            "optimum_temperature_c": 29.0,
            "min_ph": 6.2,
            "max_ph": 7.8,
            "min_annual_rainfall_mm": 400,
            "max_annual_rainfall_mm": 800
        },
        "production_economics": {
            "potential_yield_kg_acre": 650,
            "benchmark_mandi_price_rs_qtl": 8500,
            "estimated_cost_cultivation_acre": 24000,
            "gross_return_acre": 55250
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 340.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0140",
        "crop_name": "Black Gram (T-9 / PU 31) - Select Genotype v4",
        "category": "Pulse",
        "growing_duration_days": 75,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 15,
            "phosphorus_kg_ha": 40,
            "potassium_kg_ha": 20,
            "sulfur_kg_ha": 29,
            "zinc_sulfate_kg_ha": 16.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 36,
            "optimum_temperature_c": 29.0,
            "min_ph": 6.0,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 450,
            "max_annual_rainfall_mm": 900
        },
        "production_economics": {
            "potential_yield_kg_acre": 700,
            "benchmark_mandi_price_rs_qtl": 7800,
            "estimated_cost_cultivation_acre": 25000,
            "gross_return_acre": 54600
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 382.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0141",
        "crop_name": "Soybean (JS 335 Central Pride) - Select Genotype v4",
        "category": "Oilseed",
        "growing_duration_days": 95,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 30,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 40,
            "sulfur_kg_ha": 30,
            "zinc_sulfate_kg_ha": 17.5
        },
        "climate_envelope": {
            "min_temperature_c": 20,
            "max_temperature_c": 33,
            "optimum_temperature_c": 26.5,
            "min_ph": 6.0,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 700,
            "max_annual_rainfall_mm": 1400
        },
        "production_economics": {
            "potential_yield_kg_acre": 1100,
            "benchmark_mandi_price_rs_qtl": 4700,
            "estimated_cost_cultivation_acre": 26000,
            "gross_return_acre": 51700
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 595.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0142",
        "crop_name": "Soybean (JS 95-60 Short Duration) - Select Genotype v4",
        "category": "Oilseed",
        "growing_duration_days": 85,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 30,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 40,
            "sulfur_kg_ha": 31,
            "zinc_sulfate_kg_ha": 18.5
        },
        "climate_envelope": {
            "min_temperature_c": 20,
            "max_temperature_c": 33,
            "optimum_temperature_c": 26.5,
            "min_ph": 6.0,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 650,
            "max_annual_rainfall_mm": 1300
        },
        "production_economics": {
            "potential_yield_kg_acre": 1000,
            "benchmark_mandi_price_rs_qtl": 4700,
            "estimated_cost_cultivation_acre": 27000,
            "gross_return_acre": 47000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 552.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0143",
        "crop_name": "Groundnut (TAG 24 Semi-Dwarf) - Select Genotype v4",
        "category": "Oilseed",
        "growing_duration_days": 105,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 25,
            "phosphorus_kg_ha": 50,
            "potassium_kg_ha": 40,
            "sulfur_kg_ha": 32,
            "zinc_sulfate_kg_ha": 19.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 34,
            "optimum_temperature_c": 28.0,
            "min_ph": 5.8,
            "max_ph": 7.2,
            "min_annual_rainfall_mm": 500,
            "max_annual_rainfall_mm": 1000
        },
        "production_economics": {
            "potential_yield_kg_acre": 1250,
            "benchmark_mandi_price_rs_qtl": 6800,
            "estimated_cost_cultivation_acre": 28000,
            "gross_return_acre": 85000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 425.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0144",
        "crop_name": "Groundnut (Kadiri 6 Drought Resilient) - Select Genotype v4",
        "category": "Oilseed",
        "growing_duration_days": 115,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 25,
            "phosphorus_kg_ha": 50,
            "potassium_kg_ha": 40,
            "sulfur_kg_ha": 33,
            "zinc_sulfate_kg_ha": 20.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 34,
            "optimum_temperature_c": 28.0,
            "min_ph": 5.8,
            "max_ph": 7.2,
            "min_annual_rainfall_mm": 450,
            "max_annual_rainfall_mm": 900
        },
        "production_economics": {
            "potential_yield_kg_acre": 1200,
            "benchmark_mandi_price_rs_qtl": 6800,
            "estimated_cost_cultivation_acre": 29000,
            "gross_return_acre": 81600
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 382.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0145",
        "crop_name": "Mustard (Pusa Mustard 30 Zero Erucic) - Select Genotype v4",
        "category": "Oilseed",
        "growing_duration_days": 110,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 60,
            "phosphorus_kg_ha": 30,
            "potassium_kg_ha": 30,
            "sulfur_kg_ha": 34,
            "zinc_sulfate_kg_ha": 21.5
        },
        "climate_envelope": {
            "min_temperature_c": 10,
            "max_temperature_c": 25,
            "optimum_temperature_c": 17.5,
            "min_ph": 6.0,
            "max_ph": 7.8,
            "min_annual_rainfall_mm": 350,
            "max_annual_rainfall_mm": 700
        },
        "production_economics": {
            "potential_yield_kg_acre": 950,
            "benchmark_mandi_price_rs_qtl": 5600,
            "estimated_cost_cultivation_acre": 12000,
            "gross_return_acre": 53200
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 297.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0146",
        "crop_name": "Mustard (Giriraj / DRMRIJ 31) - Select Genotype v4",
        "category": "Oilseed",
        "growing_duration_days": 120,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 80,
            "phosphorus_kg_ha": 40,
            "potassium_kg_ha": 35,
            "sulfur_kg_ha": 35,
            "zinc_sulfate_kg_ha": 22.5
        },
        "climate_envelope": {
            "min_temperature_c": 10,
            "max_temperature_c": 25,
            "optimum_temperature_c": 17.5,
            "min_ph": 6.0,
            "max_ph": 7.8,
            "min_annual_rainfall_mm": 400,
            "max_annual_rainfall_mm": 800
        },
        "production_economics": {
            "potential_yield_kg_acre": 1100,
            "benchmark_mandi_price_rs_qtl": 5600,
            "estimated_cost_cultivation_acre": 13000,
            "gross_return_acre": 61600
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 340.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0147",
        "crop_name": "Cotton (RCH 659 BG II Bt) - Select Genotype v4",
        "category": "Fiber",
        "growing_duration_days": 160,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 36,
            "zinc_sulfate_kg_ha": 23.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 38,
            "optimum_temperature_c": 30.0,
            "min_ph": 6.5,
            "max_ph": 8.2,
            "min_annual_rainfall_mm": 650,
            "max_annual_rainfall_mm": 1300
        },
        "production_economics": {
            "potential_yield_kg_acre": 1400,
            "benchmark_mandi_price_rs_qtl": 7500,
            "estimated_cost_cultivation_acre": 14000,
            "gross_return_acre": 105000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 552.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0148",
        "crop_name": "Cotton (Ajeet 155 BG II) - Select Genotype v4",
        "category": "Fiber",
        "growing_duration_days": 165,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 37,
            "zinc_sulfate_kg_ha": 24.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 38,
            "optimum_temperature_c": 30.0,
            "min_ph": 6.5,
            "max_ph": 8.2,
            "min_annual_rainfall_mm": 650,
            "max_annual_rainfall_mm": 1300
        },
        "production_economics": {
            "potential_yield_kg_acre": 1350,
            "benchmark_mandi_price_rs_qtl": 7500,
            "estimated_cost_cultivation_acre": 15000,
            "gross_return_acre": 101250
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 552.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0149",
        "crop_name": "Sugarcane (Co 0238 High Sugar) - Select Genotype v4",
        "category": "Commercial",
        "growing_duration_days": 330,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 220,
            "phosphorus_kg_ha": 80,
            "potassium_kg_ha": 120,
            "sulfur_kg_ha": 38,
            "zinc_sulfate_kg_ha": 25.5
        },
        "climate_envelope": {
            "min_temperature_c": 24,
            "max_temperature_c": 38,
            "optimum_temperature_c": 31.0,
            "min_ph": 6.2,
            "max_ph": 7.8,
            "min_annual_rainfall_mm": 1600,
            "max_annual_rainfall_mm": 3200
        },
        "production_economics": {
            "potential_yield_kg_acre": 42000,
            "benchmark_mandi_price_rs_qtl": 340,
            "estimated_cost_cultivation_acre": 16000,
            "gross_return_acre": 142800
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1360.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0150",
        "crop_name": "Sugarcane (Co 86032 Wonder Cane) - Select Genotype v4",
        "category": "Commercial",
        "growing_duration_days": 340,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 240,
            "phosphorus_kg_ha": 80,
            "potassium_kg_ha": 120,
            "sulfur_kg_ha": 39,
            "zinc_sulfate_kg_ha": 26.5
        },
        "climate_envelope": {
            "min_temperature_c": 24,
            "max_temperature_c": 38,
            "optimum_temperature_c": 31.0,
            "min_ph": 6.2,
            "max_ph": 7.8,
            "min_annual_rainfall_mm": 1600,
            "max_annual_rainfall_mm": 3200
        },
        "production_economics": {
            "potential_yield_kg_acre": 45000,
            "benchmark_mandi_price_rs_qtl": 340,
            "estimated_cost_cultivation_acre": 17000,
            "gross_return_acre": 153000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1360.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0151",
        "crop_name": "Tomato (Seminis Abhinav Hybrid) - Select Genotype v4",
        "category": "Vegetable",
        "growing_duration_days": 105,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 90,
            "sulfur_kg_ha": 15,
            "zinc_sulfate_kg_ha": 12.5
        },
        "climate_envelope": {
            "min_temperature_c": 18,
            "max_temperature_c": 32,
            "optimum_temperature_c": 25.0,
            "min_ph": 6.0,
            "max_ph": 7.2,
            "min_annual_rainfall_mm": 500,
            "max_annual_rainfall_mm": 1000
        },
        "production_economics": {
            "potential_yield_kg_acre": 16000,
            "benchmark_mandi_price_rs_qtl": 2200,
            "estimated_cost_cultivation_acre": 18000,
            "gross_return_acre": 352000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 425.0,
            "preferred_method": "Drip Irrigation with 1.2 LPH emitters"
        }
    },
    {
        "crop_id": "CROP-0152",
        "crop_name": "Tomato (Syngenta TO-1057) - Select Genotype v4",
        "category": "Vegetable",
        "growing_duration_days": 110,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 90,
            "sulfur_kg_ha": 16,
            "zinc_sulfate_kg_ha": 13.5
        },
        "climate_envelope": {
            "min_temperature_c": 18,
            "max_temperature_c": 32,
            "optimum_temperature_c": 25.0,
            "min_ph": 6.0,
            "max_ph": 7.2,
            "min_annual_rainfall_mm": 500,
            "max_annual_rainfall_mm": 1000
        },
        "production_economics": {
            "potential_yield_kg_acre": 17000,
            "benchmark_mandi_price_rs_qtl": 2200,
            "estimated_cost_cultivation_acre": 19000,
            "gross_return_acre": 374000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 425.0,
            "preferred_method": "Drip Irrigation with 1.2 LPH emitters"
        }
    },
    {
        "crop_id": "CROP-0153",
        "crop_name": "Chilli (Syngenta Armoor Hot) - Select Genotype v4",
        "category": "Spice",
        "growing_duration_days": 155,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 80,
            "sulfur_kg_ha": 17,
            "zinc_sulfate_kg_ha": 14.5
        },
        "climate_envelope": {
            "min_temperature_c": 20,
            "max_temperature_c": 35,
            "optimum_temperature_c": 27.5,
            "min_ph": 6.0,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 750,
            "max_annual_rainfall_mm": 1500
        },
        "production_economics": {
            "potential_yield_kg_acre": 2600,
            "benchmark_mandi_price_rs_qtl": 19500,
            "estimated_cost_cultivation_acre": 20000,
            "gross_return_acre": 507000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 637.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0154",
        "crop_name": "Chilli (US 341 Red Teja) - Select Genotype v4",
        "category": "Spice",
        "growing_duration_days": 160,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 80,
            "sulfur_kg_ha": 18,
            "zinc_sulfate_kg_ha": 15.5
        },
        "climate_envelope": {
            "min_temperature_c": 20,
            "max_temperature_c": 35,
            "optimum_temperature_c": 27.5,
            "min_ph": 6.0,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 750,
            "max_annual_rainfall_mm": 1500
        },
        "production_economics": {
            "potential_yield_kg_acre": 2700,
            "benchmark_mandi_price_rs_qtl": 21000,
            "estimated_cost_cultivation_acre": 21000,
            "gross_return_acre": 567000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 637.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0155",
        "crop_name": "Potato (Kufri Jyoti Table Potato) - Select Genotype v4",
        "category": "Vegetable",
        "growing_duration_days": 90,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 100,
            "sulfur_kg_ha": 19,
            "zinc_sulfate_kg_ha": 16.5
        },
        "climate_envelope": {
            "min_temperature_c": 14,
            "max_temperature_c": 24,
            "optimum_temperature_c": 19.0,
            "min_ph": 5.2,
            "max_ph": 6.5,
            "min_annual_rainfall_mm": 500,
            "max_annual_rainfall_mm": 1000
        },
        "production_economics": {
            "potential_yield_kg_acre": 13000,
            "benchmark_mandi_price_rs_qtl": 1500,
            "estimated_cost_cultivation_acre": 22000,
            "gross_return_acre": 195000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 425.0,
            "preferred_method": "Drip Irrigation with 1.2 LPH emitters"
        }
    },
    {
        "crop_id": "CROP-0156",
        "crop_name": "Potato (Kufri Chipsona Processing) - Select Genotype v4",
        "category": "Vegetable",
        "growing_duration_days": 100,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 130,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 110,
            "sulfur_kg_ha": 20,
            "zinc_sulfate_kg_ha": 17.5
        },
        "climate_envelope": {
            "min_temperature_c": 14,
            "max_temperature_c": 24,
            "optimum_temperature_c": 19.0,
            "min_ph": 5.2,
            "max_ph": 6.5,
            "min_annual_rainfall_mm": 500,
            "max_annual_rainfall_mm": 1000
        },
        "production_economics": {
            "potential_yield_kg_acre": 14000,
            "benchmark_mandi_price_rs_qtl": 1800,
            "estimated_cost_cultivation_acre": 23000,
            "gross_return_acre": 252000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 425.0,
            "preferred_method": "Drip Irrigation with 1.2 LPH emitters"
        }
    },
    {
        "crop_id": "CROP-0157",
        "crop_name": "Onion (Bhima Super Red) - Select Genotype v4",
        "category": "Vegetable",
        "growing_duration_days": 125,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 90,
            "phosphorus_kg_ha": 45,
            "potassium_kg_ha": 50,
            "sulfur_kg_ha": 21,
            "zinc_sulfate_kg_ha": 18.5
        },
        "climate_envelope": {
            "min_temperature_c": 13,
            "max_temperature_c": 30,
            "optimum_temperature_c": 21.5,
            "min_ph": 6.0,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 550,
            "max_annual_rainfall_mm": 1100
        },
        "production_economics": {
            "potential_yield_kg_acre": 11500,
            "benchmark_mandi_price_rs_qtl": 2200,
            "estimated_cost_cultivation_acre": 24000,
            "gross_return_acre": 253000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 467.5,
            "preferred_method": "Drip Irrigation with 1.2 LPH emitters"
        }
    },
    {
        "crop_id": "CROP-0158",
        "crop_name": "Garlic (Yamuna Safed G-1) - Select Genotype v4",
        "category": "Spice",
        "growing_duration_days": 140,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 80,
            "phosphorus_kg_ha": 40,
            "potassium_kg_ha": 40,
            "sulfur_kg_ha": 22,
            "zinc_sulfate_kg_ha": 19.5
        },
        "climate_envelope": {
            "min_temperature_c": 12,
            "max_temperature_c": 25,
            "optimum_temperature_c": 18.5,
            "min_ph": 6.0,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 450,
            "max_annual_rainfall_mm": 900
        },
        "production_economics": {
            "potential_yield_kg_acre": 4200,
            "benchmark_mandi_price_rs_qtl": 14000,
            "estimated_cost_cultivation_acre": 25000,
            "gross_return_acre": 588000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 382.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0159",
        "crop_name": "Turmeric (Prathibha IISR) - Select Genotype v4",
        "category": "Spice",
        "growing_duration_days": 225,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 100,
            "phosphorus_kg_ha": 50,
            "potassium_kg_ha": 90,
            "sulfur_kg_ha": 23,
            "zinc_sulfate_kg_ha": 20.5
        },
        "climate_envelope": {
            "min_temperature_c": 20,
            "max_temperature_c": 35,
            "optimum_temperature_c": 27.5,
            "min_ph": 5.5,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 1400,
            "max_annual_rainfall_mm": 2800
        },
        "production_economics": {
            "potential_yield_kg_acre": 9500,
            "benchmark_mandi_price_rs_qtl": 14500,
            "estimated_cost_cultivation_acre": 26000,
            "gross_return_acre": 1377500
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1190.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0160",
        "crop_name": "Ginger (Varada IISR) - Select Genotype v4",
        "category": "Spice",
        "growing_duration_days": 220,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 90,
            "phosphorus_kg_ha": 50,
            "potassium_kg_ha": 90,
            "sulfur_kg_ha": 24,
            "zinc_sulfate_kg_ha": 21.5
        },
        "climate_envelope": {
            "min_temperature_c": 20,
            "max_temperature_c": 32,
            "optimum_temperature_c": 26.0,
            "min_ph": 5.5,
            "max_ph": 6.5,
            "min_annual_rainfall_mm": 1500,
            "max_annual_rainfall_mm": 3000
        },
        "production_economics": {
            "potential_yield_kg_acre": 8500,
            "benchmark_mandi_price_rs_qtl": 9000,
            "estimated_cost_cultivation_acre": 27000,
            "gross_return_acre": 765000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1275.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0161",
        "crop_name": "Rice (Pusa Basmati 1121) - Select Genotype v5",
        "category": "Cereal",
        "growing_duration_days": 140,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 90,
            "phosphorus_kg_ha": 45,
            "potassium_kg_ha": 45,
            "sulfur_kg_ha": 25,
            "zinc_sulfate_kg_ha": 22.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 36,
            "optimum_temperature_c": 29.0,
            "min_ph": 5.5,
            "max_ph": 7.2,
            "min_annual_rainfall_mm": 1600,
            "max_annual_rainfall_mm": 3200
        },
        "production_economics": {
            "potential_yield_kg_acre": 2200,
            "benchmark_mandi_price_rs_qtl": 2400,
            "estimated_cost_cultivation_acre": 28000,
            "gross_return_acre": 52800
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1360.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0162",
        "crop_name": "Rice (Pusa Basmati 1509) - Select Genotype v5",
        "category": "Cereal",
        "growing_duration_days": 120,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 85,
            "phosphorus_kg_ha": 40,
            "potassium_kg_ha": 40,
            "sulfur_kg_ha": 26,
            "zinc_sulfate_kg_ha": 23.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 38,
            "optimum_temperature_c": 30.0,
            "min_ph": 5.5,
            "max_ph": 7.2,
            "min_annual_rainfall_mm": 1400,
            "max_annual_rainfall_mm": 2800
        },
        "production_economics": {
            "potential_yield_kg_acre": 2400,
            "benchmark_mandi_price_rs_qtl": 2500,
            "estimated_cost_cultivation_acre": 29000,
            "gross_return_acre": 60000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1190.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0163",
        "crop_name": "Rice (BPT 5204 / Samba Mahsuri) - Select Genotype v5",
        "category": "Cereal",
        "growing_duration_days": 150,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 100,
            "phosphorus_kg_ha": 50,
            "potassium_kg_ha": 50,
            "sulfur_kg_ha": 27,
            "zinc_sulfate_kg_ha": 24.5
        },
        "climate_envelope": {
            "min_temperature_c": 20,
            "max_temperature_c": 36,
            "optimum_temperature_c": 28.0,
            "min_ph": 6.0,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 1500,
            "max_annual_rainfall_mm": 3000
        },
        "production_economics": {
            "potential_yield_kg_acre": 2600,
            "benchmark_mandi_price_rs_qtl": 2700,
            "estimated_cost_cultivation_acre": 12000,
            "gross_return_acre": 70200
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1275.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0164",
        "crop_name": "Rice (MTU 1010 / Cottondora Sannalu) - Select Genotype v5",
        "category": "Cereal",
        "growing_duration_days": 125,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 28,
            "zinc_sulfate_kg_ha": 25.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 38,
            "optimum_temperature_c": 30.0,
            "min_ph": 5.5,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 1300,
            "max_annual_rainfall_mm": 2600
        },
        "production_economics": {
            "potential_yield_kg_acre": 3100,
            "benchmark_mandi_price_rs_qtl": 2200,
            "estimated_cost_cultivation_acre": 13000,
            "gross_return_acre": 68200
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1105.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0165",
        "crop_name": "Rice (IR 64 High Yield) - Select Genotype v5",
        "category": "Cereal",
        "growing_duration_days": 120,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 29,
            "zinc_sulfate_kg_ha": 26.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 38,
            "optimum_temperature_c": 30.0,
            "min_ph": 5.5,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 1400,
            "max_annual_rainfall_mm": 2800
        },
        "production_economics": {
            "potential_yield_kg_acre": 3200,
            "benchmark_mandi_price_rs_qtl": 2100,
            "estimated_cost_cultivation_acre": 14000,
            "gross_return_acre": 67200
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1190.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0166",
        "crop_name": "Wheat (HD 2967 High Yield) - Select Genotype v5",
        "category": "Cereal",
        "growing_duration_days": 125,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 30,
            "zinc_sulfate_kg_ha": 12.5
        },
        "climate_envelope": {
            "min_temperature_c": 12,
            "max_temperature_c": 25,
            "optimum_temperature_c": 18.5,
            "min_ph": 6.0,
            "max_ph": 7.8,
            "min_annual_rainfall_mm": 450,
            "max_annual_rainfall_mm": 900
        },
        "production_economics": {
            "potential_yield_kg_acre": 2400,
            "benchmark_mandi_price_rs_qtl": 2350,
            "estimated_cost_cultivation_acre": 15000,
            "gross_return_acre": 56400
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 382.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0167",
        "crop_name": "Wheat (HD 3086 Pusa Gautami) - Select Genotype v5",
        "category": "Cereal",
        "growing_duration_days": 120,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 31,
            "zinc_sulfate_kg_ha": 13.5
        },
        "climate_envelope": {
            "min_temperature_c": 12,
            "max_temperature_c": 26,
            "optimum_temperature_c": 19.0,
            "min_ph": 6.0,
            "max_ph": 7.8,
            "min_annual_rainfall_mm": 450,
            "max_annual_rainfall_mm": 900
        },
        "production_economics": {
            "potential_yield_kg_acre": 2500,
            "benchmark_mandi_price_rs_qtl": 2400,
            "estimated_cost_cultivation_acre": 16000,
            "gross_return_acre": 60000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 382.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0168",
        "crop_name": "Wheat (PBW 343 / Shriram 303) - Select Genotype v5",
        "category": "Cereal",
        "growing_duration_days": 130,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 130,
            "phosphorus_kg_ha": 65,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 32,
            "zinc_sulfate_kg_ha": 14.5
        },
        "climate_envelope": {
            "min_temperature_c": 10,
            "max_temperature_c": 24,
            "optimum_temperature_c": 17.0,
            "min_ph": 6.0,
            "max_ph": 7.8,
            "min_annual_rainfall_mm": 450,
            "max_annual_rainfall_mm": 900
        },
        "production_economics": {
            "potential_yield_kg_acre": 2600,
            "benchmark_mandi_price_rs_qtl": 2300,
            "estimated_cost_cultivation_acre": 17000,
            "gross_return_acre": 59800
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 382.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0169",
        "crop_name": "Wheat (DBW 187 Karan Vandana) - Select Genotype v5",
        "category": "Cereal",
        "growing_duration_days": 120,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 130,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 33,
            "zinc_sulfate_kg_ha": 15.5
        },
        "climate_envelope": {
            "min_temperature_c": 12,
            "max_temperature_c": 27,
            "optimum_temperature_c": 19.5,
            "min_ph": 6.0,
            "max_ph": 7.8,
            "min_annual_rainfall_mm": 400,
            "max_annual_rainfall_mm": 800
        },
        "production_economics": {
            "potential_yield_kg_acre": 2700,
            "benchmark_mandi_price_rs_qtl": 2500,
            "estimated_cost_cultivation_acre": 18000,
            "gross_return_acre": 67500
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 340.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0170",
        "crop_name": "Maize (Pioneer P3396 Hybrid) - Select Genotype v5",
        "category": "Cereal",
        "growing_duration_days": 110,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 140,
            "phosphorus_kg_ha": 65,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 34,
            "zinc_sulfate_kg_ha": 16.5
        },
        "climate_envelope": {
            "min_temperature_c": 18,
            "max_temperature_c": 35,
            "optimum_temperature_c": 26.5,
            "min_ph": 5.8,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 600,
            "max_annual_rainfall_mm": 1200
        },
        "production_economics": {
            "potential_yield_kg_acre": 3600,
            "benchmark_mandi_price_rs_qtl": 2150,
            "estimated_cost_cultivation_acre": 19000,
            "gross_return_acre": 77400
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 510.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0171",
        "crop_name": "Maize (Dekalb 9108 Plus) - Select Genotype v5",
        "category": "Cereal",
        "growing_duration_days": 105,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 130,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 55,
            "sulfur_kg_ha": 35,
            "zinc_sulfate_kg_ha": 17.5
        },
        "climate_envelope": {
            "min_temperature_c": 18,
            "max_temperature_c": 35,
            "optimum_temperature_c": 26.5,
            "min_ph": 5.8,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 550,
            "max_annual_rainfall_mm": 1100
        },
        "production_economics": {
            "potential_yield_kg_acre": 3400,
            "benchmark_mandi_price_rs_qtl": 2150,
            "estimated_cost_cultivation_acre": 20000,
            "gross_return_acre": 73100
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 467.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0172",
        "crop_name": "Maize (Syngenta NK 6240) - Select Genotype v5",
        "category": "Cereal",
        "growing_duration_days": 115,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 140,
            "phosphorus_kg_ha": 70,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 36,
            "zinc_sulfate_kg_ha": 18.5
        },
        "climate_envelope": {
            "min_temperature_c": 18,
            "max_temperature_c": 36,
            "optimum_temperature_c": 27.0,
            "min_ph": 5.8,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 600,
            "max_annual_rainfall_mm": 1200
        },
        "production_economics": {
            "potential_yield_kg_acre": 3800,
            "benchmark_mandi_price_rs_qtl": 2150,
            "estimated_cost_cultivation_acre": 21000,
            "gross_return_acre": 81700
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 510.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0173",
        "crop_name": "Sorghum (CSH 16 Grain Hybrid) - Select Genotype v5",
        "category": "Millet",
        "growing_duration_days": 105,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 80,
            "phosphorus_kg_ha": 40,
            "potassium_kg_ha": 40,
            "sulfur_kg_ha": 37,
            "zinc_sulfate_kg_ha": 19.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 38,
            "optimum_temperature_c": 30.0,
            "min_ph": 6.0,
            "max_ph": 8.2,
            "min_annual_rainfall_mm": 450,
            "max_annual_rainfall_mm": 900
        },
        "production_economics": {
            "potential_yield_kg_acre": 1600,
            "benchmark_mandi_price_rs_qtl": 2900,
            "estimated_cost_cultivation_acre": 22000,
            "gross_return_acre": 46400
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 382.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0174",
        "crop_name": "Pearl Millet (HHB 67 Improved) - Select Genotype v5",
        "category": "Millet",
        "growing_duration_days": 70,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 60,
            "phosphorus_kg_ha": 30,
            "potassium_kg_ha": 30,
            "sulfur_kg_ha": 38,
            "zinc_sulfate_kg_ha": 20.5
        },
        "climate_envelope": {
            "min_temperature_c": 25,
            "max_temperature_c": 42,
            "optimum_temperature_c": 33.5,
            "min_ph": 6.5,
            "max_ph": 8.5,
            "min_annual_rainfall_mm": 300,
            "max_annual_rainfall_mm": 600
        },
        "production_economics": {
            "potential_yield_kg_acre": 1200,
            "benchmark_mandi_price_rs_qtl": 2450,
            "estimated_cost_cultivation_acre": 23000,
            "gross_return_acre": 29400
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 255.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0175",
        "crop_name": "Finger Millet (GPU 28 Ragi) - Select Genotype v5",
        "category": "Millet",
        "growing_duration_days": 110,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 60,
            "phosphorus_kg_ha": 40,
            "potassium_kg_ha": 30,
            "sulfur_kg_ha": 39,
            "zinc_sulfate_kg_ha": 21.5
        },
        "climate_envelope": {
            "min_temperature_c": 18,
            "max_temperature_c": 34,
            "optimum_temperature_c": 26.0,
            "min_ph": 5.5,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 500,
            "max_annual_rainfall_mm": 1000
        },
        "production_economics": {
            "potential_yield_kg_acre": 1300,
            "benchmark_mandi_price_rs_qtl": 3800,
            "estimated_cost_cultivation_acre": 24000,
            "gross_return_acre": 49400
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 425.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0176",
        "crop_name": "Chickpea (JG 11 Desi Gram) - Select Genotype v5",
        "category": "Pulse",
        "growing_duration_days": 95,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 20,
            "phosphorus_kg_ha": 50,
            "potassium_kg_ha": 25,
            "sulfur_kg_ha": 15,
            "zinc_sulfate_kg_ha": 22.5
        },
        "climate_envelope": {
            "min_temperature_c": 15,
            "max_temperature_c": 28,
            "optimum_temperature_c": 21.5,
            "min_ph": 6.0,
            "max_ph": 8.0,
            "min_annual_rainfall_mm": 350,
            "max_annual_rainfall_mm": 700
        },
        "production_economics": {
            "potential_yield_kg_acre": 950,
            "benchmark_mandi_price_rs_qtl": 5400,
            "estimated_cost_cultivation_acre": 25000,
            "gross_return_acre": 51300
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 297.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0177",
        "crop_name": "Chickpea (KAK 2 Kabuli) - Select Genotype v5",
        "category": "Pulse",
        "growing_duration_days": 105,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 25,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 30,
            "sulfur_kg_ha": 16,
            "zinc_sulfate_kg_ha": 23.5
        },
        "climate_envelope": {
            "min_temperature_c": 14,
            "max_temperature_c": 27,
            "optimum_temperature_c": 20.5,
            "min_ph": 6.5,
            "max_ph": 8.2,
            "min_annual_rainfall_mm": 350,
            "max_annual_rainfall_mm": 700
        },
        "production_economics": {
            "potential_yield_kg_acre": 1100,
            "benchmark_mandi_price_rs_qtl": 11000,
            "estimated_cost_cultivation_acre": 26000,
            "gross_return_acre": 121000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 297.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0178",
        "crop_name": "Pigeon Pea (ICPL 87119 Asha) - Select Genotype v5",
        "category": "Pulse",
        "growing_duration_days": 170,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 25,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 30,
            "sulfur_kg_ha": 17,
            "zinc_sulfate_kg_ha": 24.5
        },
        "climate_envelope": {
            "min_temperature_c": 20,
            "max_temperature_c": 36,
            "optimum_temperature_c": 28.0,
            "min_ph": 6.5,
            "max_ph": 8.0,
            "min_annual_rainfall_mm": 700,
            "max_annual_rainfall_mm": 1400
        },
        "production_economics": {
            "potential_yield_kg_acre": 900,
            "benchmark_mandi_price_rs_qtl": 7500,
            "estimated_cost_cultivation_acre": 27000,
            "gross_return_acre": 67500
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 595.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0179",
        "crop_name": "Green Gram (IPM 02-3 / Samrat) - Select Genotype v5",
        "category": "Pulse",
        "growing_duration_days": 65,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 15,
            "phosphorus_kg_ha": 40,
            "potassium_kg_ha": 20,
            "sulfur_kg_ha": 18,
            "zinc_sulfate_kg_ha": 25.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 36,
            "optimum_temperature_c": 29.0,
            "min_ph": 6.2,
            "max_ph": 7.8,
            "min_annual_rainfall_mm": 400,
            "max_annual_rainfall_mm": 800
        },
        "production_economics": {
            "potential_yield_kg_acre": 650,
            "benchmark_mandi_price_rs_qtl": 8500,
            "estimated_cost_cultivation_acre": 28000,
            "gross_return_acre": 55250
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 340.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0180",
        "crop_name": "Black Gram (T-9 / PU 31) - Select Genotype v5",
        "category": "Pulse",
        "growing_duration_days": 75,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 15,
            "phosphorus_kg_ha": 40,
            "potassium_kg_ha": 20,
            "sulfur_kg_ha": 19,
            "zinc_sulfate_kg_ha": 26.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 36,
            "optimum_temperature_c": 29.0,
            "min_ph": 6.0,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 450,
            "max_annual_rainfall_mm": 900
        },
        "production_economics": {
            "potential_yield_kg_acre": 700,
            "benchmark_mandi_price_rs_qtl": 7800,
            "estimated_cost_cultivation_acre": 29000,
            "gross_return_acre": 54600
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 382.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0181",
        "crop_name": "Soybean (JS 335 Central Pride) - Select Genotype v5",
        "category": "Oilseed",
        "growing_duration_days": 95,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 30,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 40,
            "sulfur_kg_ha": 20,
            "zinc_sulfate_kg_ha": 12.5
        },
        "climate_envelope": {
            "min_temperature_c": 20,
            "max_temperature_c": 33,
            "optimum_temperature_c": 26.5,
            "min_ph": 6.0,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 700,
            "max_annual_rainfall_mm": 1400
        },
        "production_economics": {
            "potential_yield_kg_acre": 1100,
            "benchmark_mandi_price_rs_qtl": 4700,
            "estimated_cost_cultivation_acre": 12000,
            "gross_return_acre": 51700
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 595.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0182",
        "crop_name": "Soybean (JS 95-60 Short Duration) - Select Genotype v5",
        "category": "Oilseed",
        "growing_duration_days": 85,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 30,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 40,
            "sulfur_kg_ha": 21,
            "zinc_sulfate_kg_ha": 13.5
        },
        "climate_envelope": {
            "min_temperature_c": 20,
            "max_temperature_c": 33,
            "optimum_temperature_c": 26.5,
            "min_ph": 6.0,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 650,
            "max_annual_rainfall_mm": 1300
        },
        "production_economics": {
            "potential_yield_kg_acre": 1000,
            "benchmark_mandi_price_rs_qtl": 4700,
            "estimated_cost_cultivation_acre": 13000,
            "gross_return_acre": 47000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 552.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0183",
        "crop_name": "Groundnut (TAG 24 Semi-Dwarf) - Select Genotype v5",
        "category": "Oilseed",
        "growing_duration_days": 105,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 25,
            "phosphorus_kg_ha": 50,
            "potassium_kg_ha": 40,
            "sulfur_kg_ha": 22,
            "zinc_sulfate_kg_ha": 14.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 34,
            "optimum_temperature_c": 28.0,
            "min_ph": 5.8,
            "max_ph": 7.2,
            "min_annual_rainfall_mm": 500,
            "max_annual_rainfall_mm": 1000
        },
        "production_economics": {
            "potential_yield_kg_acre": 1250,
            "benchmark_mandi_price_rs_qtl": 6800,
            "estimated_cost_cultivation_acre": 14000,
            "gross_return_acre": 85000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 425.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0184",
        "crop_name": "Groundnut (Kadiri 6 Drought Resilient) - Select Genotype v5",
        "category": "Oilseed",
        "growing_duration_days": 115,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 25,
            "phosphorus_kg_ha": 50,
            "potassium_kg_ha": 40,
            "sulfur_kg_ha": 23,
            "zinc_sulfate_kg_ha": 15.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 34,
            "optimum_temperature_c": 28.0,
            "min_ph": 5.8,
            "max_ph": 7.2,
            "min_annual_rainfall_mm": 450,
            "max_annual_rainfall_mm": 900
        },
        "production_economics": {
            "potential_yield_kg_acre": 1200,
            "benchmark_mandi_price_rs_qtl": 6800,
            "estimated_cost_cultivation_acre": 15000,
            "gross_return_acre": 81600
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 382.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0185",
        "crop_name": "Mustard (Pusa Mustard 30 Zero Erucic) - Select Genotype v5",
        "category": "Oilseed",
        "growing_duration_days": 110,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 60,
            "phosphorus_kg_ha": 30,
            "potassium_kg_ha": 30,
            "sulfur_kg_ha": 24,
            "zinc_sulfate_kg_ha": 16.5
        },
        "climate_envelope": {
            "min_temperature_c": 10,
            "max_temperature_c": 25,
            "optimum_temperature_c": 17.5,
            "min_ph": 6.0,
            "max_ph": 7.8,
            "min_annual_rainfall_mm": 350,
            "max_annual_rainfall_mm": 700
        },
        "production_economics": {
            "potential_yield_kg_acre": 950,
            "benchmark_mandi_price_rs_qtl": 5600,
            "estimated_cost_cultivation_acre": 16000,
            "gross_return_acre": 53200
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 297.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0186",
        "crop_name": "Mustard (Giriraj / DRMRIJ 31) - Select Genotype v5",
        "category": "Oilseed",
        "growing_duration_days": 120,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 80,
            "phosphorus_kg_ha": 40,
            "potassium_kg_ha": 35,
            "sulfur_kg_ha": 25,
            "zinc_sulfate_kg_ha": 17.5
        },
        "climate_envelope": {
            "min_temperature_c": 10,
            "max_temperature_c": 25,
            "optimum_temperature_c": 17.5,
            "min_ph": 6.0,
            "max_ph": 7.8,
            "min_annual_rainfall_mm": 400,
            "max_annual_rainfall_mm": 800
        },
        "production_economics": {
            "potential_yield_kg_acre": 1100,
            "benchmark_mandi_price_rs_qtl": 5600,
            "estimated_cost_cultivation_acre": 17000,
            "gross_return_acre": 61600
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 340.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0187",
        "crop_name": "Cotton (RCH 659 BG II Bt) - Select Genotype v5",
        "category": "Fiber",
        "growing_duration_days": 160,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 26,
            "zinc_sulfate_kg_ha": 18.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 38,
            "optimum_temperature_c": 30.0,
            "min_ph": 6.5,
            "max_ph": 8.2,
            "min_annual_rainfall_mm": 650,
            "max_annual_rainfall_mm": 1300
        },
        "production_economics": {
            "potential_yield_kg_acre": 1400,
            "benchmark_mandi_price_rs_qtl": 7500,
            "estimated_cost_cultivation_acre": 18000,
            "gross_return_acre": 105000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 552.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0188",
        "crop_name": "Cotton (Ajeet 155 BG II) - Select Genotype v5",
        "category": "Fiber",
        "growing_duration_days": 165,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 27,
            "zinc_sulfate_kg_ha": 19.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 38,
            "optimum_temperature_c": 30.0,
            "min_ph": 6.5,
            "max_ph": 8.2,
            "min_annual_rainfall_mm": 650,
            "max_annual_rainfall_mm": 1300
        },
        "production_economics": {
            "potential_yield_kg_acre": 1350,
            "benchmark_mandi_price_rs_qtl": 7500,
            "estimated_cost_cultivation_acre": 19000,
            "gross_return_acre": 101250
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 552.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0189",
        "crop_name": "Sugarcane (Co 0238 High Sugar) - Select Genotype v5",
        "category": "Commercial",
        "growing_duration_days": 330,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 220,
            "phosphorus_kg_ha": 80,
            "potassium_kg_ha": 120,
            "sulfur_kg_ha": 28,
            "zinc_sulfate_kg_ha": 20.5
        },
        "climate_envelope": {
            "min_temperature_c": 24,
            "max_temperature_c": 38,
            "optimum_temperature_c": 31.0,
            "min_ph": 6.2,
            "max_ph": 7.8,
            "min_annual_rainfall_mm": 1600,
            "max_annual_rainfall_mm": 3200
        },
        "production_economics": {
            "potential_yield_kg_acre": 42000,
            "benchmark_mandi_price_rs_qtl": 340,
            "estimated_cost_cultivation_acre": 20000,
            "gross_return_acre": 142800
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1360.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0190",
        "crop_name": "Sugarcane (Co 86032 Wonder Cane) - Select Genotype v5",
        "category": "Commercial",
        "growing_duration_days": 340,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 240,
            "phosphorus_kg_ha": 80,
            "potassium_kg_ha": 120,
            "sulfur_kg_ha": 29,
            "zinc_sulfate_kg_ha": 21.5
        },
        "climate_envelope": {
            "min_temperature_c": 24,
            "max_temperature_c": 38,
            "optimum_temperature_c": 31.0,
            "min_ph": 6.2,
            "max_ph": 7.8,
            "min_annual_rainfall_mm": 1600,
            "max_annual_rainfall_mm": 3200
        },
        "production_economics": {
            "potential_yield_kg_acre": 45000,
            "benchmark_mandi_price_rs_qtl": 340,
            "estimated_cost_cultivation_acre": 21000,
            "gross_return_acre": 153000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1360.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0191",
        "crop_name": "Tomato (Seminis Abhinav Hybrid) - Select Genotype v5",
        "category": "Vegetable",
        "growing_duration_days": 105,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 90,
            "sulfur_kg_ha": 30,
            "zinc_sulfate_kg_ha": 22.5
        },
        "climate_envelope": {
            "min_temperature_c": 18,
            "max_temperature_c": 32,
            "optimum_temperature_c": 25.0,
            "min_ph": 6.0,
            "max_ph": 7.2,
            "min_annual_rainfall_mm": 500,
            "max_annual_rainfall_mm": 1000
        },
        "production_economics": {
            "potential_yield_kg_acre": 16000,
            "benchmark_mandi_price_rs_qtl": 2200,
            "estimated_cost_cultivation_acre": 22000,
            "gross_return_acre": 352000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 425.0,
            "preferred_method": "Drip Irrigation with 1.2 LPH emitters"
        }
    },
    {
        "crop_id": "CROP-0192",
        "crop_name": "Tomato (Syngenta TO-1057) - Select Genotype v5",
        "category": "Vegetable",
        "growing_duration_days": 110,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 90,
            "sulfur_kg_ha": 31,
            "zinc_sulfate_kg_ha": 23.5
        },
        "climate_envelope": {
            "min_temperature_c": 18,
            "max_temperature_c": 32,
            "optimum_temperature_c": 25.0,
            "min_ph": 6.0,
            "max_ph": 7.2,
            "min_annual_rainfall_mm": 500,
            "max_annual_rainfall_mm": 1000
        },
        "production_economics": {
            "potential_yield_kg_acre": 17000,
            "benchmark_mandi_price_rs_qtl": 2200,
            "estimated_cost_cultivation_acre": 23000,
            "gross_return_acre": 374000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 425.0,
            "preferred_method": "Drip Irrigation with 1.2 LPH emitters"
        }
    },
    {
        "crop_id": "CROP-0193",
        "crop_name": "Chilli (Syngenta Armoor Hot) - Select Genotype v5",
        "category": "Spice",
        "growing_duration_days": 155,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 80,
            "sulfur_kg_ha": 32,
            "zinc_sulfate_kg_ha": 24.5
        },
        "climate_envelope": {
            "min_temperature_c": 20,
            "max_temperature_c": 35,
            "optimum_temperature_c": 27.5,
            "min_ph": 6.0,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 750,
            "max_annual_rainfall_mm": 1500
        },
        "production_economics": {
            "potential_yield_kg_acre": 2600,
            "benchmark_mandi_price_rs_qtl": 19500,
            "estimated_cost_cultivation_acre": 24000,
            "gross_return_acre": 507000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 637.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0194",
        "crop_name": "Chilli (US 341 Red Teja) - Select Genotype v5",
        "category": "Spice",
        "growing_duration_days": 160,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 80,
            "sulfur_kg_ha": 33,
            "zinc_sulfate_kg_ha": 25.5
        },
        "climate_envelope": {
            "min_temperature_c": 20,
            "max_temperature_c": 35,
            "optimum_temperature_c": 27.5,
            "min_ph": 6.0,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 750,
            "max_annual_rainfall_mm": 1500
        },
        "production_economics": {
            "potential_yield_kg_acre": 2700,
            "benchmark_mandi_price_rs_qtl": 21000,
            "estimated_cost_cultivation_acre": 25000,
            "gross_return_acre": 567000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 637.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0195",
        "crop_name": "Potato (Kufri Jyoti Table Potato) - Select Genotype v5",
        "category": "Vegetable",
        "growing_duration_days": 90,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 100,
            "sulfur_kg_ha": 34,
            "zinc_sulfate_kg_ha": 26.5
        },
        "climate_envelope": {
            "min_temperature_c": 14,
            "max_temperature_c": 24,
            "optimum_temperature_c": 19.0,
            "min_ph": 5.2,
            "max_ph": 6.5,
            "min_annual_rainfall_mm": 500,
            "max_annual_rainfall_mm": 1000
        },
        "production_economics": {
            "potential_yield_kg_acre": 13000,
            "benchmark_mandi_price_rs_qtl": 1500,
            "estimated_cost_cultivation_acre": 26000,
            "gross_return_acre": 195000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 425.0,
            "preferred_method": "Drip Irrigation with 1.2 LPH emitters"
        }
    },
    {
        "crop_id": "CROP-0196",
        "crop_name": "Potato (Kufri Chipsona Processing) - Select Genotype v5",
        "category": "Vegetable",
        "growing_duration_days": 100,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 130,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 110,
            "sulfur_kg_ha": 35,
            "zinc_sulfate_kg_ha": 12.5
        },
        "climate_envelope": {
            "min_temperature_c": 14,
            "max_temperature_c": 24,
            "optimum_temperature_c": 19.0,
            "min_ph": 5.2,
            "max_ph": 6.5,
            "min_annual_rainfall_mm": 500,
            "max_annual_rainfall_mm": 1000
        },
        "production_economics": {
            "potential_yield_kg_acre": 14000,
            "benchmark_mandi_price_rs_qtl": 1800,
            "estimated_cost_cultivation_acre": 27000,
            "gross_return_acre": 252000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 425.0,
            "preferred_method": "Drip Irrigation with 1.2 LPH emitters"
        }
    },
    {
        "crop_id": "CROP-0197",
        "crop_name": "Onion (Bhima Super Red) - Select Genotype v5",
        "category": "Vegetable",
        "growing_duration_days": 125,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 90,
            "phosphorus_kg_ha": 45,
            "potassium_kg_ha": 50,
            "sulfur_kg_ha": 36,
            "zinc_sulfate_kg_ha": 13.5
        },
        "climate_envelope": {
            "min_temperature_c": 13,
            "max_temperature_c": 30,
            "optimum_temperature_c": 21.5,
            "min_ph": 6.0,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 550,
            "max_annual_rainfall_mm": 1100
        },
        "production_economics": {
            "potential_yield_kg_acre": 11500,
            "benchmark_mandi_price_rs_qtl": 2200,
            "estimated_cost_cultivation_acre": 28000,
            "gross_return_acre": 253000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 467.5,
            "preferred_method": "Drip Irrigation with 1.2 LPH emitters"
        }
    },
    {
        "crop_id": "CROP-0198",
        "crop_name": "Garlic (Yamuna Safed G-1) - Select Genotype v5",
        "category": "Spice",
        "growing_duration_days": 140,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 80,
            "phosphorus_kg_ha": 40,
            "potassium_kg_ha": 40,
            "sulfur_kg_ha": 37,
            "zinc_sulfate_kg_ha": 14.5
        },
        "climate_envelope": {
            "min_temperature_c": 12,
            "max_temperature_c": 25,
            "optimum_temperature_c": 18.5,
            "min_ph": 6.0,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 450,
            "max_annual_rainfall_mm": 900
        },
        "production_economics": {
            "potential_yield_kg_acre": 4200,
            "benchmark_mandi_price_rs_qtl": 14000,
            "estimated_cost_cultivation_acre": 29000,
            "gross_return_acre": 588000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 382.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0199",
        "crop_name": "Turmeric (Prathibha IISR) - Select Genotype v5",
        "category": "Spice",
        "growing_duration_days": 225,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 100,
            "phosphorus_kg_ha": 50,
            "potassium_kg_ha": 90,
            "sulfur_kg_ha": 38,
            "zinc_sulfate_kg_ha": 15.5
        },
        "climate_envelope": {
            "min_temperature_c": 20,
            "max_temperature_c": 35,
            "optimum_temperature_c": 27.5,
            "min_ph": 5.5,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 1400,
            "max_annual_rainfall_mm": 2800
        },
        "production_economics": {
            "potential_yield_kg_acre": 9500,
            "benchmark_mandi_price_rs_qtl": 14500,
            "estimated_cost_cultivation_acre": 12000,
            "gross_return_acre": 1377500
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1190.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0200",
        "crop_name": "Ginger (Varada IISR) - Select Genotype v5",
        "category": "Spice",
        "growing_duration_days": 220,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 90,
            "phosphorus_kg_ha": 50,
            "potassium_kg_ha": 90,
            "sulfur_kg_ha": 39,
            "zinc_sulfate_kg_ha": 16.5
        },
        "climate_envelope": {
            "min_temperature_c": 20,
            "max_temperature_c": 32,
            "optimum_temperature_c": 26.0,
            "min_ph": 5.5,
            "max_ph": 6.5,
            "min_annual_rainfall_mm": 1500,
            "max_annual_rainfall_mm": 3000
        },
        "production_economics": {
            "potential_yield_kg_acre": 8500,
            "benchmark_mandi_price_rs_qtl": 9000,
            "estimated_cost_cultivation_acre": 13000,
            "gross_return_acre": 765000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1275.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0201",
        "crop_name": "Rice (Pusa Basmati 1121) - Select Genotype v6",
        "category": "Cereal",
        "growing_duration_days": 140,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 90,
            "phosphorus_kg_ha": 45,
            "potassium_kg_ha": 45,
            "sulfur_kg_ha": 15,
            "zinc_sulfate_kg_ha": 17.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 36,
            "optimum_temperature_c": 29.0,
            "min_ph": 5.5,
            "max_ph": 7.2,
            "min_annual_rainfall_mm": 1600,
            "max_annual_rainfall_mm": 3200
        },
        "production_economics": {
            "potential_yield_kg_acre": 2200,
            "benchmark_mandi_price_rs_qtl": 2400,
            "estimated_cost_cultivation_acre": 14000,
            "gross_return_acre": 52800
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1360.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0202",
        "crop_name": "Rice (Pusa Basmati 1509) - Select Genotype v6",
        "category": "Cereal",
        "growing_duration_days": 120,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 85,
            "phosphorus_kg_ha": 40,
            "potassium_kg_ha": 40,
            "sulfur_kg_ha": 16,
            "zinc_sulfate_kg_ha": 18.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 38,
            "optimum_temperature_c": 30.0,
            "min_ph": 5.5,
            "max_ph": 7.2,
            "min_annual_rainfall_mm": 1400,
            "max_annual_rainfall_mm": 2800
        },
        "production_economics": {
            "potential_yield_kg_acre": 2400,
            "benchmark_mandi_price_rs_qtl": 2500,
            "estimated_cost_cultivation_acre": 15000,
            "gross_return_acre": 60000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1190.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0203",
        "crop_name": "Rice (BPT 5204 / Samba Mahsuri) - Select Genotype v6",
        "category": "Cereal",
        "growing_duration_days": 150,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 100,
            "phosphorus_kg_ha": 50,
            "potassium_kg_ha": 50,
            "sulfur_kg_ha": 17,
            "zinc_sulfate_kg_ha": 19.5
        },
        "climate_envelope": {
            "min_temperature_c": 20,
            "max_temperature_c": 36,
            "optimum_temperature_c": 28.0,
            "min_ph": 6.0,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 1500,
            "max_annual_rainfall_mm": 3000
        },
        "production_economics": {
            "potential_yield_kg_acre": 2600,
            "benchmark_mandi_price_rs_qtl": 2700,
            "estimated_cost_cultivation_acre": 16000,
            "gross_return_acre": 70200
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1275.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0204",
        "crop_name": "Rice (MTU 1010 / Cottondora Sannalu) - Select Genotype v6",
        "category": "Cereal",
        "growing_duration_days": 125,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 18,
            "zinc_sulfate_kg_ha": 20.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 38,
            "optimum_temperature_c": 30.0,
            "min_ph": 5.5,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 1300,
            "max_annual_rainfall_mm": 2600
        },
        "production_economics": {
            "potential_yield_kg_acre": 3100,
            "benchmark_mandi_price_rs_qtl": 2200,
            "estimated_cost_cultivation_acre": 17000,
            "gross_return_acre": 68200
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1105.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0205",
        "crop_name": "Rice (IR 64 High Yield) - Select Genotype v6",
        "category": "Cereal",
        "growing_duration_days": 120,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 19,
            "zinc_sulfate_kg_ha": 21.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 38,
            "optimum_temperature_c": 30.0,
            "min_ph": 5.5,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 1400,
            "max_annual_rainfall_mm": 2800
        },
        "production_economics": {
            "potential_yield_kg_acre": 3200,
            "benchmark_mandi_price_rs_qtl": 2100,
            "estimated_cost_cultivation_acre": 18000,
            "gross_return_acre": 67200
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1190.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0206",
        "crop_name": "Wheat (HD 2967 High Yield) - Select Genotype v6",
        "category": "Cereal",
        "growing_duration_days": 125,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 20,
            "zinc_sulfate_kg_ha": 22.5
        },
        "climate_envelope": {
            "min_temperature_c": 12,
            "max_temperature_c": 25,
            "optimum_temperature_c": 18.5,
            "min_ph": 6.0,
            "max_ph": 7.8,
            "min_annual_rainfall_mm": 450,
            "max_annual_rainfall_mm": 900
        },
        "production_economics": {
            "potential_yield_kg_acre": 2400,
            "benchmark_mandi_price_rs_qtl": 2350,
            "estimated_cost_cultivation_acre": 19000,
            "gross_return_acre": 56400
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 382.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0207",
        "crop_name": "Wheat (HD 3086 Pusa Gautami) - Select Genotype v6",
        "category": "Cereal",
        "growing_duration_days": 120,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 21,
            "zinc_sulfate_kg_ha": 23.5
        },
        "climate_envelope": {
            "min_temperature_c": 12,
            "max_temperature_c": 26,
            "optimum_temperature_c": 19.0,
            "min_ph": 6.0,
            "max_ph": 7.8,
            "min_annual_rainfall_mm": 450,
            "max_annual_rainfall_mm": 900
        },
        "production_economics": {
            "potential_yield_kg_acre": 2500,
            "benchmark_mandi_price_rs_qtl": 2400,
            "estimated_cost_cultivation_acre": 20000,
            "gross_return_acre": 60000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 382.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0208",
        "crop_name": "Wheat (PBW 343 / Shriram 303) - Select Genotype v6",
        "category": "Cereal",
        "growing_duration_days": 130,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 130,
            "phosphorus_kg_ha": 65,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 22,
            "zinc_sulfate_kg_ha": 24.5
        },
        "climate_envelope": {
            "min_temperature_c": 10,
            "max_temperature_c": 24,
            "optimum_temperature_c": 17.0,
            "min_ph": 6.0,
            "max_ph": 7.8,
            "min_annual_rainfall_mm": 450,
            "max_annual_rainfall_mm": 900
        },
        "production_economics": {
            "potential_yield_kg_acre": 2600,
            "benchmark_mandi_price_rs_qtl": 2300,
            "estimated_cost_cultivation_acre": 21000,
            "gross_return_acre": 59800
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 382.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0209",
        "crop_name": "Wheat (DBW 187 Karan Vandana) - Select Genotype v6",
        "category": "Cereal",
        "growing_duration_days": 120,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 130,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 23,
            "zinc_sulfate_kg_ha": 25.5
        },
        "climate_envelope": {
            "min_temperature_c": 12,
            "max_temperature_c": 27,
            "optimum_temperature_c": 19.5,
            "min_ph": 6.0,
            "max_ph": 7.8,
            "min_annual_rainfall_mm": 400,
            "max_annual_rainfall_mm": 800
        },
        "production_economics": {
            "potential_yield_kg_acre": 2700,
            "benchmark_mandi_price_rs_qtl": 2500,
            "estimated_cost_cultivation_acre": 22000,
            "gross_return_acre": 67500
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 340.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0210",
        "crop_name": "Maize (Pioneer P3396 Hybrid) - Select Genotype v6",
        "category": "Cereal",
        "growing_duration_days": 110,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 140,
            "phosphorus_kg_ha": 65,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 24,
            "zinc_sulfate_kg_ha": 26.5
        },
        "climate_envelope": {
            "min_temperature_c": 18,
            "max_temperature_c": 35,
            "optimum_temperature_c": 26.5,
            "min_ph": 5.8,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 600,
            "max_annual_rainfall_mm": 1200
        },
        "production_economics": {
            "potential_yield_kg_acre": 3600,
            "benchmark_mandi_price_rs_qtl": 2150,
            "estimated_cost_cultivation_acre": 23000,
            "gross_return_acre": 77400
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 510.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0211",
        "crop_name": "Maize (Dekalb 9108 Plus) - Select Genotype v6",
        "category": "Cereal",
        "growing_duration_days": 105,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 130,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 55,
            "sulfur_kg_ha": 25,
            "zinc_sulfate_kg_ha": 12.5
        },
        "climate_envelope": {
            "min_temperature_c": 18,
            "max_temperature_c": 35,
            "optimum_temperature_c": 26.5,
            "min_ph": 5.8,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 550,
            "max_annual_rainfall_mm": 1100
        },
        "production_economics": {
            "potential_yield_kg_acre": 3400,
            "benchmark_mandi_price_rs_qtl": 2150,
            "estimated_cost_cultivation_acre": 24000,
            "gross_return_acre": 73100
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 467.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0212",
        "crop_name": "Maize (Syngenta NK 6240) - Select Genotype v6",
        "category": "Cereal",
        "growing_duration_days": 115,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 140,
            "phosphorus_kg_ha": 70,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 26,
            "zinc_sulfate_kg_ha": 13.5
        },
        "climate_envelope": {
            "min_temperature_c": 18,
            "max_temperature_c": 36,
            "optimum_temperature_c": 27.0,
            "min_ph": 5.8,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 600,
            "max_annual_rainfall_mm": 1200
        },
        "production_economics": {
            "potential_yield_kg_acre": 3800,
            "benchmark_mandi_price_rs_qtl": 2150,
            "estimated_cost_cultivation_acre": 25000,
            "gross_return_acre": 81700
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 510.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0213",
        "crop_name": "Sorghum (CSH 16 Grain Hybrid) - Select Genotype v6",
        "category": "Millet",
        "growing_duration_days": 105,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 80,
            "phosphorus_kg_ha": 40,
            "potassium_kg_ha": 40,
            "sulfur_kg_ha": 27,
            "zinc_sulfate_kg_ha": 14.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 38,
            "optimum_temperature_c": 30.0,
            "min_ph": 6.0,
            "max_ph": 8.2,
            "min_annual_rainfall_mm": 450,
            "max_annual_rainfall_mm": 900
        },
        "production_economics": {
            "potential_yield_kg_acre": 1600,
            "benchmark_mandi_price_rs_qtl": 2900,
            "estimated_cost_cultivation_acre": 26000,
            "gross_return_acre": 46400
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 382.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0214",
        "crop_name": "Pearl Millet (HHB 67 Improved) - Select Genotype v6",
        "category": "Millet",
        "growing_duration_days": 70,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 60,
            "phosphorus_kg_ha": 30,
            "potassium_kg_ha": 30,
            "sulfur_kg_ha": 28,
            "zinc_sulfate_kg_ha": 15.5
        },
        "climate_envelope": {
            "min_temperature_c": 25,
            "max_temperature_c": 42,
            "optimum_temperature_c": 33.5,
            "min_ph": 6.5,
            "max_ph": 8.5,
            "min_annual_rainfall_mm": 300,
            "max_annual_rainfall_mm": 600
        },
        "production_economics": {
            "potential_yield_kg_acre": 1200,
            "benchmark_mandi_price_rs_qtl": 2450,
            "estimated_cost_cultivation_acre": 27000,
            "gross_return_acre": 29400
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 255.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0215",
        "crop_name": "Finger Millet (GPU 28 Ragi) - Select Genotype v6",
        "category": "Millet",
        "growing_duration_days": 110,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 60,
            "phosphorus_kg_ha": 40,
            "potassium_kg_ha": 30,
            "sulfur_kg_ha": 29,
            "zinc_sulfate_kg_ha": 16.5
        },
        "climate_envelope": {
            "min_temperature_c": 18,
            "max_temperature_c": 34,
            "optimum_temperature_c": 26.0,
            "min_ph": 5.5,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 500,
            "max_annual_rainfall_mm": 1000
        },
        "production_economics": {
            "potential_yield_kg_acre": 1300,
            "benchmark_mandi_price_rs_qtl": 3800,
            "estimated_cost_cultivation_acre": 28000,
            "gross_return_acre": 49400
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 425.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0216",
        "crop_name": "Chickpea (JG 11 Desi Gram) - Select Genotype v6",
        "category": "Pulse",
        "growing_duration_days": 95,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 20,
            "phosphorus_kg_ha": 50,
            "potassium_kg_ha": 25,
            "sulfur_kg_ha": 30,
            "zinc_sulfate_kg_ha": 17.5
        },
        "climate_envelope": {
            "min_temperature_c": 15,
            "max_temperature_c": 28,
            "optimum_temperature_c": 21.5,
            "min_ph": 6.0,
            "max_ph": 8.0,
            "min_annual_rainfall_mm": 350,
            "max_annual_rainfall_mm": 700
        },
        "production_economics": {
            "potential_yield_kg_acre": 950,
            "benchmark_mandi_price_rs_qtl": 5400,
            "estimated_cost_cultivation_acre": 29000,
            "gross_return_acre": 51300
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 297.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0217",
        "crop_name": "Chickpea (KAK 2 Kabuli) - Select Genotype v6",
        "category": "Pulse",
        "growing_duration_days": 105,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 25,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 30,
            "sulfur_kg_ha": 31,
            "zinc_sulfate_kg_ha": 18.5
        },
        "climate_envelope": {
            "min_temperature_c": 14,
            "max_temperature_c": 27,
            "optimum_temperature_c": 20.5,
            "min_ph": 6.5,
            "max_ph": 8.2,
            "min_annual_rainfall_mm": 350,
            "max_annual_rainfall_mm": 700
        },
        "production_economics": {
            "potential_yield_kg_acre": 1100,
            "benchmark_mandi_price_rs_qtl": 11000,
            "estimated_cost_cultivation_acre": 12000,
            "gross_return_acre": 121000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 297.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0218",
        "crop_name": "Pigeon Pea (ICPL 87119 Asha) - Select Genotype v6",
        "category": "Pulse",
        "growing_duration_days": 170,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 25,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 30,
            "sulfur_kg_ha": 32,
            "zinc_sulfate_kg_ha": 19.5
        },
        "climate_envelope": {
            "min_temperature_c": 20,
            "max_temperature_c": 36,
            "optimum_temperature_c": 28.0,
            "min_ph": 6.5,
            "max_ph": 8.0,
            "min_annual_rainfall_mm": 700,
            "max_annual_rainfall_mm": 1400
        },
        "production_economics": {
            "potential_yield_kg_acre": 900,
            "benchmark_mandi_price_rs_qtl": 7500,
            "estimated_cost_cultivation_acre": 13000,
            "gross_return_acre": 67500
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 595.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0219",
        "crop_name": "Green Gram (IPM 02-3 / Samrat) - Select Genotype v6",
        "category": "Pulse",
        "growing_duration_days": 65,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 15,
            "phosphorus_kg_ha": 40,
            "potassium_kg_ha": 20,
            "sulfur_kg_ha": 33,
            "zinc_sulfate_kg_ha": 20.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 36,
            "optimum_temperature_c": 29.0,
            "min_ph": 6.2,
            "max_ph": 7.8,
            "min_annual_rainfall_mm": 400,
            "max_annual_rainfall_mm": 800
        },
        "production_economics": {
            "potential_yield_kg_acre": 650,
            "benchmark_mandi_price_rs_qtl": 8500,
            "estimated_cost_cultivation_acre": 14000,
            "gross_return_acre": 55250
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 340.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0220",
        "crop_name": "Black Gram (T-9 / PU 31) - Select Genotype v6",
        "category": "Pulse",
        "growing_duration_days": 75,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 15,
            "phosphorus_kg_ha": 40,
            "potassium_kg_ha": 20,
            "sulfur_kg_ha": 34,
            "zinc_sulfate_kg_ha": 21.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 36,
            "optimum_temperature_c": 29.0,
            "min_ph": 6.0,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 450,
            "max_annual_rainfall_mm": 900
        },
        "production_economics": {
            "potential_yield_kg_acre": 700,
            "benchmark_mandi_price_rs_qtl": 7800,
            "estimated_cost_cultivation_acre": 15000,
            "gross_return_acre": 54600
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 382.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0221",
        "crop_name": "Soybean (JS 335 Central Pride) - Select Genotype v6",
        "category": "Oilseed",
        "growing_duration_days": 95,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 30,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 40,
            "sulfur_kg_ha": 35,
            "zinc_sulfate_kg_ha": 22.5
        },
        "climate_envelope": {
            "min_temperature_c": 20,
            "max_temperature_c": 33,
            "optimum_temperature_c": 26.5,
            "min_ph": 6.0,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 700,
            "max_annual_rainfall_mm": 1400
        },
        "production_economics": {
            "potential_yield_kg_acre": 1100,
            "benchmark_mandi_price_rs_qtl": 4700,
            "estimated_cost_cultivation_acre": 16000,
            "gross_return_acre": 51700
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 595.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0222",
        "crop_name": "Soybean (JS 95-60 Short Duration) - Select Genotype v6",
        "category": "Oilseed",
        "growing_duration_days": 85,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 30,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 40,
            "sulfur_kg_ha": 36,
            "zinc_sulfate_kg_ha": 23.5
        },
        "climate_envelope": {
            "min_temperature_c": 20,
            "max_temperature_c": 33,
            "optimum_temperature_c": 26.5,
            "min_ph": 6.0,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 650,
            "max_annual_rainfall_mm": 1300
        },
        "production_economics": {
            "potential_yield_kg_acre": 1000,
            "benchmark_mandi_price_rs_qtl": 4700,
            "estimated_cost_cultivation_acre": 17000,
            "gross_return_acre": 47000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 552.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0223",
        "crop_name": "Groundnut (TAG 24 Semi-Dwarf) - Select Genotype v6",
        "category": "Oilseed",
        "growing_duration_days": 105,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 25,
            "phosphorus_kg_ha": 50,
            "potassium_kg_ha": 40,
            "sulfur_kg_ha": 37,
            "zinc_sulfate_kg_ha": 24.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 34,
            "optimum_temperature_c": 28.0,
            "min_ph": 5.8,
            "max_ph": 7.2,
            "min_annual_rainfall_mm": 500,
            "max_annual_rainfall_mm": 1000
        },
        "production_economics": {
            "potential_yield_kg_acre": 1250,
            "benchmark_mandi_price_rs_qtl": 6800,
            "estimated_cost_cultivation_acre": 18000,
            "gross_return_acre": 85000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 425.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0224",
        "crop_name": "Groundnut (Kadiri 6 Drought Resilient) - Select Genotype v6",
        "category": "Oilseed",
        "growing_duration_days": 115,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 25,
            "phosphorus_kg_ha": 50,
            "potassium_kg_ha": 40,
            "sulfur_kg_ha": 38,
            "zinc_sulfate_kg_ha": 25.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 34,
            "optimum_temperature_c": 28.0,
            "min_ph": 5.8,
            "max_ph": 7.2,
            "min_annual_rainfall_mm": 450,
            "max_annual_rainfall_mm": 900
        },
        "production_economics": {
            "potential_yield_kg_acre": 1200,
            "benchmark_mandi_price_rs_qtl": 6800,
            "estimated_cost_cultivation_acre": 19000,
            "gross_return_acre": 81600
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 382.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0225",
        "crop_name": "Mustard (Pusa Mustard 30 Zero Erucic) - Select Genotype v6",
        "category": "Oilseed",
        "growing_duration_days": 110,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 60,
            "phosphorus_kg_ha": 30,
            "potassium_kg_ha": 30,
            "sulfur_kg_ha": 39,
            "zinc_sulfate_kg_ha": 26.5
        },
        "climate_envelope": {
            "min_temperature_c": 10,
            "max_temperature_c": 25,
            "optimum_temperature_c": 17.5,
            "min_ph": 6.0,
            "max_ph": 7.8,
            "min_annual_rainfall_mm": 350,
            "max_annual_rainfall_mm": 700
        },
        "production_economics": {
            "potential_yield_kg_acre": 950,
            "benchmark_mandi_price_rs_qtl": 5600,
            "estimated_cost_cultivation_acre": 20000,
            "gross_return_acre": 53200
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 297.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0226",
        "crop_name": "Mustard (Giriraj / DRMRIJ 31) - Select Genotype v6",
        "category": "Oilseed",
        "growing_duration_days": 120,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 80,
            "phosphorus_kg_ha": 40,
            "potassium_kg_ha": 35,
            "sulfur_kg_ha": 15,
            "zinc_sulfate_kg_ha": 12.5
        },
        "climate_envelope": {
            "min_temperature_c": 10,
            "max_temperature_c": 25,
            "optimum_temperature_c": 17.5,
            "min_ph": 6.0,
            "max_ph": 7.8,
            "min_annual_rainfall_mm": 400,
            "max_annual_rainfall_mm": 800
        },
        "production_economics": {
            "potential_yield_kg_acre": 1100,
            "benchmark_mandi_price_rs_qtl": 5600,
            "estimated_cost_cultivation_acre": 21000,
            "gross_return_acre": 61600
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 340.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0227",
        "crop_name": "Cotton (RCH 659 BG II Bt) - Select Genotype v6",
        "category": "Fiber",
        "growing_duration_days": 160,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 16,
            "zinc_sulfate_kg_ha": 13.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 38,
            "optimum_temperature_c": 30.0,
            "min_ph": 6.5,
            "max_ph": 8.2,
            "min_annual_rainfall_mm": 650,
            "max_annual_rainfall_mm": 1300
        },
        "production_economics": {
            "potential_yield_kg_acre": 1400,
            "benchmark_mandi_price_rs_qtl": 7500,
            "estimated_cost_cultivation_acre": 22000,
            "gross_return_acre": 105000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 552.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0228",
        "crop_name": "Cotton (Ajeet 155 BG II) - Select Genotype v6",
        "category": "Fiber",
        "growing_duration_days": 165,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 17,
            "zinc_sulfate_kg_ha": 14.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 38,
            "optimum_temperature_c": 30.0,
            "min_ph": 6.5,
            "max_ph": 8.2,
            "min_annual_rainfall_mm": 650,
            "max_annual_rainfall_mm": 1300
        },
        "production_economics": {
            "potential_yield_kg_acre": 1350,
            "benchmark_mandi_price_rs_qtl": 7500,
            "estimated_cost_cultivation_acre": 23000,
            "gross_return_acre": 101250
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 552.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0229",
        "crop_name": "Sugarcane (Co 0238 High Sugar) - Select Genotype v6",
        "category": "Commercial",
        "growing_duration_days": 330,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 220,
            "phosphorus_kg_ha": 80,
            "potassium_kg_ha": 120,
            "sulfur_kg_ha": 18,
            "zinc_sulfate_kg_ha": 15.5
        },
        "climate_envelope": {
            "min_temperature_c": 24,
            "max_temperature_c": 38,
            "optimum_temperature_c": 31.0,
            "min_ph": 6.2,
            "max_ph": 7.8,
            "min_annual_rainfall_mm": 1600,
            "max_annual_rainfall_mm": 3200
        },
        "production_economics": {
            "potential_yield_kg_acre": 42000,
            "benchmark_mandi_price_rs_qtl": 340,
            "estimated_cost_cultivation_acre": 24000,
            "gross_return_acre": 142800
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1360.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0230",
        "crop_name": "Sugarcane (Co 86032 Wonder Cane) - Select Genotype v6",
        "category": "Commercial",
        "growing_duration_days": 340,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 240,
            "phosphorus_kg_ha": 80,
            "potassium_kg_ha": 120,
            "sulfur_kg_ha": 19,
            "zinc_sulfate_kg_ha": 16.5
        },
        "climate_envelope": {
            "min_temperature_c": 24,
            "max_temperature_c": 38,
            "optimum_temperature_c": 31.0,
            "min_ph": 6.2,
            "max_ph": 7.8,
            "min_annual_rainfall_mm": 1600,
            "max_annual_rainfall_mm": 3200
        },
        "production_economics": {
            "potential_yield_kg_acre": 45000,
            "benchmark_mandi_price_rs_qtl": 340,
            "estimated_cost_cultivation_acre": 25000,
            "gross_return_acre": 153000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1360.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0231",
        "crop_name": "Tomato (Seminis Abhinav Hybrid) - Select Genotype v6",
        "category": "Vegetable",
        "growing_duration_days": 105,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 90,
            "sulfur_kg_ha": 20,
            "zinc_sulfate_kg_ha": 17.5
        },
        "climate_envelope": {
            "min_temperature_c": 18,
            "max_temperature_c": 32,
            "optimum_temperature_c": 25.0,
            "min_ph": 6.0,
            "max_ph": 7.2,
            "min_annual_rainfall_mm": 500,
            "max_annual_rainfall_mm": 1000
        },
        "production_economics": {
            "potential_yield_kg_acre": 16000,
            "benchmark_mandi_price_rs_qtl": 2200,
            "estimated_cost_cultivation_acre": 26000,
            "gross_return_acre": 352000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 425.0,
            "preferred_method": "Drip Irrigation with 1.2 LPH emitters"
        }
    },
    {
        "crop_id": "CROP-0232",
        "crop_name": "Tomato (Syngenta TO-1057) - Select Genotype v6",
        "category": "Vegetable",
        "growing_duration_days": 110,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 90,
            "sulfur_kg_ha": 21,
            "zinc_sulfate_kg_ha": 18.5
        },
        "climate_envelope": {
            "min_temperature_c": 18,
            "max_temperature_c": 32,
            "optimum_temperature_c": 25.0,
            "min_ph": 6.0,
            "max_ph": 7.2,
            "min_annual_rainfall_mm": 500,
            "max_annual_rainfall_mm": 1000
        },
        "production_economics": {
            "potential_yield_kg_acre": 17000,
            "benchmark_mandi_price_rs_qtl": 2200,
            "estimated_cost_cultivation_acre": 27000,
            "gross_return_acre": 374000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 425.0,
            "preferred_method": "Drip Irrigation with 1.2 LPH emitters"
        }
    },
    {
        "crop_id": "CROP-0233",
        "crop_name": "Chilli (Syngenta Armoor Hot) - Select Genotype v6",
        "category": "Spice",
        "growing_duration_days": 155,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 80,
            "sulfur_kg_ha": 22,
            "zinc_sulfate_kg_ha": 19.5
        },
        "climate_envelope": {
            "min_temperature_c": 20,
            "max_temperature_c": 35,
            "optimum_temperature_c": 27.5,
            "min_ph": 6.0,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 750,
            "max_annual_rainfall_mm": 1500
        },
        "production_economics": {
            "potential_yield_kg_acre": 2600,
            "benchmark_mandi_price_rs_qtl": 19500,
            "estimated_cost_cultivation_acre": 28000,
            "gross_return_acre": 507000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 637.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0234",
        "crop_name": "Chilli (US 341 Red Teja) - Select Genotype v6",
        "category": "Spice",
        "growing_duration_days": 160,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 80,
            "sulfur_kg_ha": 23,
            "zinc_sulfate_kg_ha": 20.5
        },
        "climate_envelope": {
            "min_temperature_c": 20,
            "max_temperature_c": 35,
            "optimum_temperature_c": 27.5,
            "min_ph": 6.0,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 750,
            "max_annual_rainfall_mm": 1500
        },
        "production_economics": {
            "potential_yield_kg_acre": 2700,
            "benchmark_mandi_price_rs_qtl": 21000,
            "estimated_cost_cultivation_acre": 29000,
            "gross_return_acre": 567000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 637.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0235",
        "crop_name": "Potato (Kufri Jyoti Table Potato) - Select Genotype v6",
        "category": "Vegetable",
        "growing_duration_days": 90,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 100,
            "sulfur_kg_ha": 24,
            "zinc_sulfate_kg_ha": 21.5
        },
        "climate_envelope": {
            "min_temperature_c": 14,
            "max_temperature_c": 24,
            "optimum_temperature_c": 19.0,
            "min_ph": 5.2,
            "max_ph": 6.5,
            "min_annual_rainfall_mm": 500,
            "max_annual_rainfall_mm": 1000
        },
        "production_economics": {
            "potential_yield_kg_acre": 13000,
            "benchmark_mandi_price_rs_qtl": 1500,
            "estimated_cost_cultivation_acre": 12000,
            "gross_return_acre": 195000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 425.0,
            "preferred_method": "Drip Irrigation with 1.2 LPH emitters"
        }
    },
    {
        "crop_id": "CROP-0236",
        "crop_name": "Potato (Kufri Chipsona Processing) - Select Genotype v6",
        "category": "Vegetable",
        "growing_duration_days": 100,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 130,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 110,
            "sulfur_kg_ha": 25,
            "zinc_sulfate_kg_ha": 22.5
        },
        "climate_envelope": {
            "min_temperature_c": 14,
            "max_temperature_c": 24,
            "optimum_temperature_c": 19.0,
            "min_ph": 5.2,
            "max_ph": 6.5,
            "min_annual_rainfall_mm": 500,
            "max_annual_rainfall_mm": 1000
        },
        "production_economics": {
            "potential_yield_kg_acre": 14000,
            "benchmark_mandi_price_rs_qtl": 1800,
            "estimated_cost_cultivation_acre": 13000,
            "gross_return_acre": 252000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 425.0,
            "preferred_method": "Drip Irrigation with 1.2 LPH emitters"
        }
    },
    {
        "crop_id": "CROP-0237",
        "crop_name": "Onion (Bhima Super Red) - Select Genotype v6",
        "category": "Vegetable",
        "growing_duration_days": 125,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 90,
            "phosphorus_kg_ha": 45,
            "potassium_kg_ha": 50,
            "sulfur_kg_ha": 26,
            "zinc_sulfate_kg_ha": 23.5
        },
        "climate_envelope": {
            "min_temperature_c": 13,
            "max_temperature_c": 30,
            "optimum_temperature_c": 21.5,
            "min_ph": 6.0,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 550,
            "max_annual_rainfall_mm": 1100
        },
        "production_economics": {
            "potential_yield_kg_acre": 11500,
            "benchmark_mandi_price_rs_qtl": 2200,
            "estimated_cost_cultivation_acre": 14000,
            "gross_return_acre": 253000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 467.5,
            "preferred_method": "Drip Irrigation with 1.2 LPH emitters"
        }
    },
    {
        "crop_id": "CROP-0238",
        "crop_name": "Garlic (Yamuna Safed G-1) - Select Genotype v6",
        "category": "Spice",
        "growing_duration_days": 140,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 80,
            "phosphorus_kg_ha": 40,
            "potassium_kg_ha": 40,
            "sulfur_kg_ha": 27,
            "zinc_sulfate_kg_ha": 24.5
        },
        "climate_envelope": {
            "min_temperature_c": 12,
            "max_temperature_c": 25,
            "optimum_temperature_c": 18.5,
            "min_ph": 6.0,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 450,
            "max_annual_rainfall_mm": 900
        },
        "production_economics": {
            "potential_yield_kg_acre": 4200,
            "benchmark_mandi_price_rs_qtl": 14000,
            "estimated_cost_cultivation_acre": 15000,
            "gross_return_acre": 588000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 382.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0239",
        "crop_name": "Turmeric (Prathibha IISR) - Select Genotype v6",
        "category": "Spice",
        "growing_duration_days": 225,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 100,
            "phosphorus_kg_ha": 50,
            "potassium_kg_ha": 90,
            "sulfur_kg_ha": 28,
            "zinc_sulfate_kg_ha": 25.5
        },
        "climate_envelope": {
            "min_temperature_c": 20,
            "max_temperature_c": 35,
            "optimum_temperature_c": 27.5,
            "min_ph": 5.5,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 1400,
            "max_annual_rainfall_mm": 2800
        },
        "production_economics": {
            "potential_yield_kg_acre": 9500,
            "benchmark_mandi_price_rs_qtl": 14500,
            "estimated_cost_cultivation_acre": 16000,
            "gross_return_acre": 1377500
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1190.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0240",
        "crop_name": "Ginger (Varada IISR) - Select Genotype v6",
        "category": "Spice",
        "growing_duration_days": 220,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 90,
            "phosphorus_kg_ha": 50,
            "potassium_kg_ha": 90,
            "sulfur_kg_ha": 29,
            "zinc_sulfate_kg_ha": 26.5
        },
        "climate_envelope": {
            "min_temperature_c": 20,
            "max_temperature_c": 32,
            "optimum_temperature_c": 26.0,
            "min_ph": 5.5,
            "max_ph": 6.5,
            "min_annual_rainfall_mm": 1500,
            "max_annual_rainfall_mm": 3000
        },
        "production_economics": {
            "potential_yield_kg_acre": 8500,
            "benchmark_mandi_price_rs_qtl": 9000,
            "estimated_cost_cultivation_acre": 17000,
            "gross_return_acre": 765000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1275.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0241",
        "crop_name": "Rice (Pusa Basmati 1121) - Select Genotype v7",
        "category": "Cereal",
        "growing_duration_days": 140,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 90,
            "phosphorus_kg_ha": 45,
            "potassium_kg_ha": 45,
            "sulfur_kg_ha": 30,
            "zinc_sulfate_kg_ha": 12.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 36,
            "optimum_temperature_c": 29.0,
            "min_ph": 5.5,
            "max_ph": 7.2,
            "min_annual_rainfall_mm": 1600,
            "max_annual_rainfall_mm": 3200
        },
        "production_economics": {
            "potential_yield_kg_acre": 2200,
            "benchmark_mandi_price_rs_qtl": 2400,
            "estimated_cost_cultivation_acre": 18000,
            "gross_return_acre": 52800
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1360.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0242",
        "crop_name": "Rice (Pusa Basmati 1509) - Select Genotype v7",
        "category": "Cereal",
        "growing_duration_days": 120,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 85,
            "phosphorus_kg_ha": 40,
            "potassium_kg_ha": 40,
            "sulfur_kg_ha": 31,
            "zinc_sulfate_kg_ha": 13.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 38,
            "optimum_temperature_c": 30.0,
            "min_ph": 5.5,
            "max_ph": 7.2,
            "min_annual_rainfall_mm": 1400,
            "max_annual_rainfall_mm": 2800
        },
        "production_economics": {
            "potential_yield_kg_acre": 2400,
            "benchmark_mandi_price_rs_qtl": 2500,
            "estimated_cost_cultivation_acre": 19000,
            "gross_return_acre": 60000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1190.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0243",
        "crop_name": "Rice (BPT 5204 / Samba Mahsuri) - Select Genotype v7",
        "category": "Cereal",
        "growing_duration_days": 150,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 100,
            "phosphorus_kg_ha": 50,
            "potassium_kg_ha": 50,
            "sulfur_kg_ha": 32,
            "zinc_sulfate_kg_ha": 14.5
        },
        "climate_envelope": {
            "min_temperature_c": 20,
            "max_temperature_c": 36,
            "optimum_temperature_c": 28.0,
            "min_ph": 6.0,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 1500,
            "max_annual_rainfall_mm": 3000
        },
        "production_economics": {
            "potential_yield_kg_acre": 2600,
            "benchmark_mandi_price_rs_qtl": 2700,
            "estimated_cost_cultivation_acre": 20000,
            "gross_return_acre": 70200
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1275.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0244",
        "crop_name": "Rice (MTU 1010 / Cottondora Sannalu) - Select Genotype v7",
        "category": "Cereal",
        "growing_duration_days": 125,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 33,
            "zinc_sulfate_kg_ha": 15.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 38,
            "optimum_temperature_c": 30.0,
            "min_ph": 5.5,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 1300,
            "max_annual_rainfall_mm": 2600
        },
        "production_economics": {
            "potential_yield_kg_acre": 3100,
            "benchmark_mandi_price_rs_qtl": 2200,
            "estimated_cost_cultivation_acre": 21000,
            "gross_return_acre": 68200
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1105.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0245",
        "crop_name": "Rice (IR 64 High Yield) - Select Genotype v7",
        "category": "Cereal",
        "growing_duration_days": 120,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 34,
            "zinc_sulfate_kg_ha": 16.5
        },
        "climate_envelope": {
            "min_temperature_c": 22,
            "max_temperature_c": 38,
            "optimum_temperature_c": 30.0,
            "min_ph": 5.5,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 1400,
            "max_annual_rainfall_mm": 2800
        },
        "production_economics": {
            "potential_yield_kg_acre": 3200,
            "benchmark_mandi_price_rs_qtl": 2100,
            "estimated_cost_cultivation_acre": 22000,
            "gross_return_acre": 67200
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 1190.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0246",
        "crop_name": "Wheat (HD 2967 High Yield) - Select Genotype v7",
        "category": "Cereal",
        "growing_duration_days": 125,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 35,
            "zinc_sulfate_kg_ha": 17.5
        },
        "climate_envelope": {
            "min_temperature_c": 12,
            "max_temperature_c": 25,
            "optimum_temperature_c": 18.5,
            "min_ph": 6.0,
            "max_ph": 7.8,
            "min_annual_rainfall_mm": 450,
            "max_annual_rainfall_mm": 900
        },
        "production_economics": {
            "potential_yield_kg_acre": 2400,
            "benchmark_mandi_price_rs_qtl": 2350,
            "estimated_cost_cultivation_acre": 23000,
            "gross_return_acre": 56400
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 382.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0247",
        "crop_name": "Wheat (HD 3086 Pusa Gautami) - Select Genotype v7",
        "category": "Cereal",
        "growing_duration_days": 120,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 120,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 36,
            "zinc_sulfate_kg_ha": 18.5
        },
        "climate_envelope": {
            "min_temperature_c": 12,
            "max_temperature_c": 26,
            "optimum_temperature_c": 19.0,
            "min_ph": 6.0,
            "max_ph": 7.8,
            "min_annual_rainfall_mm": 450,
            "max_annual_rainfall_mm": 900
        },
        "production_economics": {
            "potential_yield_kg_acre": 2500,
            "benchmark_mandi_price_rs_qtl": 2400,
            "estimated_cost_cultivation_acre": 24000,
            "gross_return_acre": 60000
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 382.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0248",
        "crop_name": "Wheat (PBW 343 / Shriram 303) - Select Genotype v7",
        "category": "Cereal",
        "growing_duration_days": 130,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 130,
            "phosphorus_kg_ha": 65,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 37,
            "zinc_sulfate_kg_ha": 19.5
        },
        "climate_envelope": {
            "min_temperature_c": 10,
            "max_temperature_c": 24,
            "optimum_temperature_c": 17.0,
            "min_ph": 6.0,
            "max_ph": 7.8,
            "min_annual_rainfall_mm": 450,
            "max_annual_rainfall_mm": 900
        },
        "production_economics": {
            "potential_yield_kg_acre": 2600,
            "benchmark_mandi_price_rs_qtl": 2300,
            "estimated_cost_cultivation_acre": 25000,
            "gross_return_acre": 59800
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 382.5,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0249",
        "crop_name": "Wheat (DBW 187 Karan Vandana) - Select Genotype v7",
        "category": "Cereal",
        "growing_duration_days": 120,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 130,
            "phosphorus_kg_ha": 60,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 38,
            "zinc_sulfate_kg_ha": 20.5
        },
        "climate_envelope": {
            "min_temperature_c": 12,
            "max_temperature_c": 27,
            "optimum_temperature_c": 19.5,
            "min_ph": 6.0,
            "max_ph": 7.8,
            "min_annual_rainfall_mm": 400,
            "max_annual_rainfall_mm": 800
        },
        "production_economics": {
            "potential_yield_kg_acre": 2700,
            "benchmark_mandi_price_rs_qtl": 2500,
            "estimated_cost_cultivation_acre": 26000,
            "gross_return_acre": 67500
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 340.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
    {
        "crop_id": "CROP-0250",
        "crop_name": "Maize (Pioneer P3396 Hybrid) - Select Genotype v7",
        "category": "Cereal",
        "growing_duration_days": 110,
        "nutrient_requirements": {
            "nitrogen_kg_ha": 140,
            "phosphorus_kg_ha": 65,
            "potassium_kg_ha": 60,
            "sulfur_kg_ha": 39,
            "zinc_sulfate_kg_ha": 21.5
        },
        "climate_envelope": {
            "min_temperature_c": 18,
            "max_temperature_c": 35,
            "optimum_temperature_c": 26.5,
            "min_ph": 5.8,
            "max_ph": 7.5,
            "min_annual_rainfall_mm": 600,
            "max_annual_rainfall_mm": 1200
        },
        "production_economics": {
            "potential_yield_kg_acre": 3600,
            "benchmark_mandi_price_rs_qtl": 2150,
            "estimated_cost_cultivation_acre": 27000,
            "gross_return_acre": 77400
        },
        "irrigation_protocol": {
            "critical_stages": ["Crown Root Initiation", "Tillering", "Heading", "Grain Filling"],
            "total_water_requirement_mm": 510.0,
            "preferred_method": "Micro-Sprinkler / Furrow"
        }
    },
]
