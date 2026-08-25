"""
Unit Tests for Inter-Mandi Price Arbitrage Optimizer
"""

from services.farm_erp_market.market_and_mandi.inter_mandi_arbitrage_engine import MandiArbitrageOptimizer

def test_mandi_arbitrage_ranking():
    markets = [
        {"market_name": "Local District APMC", "distance_km": 15.0, "modal_price_rs_qtl": 2200.0},
        {"market_name": "Major Terminal Hub APMC", "distance_km": 120.0, "modal_price_rs_qtl": 2650.0}
    ]
    
    res = MandiArbitrageOptimizer.calculate_best_mandi_destination(
        origin_district="Kurnool",
        commodity="Paddy Sona Masoori",
        total_quantity_quintals=100.0,
        candidate_markets=markets
    )
    
    assert "optimal_market_destination" in res
    assert len(res["market_comparison_table"]) == 2
    # Even after 120km freight, major terminal hub yields higher net profit
    assert res["optimal_market_destination"]["market_name"] == "Major Terminal Hub APMC"
    assert res["optimal_market_destination"]["net_realizable_revenue_inr"] > 0
