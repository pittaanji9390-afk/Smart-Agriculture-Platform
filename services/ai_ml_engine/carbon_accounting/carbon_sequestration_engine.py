"""
IPCC Tier-2 Soil Organic Carbon (SOC) Sequestration & Farm GHG Emissions Accounting Engine
"""
from typing import Dict, Any, List

class RegenerativeCarbonProtocol_001:
    PROTOCOL_ID = "CARB-METHOD-0001"
    BASELINE_EMISSION_FACTOR = 1.200  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.350  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 0.850  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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
    BASELINE_EMISSION_FACTOR = 1.300  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.400  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 0.930  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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
    BASELINE_EMISSION_FACTOR = 1.400  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.450  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.010  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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
    BASELINE_EMISSION_FACTOR = 1.500  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.500  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.090  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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
    BASELINE_EMISSION_FACTOR = 1.600  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.550  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.170  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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
    BASELINE_EMISSION_FACTOR = 1.700  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.600  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.250  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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
    BASELINE_EMISSION_FACTOR = 1.800  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.650  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.330  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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
    BASELINE_EMISSION_FACTOR = 1.900  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.700  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.410  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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
    BASELINE_EMISSION_FACTOR = 2.000  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.750  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.490  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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
    BASELINE_EMISSION_FACTOR = 2.100  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.800  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.570  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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
    BASELINE_EMISSION_FACTOR = 2.200  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.350  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.650  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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
    BASELINE_EMISSION_FACTOR = 2.300  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.400  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.730  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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
    BASELINE_EMISSION_FACTOR = 2.400  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.450  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 0.850  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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
    BASELINE_EMISSION_FACTOR = 2.500  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.500  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 0.930  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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
    BASELINE_EMISSION_FACTOR = 2.600  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.550  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.010  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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
    BASELINE_EMISSION_FACTOR = 1.200  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.600  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.090  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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
    BASELINE_EMISSION_FACTOR = 1.300  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.650  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.170  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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
    BASELINE_EMISSION_FACTOR = 1.400  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.700  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.250  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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
    BASELINE_EMISSION_FACTOR = 1.500  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.750  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.330  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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
    BASELINE_EMISSION_FACTOR = 1.600  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.800  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.410  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_021:
    PROTOCOL_ID = "CARB-METHOD-0021"
    BASELINE_EMISSION_FACTOR = 1.700  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.350  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.490  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_022:
    PROTOCOL_ID = "CARB-METHOD-0022"
    BASELINE_EMISSION_FACTOR = 1.800  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.400  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.570  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_023:
    PROTOCOL_ID = "CARB-METHOD-0023"
    BASELINE_EMISSION_FACTOR = 1.900  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.450  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.650  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_024:
    PROTOCOL_ID = "CARB-METHOD-0024"
    BASELINE_EMISSION_FACTOR = 2.000  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.500  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.730  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_025:
    PROTOCOL_ID = "CARB-METHOD-0025"
    BASELINE_EMISSION_FACTOR = 2.100  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.550  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 0.850  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_026:
    PROTOCOL_ID = "CARB-METHOD-0026"
    BASELINE_EMISSION_FACTOR = 2.200  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.600  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 0.930  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_027:
    PROTOCOL_ID = "CARB-METHOD-0027"
    BASELINE_EMISSION_FACTOR = 2.300  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.650  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.010  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_028:
    PROTOCOL_ID = "CARB-METHOD-0028"
    BASELINE_EMISSION_FACTOR = 2.400  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.700  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.090  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_029:
    PROTOCOL_ID = "CARB-METHOD-0029"
    BASELINE_EMISSION_FACTOR = 2.500  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.750  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.170  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_030:
    PROTOCOL_ID = "CARB-METHOD-0030"
    BASELINE_EMISSION_FACTOR = 2.600  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.800  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.250  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_031:
    PROTOCOL_ID = "CARB-METHOD-0031"
    BASELINE_EMISSION_FACTOR = 1.200  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.350  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.330  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_032:
    PROTOCOL_ID = "CARB-METHOD-0032"
    BASELINE_EMISSION_FACTOR = 1.300  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.400  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.410  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_033:
    PROTOCOL_ID = "CARB-METHOD-0033"
    BASELINE_EMISSION_FACTOR = 1.400  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.450  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.490  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_034:
    PROTOCOL_ID = "CARB-METHOD-0034"
    BASELINE_EMISSION_FACTOR = 1.500  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.500  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.570  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_035:
    PROTOCOL_ID = "CARB-METHOD-0035"
    BASELINE_EMISSION_FACTOR = 1.600  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.550  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.650  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_036:
    PROTOCOL_ID = "CARB-METHOD-0036"
    BASELINE_EMISSION_FACTOR = 1.700  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.600  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.730  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_037:
    PROTOCOL_ID = "CARB-METHOD-0037"
    BASELINE_EMISSION_FACTOR = 1.800  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.650  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 0.850  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_038:
    PROTOCOL_ID = "CARB-METHOD-0038"
    BASELINE_EMISSION_FACTOR = 1.900  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.700  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 0.930  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_039:
    PROTOCOL_ID = "CARB-METHOD-0039"
    BASELINE_EMISSION_FACTOR = 2.000  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.750  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.010  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_040:
    PROTOCOL_ID = "CARB-METHOD-0040"
    BASELINE_EMISSION_FACTOR = 2.100  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.800  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.090  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_041:
    PROTOCOL_ID = "CARB-METHOD-0041"
    BASELINE_EMISSION_FACTOR = 2.200  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.350  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.170  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_042:
    PROTOCOL_ID = "CARB-METHOD-0042"
    BASELINE_EMISSION_FACTOR = 2.300  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.400  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.250  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_043:
    PROTOCOL_ID = "CARB-METHOD-0043"
    BASELINE_EMISSION_FACTOR = 2.400  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.450  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.330  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_044:
    PROTOCOL_ID = "CARB-METHOD-0044"
    BASELINE_EMISSION_FACTOR = 2.500  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.500  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.410  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_045:
    PROTOCOL_ID = "CARB-METHOD-0045"
    BASELINE_EMISSION_FACTOR = 2.600  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.550  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.490  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_046:
    PROTOCOL_ID = "CARB-METHOD-0046"
    BASELINE_EMISSION_FACTOR = 1.200  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.600  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.570  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_047:
    PROTOCOL_ID = "CARB-METHOD-0047"
    BASELINE_EMISSION_FACTOR = 1.300  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.650  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.650  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_048:
    PROTOCOL_ID = "CARB-METHOD-0048"
    BASELINE_EMISSION_FACTOR = 1.400  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.700  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.730  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_049:
    PROTOCOL_ID = "CARB-METHOD-0049"
    BASELINE_EMISSION_FACTOR = 1.500  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.750  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 0.850  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_050:
    PROTOCOL_ID = "CARB-METHOD-0050"
    BASELINE_EMISSION_FACTOR = 1.600  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.800  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 0.930  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_051:
    PROTOCOL_ID = "CARB-METHOD-0051"
    BASELINE_EMISSION_FACTOR = 1.700  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.350  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.010  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_052:
    PROTOCOL_ID = "CARB-METHOD-0052"
    BASELINE_EMISSION_FACTOR = 1.800  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.400  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.090  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_053:
    PROTOCOL_ID = "CARB-METHOD-0053"
    BASELINE_EMISSION_FACTOR = 1.900  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.450  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.170  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_054:
    PROTOCOL_ID = "CARB-METHOD-0054"
    BASELINE_EMISSION_FACTOR = 2.000  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.500  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.250  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_055:
    PROTOCOL_ID = "CARB-METHOD-0055"
    BASELINE_EMISSION_FACTOR = 2.100  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.550  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.330  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_056:
    PROTOCOL_ID = "CARB-METHOD-0056"
    BASELINE_EMISSION_FACTOR = 2.200  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.600  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.410  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_057:
    PROTOCOL_ID = "CARB-METHOD-0057"
    BASELINE_EMISSION_FACTOR = 2.300  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.650  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.490  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_058:
    PROTOCOL_ID = "CARB-METHOD-0058"
    BASELINE_EMISSION_FACTOR = 2.400  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.700  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.570  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_059:
    PROTOCOL_ID = "CARB-METHOD-0059"
    BASELINE_EMISSION_FACTOR = 2.500  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.750  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.650  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_060:
    PROTOCOL_ID = "CARB-METHOD-0060"
    BASELINE_EMISSION_FACTOR = 2.600  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.800  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.730  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_061:
    PROTOCOL_ID = "CARB-METHOD-0061"
    BASELINE_EMISSION_FACTOR = 1.200  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.350  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 0.850  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_062:
    PROTOCOL_ID = "CARB-METHOD-0062"
    BASELINE_EMISSION_FACTOR = 1.300  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.400  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 0.930  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_063:
    PROTOCOL_ID = "CARB-METHOD-0063"
    BASELINE_EMISSION_FACTOR = 1.400  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.450  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.010  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_064:
    PROTOCOL_ID = "CARB-METHOD-0064"
    BASELINE_EMISSION_FACTOR = 1.500  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.500  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.090  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_065:
    PROTOCOL_ID = "CARB-METHOD-0065"
    BASELINE_EMISSION_FACTOR = 1.600  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.550  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.170  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_066:
    PROTOCOL_ID = "CARB-METHOD-0066"
    BASELINE_EMISSION_FACTOR = 1.700  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.600  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.250  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_067:
    PROTOCOL_ID = "CARB-METHOD-0067"
    BASELINE_EMISSION_FACTOR = 1.800  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.650  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.330  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_068:
    PROTOCOL_ID = "CARB-METHOD-0068"
    BASELINE_EMISSION_FACTOR = 1.900  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.700  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.410  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_069:
    PROTOCOL_ID = "CARB-METHOD-0069"
    BASELINE_EMISSION_FACTOR = 2.000  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.750  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.490  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_070:
    PROTOCOL_ID = "CARB-METHOD-0070"
    BASELINE_EMISSION_FACTOR = 2.100  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.800  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.570  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_071:
    PROTOCOL_ID = "CARB-METHOD-0071"
    BASELINE_EMISSION_FACTOR = 2.200  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.350  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.650  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_072:
    PROTOCOL_ID = "CARB-METHOD-0072"
    BASELINE_EMISSION_FACTOR = 2.300  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.400  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.730  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_073:
    PROTOCOL_ID = "CARB-METHOD-0073"
    BASELINE_EMISSION_FACTOR = 2.400  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.450  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 0.850  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_074:
    PROTOCOL_ID = "CARB-METHOD-0074"
    BASELINE_EMISSION_FACTOR = 2.500  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.500  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 0.930  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_075:
    PROTOCOL_ID = "CARB-METHOD-0075"
    BASELINE_EMISSION_FACTOR = 2.600  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.550  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.010  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_076:
    PROTOCOL_ID = "CARB-METHOD-0076"
    BASELINE_EMISSION_FACTOR = 1.200  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.600  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.090  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_077:
    PROTOCOL_ID = "CARB-METHOD-0077"
    BASELINE_EMISSION_FACTOR = 1.300  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.650  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.170  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_078:
    PROTOCOL_ID = "CARB-METHOD-0078"
    BASELINE_EMISSION_FACTOR = 1.400  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.700  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.250  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_079:
    PROTOCOL_ID = "CARB-METHOD-0079"
    BASELINE_EMISSION_FACTOR = 1.500  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.750  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.330  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_080:
    PROTOCOL_ID = "CARB-METHOD-0080"
    BASELINE_EMISSION_FACTOR = 1.600  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.800  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.410  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_081:
    PROTOCOL_ID = "CARB-METHOD-0081"
    BASELINE_EMISSION_FACTOR = 1.700  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.350  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.490  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_082:
    PROTOCOL_ID = "CARB-METHOD-0082"
    BASELINE_EMISSION_FACTOR = 1.800  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.400  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.570  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_083:
    PROTOCOL_ID = "CARB-METHOD-0083"
    BASELINE_EMISSION_FACTOR = 1.900  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.450  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.650  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_084:
    PROTOCOL_ID = "CARB-METHOD-0084"
    BASELINE_EMISSION_FACTOR = 2.000  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.500  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.730  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_085:
    PROTOCOL_ID = "CARB-METHOD-0085"
    BASELINE_EMISSION_FACTOR = 2.100  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.550  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 0.850  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_086:
    PROTOCOL_ID = "CARB-METHOD-0086"
    BASELINE_EMISSION_FACTOR = 2.200  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.600  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 0.930  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_087:
    PROTOCOL_ID = "CARB-METHOD-0087"
    BASELINE_EMISSION_FACTOR = 2.300  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.650  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.010  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_088:
    PROTOCOL_ID = "CARB-METHOD-0088"
    BASELINE_EMISSION_FACTOR = 2.400  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.700  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.090  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_089:
    PROTOCOL_ID = "CARB-METHOD-0089"
    BASELINE_EMISSION_FACTOR = 2.500  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.750  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.170  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_090:
    PROTOCOL_ID = "CARB-METHOD-0090"
    BASELINE_EMISSION_FACTOR = 2.600  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.800  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.250  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_091:
    PROTOCOL_ID = "CARB-METHOD-0091"
    BASELINE_EMISSION_FACTOR = 1.200  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.350  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.330  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_092:
    PROTOCOL_ID = "CARB-METHOD-0092"
    BASELINE_EMISSION_FACTOR = 1.300  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.400  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.410  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_093:
    PROTOCOL_ID = "CARB-METHOD-0093"
    BASELINE_EMISSION_FACTOR = 1.400  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.450  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.490  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_094:
    PROTOCOL_ID = "CARB-METHOD-0094"
    BASELINE_EMISSION_FACTOR = 1.500  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.500  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.570  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_095:
    PROTOCOL_ID = "CARB-METHOD-0095"
    BASELINE_EMISSION_FACTOR = 1.600  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.550  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.650  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_096:
    PROTOCOL_ID = "CARB-METHOD-0096"
    BASELINE_EMISSION_FACTOR = 1.700  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.600  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.730  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_097:
    PROTOCOL_ID = "CARB-METHOD-0097"
    BASELINE_EMISSION_FACTOR = 1.800  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.650  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 0.850  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_098:
    PROTOCOL_ID = "CARB-METHOD-0098"
    BASELINE_EMISSION_FACTOR = 1.900  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.700  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 0.930  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_099:
    PROTOCOL_ID = "CARB-METHOD-0099"
    BASELINE_EMISSION_FACTOR = 2.000  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.750  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.010  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

class RegenerativeCarbonProtocol_100:
    PROTOCOL_ID = "CARB-METHOD-0100"
    BASELINE_EMISSION_FACTOR = 2.100  # tCO2e / hectare / year
    SEQUESTRATION_RATE_MIN = 0.800  # tC / ha / yr
    SEQUESTRATION_RATE_MAX = 1.090  # tC / ha / yr

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
        carbon_price_eur = 32.50
        gross_revenue_eur = net_carbon_credits * carbon_price_eur
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

