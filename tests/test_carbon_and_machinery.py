"""
Unit Tests for Carbon Sequestration Accounting & Farm Machinery Fleet Telematics
"""

from services.ai_ml_engine.carbon_accounting.carbon_sequestration_engine import RegenerativeCarbonProtocol_001
from services.farm_erp_market.machinery_fleet.farm_machinery_telematics import MachineryTelematicsController_001

def test_carbon_sequestration_accounting():
    res = RegenerativeCarbonProtocol_001.compute_net_co2e_reduction(
        field_area_ha=10.0,
        adoption_years=5,
        cover_crop_adopted=True,
        biochar_rate_tonnes_ha=3.0,
        zero_tillage_practiced=True
    )
    assert res["field_area_ha"] == 10.0
    assert res["adoption_years"] == 5
    assert res["total_co2e_sequestered_tonnes"] > 0
    assert res["total_verifiable_carbon_credits_tco2e"] > 0
    assert res["carbon_credit_market_value_eur"] > 0
    assert res["carbon_credit_market_value_inr"] > 0

def test_machinery_telematics_efficiency():
    telematics = MachineryTelematicsController_001.compute_field_operation_efficiency(
        engine_hours=8.0,
        field_area_ha=6.0,
        implement_type="Rotavator",
        soil_hardness_penetrometer_kpa=1100.0,
        engine_load_percentage=75.0
    )
    assert telematics["total_engine_runtime_hours"] == 8.0
    assert telematics["field_coverage_rate_ha_per_hr"] == 0.75
    assert telematics["diesel_consumed_liters"] > 0
    assert telematics["total_fuel_expense_inr"] > 0
    assert "telematics_health_status" in telematics
