"""
Farm Input Cost, Machinery Telematics & Enterprise P&L Accounting Engine
Provides comprehensive cost of cultivation analysis (seeds, tillage, fertilizers, crop protection, harvest, labor, machinery).
"""

from typing import Dict, Any, List

class FarmEconomicsAccountingEngine:
    @staticmethod
    def compute_enterprise_crop_pl(
        crop_name: str,
        cultivated_acres: float,
        seed_cost_inr: float,
        tillage_machinery_cost_inr: float,
        fertilizer_cost_inr: float,
        pesticide_spray_cost_inr: float,
        irrigation_electricity_cost_inr: float,
        labor_cost_inr: float,
        harvesting_threshing_cost_inr: float,
        actual_harvest_yield_quintals: float,
        modal_selling_price_rs_qtl: float
    ) -> Dict[str, Any]:
        """
        Calculates detailed economic balance sheet for a crop season.
        """
        total_input_cost = (
            seed_cost_inr +
            tillage_machinery_cost_inr +
            fertilizer_cost_inr +
            pesticide_spray_cost_inr +
            irrigation_electricity_cost_inr +
            labor_cost_inr +
            harvesting_threshing_cost_inr
        )

        cost_per_acre = total_input_cost / max(0.1, cultivated_acres)
        cost_per_quintal_produced = total_input_cost / max(0.1, actual_harvest_yield_quintals)

        gross_revenue = actual_harvest_yield_quintals * modal_selling_price_rs_qtl
        net_profit = gross_revenue - total_input_cost
        profit_per_acre = net_profit / max(0.1, cultivated_acres)
        roi_percentage = (net_profit / total_input_cost) * 100.0 if total_input_cost > 0 else 0.0
        benefit_cost_ratio = gross_revenue / total_input_cost if total_input_cost > 0 else 0.0

        return {
            "crop_name": crop_name,
            "cultivated_acres": cultivated_acres,
            "total_harvest_yield_quintals": round(actual_harvest_yield_quintals, 2),
            "yield_per_acre_quintals": round(actual_harvest_yield_quintals / max(0.1, cultivated_acres), 2),
            "financial_summary": {
                "total_input_cost_inr": round(total_input_cost, 2),
                "gross_revenue_inr": round(gross_revenue, 2),
                "net_profit_inr": round(net_profit, 2),
                "profit_per_acre_inr": round(profit_per_acre, 2),
                "cost_per_quintal_inr": round(cost_per_quintal_produced, 2),
                "return_on_investment_pct": round(roi_percentage, 1),
                "benefit_cost_ratio": round(benefit_cost_ratio, 2)
            },
            "cost_breakdown_percentages": {
                "seeds_pct": round((seed_cost_inr / total_input_cost) * 100.0, 1),
                "tillage_machinery_pct": round((tillage_machinery_cost_inr / total_input_cost) * 100.0, 1),
                "fertilizers_pct": round((fertilizer_cost_inr / total_input_cost) * 100.0, 1),
                "pesticides_pct": round((pesticide_spray_cost_inr / total_input_cost) * 100.0, 1),
                "irrigation_power_pct": round((irrigation_electricity_cost_inr / total_input_cost) * 100.0, 1),
                "labor_pct": round((labor_cost_inr / total_input_cost) * 100.0, 1),
                "harvesting_pct": round((harvesting_threshing_cost_inr / total_input_cost) * 100.0, 1)
            }
        }
