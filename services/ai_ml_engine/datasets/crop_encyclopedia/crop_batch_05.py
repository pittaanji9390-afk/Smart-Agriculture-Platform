"""
Crop Cultivation Dossiers - Batch 5
"""
from typing import Dict, Any, List

CROPS_CROP_BATCH_05: List[Dict[str, Any]] = [
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
]
