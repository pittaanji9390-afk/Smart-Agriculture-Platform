"""
Crop Cultivation Dossiers - Batch 3
"""
from typing import Dict, Any, List

CROPS_CROP_BATCH_03: List[Dict[str, Any]] = [
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
]
