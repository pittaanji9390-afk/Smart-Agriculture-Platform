"""
National Varietal Seed Certification & Genetic Purity Standards Registry
Covers Indian Minimum Seed Certification Standards (IMSCS) across Breeder, Foundation, and Certified Seed classes.
"""

from typing import Dict, Any, List

NATIONAL_SEED_CERTIFICATION_STANDARDS: List[Dict[str, Any]] = [
    {
        "crop_group": "Cereals (Paddy / Rice)",
        "isolation_distance_meters_foundation": 3.0,
        "isolation_distance_meters_certified": 3.0,
        "min_pure_seed_pct": 98.0,
        "max_inert_matter_pct": 2.0,
        "max_other_crop_seeds_count_per_kg": 10,
        "max_weed_seeds_count_per_kg": 10,
        "min_germination_percentage": 80.0,
        "max_moisture_content_pct": 13.0,
        "genetic_purity_odv_test_pct": 99.0
    },
    {
        "crop_group": "Cereals (Wheat)",
        "isolation_distance_meters_foundation": 3.0,
        "isolation_distance_meters_certified": 3.0,
        "min_pure_seed_pct": 98.0,
        "max_inert_matter_pct": 2.0,
        "max_other_crop_seeds_count_per_kg": 10,
        "max_weed_seeds_count_per_kg": 5,
        "min_germination_percentage": 85.0,
        "max_moisture_content_pct": 12.0,
        "genetic_purity_odv_test_pct": 99.0
    },
    {
        "crop_group": "Cereals (Maize Hybrid Inbred Lines)",
        "isolation_distance_meters_foundation": 400.0,
        "isolation_distance_meters_certified": 200.0,
        "min_pure_seed_pct": 98.0,
        "max_inert_matter_pct": 2.0,
        "max_other_crop_seeds_count_per_kg": 0,
        "max_weed_seeds_count_per_kg": 0,
        "min_germination_percentage": 90.0,
        "max_moisture_content_pct": 12.0,
        "genetic_purity_odv_test_pct": 99.5
    },
    {
        "crop_group": "Pulses (Chickpea / Bengal Gram)",
        "isolation_distance_meters_foundation": 10.0,
        "isolation_distance_meters_certified": 5.0,
        "min_pure_seed_pct": 98.0,
        "max_inert_matter_pct": 2.0,
        "max_other_crop_seeds_count_per_kg": 0,
        "max_weed_seeds_count_per_kg": 0,
        "min_germination_percentage": 85.0,
        "max_moisture_content_pct": 9.0,
        "genetic_purity_odv_test_pct": 99.0
    },
    {
        "crop_group": "Pulses (Pigeon Pea / Red Gram)",
        "isolation_distance_meters_foundation": 200.0,
        "isolation_distance_meters_certified": 100.0,
        "min_pure_seed_pct": 98.0,
        "max_inert_matter_pct": 2.0,
        "max_other_crop_seeds_count_per_kg": 5,
        "max_weed_seeds_count_per_kg": 5,
        "min_germination_percentage": 75.0,
        "max_moisture_content_pct": 9.0,
        "genetic_purity_odv_test_pct": 99.0
    },
    {
        "crop_group": "Oilseeds (Soybean)",
        "isolation_distance_meters_foundation": 3.0,
        "isolation_distance_meters_certified": 3.0,
        "min_pure_seed_pct": 98.0,
        "max_inert_matter_pct": 2.0,
        "max_other_crop_seeds_count_per_kg": 5,
        "max_weed_seeds_count_per_kg": 0,
        "min_germination_percentage": 70.0,
        "max_moisture_content_pct": 12.0,
        "genetic_purity_odv_test_pct": 99.0
    },
    {
        "crop_group": "Oilseeds (Groundnut)",
        "isolation_distance_meters_foundation": 3.0,
        "isolation_distance_meters_certified": 3.0,
        "min_pure_seed_pct": 96.0,
        "max_inert_matter_pct": 4.0,
        "max_other_crop_seeds_count_per_kg": 0,
        "max_weed_seeds_count_per_kg": 0,
        "min_germination_percentage": 70.0,
        "max_moisture_content_pct": 9.0,
        "genetic_purity_odv_test_pct": 99.0
    },
    {
        "crop_group": "Fiber (Cotton Hybrid)",
        "isolation_distance_meters_foundation": 50.0,
        "isolation_distance_meters_certified": 30.0,
        "min_pure_seed_pct": 98.0,
        "max_inert_matter_pct": 2.0,
        "max_other_crop_seeds_count_per_kg": 5,
        "max_weed_seeds_count_per_kg": 0,
        "min_germination_percentage": 65.0,
        "max_moisture_content_pct": 10.0,
        "genetic_purity_odv_test_pct": 99.0
    },
    {
        "crop_group": "Vegetables (Tomato Hybrid F1)",
        "isolation_distance_meters_foundation": 200.0,
        "isolation_distance_meters_certified": 100.0,
        "min_pure_seed_pct": 98.0,
        "max_inert_matter_pct": 2.0,
        "max_other_crop_seeds_count_per_kg": 0,
        "max_weed_seeds_count_per_kg": 0,
        "min_germination_percentage": 70.0,
        "max_moisture_content_pct": 8.0,
        "genetic_purity_odv_test_pct": 99.5
    },
    {
        "crop_group": "Vegetables (Chilli Hybrid F1)",
        "isolation_distance_meters_foundation": 400.0,
        "isolation_distance_meters_certified": 200.0,
        "min_pure_seed_pct": 98.0,
        "max_inert_matter_pct": 2.0,
        "max_other_crop_seeds_count_per_kg": 0,
        "max_weed_seeds_count_per_kg": 0,
        "min_germination_percentage": 60.0,
        "max_moisture_content_pct": 8.0,
        "genetic_purity_odv_test_pct": 99.0
    }
]
