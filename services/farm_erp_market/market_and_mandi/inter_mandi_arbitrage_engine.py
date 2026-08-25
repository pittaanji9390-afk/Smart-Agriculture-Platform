"""
Inter-Mandi Price Arbitrage & Freight Logistics Optimization Engine
"""

from typing import Dict, Any, List

class MandiArbitrageOptimizer:
    """
    Computes net profit realization across alternative regional APMC terminal markets
    accounting for freight hauling distance, truck diesel fuel costs, toll taxes, and market cess.
    """
    DIESEL_COST_PER_KM = 22.50 # INR per km for 10-tonne commercial truck
    LOADING_UNLOADING_PER_QTL = 35.0 # INR per quintal
    APMC_CESS_PERCENTAGE = 1.50 # % mandi fee

    @classmethod
    def calculate_best_mandi_destination(
        cls,
        origin_district: str,
        commodity: str,
        total_quantity_quintals: float,
        candidate_markets: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        results = []
        for m in candidate_markets:
            market_name = m["market_name"]
            distance_km = m.get("distance_km", 50.0)
            modal_price_qtl = m["modal_price_rs_qtl"]

            gross_revenue = total_quantity_quintals * modal_price_qtl
            freight_cost = distance_km * cls.DIESEL_COST_PER_KM * 2.0 # Round-trip hauling
            handling_cost = total_quantity_quintals * cls.LOADING_UNLOADING_PER_QTL
            mandi_cess = gross_revenue * (cls.APMC_CESS_PERCENTAGE / 100.0)
            total_logistics = freight_cost + handling_cost + mandi_cess

            net_revenue = gross_revenue - total_logistics
            net_price_per_qtl = net_revenue / max(1.0, total_quantity_quintals)

            results.append({
                "market_name": market_name,
                "distance_km": distance_km,
                "gross_modal_price_rs_qtl": modal_price_qtl,
                "freight_cost_inr": round(freight_cost, 2),
                "total_expenses_inr": round(total_logistics, 2),
                "net_realizable_revenue_inr": round(net_revenue, 2),
                "net_realized_price_rs_qtl": round(net_price_per_qtl, 2)
            })

        # Sort by highest net realizable revenue
        ranked = sorted(results, key=lambda x: x["net_realizable_revenue_inr"], reverse=True)
        best_choice = ranked[0] if ranked else None

        return {
            "origin_district": origin_district,
            "commodity": commodity,
            "total_quantity_quintals": total_quantity_quintals,
            "optimal_market_destination": best_choice,
            "market_comparison_table": ranked
        }
