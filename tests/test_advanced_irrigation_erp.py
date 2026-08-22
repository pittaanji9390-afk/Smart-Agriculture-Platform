"""
Unit Tests for Dual Crop Coefficient Water Balance, A/B Fertigation Recipes & Farm P&L Accounting
"""

from services.smart_irrigation.fao56_engine.dual_crop_coefficient import FAODualCropCoefficientEngine
from services.smart_irrigation.scheduling.fertigation_recipe_engine import FertigationRecipeEngine
from services.farm_erp_market.accounting_economics.input_cost_analyzer import FarmEconomicsAccountingEngine
from services.farm_erp_market.market_and_mandi.apmc_mandi_database import APMCMandiAnalyticsEngine

def test_dual_crop_coefficient_water_balance():
    res = FAODualCropCoefficientEngine.calculate_soil_water_balance(
        crop="Tomato",
        soil_type="Sandy Loam",
        root_depth_m=0.6,
        reference_et0_mm=5.5,
        stage_fraction=0.5,
        current_depletion_mm=38.0
    )
    assert res["taw_mm"] > 0.0
    assert res["raw_mm"] > 0.0
    assert "irrigation_trigger_status" in res

def test_fertigation_recipe_calculator():
    batch = FertigationRecipeEngine.calculate_tank_batch(
        crop_recipe="Tomato (Fruiting)",
        water_volume_liters=20000.0
    )
    assert len(batch["tank_a_fertilizers"]) == 3
    assert len(batch["tank_b_fertilizers"]) == 3
    assert batch["tank_a_fertilizers"][0]["weight_kg"] > 0

def test_farm_enterprise_pl():
    pl = FarmEconomicsAccountingEngine.compute_enterprise_crop_pl(
        crop_name="Cotton",
        cultivated_acres=4.0,
        seed_cost_inr=6000.0,
        tillage_machinery_cost_inr=8000.0,
        fertilizer_cost_inr=14000.0,
        pesticide_spray_cost_inr=8000.0,
        irrigation_electricity_cost_inr=4000.0,
        labor_cost_inr=20000.0,
        harvesting_threshing_cost_inr=10000.0,
        actual_harvest_yield_quintals=48.0,
        modal_selling_price_rs_qtl=7500.0
    )
    assert pl["financial_summary"]["gross_revenue_inr"] == 360000.0
    assert pl["financial_summary"]["net_profit_inr"] > 250000.0
    assert pl["financial_summary"]["return_on_investment_pct"] > 300.0

def test_mandi_volatility():
    prices = [2100.0, 2150.0, 2200.0, 2180.0, 2250.0]
    vol = APMCMandiAnalyticsEngine.compute_price_volatility_index(prices)
    assert vol > 0.0
    assert vol < 10.0
