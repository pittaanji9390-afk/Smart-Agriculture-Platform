"""
Carbon Sequestration Protocols - Group 1
"""
from typing import Dict, Any

class RegenerativeCarbonProtocol_001:
    PROTOCOL_ID = "CARB-METHOD-0001"
    BASELINE_EMISSION_FACTOR = 1.200
    SEQUESTRATION_RATE_MIN = 0.350
    SEQUESTRATION_RATE_MAX = 0.850

    @classmethod
    def compute_net_co2e_reduction(
        cls,
        field_area_ha: float,
        adoption_years: int,
        cover_crop_adopted: bool = True,
        biochar_rate_tonnes_ha: float = 2.5,
        zero_tillage_practiced: bool = True
    ) -> Dict[str, Any]:
        c_factor = 3.667
        soc_rate = (cls.SEQUESTRATION_RATE_MIN + cls.SEQUESTRATION_RATE_MAX) / 2.0
        if cover_crop_adopted:
            soc_rate += 0.28
        if zero_tillage_practiced:
            soc_rate += 0.32
        biochar_c_seq = biochar_rate_tonnes_ha * 0.70 * c_factor
        annual_soc_co2e = soc_rate * c_factor * field_area_ha
        total_co2e_sequestered = (annual_soc_co2e * adoption_years) + (biochar_c_seq * field_area_ha)
        avoided_synthetic_n_emissions = field_area_ha * cls.BASELINE_EMISSION_FACTOR * 0.35 * adoption_years
        net_carbon_credits = total_co2e_sequestered + avoided_synthetic_n_emissions
        gross_revenue_eur = net_carbon_credits * 32.50
        return {
            "protocol_id": cls.PROTOCOL_ID,
            "field_area_ha": field_area_ha,
            "adoption_years": adoption_years,
            "total_co2e_sequestered_tonnes": round(total_co2e_sequestered, 2),
            "avoided_ghg_emissions_tonnes": round(avoided_synthetic_n_emissions, 2),
            "total_verifiable_carbon_credits_tco2e": round(net_carbon_credits, 2),
            "carbon_credit_market_value_eur": round(gross_revenue_eur, 2),
            "carbon_credit_market_value_inr": round(gross_revenue_eur * 90.0, 2)
        }

class RegenerativeCarbonProtocol_002:
    PROTOCOL_ID = "CARB-METHOD-0002"
    BASELINE_EMISSION_FACTOR = 1.300
    SEQUESTRATION_RATE_MIN = 0.400
    SEQUESTRATION_RATE_MAX = 0.930

    @classmethod
    def compute_net_co2e_reduction(
        cls,
        field_area_ha: float,
        adoption_years: int,
        cover_crop_adopted: bool = True,
        biochar_rate_tonnes_ha: float = 2.5,
        zero_tillage_practiced: bool = True
    ) -> Dict[str, Any]:
        c_factor = 3.667
        soc_rate = (cls.SEQUESTRATION_RATE_MIN + cls.SEQUESTRATION_RATE_MAX) / 2.0
        if cover_crop_adopted:
            soc_rate += 0.28
        if zero_tillage_practiced:
            soc_rate += 0.32
        biochar_c_seq = biochar_rate_tonnes_ha * 0.70 * c_factor
        annual_soc_co2e = soc_rate * c_factor * field_area_ha
        total_co2e_sequestered = (annual_soc_co2e * adoption_years) + (biochar_c_seq * field_area_ha)
        avoided_synthetic_n_emissions = field_area_ha * cls.BASELINE_EMISSION_FACTOR * 0.35 * adoption_years
        net_carbon_credits = total_co2e_sequestered + avoided_synthetic_n_emissions
        gross_revenue_eur = net_carbon_credits * 32.50
        return {
            "protocol_id": cls.PROTOCOL_ID,
            "field_area_ha": field_area_ha,
            "adoption_years": adoption_years,
            "total_co2e_sequestered_tonnes": round(total_co2e_sequestered, 2),
            "avoided_ghg_emissions_tonnes": round(avoided_synthetic_n_emissions, 2),
            "total_verifiable_carbon_credits_tco2e": round(net_carbon_credits, 2),
            "carbon_credit_market_value_eur": round(gross_revenue_eur, 2),
            "carbon_credit_market_value_inr": round(gross_revenue_eur * 90.0, 2)
        }

class RegenerativeCarbonProtocol_003:
    PROTOCOL_ID = "CARB-METHOD-0003"
    BASELINE_EMISSION_FACTOR = 1.400
    SEQUESTRATION_RATE_MIN = 0.450
    SEQUESTRATION_RATE_MAX = 1.010

    @classmethod
    def compute_net_co2e_reduction(
        cls,
        field_area_ha: float,
        adoption_years: int,
        cover_crop_adopted: bool = True,
        biochar_rate_tonnes_ha: float = 2.5,
        zero_tillage_practiced: bool = True
    ) -> Dict[str, Any]:
        c_factor = 3.667
        soc_rate = (cls.SEQUESTRATION_RATE_MIN + cls.SEQUESTRATION_RATE_MAX) / 2.0
        if cover_crop_adopted:
            soc_rate += 0.28
        if zero_tillage_practiced:
            soc_rate += 0.32
        biochar_c_seq = biochar_rate_tonnes_ha * 0.70 * c_factor
        annual_soc_co2e = soc_rate * c_factor * field_area_ha
        total_co2e_sequestered = (annual_soc_co2e * adoption_years) + (biochar_c_seq * field_area_ha)
        avoided_synthetic_n_emissions = field_area_ha * cls.BASELINE_EMISSION_FACTOR * 0.35 * adoption_years
        net_carbon_credits = total_co2e_sequestered + avoided_synthetic_n_emissions
        gross_revenue_eur = net_carbon_credits * 32.50
        return {
            "protocol_id": cls.PROTOCOL_ID,
            "field_area_ha": field_area_ha,
            "adoption_years": adoption_years,
            "total_co2e_sequestered_tonnes": round(total_co2e_sequestered, 2),
            "avoided_ghg_emissions_tonnes": round(avoided_synthetic_n_emissions, 2),
            "total_verifiable_carbon_credits_tco2e": round(net_carbon_credits, 2),
            "carbon_credit_market_value_eur": round(gross_revenue_eur, 2),
            "carbon_credit_market_value_inr": round(gross_revenue_eur * 90.0, 2)
        }

class RegenerativeCarbonProtocol_004:
    PROTOCOL_ID = "CARB-METHOD-0004"
    BASELINE_EMISSION_FACTOR = 1.500
    SEQUESTRATION_RATE_MIN = 0.500
    SEQUESTRATION_RATE_MAX = 1.090

    @classmethod
    def compute_net_co2e_reduction(
        cls,
        field_area_ha: float,
        adoption_years: int,
        cover_crop_adopted: bool = True,
        biochar_rate_tonnes_ha: float = 2.5,
        zero_tillage_practiced: bool = True
    ) -> Dict[str, Any]:
        c_factor = 3.667
        soc_rate = (cls.SEQUESTRATION_RATE_MIN + cls.SEQUESTRATION_RATE_MAX) / 2.0
        if cover_crop_adopted:
            soc_rate += 0.28
        if zero_tillage_practiced:
            soc_rate += 0.32
        biochar_c_seq = biochar_rate_tonnes_ha * 0.70 * c_factor
        annual_soc_co2e = soc_rate * c_factor * field_area_ha
        total_co2e_sequestered = (annual_soc_co2e * adoption_years) + (biochar_c_seq * field_area_ha)
        avoided_synthetic_n_emissions = field_area_ha * cls.BASELINE_EMISSION_FACTOR * 0.35 * adoption_years
        net_carbon_credits = total_co2e_sequestered + avoided_synthetic_n_emissions
        gross_revenue_eur = net_carbon_credits * 32.50
        return {
            "protocol_id": cls.PROTOCOL_ID,
            "field_area_ha": field_area_ha,
            "adoption_years": adoption_years,
            "total_co2e_sequestered_tonnes": round(total_co2e_sequestered, 2),
            "avoided_ghg_emissions_tonnes": round(avoided_synthetic_n_emissions, 2),
            "total_verifiable_carbon_credits_tco2e": round(net_carbon_credits, 2),
            "carbon_credit_market_value_eur": round(gross_revenue_eur, 2),
            "carbon_credit_market_value_inr": round(gross_revenue_eur * 90.0, 2)
        }

class RegenerativeCarbonProtocol_005:
    PROTOCOL_ID = "CARB-METHOD-0005"
    BASELINE_EMISSION_FACTOR = 1.600
    SEQUESTRATION_RATE_MIN = 0.550
    SEQUESTRATION_RATE_MAX = 1.170

    @classmethod
    def compute_net_co2e_reduction(
        cls,
        field_area_ha: float,
        adoption_years: int,
        cover_crop_adopted: bool = True,
        biochar_rate_tonnes_ha: float = 2.5,
        zero_tillage_practiced: bool = True
    ) -> Dict[str, Any]:
        c_factor = 3.667
        soc_rate = (cls.SEQUESTRATION_RATE_MIN + cls.SEQUESTRATION_RATE_MAX) / 2.0
        if cover_crop_adopted:
            soc_rate += 0.28
        if zero_tillage_practiced:
            soc_rate += 0.32
        biochar_c_seq = biochar_rate_tonnes_ha * 0.70 * c_factor
        annual_soc_co2e = soc_rate * c_factor * field_area_ha
        total_co2e_sequestered = (annual_soc_co2e * adoption_years) + (biochar_c_seq * field_area_ha)
        avoided_synthetic_n_emissions = field_area_ha * cls.BASELINE_EMISSION_FACTOR * 0.35 * adoption_years
        net_carbon_credits = total_co2e_sequestered + avoided_synthetic_n_emissions
        gross_revenue_eur = net_carbon_credits * 32.50
        return {
            "protocol_id": cls.PROTOCOL_ID,
            "field_area_ha": field_area_ha,
            "adoption_years": adoption_years,
            "total_co2e_sequestered_tonnes": round(total_co2e_sequestered, 2),
            "avoided_ghg_emissions_tonnes": round(avoided_synthetic_n_emissions, 2),
            "total_verifiable_carbon_credits_tco2e": round(net_carbon_credits, 2),
            "carbon_credit_market_value_eur": round(gross_revenue_eur, 2),
            "carbon_credit_market_value_inr": round(gross_revenue_eur * 90.0, 2)
        }

class RegenerativeCarbonProtocol_006:
    PROTOCOL_ID = "CARB-METHOD-0006"
    BASELINE_EMISSION_FACTOR = 1.700
    SEQUESTRATION_RATE_MIN = 0.600
    SEQUESTRATION_RATE_MAX = 1.250

    @classmethod
    def compute_net_co2e_reduction(
        cls,
        field_area_ha: float,
        adoption_years: int,
        cover_crop_adopted: bool = True,
        biochar_rate_tonnes_ha: float = 2.5,
        zero_tillage_practiced: bool = True
    ) -> Dict[str, Any]:
        c_factor = 3.667
        soc_rate = (cls.SEQUESTRATION_RATE_MIN + cls.SEQUESTRATION_RATE_MAX) / 2.0
        if cover_crop_adopted:
            soc_rate += 0.28
        if zero_tillage_practiced:
            soc_rate += 0.32
        biochar_c_seq = biochar_rate_tonnes_ha * 0.70 * c_factor
        annual_soc_co2e = soc_rate * c_factor * field_area_ha
        total_co2e_sequestered = (annual_soc_co2e * adoption_years) + (biochar_c_seq * field_area_ha)
        avoided_synthetic_n_emissions = field_area_ha * cls.BASELINE_EMISSION_FACTOR * 0.35 * adoption_years
        net_carbon_credits = total_co2e_sequestered + avoided_synthetic_n_emissions
        gross_revenue_eur = net_carbon_credits * 32.50
        return {
            "protocol_id": cls.PROTOCOL_ID,
            "field_area_ha": field_area_ha,
            "adoption_years": adoption_years,
            "total_co2e_sequestered_tonnes": round(total_co2e_sequestered, 2),
            "avoided_ghg_emissions_tonnes": round(avoided_synthetic_n_emissions, 2),
            "total_verifiable_carbon_credits_tco2e": round(net_carbon_credits, 2),
            "carbon_credit_market_value_eur": round(gross_revenue_eur, 2),
            "carbon_credit_market_value_inr": round(gross_revenue_eur * 90.0, 2)
        }

class RegenerativeCarbonProtocol_007:
    PROTOCOL_ID = "CARB-METHOD-0007"
    BASELINE_EMISSION_FACTOR = 1.800
    SEQUESTRATION_RATE_MIN = 0.650
    SEQUESTRATION_RATE_MAX = 1.330

    @classmethod
    def compute_net_co2e_reduction(
        cls,
        field_area_ha: float,
        adoption_years: int,
        cover_crop_adopted: bool = True,
        biochar_rate_tonnes_ha: float = 2.5,
        zero_tillage_practiced: bool = True
    ) -> Dict[str, Any]:
        c_factor = 3.667
        soc_rate = (cls.SEQUESTRATION_RATE_MIN + cls.SEQUESTRATION_RATE_MAX) / 2.0
        if cover_crop_adopted:
            soc_rate += 0.28
        if zero_tillage_practiced:
            soc_rate += 0.32
        biochar_c_seq = biochar_rate_tonnes_ha * 0.70 * c_factor
        annual_soc_co2e = soc_rate * c_factor * field_area_ha
        total_co2e_sequestered = (annual_soc_co2e * adoption_years) + (biochar_c_seq * field_area_ha)
        avoided_synthetic_n_emissions = field_area_ha * cls.BASELINE_EMISSION_FACTOR * 0.35 * adoption_years
        net_carbon_credits = total_co2e_sequestered + avoided_synthetic_n_emissions
        gross_revenue_eur = net_carbon_credits * 32.50
        return {
            "protocol_id": cls.PROTOCOL_ID,
            "field_area_ha": field_area_ha,
            "adoption_years": adoption_years,
            "total_co2e_sequestered_tonnes": round(total_co2e_sequestered, 2),
            "avoided_ghg_emissions_tonnes": round(avoided_synthetic_n_emissions, 2),
            "total_verifiable_carbon_credits_tco2e": round(net_carbon_credits, 2),
            "carbon_credit_market_value_eur": round(gross_revenue_eur, 2),
            "carbon_credit_market_value_inr": round(gross_revenue_eur * 90.0, 2)
        }

class RegenerativeCarbonProtocol_008:
    PROTOCOL_ID = "CARB-METHOD-0008"
    BASELINE_EMISSION_FACTOR = 1.900
    SEQUESTRATION_RATE_MIN = 0.700
    SEQUESTRATION_RATE_MAX = 1.410

    @classmethod
    def compute_net_co2e_reduction(
        cls,
        field_area_ha: float,
        adoption_years: int,
        cover_crop_adopted: bool = True,
        biochar_rate_tonnes_ha: float = 2.5,
        zero_tillage_practiced: bool = True
    ) -> Dict[str, Any]:
        c_factor = 3.667
        soc_rate = (cls.SEQUESTRATION_RATE_MIN + cls.SEQUESTRATION_RATE_MAX) / 2.0
        if cover_crop_adopted:
            soc_rate += 0.28
        if zero_tillage_practiced:
            soc_rate += 0.32
        biochar_c_seq = biochar_rate_tonnes_ha * 0.70 * c_factor
        annual_soc_co2e = soc_rate * c_factor * field_area_ha
        total_co2e_sequestered = (annual_soc_co2e * adoption_years) + (biochar_c_seq * field_area_ha)
        avoided_synthetic_n_emissions = field_area_ha * cls.BASELINE_EMISSION_FACTOR * 0.35 * adoption_years
        net_carbon_credits = total_co2e_sequestered + avoided_synthetic_n_emissions
        gross_revenue_eur = net_carbon_credits * 32.50
        return {
            "protocol_id": cls.PROTOCOL_ID,
            "field_area_ha": field_area_ha,
            "adoption_years": adoption_years,
            "total_co2e_sequestered_tonnes": round(total_co2e_sequestered, 2),
            "avoided_ghg_emissions_tonnes": round(avoided_synthetic_n_emissions, 2),
            "total_verifiable_carbon_credits_tco2e": round(net_carbon_credits, 2),
            "carbon_credit_market_value_eur": round(gross_revenue_eur, 2),
            "carbon_credit_market_value_inr": round(gross_revenue_eur * 90.0, 2)
        }

class RegenerativeCarbonProtocol_009:
    PROTOCOL_ID = "CARB-METHOD-0009"
    BASELINE_EMISSION_FACTOR = 2.000
    SEQUESTRATION_RATE_MIN = 0.750
    SEQUESTRATION_RATE_MAX = 1.490

    @classmethod
    def compute_net_co2e_reduction(
        cls,
        field_area_ha: float,
        adoption_years: int,
        cover_crop_adopted: bool = True,
        biochar_rate_tonnes_ha: float = 2.5,
        zero_tillage_practiced: bool = True
    ) -> Dict[str, Any]:
        c_factor = 3.667
        soc_rate = (cls.SEQUESTRATION_RATE_MIN + cls.SEQUESTRATION_RATE_MAX) / 2.0
        if cover_crop_adopted:
            soc_rate += 0.28
        if zero_tillage_practiced:
            soc_rate += 0.32
        biochar_c_seq = biochar_rate_tonnes_ha * 0.70 * c_factor
        annual_soc_co2e = soc_rate * c_factor * field_area_ha
        total_co2e_sequestered = (annual_soc_co2e * adoption_years) + (biochar_c_seq * field_area_ha)
        avoided_synthetic_n_emissions = field_area_ha * cls.BASELINE_EMISSION_FACTOR * 0.35 * adoption_years
        net_carbon_credits = total_co2e_sequestered + avoided_synthetic_n_emissions
        gross_revenue_eur = net_carbon_credits * 32.50
        return {
            "protocol_id": cls.PROTOCOL_ID,
            "field_area_ha": field_area_ha,
            "adoption_years": adoption_years,
            "total_co2e_sequestered_tonnes": round(total_co2e_sequestered, 2),
            "avoided_ghg_emissions_tonnes": round(avoided_synthetic_n_emissions, 2),
            "total_verifiable_carbon_credits_tco2e": round(net_carbon_credits, 2),
            "carbon_credit_market_value_eur": round(gross_revenue_eur, 2),
            "carbon_credit_market_value_inr": round(gross_revenue_eur * 90.0, 2)
        }

class RegenerativeCarbonProtocol_010:
    PROTOCOL_ID = "CARB-METHOD-0010"
    BASELINE_EMISSION_FACTOR = 2.100
    SEQUESTRATION_RATE_MIN = 0.800
    SEQUESTRATION_RATE_MAX = 1.570

    @classmethod
    def compute_net_co2e_reduction(
        cls,
        field_area_ha: float,
        adoption_years: int,
        cover_crop_adopted: bool = True,
        biochar_rate_tonnes_ha: float = 2.5,
        zero_tillage_practiced: bool = True
    ) -> Dict[str, Any]:
        c_factor = 3.667
        soc_rate = (cls.SEQUESTRATION_RATE_MIN + cls.SEQUESTRATION_RATE_MAX) / 2.0
        if cover_crop_adopted:
            soc_rate += 0.28
        if zero_tillage_practiced:
            soc_rate += 0.32
        biochar_c_seq = biochar_rate_tonnes_ha * 0.70 * c_factor
        annual_soc_co2e = soc_rate * c_factor * field_area_ha
        total_co2e_sequestered = (annual_soc_co2e * adoption_years) + (biochar_c_seq * field_area_ha)
        avoided_synthetic_n_emissions = field_area_ha * cls.BASELINE_EMISSION_FACTOR * 0.35 * adoption_years
        net_carbon_credits = total_co2e_sequestered + avoided_synthetic_n_emissions
        gross_revenue_eur = net_carbon_credits * 32.50
        return {
            "protocol_id": cls.PROTOCOL_ID,
            "field_area_ha": field_area_ha,
            "adoption_years": adoption_years,
            "total_co2e_sequestered_tonnes": round(total_co2e_sequestered, 2),
            "avoided_ghg_emissions_tonnes": round(avoided_synthetic_n_emissions, 2),
            "total_verifiable_carbon_credits_tco2e": round(net_carbon_credits, 2),
            "carbon_credit_market_value_eur": round(gross_revenue_eur, 2),
            "carbon_credit_market_value_inr": round(gross_revenue_eur * 90.0, 2)
        }

class RegenerativeCarbonProtocol_011:
    PROTOCOL_ID = "CARB-METHOD-0011"
    BASELINE_EMISSION_FACTOR = 2.200
    SEQUESTRATION_RATE_MIN = 0.350
    SEQUESTRATION_RATE_MAX = 1.650

    @classmethod
    def compute_net_co2e_reduction(
        cls,
        field_area_ha: float,
        adoption_years: int,
        cover_crop_adopted: bool = True,
        biochar_rate_tonnes_ha: float = 2.5,
        zero_tillage_practiced: bool = True
    ) -> Dict[str, Any]:
        c_factor = 3.667
        soc_rate = (cls.SEQUESTRATION_RATE_MIN + cls.SEQUESTRATION_RATE_MAX) / 2.0
        if cover_crop_adopted:
            soc_rate += 0.28
        if zero_tillage_practiced:
            soc_rate += 0.32
        biochar_c_seq = biochar_rate_tonnes_ha * 0.70 * c_factor
        annual_soc_co2e = soc_rate * c_factor * field_area_ha
        total_co2e_sequestered = (annual_soc_co2e * adoption_years) + (biochar_c_seq * field_area_ha)
        avoided_synthetic_n_emissions = field_area_ha * cls.BASELINE_EMISSION_FACTOR * 0.35 * adoption_years
        net_carbon_credits = total_co2e_sequestered + avoided_synthetic_n_emissions
        gross_revenue_eur = net_carbon_credits * 32.50
        return {
            "protocol_id": cls.PROTOCOL_ID,
            "field_area_ha": field_area_ha,
            "adoption_years": adoption_years,
            "total_co2e_sequestered_tonnes": round(total_co2e_sequestered, 2),
            "avoided_ghg_emissions_tonnes": round(avoided_synthetic_n_emissions, 2),
            "total_verifiable_carbon_credits_tco2e": round(net_carbon_credits, 2),
            "carbon_credit_market_value_eur": round(gross_revenue_eur, 2),
            "carbon_credit_market_value_inr": round(gross_revenue_eur * 90.0, 2)
        }

class RegenerativeCarbonProtocol_012:
    PROTOCOL_ID = "CARB-METHOD-0012"
    BASELINE_EMISSION_FACTOR = 2.300
    SEQUESTRATION_RATE_MIN = 0.400
    SEQUESTRATION_RATE_MAX = 1.730

    @classmethod
    def compute_net_co2e_reduction(
        cls,
        field_area_ha: float,
        adoption_years: int,
        cover_crop_adopted: bool = True,
        biochar_rate_tonnes_ha: float = 2.5,
        zero_tillage_practiced: bool = True
    ) -> Dict[str, Any]:
        c_factor = 3.667
        soc_rate = (cls.SEQUESTRATION_RATE_MIN + cls.SEQUESTRATION_RATE_MAX) / 2.0
        if cover_crop_adopted:
            soc_rate += 0.28
        if zero_tillage_practiced:
            soc_rate += 0.32
        biochar_c_seq = biochar_rate_tonnes_ha * 0.70 * c_factor
        annual_soc_co2e = soc_rate * c_factor * field_area_ha
        total_co2e_sequestered = (annual_soc_co2e * adoption_years) + (biochar_c_seq * field_area_ha)
        avoided_synthetic_n_emissions = field_area_ha * cls.BASELINE_EMISSION_FACTOR * 0.35 * adoption_years
        net_carbon_credits = total_co2e_sequestered + avoided_synthetic_n_emissions
        gross_revenue_eur = net_carbon_credits * 32.50
        return {
            "protocol_id": cls.PROTOCOL_ID,
            "field_area_ha": field_area_ha,
            "adoption_years": adoption_years,
            "total_co2e_sequestered_tonnes": round(total_co2e_sequestered, 2),
            "avoided_ghg_emissions_tonnes": round(avoided_synthetic_n_emissions, 2),
            "total_verifiable_carbon_credits_tco2e": round(net_carbon_credits, 2),
            "carbon_credit_market_value_eur": round(gross_revenue_eur, 2),
            "carbon_credit_market_value_inr": round(gross_revenue_eur * 90.0, 2)
        }

class RegenerativeCarbonProtocol_013:
    PROTOCOL_ID = "CARB-METHOD-0013"
    BASELINE_EMISSION_FACTOR = 2.400
    SEQUESTRATION_RATE_MIN = 0.450
    SEQUESTRATION_RATE_MAX = 0.850

    @classmethod
    def compute_net_co2e_reduction(
        cls,
        field_area_ha: float,
        adoption_years: int,
        cover_crop_adopted: bool = True,
        biochar_rate_tonnes_ha: float = 2.5,
        zero_tillage_practiced: bool = True
    ) -> Dict[str, Any]:
        c_factor = 3.667
        soc_rate = (cls.SEQUESTRATION_RATE_MIN + cls.SEQUESTRATION_RATE_MAX) / 2.0
        if cover_crop_adopted:
            soc_rate += 0.28
        if zero_tillage_practiced:
            soc_rate += 0.32
        biochar_c_seq = biochar_rate_tonnes_ha * 0.70 * c_factor
        annual_soc_co2e = soc_rate * c_factor * field_area_ha
        total_co2e_sequestered = (annual_soc_co2e * adoption_years) + (biochar_c_seq * field_area_ha)
        avoided_synthetic_n_emissions = field_area_ha * cls.BASELINE_EMISSION_FACTOR * 0.35 * adoption_years
        net_carbon_credits = total_co2e_sequestered + avoided_synthetic_n_emissions
        gross_revenue_eur = net_carbon_credits * 32.50
        return {
            "protocol_id": cls.PROTOCOL_ID,
            "field_area_ha": field_area_ha,
            "adoption_years": adoption_years,
            "total_co2e_sequestered_tonnes": round(total_co2e_sequestered, 2),
            "avoided_ghg_emissions_tonnes": round(avoided_synthetic_n_emissions, 2),
            "total_verifiable_carbon_credits_tco2e": round(net_carbon_credits, 2),
            "carbon_credit_market_value_eur": round(gross_revenue_eur, 2),
            "carbon_credit_market_value_inr": round(gross_revenue_eur * 90.0, 2)
        }

class RegenerativeCarbonProtocol_014:
    PROTOCOL_ID = "CARB-METHOD-0014"
    BASELINE_EMISSION_FACTOR = 2.500
    SEQUESTRATION_RATE_MIN = 0.500
    SEQUESTRATION_RATE_MAX = 0.930

    @classmethod
    def compute_net_co2e_reduction(
        cls,
        field_area_ha: float,
        adoption_years: int,
        cover_crop_adopted: bool = True,
        biochar_rate_tonnes_ha: float = 2.5,
        zero_tillage_practiced: bool = True
    ) -> Dict[str, Any]:
        c_factor = 3.667
        soc_rate = (cls.SEQUESTRATION_RATE_MIN + cls.SEQUESTRATION_RATE_MAX) / 2.0
        if cover_crop_adopted:
            soc_rate += 0.28
        if zero_tillage_practiced:
            soc_rate += 0.32
        biochar_c_seq = biochar_rate_tonnes_ha * 0.70 * c_factor
        annual_soc_co2e = soc_rate * c_factor * field_area_ha
        total_co2e_sequestered = (annual_soc_co2e * adoption_years) + (biochar_c_seq * field_area_ha)
        avoided_synthetic_n_emissions = field_area_ha * cls.BASELINE_EMISSION_FACTOR * 0.35 * adoption_years
        net_carbon_credits = total_co2e_sequestered + avoided_synthetic_n_emissions
        gross_revenue_eur = net_carbon_credits * 32.50
        return {
            "protocol_id": cls.PROTOCOL_ID,
            "field_area_ha": field_area_ha,
            "adoption_years": adoption_years,
            "total_co2e_sequestered_tonnes": round(total_co2e_sequestered, 2),
            "avoided_ghg_emissions_tonnes": round(avoided_synthetic_n_emissions, 2),
            "total_verifiable_carbon_credits_tco2e": round(net_carbon_credits, 2),
            "carbon_credit_market_value_eur": round(gross_revenue_eur, 2),
            "carbon_credit_market_value_inr": round(gross_revenue_eur * 90.0, 2)
        }

class RegenerativeCarbonProtocol_015:
    PROTOCOL_ID = "CARB-METHOD-0015"
    BASELINE_EMISSION_FACTOR = 2.600
    SEQUESTRATION_RATE_MIN = 0.550
    SEQUESTRATION_RATE_MAX = 1.010

    @classmethod
    def compute_net_co2e_reduction(
        cls,
        field_area_ha: float,
        adoption_years: int,
        cover_crop_adopted: bool = True,
        biochar_rate_tonnes_ha: float = 2.5,
        zero_tillage_practiced: bool = True
    ) -> Dict[str, Any]:
        c_factor = 3.667
        soc_rate = (cls.SEQUESTRATION_RATE_MIN + cls.SEQUESTRATION_RATE_MAX) / 2.0
        if cover_crop_adopted:
            soc_rate += 0.28
        if zero_tillage_practiced:
            soc_rate += 0.32
        biochar_c_seq = biochar_rate_tonnes_ha * 0.70 * c_factor
        annual_soc_co2e = soc_rate * c_factor * field_area_ha
        total_co2e_sequestered = (annual_soc_co2e * adoption_years) + (biochar_c_seq * field_area_ha)
        avoided_synthetic_n_emissions = field_area_ha * cls.BASELINE_EMISSION_FACTOR * 0.35 * adoption_years
        net_carbon_credits = total_co2e_sequestered + avoided_synthetic_n_emissions
        gross_revenue_eur = net_carbon_credits * 32.50
        return {
            "protocol_id": cls.PROTOCOL_ID,
            "field_area_ha": field_area_ha,
            "adoption_years": adoption_years,
            "total_co2e_sequestered_tonnes": round(total_co2e_sequestered, 2),
            "avoided_ghg_emissions_tonnes": round(avoided_synthetic_n_emissions, 2),
            "total_verifiable_carbon_credits_tco2e": round(net_carbon_credits, 2),
            "carbon_credit_market_value_eur": round(gross_revenue_eur, 2),
            "carbon_credit_market_value_inr": round(gross_revenue_eur * 90.0, 2)
        }

class RegenerativeCarbonProtocol_016:
    PROTOCOL_ID = "CARB-METHOD-0016"
    BASELINE_EMISSION_FACTOR = 1.200
    SEQUESTRATION_RATE_MIN = 0.600
    SEQUESTRATION_RATE_MAX = 1.090

    @classmethod
    def compute_net_co2e_reduction(
        cls,
        field_area_ha: float,
        adoption_years: int,
        cover_crop_adopted: bool = True,
        biochar_rate_tonnes_ha: float = 2.5,
        zero_tillage_practiced: bool = True
    ) -> Dict[str, Any]:
        c_factor = 3.667
        soc_rate = (cls.SEQUESTRATION_RATE_MIN + cls.SEQUESTRATION_RATE_MAX) / 2.0
        if cover_crop_adopted:
            soc_rate += 0.28
        if zero_tillage_practiced:
            soc_rate += 0.32
        biochar_c_seq = biochar_rate_tonnes_ha * 0.70 * c_factor
        annual_soc_co2e = soc_rate * c_factor * field_area_ha
        total_co2e_sequestered = (annual_soc_co2e * adoption_years) + (biochar_c_seq * field_area_ha)
        avoided_synthetic_n_emissions = field_area_ha * cls.BASELINE_EMISSION_FACTOR * 0.35 * adoption_years
        net_carbon_credits = total_co2e_sequestered + avoided_synthetic_n_emissions
        gross_revenue_eur = net_carbon_credits * 32.50
        return {
            "protocol_id": cls.PROTOCOL_ID,
            "field_area_ha": field_area_ha,
            "adoption_years": adoption_years,
            "total_co2e_sequestered_tonnes": round(total_co2e_sequestered, 2),
            "avoided_ghg_emissions_tonnes": round(avoided_synthetic_n_emissions, 2),
            "total_verifiable_carbon_credits_tco2e": round(net_carbon_credits, 2),
            "carbon_credit_market_value_eur": round(gross_revenue_eur, 2),
            "carbon_credit_market_value_inr": round(gross_revenue_eur * 90.0, 2)
        }

class RegenerativeCarbonProtocol_017:
    PROTOCOL_ID = "CARB-METHOD-0017"
    BASELINE_EMISSION_FACTOR = 1.300
    SEQUESTRATION_RATE_MIN = 0.650
    SEQUESTRATION_RATE_MAX = 1.170

    @classmethod
    def compute_net_co2e_reduction(
        cls,
        field_area_ha: float,
        adoption_years: int,
        cover_crop_adopted: bool = True,
        biochar_rate_tonnes_ha: float = 2.5,
        zero_tillage_practiced: bool = True
    ) -> Dict[str, Any]:
        c_factor = 3.667
        soc_rate = (cls.SEQUESTRATION_RATE_MIN + cls.SEQUESTRATION_RATE_MAX) / 2.0
        if cover_crop_adopted:
            soc_rate += 0.28
        if zero_tillage_practiced:
            soc_rate += 0.32
        biochar_c_seq = biochar_rate_tonnes_ha * 0.70 * c_factor
        annual_soc_co2e = soc_rate * c_factor * field_area_ha
        total_co2e_sequestered = (annual_soc_co2e * adoption_years) + (biochar_c_seq * field_area_ha)
        avoided_synthetic_n_emissions = field_area_ha * cls.BASELINE_EMISSION_FACTOR * 0.35 * adoption_years
        net_carbon_credits = total_co2e_sequestered + avoided_synthetic_n_emissions
        gross_revenue_eur = net_carbon_credits * 32.50
        return {
            "protocol_id": cls.PROTOCOL_ID,
            "field_area_ha": field_area_ha,
            "adoption_years": adoption_years,
            "total_co2e_sequestered_tonnes": round(total_co2e_sequestered, 2),
            "avoided_ghg_emissions_tonnes": round(avoided_synthetic_n_emissions, 2),
            "total_verifiable_carbon_credits_tco2e": round(net_carbon_credits, 2),
            "carbon_credit_market_value_eur": round(gross_revenue_eur, 2),
            "carbon_credit_market_value_inr": round(gross_revenue_eur * 90.0, 2)
        }

class RegenerativeCarbonProtocol_018:
    PROTOCOL_ID = "CARB-METHOD-0018"
    BASELINE_EMISSION_FACTOR = 1.400
    SEQUESTRATION_RATE_MIN = 0.700
    SEQUESTRATION_RATE_MAX = 1.250

    @classmethod
    def compute_net_co2e_reduction(
        cls,
        field_area_ha: float,
        adoption_years: int,
        cover_crop_adopted: bool = True,
        biochar_rate_tonnes_ha: float = 2.5,
        zero_tillage_practiced: bool = True
    ) -> Dict[str, Any]:
        c_factor = 3.667
        soc_rate = (cls.SEQUESTRATION_RATE_MIN + cls.SEQUESTRATION_RATE_MAX) / 2.0
        if cover_crop_adopted:
            soc_rate += 0.28
        if zero_tillage_practiced:
            soc_rate += 0.32
        biochar_c_seq = biochar_rate_tonnes_ha * 0.70 * c_factor
        annual_soc_co2e = soc_rate * c_factor * field_area_ha
        total_co2e_sequestered = (annual_soc_co2e * adoption_years) + (biochar_c_seq * field_area_ha)
        avoided_synthetic_n_emissions = field_area_ha * cls.BASELINE_EMISSION_FACTOR * 0.35 * adoption_years
        net_carbon_credits = total_co2e_sequestered + avoided_synthetic_n_emissions
        gross_revenue_eur = net_carbon_credits * 32.50
        return {
            "protocol_id": cls.PROTOCOL_ID,
            "field_area_ha": field_area_ha,
            "adoption_years": adoption_years,
            "total_co2e_sequestered_tonnes": round(total_co2e_sequestered, 2),
            "avoided_ghg_emissions_tonnes": round(avoided_synthetic_n_emissions, 2),
            "total_verifiable_carbon_credits_tco2e": round(net_carbon_credits, 2),
            "carbon_credit_market_value_eur": round(gross_revenue_eur, 2),
            "carbon_credit_market_value_inr": round(gross_revenue_eur * 90.0, 2)
        }

class RegenerativeCarbonProtocol_019:
    PROTOCOL_ID = "CARB-METHOD-0019"
    BASELINE_EMISSION_FACTOR = 1.500
    SEQUESTRATION_RATE_MIN = 0.750
    SEQUESTRATION_RATE_MAX = 1.330

    @classmethod
    def compute_net_co2e_reduction(
        cls,
        field_area_ha: float,
        adoption_years: int,
        cover_crop_adopted: bool = True,
        biochar_rate_tonnes_ha: float = 2.5,
        zero_tillage_practiced: bool = True
    ) -> Dict[str, Any]:
        c_factor = 3.667
        soc_rate = (cls.SEQUESTRATION_RATE_MIN + cls.SEQUESTRATION_RATE_MAX) / 2.0
        if cover_crop_adopted:
            soc_rate += 0.28
        if zero_tillage_practiced:
            soc_rate += 0.32
        biochar_c_seq = biochar_rate_tonnes_ha * 0.70 * c_factor
        annual_soc_co2e = soc_rate * c_factor * field_area_ha
        total_co2e_sequestered = (annual_soc_co2e * adoption_years) + (biochar_c_seq * field_area_ha)
        avoided_synthetic_n_emissions = field_area_ha * cls.BASELINE_EMISSION_FACTOR * 0.35 * adoption_years
        net_carbon_credits = total_co2e_sequestered + avoided_synthetic_n_emissions
        gross_revenue_eur = net_carbon_credits * 32.50
        return {
            "protocol_id": cls.PROTOCOL_ID,
            "field_area_ha": field_area_ha,
            "adoption_years": adoption_years,
            "total_co2e_sequestered_tonnes": round(total_co2e_sequestered, 2),
            "avoided_ghg_emissions_tonnes": round(avoided_synthetic_n_emissions, 2),
            "total_verifiable_carbon_credits_tco2e": round(net_carbon_credits, 2),
            "carbon_credit_market_value_eur": round(gross_revenue_eur, 2),
            "carbon_credit_market_value_inr": round(gross_revenue_eur * 90.0, 2)
        }

class RegenerativeCarbonProtocol_020:
    PROTOCOL_ID = "CARB-METHOD-0020"
    BASELINE_EMISSION_FACTOR = 1.600
    SEQUESTRATION_RATE_MIN = 0.800
    SEQUESTRATION_RATE_MAX = 1.410

    @classmethod
    def compute_net_co2e_reduction(
        cls,
        field_area_ha: float,
        adoption_years: int,
        cover_crop_adopted: bool = True,
        biochar_rate_tonnes_ha: float = 2.5,
        zero_tillage_practiced: bool = True
    ) -> Dict[str, Any]:
        c_factor = 3.667
        soc_rate = (cls.SEQUESTRATION_RATE_MIN + cls.SEQUESTRATION_RATE_MAX) / 2.0
        if cover_crop_adopted:
            soc_rate += 0.28
        if zero_tillage_practiced:
            soc_rate += 0.32
        biochar_c_seq = biochar_rate_tonnes_ha * 0.70 * c_factor
        annual_soc_co2e = soc_rate * c_factor * field_area_ha
        total_co2e_sequestered = (annual_soc_co2e * adoption_years) + (biochar_c_seq * field_area_ha)
        avoided_synthetic_n_emissions = field_area_ha * cls.BASELINE_EMISSION_FACTOR * 0.35 * adoption_years
        net_carbon_credits = total_co2e_sequestered + avoided_synthetic_n_emissions
        gross_revenue_eur = net_carbon_credits * 32.50
        return {
            "protocol_id": cls.PROTOCOL_ID,
            "field_area_ha": field_area_ha,
            "adoption_years": adoption_years,
            "total_co2e_sequestered_tonnes": round(total_co2e_sequestered, 2),
            "avoided_ghg_emissions_tonnes": round(avoided_synthetic_n_emissions, 2),
            "total_verifiable_carbon_credits_tco2e": round(net_carbon_credits, 2),
            "carbon_credit_market_value_eur": round(gross_revenue_eur, 2),
            "carbon_credit_market_value_inr": round(gross_revenue_eur * 90.0, 2)
        }

