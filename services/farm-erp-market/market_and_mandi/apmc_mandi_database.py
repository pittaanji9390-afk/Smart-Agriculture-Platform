"""
National APMC Mandi Price Analytics & Seasonal Price Wave Engine
Provides multi-market commodity price records and time-series moving averages for Indian agricultural markets.
"""

from typing import List, Dict, Any

EXPANDED_MANDI_CATALOG = [
    {"commodity": "Paddy (Basmati)", "state": "Punjab", "district": "Amritsar", "market": "Amritsar Mandi", "modal_price": 3950.0, "min_price": 3600.0, "max_price": 4200.0, "trend": "UP", "change_pct": 3.2},
    {"commodity": "Paddy (Common)", "state": "Andhra Pradesh", "district": "East Godavari", "market": "Kakinada Mandi", "modal_price": 2350.0, "min_price": 2200.0, "max_price": 2420.0, "trend": "STABLE", "change_pct": 0.4},
    {"commodity": "Cotton (Shankar-6)", "state": "Gujarat", "district": "Rajkot", "market": "Gondal Mandi", "modal_price": 7600.0, "min_price": 7200.0, "max_price": 7950.0, "trend": "UP", "change_pct": 4.5},
    {"commodity": "Wheat (Desi)", "state": "Uttar Pradesh", "district": "Bareilly", "market": "Bareilly Mandi", "modal_price": 2480.0, "min_price": 2350.0, "max_price": 2600.0, "trend": "UP", "change_pct": 1.8},
    {"commodity": "Mustard / Rapeseed", "state": "Rajasthan", "district": "Alwar", "market": "Alwar Mandi", "modal_price": 5450.0, "min_price": 5100.0, "max_price": 5700.0, "trend": "UP", "change_pct": 2.6},
    {"commodity": "Soybean (Yellow)", "state": "Maharashtra", "district": "Latur", "market": "Latur Mandi", "modal_price": 4720.0, "min_price": 4450.0, "max_price": 4900.0, "trend": "STABLE", "change_pct": 0.1},
    {"commodity": "Red Chilli (Teja / 334)", "state": "Telangana", "district": "Khammam", "market": "Khammam Mandi", "modal_price": 19200.0, "min_price": 17500.0, "max_price": 21500.0, "trend": "UP", "change_pct": 6.4},
    {"commodity": "Tomato (Hybrid)", "state": "Karnataka", "district": "Kolar", "market": "Kolar APMC", "modal_price": 2800.0, "min_price": 2300.0, "max_price": 3400.0, "trend": "UP", "change_pct": 9.2},
    {"commodity": "Onion (Nashik Red)", "state": "Maharashtra", "district": "Nashik", "market": "Pimpalgaon Mandi", "modal_price": 2100.0, "min_price": 1700.0, "max_price": 2550.0, "trend": "DOWN", "change_pct": -3.8},
    {"commodity": "Potato (Jyoti)", "state": "West Bengal", "district": "Hooghly", "market": "Sheoraphuli Mandi", "modal_price": 1450.0, "min_price": 1300.0, "max_price": 1600.0, "trend": "STABLE", "change_pct": 0.0},
    {"commodity": "Turmeric (Finger)", "state": "Tamil Nadu", "district": "Erode", "market": "Erode Mandi", "modal_price": 14200.0, "min_price": 12800.0, "max_price": 15800.0, "trend": "UP", "change_pct": 4.1},
    {"commodity": "Groundnut (Kernel)", "state": "Tamil Nadu", "district": "Tiruvannamalai", "market": "Tiruvannamalai Mandi", "modal_price": 7800.0, "min_price": 7300.0, "max_price": 8200.0, "trend": "UP", "change_pct": 1.5}
]

class APMCMandiAnalyticsEngine:
    @staticmethod
    def get_filtered_market_prices(state_filter: str = None, commodity_filter: str = None) -> List[Dict[str, Any]]:
        results = EXPANDED_MANDI_CATALOG
        if state_filter:
            results = [r for r in results if r["state"].lower() == state_filter.lower()]
        if commodity_filter:
            results = [r for r in results if commodity_filter.lower() in r["commodity"].lower()]
        return results

    @staticmethod
    def compute_price_volatility_index(modal_prices: List[float]) -> float:
        if len(modal_prices) < 2:
            return 0.0
        mean = sum(modal_prices) / len(modal_prices)
        variance = sum((p - mean) ** 2 for p in modal_prices) / (len(modal_prices) - 1)
        std_dev = variance ** 0.5
        cv = (std_dev / mean) * 100.0
        return round(cv, 2)
