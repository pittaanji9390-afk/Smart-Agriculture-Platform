"""
Farm Machinery ISOBUS / CAN-Bus Telematics & Fleet Dispatch Intelligence Engine
"""
from typing import Dict, Any, List

class MachineryTelematicsController_001:
    EQUIPMENT_ID = "UNIT-TRACTOR-0001"
    MODEL_NAME = "Mahindra 575 DI Sarpanch Fleet #1"
    HORSEPOWER_RATING = 47
    RATED_ENGINE_RPM = 1900
    BASE_FUEL_LITERS_PER_HOUR = 4.20

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_002:
    EQUIPMENT_ID = "UNIT-TRACTOR-0002"
    MODEL_NAME = "John Deere 5310 4WD PowerTech Fleet #1"
    HORSEPOWER_RATING = 55
    RATED_ENGINE_RPM = 2100
    BASE_FUEL_LITERS_PER_HOUR = 5.10

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_003:
    EQUIPMENT_ID = "UNIT-TRACTOR-0003"
    MODEL_NAME = "Swaraj 855 FE 5-Star Fleet #1"
    HORSEPOWER_RATING = 52
    RATED_ENGINE_RPM = 2000
    BASE_FUEL_LITERS_PER_HOUR = 4.80

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_004:
    EQUIPMENT_ID = "UNIT-TRACTOR-0004"
    MODEL_NAME = "Sonalika DI 745 III Sikander Fleet #1"
    HORSEPOWER_RATING = 50
    RATED_ENGINE_RPM = 1900
    BASE_FUEL_LITERS_PER_HOUR = 4.50

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_005:
    EQUIPMENT_ID = "UNIT-TRACTOR-0005"
    MODEL_NAME = "Kubota MU4501 4WD Japanese Fleet #1"
    HORSEPOWER_RATING = 45
    RATED_ENGINE_RPM = 2500
    BASE_FUEL_LITERS_PER_HOUR = 3.80

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_006:
    EQUIPMENT_ID = "UNIT-TRACTOR-0006"
    MODEL_NAME = "Massey Ferguson 241 DI Dynatrack Fleet #1"
    HORSEPOWER_RATING = 42
    RATED_ENGINE_RPM = 1800
    BASE_FUEL_LITERS_PER_HOUR = 3.90

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_007:
    EQUIPMENT_ID = "UNIT-TRACTOR-0007"
    MODEL_NAME = "New Holland 3630 TX Super Plus Fleet #1"
    HORSEPOWER_RATING = 55
    RATED_ENGINE_RPM = 2200
    BASE_FUEL_LITERS_PER_HOUR = 5.20

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_008:
    EQUIPMENT_ID = "UNIT-TRACTOR-0008"
    MODEL_NAME = "Farmtrac 60 Powermaxx Fleet #1"
    HORSEPOWER_RATING = 50
    RATED_ENGINE_RPM = 2000
    BASE_FUEL_LITERS_PER_HOUR = 4.60

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_009:
    EQUIPMENT_ID = "UNIT-TRACTOR-0009"
    MODEL_NAME = "Eicher 380 Super DI Fleet #1"
    HORSEPOWER_RATING = 40
    RATED_ENGINE_RPM = 1800
    BASE_FUEL_LITERS_PER_HOUR = 3.50

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_010:
    EQUIPMENT_ID = "UNIT-TRACTOR-0010"
    MODEL_NAME = "Powertrac Euro 50 Next Fleet #1"
    HORSEPOWER_RATING = 52
    RATED_ENGINE_RPM = 2200
    BASE_FUEL_LITERS_PER_HOUR = 4.70

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_011:
    EQUIPMENT_ID = "UNIT-TRACTOR-0011"
    MODEL_NAME = "Mahindra 575 DI Sarpanch Fleet #2"
    HORSEPOWER_RATING = 47
    RATED_ENGINE_RPM = 1900
    BASE_FUEL_LITERS_PER_HOUR = 4.20

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_012:
    EQUIPMENT_ID = "UNIT-TRACTOR-0012"
    MODEL_NAME = "John Deere 5310 4WD PowerTech Fleet #2"
    HORSEPOWER_RATING = 55
    RATED_ENGINE_RPM = 2100
    BASE_FUEL_LITERS_PER_HOUR = 5.10

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_013:
    EQUIPMENT_ID = "UNIT-TRACTOR-0013"
    MODEL_NAME = "Swaraj 855 FE 5-Star Fleet #2"
    HORSEPOWER_RATING = 52
    RATED_ENGINE_RPM = 2000
    BASE_FUEL_LITERS_PER_HOUR = 4.80

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_014:
    EQUIPMENT_ID = "UNIT-TRACTOR-0014"
    MODEL_NAME = "Sonalika DI 745 III Sikander Fleet #2"
    HORSEPOWER_RATING = 50
    RATED_ENGINE_RPM = 1900
    BASE_FUEL_LITERS_PER_HOUR = 4.50

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_015:
    EQUIPMENT_ID = "UNIT-TRACTOR-0015"
    MODEL_NAME = "Kubota MU4501 4WD Japanese Fleet #2"
    HORSEPOWER_RATING = 45
    RATED_ENGINE_RPM = 2500
    BASE_FUEL_LITERS_PER_HOUR = 3.80

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_016:
    EQUIPMENT_ID = "UNIT-TRACTOR-0016"
    MODEL_NAME = "Massey Ferguson 241 DI Dynatrack Fleet #2"
    HORSEPOWER_RATING = 42
    RATED_ENGINE_RPM = 1800
    BASE_FUEL_LITERS_PER_HOUR = 3.90

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_017:
    EQUIPMENT_ID = "UNIT-TRACTOR-0017"
    MODEL_NAME = "New Holland 3630 TX Super Plus Fleet #2"
    HORSEPOWER_RATING = 55
    RATED_ENGINE_RPM = 2200
    BASE_FUEL_LITERS_PER_HOUR = 5.20

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_018:
    EQUIPMENT_ID = "UNIT-TRACTOR-0018"
    MODEL_NAME = "Farmtrac 60 Powermaxx Fleet #2"
    HORSEPOWER_RATING = 50
    RATED_ENGINE_RPM = 2000
    BASE_FUEL_LITERS_PER_HOUR = 4.60

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_019:
    EQUIPMENT_ID = "UNIT-TRACTOR-0019"
    MODEL_NAME = "Eicher 380 Super DI Fleet #2"
    HORSEPOWER_RATING = 40
    RATED_ENGINE_RPM = 1800
    BASE_FUEL_LITERS_PER_HOUR = 3.50

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_020:
    EQUIPMENT_ID = "UNIT-TRACTOR-0020"
    MODEL_NAME = "Powertrac Euro 50 Next Fleet #2"
    HORSEPOWER_RATING = 52
    RATED_ENGINE_RPM = 2200
    BASE_FUEL_LITERS_PER_HOUR = 4.70

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_021:
    EQUIPMENT_ID = "UNIT-TRACTOR-0021"
    MODEL_NAME = "Mahindra 575 DI Sarpanch Fleet #3"
    HORSEPOWER_RATING = 47
    RATED_ENGINE_RPM = 1900
    BASE_FUEL_LITERS_PER_HOUR = 4.20

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_022:
    EQUIPMENT_ID = "UNIT-TRACTOR-0022"
    MODEL_NAME = "John Deere 5310 4WD PowerTech Fleet #3"
    HORSEPOWER_RATING = 55
    RATED_ENGINE_RPM = 2100
    BASE_FUEL_LITERS_PER_HOUR = 5.10

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_023:
    EQUIPMENT_ID = "UNIT-TRACTOR-0023"
    MODEL_NAME = "Swaraj 855 FE 5-Star Fleet #3"
    HORSEPOWER_RATING = 52
    RATED_ENGINE_RPM = 2000
    BASE_FUEL_LITERS_PER_HOUR = 4.80

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_024:
    EQUIPMENT_ID = "UNIT-TRACTOR-0024"
    MODEL_NAME = "Sonalika DI 745 III Sikander Fleet #3"
    HORSEPOWER_RATING = 50
    RATED_ENGINE_RPM = 1900
    BASE_FUEL_LITERS_PER_HOUR = 4.50

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_025:
    EQUIPMENT_ID = "UNIT-TRACTOR-0025"
    MODEL_NAME = "Kubota MU4501 4WD Japanese Fleet #3"
    HORSEPOWER_RATING = 45
    RATED_ENGINE_RPM = 2500
    BASE_FUEL_LITERS_PER_HOUR = 3.80

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_026:
    EQUIPMENT_ID = "UNIT-TRACTOR-0026"
    MODEL_NAME = "Massey Ferguson 241 DI Dynatrack Fleet #3"
    HORSEPOWER_RATING = 42
    RATED_ENGINE_RPM = 1800
    BASE_FUEL_LITERS_PER_HOUR = 3.90

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_027:
    EQUIPMENT_ID = "UNIT-TRACTOR-0027"
    MODEL_NAME = "New Holland 3630 TX Super Plus Fleet #3"
    HORSEPOWER_RATING = 55
    RATED_ENGINE_RPM = 2200
    BASE_FUEL_LITERS_PER_HOUR = 5.20

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_028:
    EQUIPMENT_ID = "UNIT-TRACTOR-0028"
    MODEL_NAME = "Farmtrac 60 Powermaxx Fleet #3"
    HORSEPOWER_RATING = 50
    RATED_ENGINE_RPM = 2000
    BASE_FUEL_LITERS_PER_HOUR = 4.60

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_029:
    EQUIPMENT_ID = "UNIT-TRACTOR-0029"
    MODEL_NAME = "Eicher 380 Super DI Fleet #3"
    HORSEPOWER_RATING = 40
    RATED_ENGINE_RPM = 1800
    BASE_FUEL_LITERS_PER_HOUR = 3.50

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_030:
    EQUIPMENT_ID = "UNIT-TRACTOR-0030"
    MODEL_NAME = "Powertrac Euro 50 Next Fleet #3"
    HORSEPOWER_RATING = 52
    RATED_ENGINE_RPM = 2200
    BASE_FUEL_LITERS_PER_HOUR = 4.70

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_031:
    EQUIPMENT_ID = "UNIT-TRACTOR-0031"
    MODEL_NAME = "Mahindra 575 DI Sarpanch Fleet #4"
    HORSEPOWER_RATING = 47
    RATED_ENGINE_RPM = 1900
    BASE_FUEL_LITERS_PER_HOUR = 4.20

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_032:
    EQUIPMENT_ID = "UNIT-TRACTOR-0032"
    MODEL_NAME = "John Deere 5310 4WD PowerTech Fleet #4"
    HORSEPOWER_RATING = 55
    RATED_ENGINE_RPM = 2100
    BASE_FUEL_LITERS_PER_HOUR = 5.10

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_033:
    EQUIPMENT_ID = "UNIT-TRACTOR-0033"
    MODEL_NAME = "Swaraj 855 FE 5-Star Fleet #4"
    HORSEPOWER_RATING = 52
    RATED_ENGINE_RPM = 2000
    BASE_FUEL_LITERS_PER_HOUR = 4.80

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_034:
    EQUIPMENT_ID = "UNIT-TRACTOR-0034"
    MODEL_NAME = "Sonalika DI 745 III Sikander Fleet #4"
    HORSEPOWER_RATING = 50
    RATED_ENGINE_RPM = 1900
    BASE_FUEL_LITERS_PER_HOUR = 4.50

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_035:
    EQUIPMENT_ID = "UNIT-TRACTOR-0035"
    MODEL_NAME = "Kubota MU4501 4WD Japanese Fleet #4"
    HORSEPOWER_RATING = 45
    RATED_ENGINE_RPM = 2500
    BASE_FUEL_LITERS_PER_HOUR = 3.80

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_036:
    EQUIPMENT_ID = "UNIT-TRACTOR-0036"
    MODEL_NAME = "Massey Ferguson 241 DI Dynatrack Fleet #4"
    HORSEPOWER_RATING = 42
    RATED_ENGINE_RPM = 1800
    BASE_FUEL_LITERS_PER_HOUR = 3.90

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_037:
    EQUIPMENT_ID = "UNIT-TRACTOR-0037"
    MODEL_NAME = "New Holland 3630 TX Super Plus Fleet #4"
    HORSEPOWER_RATING = 55
    RATED_ENGINE_RPM = 2200
    BASE_FUEL_LITERS_PER_HOUR = 5.20

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_038:
    EQUIPMENT_ID = "UNIT-TRACTOR-0038"
    MODEL_NAME = "Farmtrac 60 Powermaxx Fleet #4"
    HORSEPOWER_RATING = 50
    RATED_ENGINE_RPM = 2000
    BASE_FUEL_LITERS_PER_HOUR = 4.60

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_039:
    EQUIPMENT_ID = "UNIT-TRACTOR-0039"
    MODEL_NAME = "Eicher 380 Super DI Fleet #4"
    HORSEPOWER_RATING = 40
    RATED_ENGINE_RPM = 1800
    BASE_FUEL_LITERS_PER_HOUR = 3.50

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_040:
    EQUIPMENT_ID = "UNIT-TRACTOR-0040"
    MODEL_NAME = "Powertrac Euro 50 Next Fleet #4"
    HORSEPOWER_RATING = 52
    RATED_ENGINE_RPM = 2200
    BASE_FUEL_LITERS_PER_HOUR = 4.70

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_041:
    EQUIPMENT_ID = "UNIT-TRACTOR-0041"
    MODEL_NAME = "Mahindra 575 DI Sarpanch Fleet #5"
    HORSEPOWER_RATING = 47
    RATED_ENGINE_RPM = 1900
    BASE_FUEL_LITERS_PER_HOUR = 4.20

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_042:
    EQUIPMENT_ID = "UNIT-TRACTOR-0042"
    MODEL_NAME = "John Deere 5310 4WD PowerTech Fleet #5"
    HORSEPOWER_RATING = 55
    RATED_ENGINE_RPM = 2100
    BASE_FUEL_LITERS_PER_HOUR = 5.10

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_043:
    EQUIPMENT_ID = "UNIT-TRACTOR-0043"
    MODEL_NAME = "Swaraj 855 FE 5-Star Fleet #5"
    HORSEPOWER_RATING = 52
    RATED_ENGINE_RPM = 2000
    BASE_FUEL_LITERS_PER_HOUR = 4.80

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_044:
    EQUIPMENT_ID = "UNIT-TRACTOR-0044"
    MODEL_NAME = "Sonalika DI 745 III Sikander Fleet #5"
    HORSEPOWER_RATING = 50
    RATED_ENGINE_RPM = 1900
    BASE_FUEL_LITERS_PER_HOUR = 4.50

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_045:
    EQUIPMENT_ID = "UNIT-TRACTOR-0045"
    MODEL_NAME = "Kubota MU4501 4WD Japanese Fleet #5"
    HORSEPOWER_RATING = 45
    RATED_ENGINE_RPM = 2500
    BASE_FUEL_LITERS_PER_HOUR = 3.80

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_046:
    EQUIPMENT_ID = "UNIT-TRACTOR-0046"
    MODEL_NAME = "Massey Ferguson 241 DI Dynatrack Fleet #5"
    HORSEPOWER_RATING = 42
    RATED_ENGINE_RPM = 1800
    BASE_FUEL_LITERS_PER_HOUR = 3.90

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_047:
    EQUIPMENT_ID = "UNIT-TRACTOR-0047"
    MODEL_NAME = "New Holland 3630 TX Super Plus Fleet #5"
    HORSEPOWER_RATING = 55
    RATED_ENGINE_RPM = 2200
    BASE_FUEL_LITERS_PER_HOUR = 5.20

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_048:
    EQUIPMENT_ID = "UNIT-TRACTOR-0048"
    MODEL_NAME = "Farmtrac 60 Powermaxx Fleet #5"
    HORSEPOWER_RATING = 50
    RATED_ENGINE_RPM = 2000
    BASE_FUEL_LITERS_PER_HOUR = 4.60

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_049:
    EQUIPMENT_ID = "UNIT-TRACTOR-0049"
    MODEL_NAME = "Eicher 380 Super DI Fleet #5"
    HORSEPOWER_RATING = 40
    RATED_ENGINE_RPM = 1800
    BASE_FUEL_LITERS_PER_HOUR = 3.50

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_050:
    EQUIPMENT_ID = "UNIT-TRACTOR-0050"
    MODEL_NAME = "Powertrac Euro 50 Next Fleet #5"
    HORSEPOWER_RATING = 52
    RATED_ENGINE_RPM = 2200
    BASE_FUEL_LITERS_PER_HOUR = 4.70

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_051:
    EQUIPMENT_ID = "UNIT-TRACTOR-0051"
    MODEL_NAME = "Mahindra 575 DI Sarpanch Fleet #6"
    HORSEPOWER_RATING = 47
    RATED_ENGINE_RPM = 1900
    BASE_FUEL_LITERS_PER_HOUR = 4.20

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_052:
    EQUIPMENT_ID = "UNIT-TRACTOR-0052"
    MODEL_NAME = "John Deere 5310 4WD PowerTech Fleet #6"
    HORSEPOWER_RATING = 55
    RATED_ENGINE_RPM = 2100
    BASE_FUEL_LITERS_PER_HOUR = 5.10

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_053:
    EQUIPMENT_ID = "UNIT-TRACTOR-0053"
    MODEL_NAME = "Swaraj 855 FE 5-Star Fleet #6"
    HORSEPOWER_RATING = 52
    RATED_ENGINE_RPM = 2000
    BASE_FUEL_LITERS_PER_HOUR = 4.80

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_054:
    EQUIPMENT_ID = "UNIT-TRACTOR-0054"
    MODEL_NAME = "Sonalika DI 745 III Sikander Fleet #6"
    HORSEPOWER_RATING = 50
    RATED_ENGINE_RPM = 1900
    BASE_FUEL_LITERS_PER_HOUR = 4.50

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_055:
    EQUIPMENT_ID = "UNIT-TRACTOR-0055"
    MODEL_NAME = "Kubota MU4501 4WD Japanese Fleet #6"
    HORSEPOWER_RATING = 45
    RATED_ENGINE_RPM = 2500
    BASE_FUEL_LITERS_PER_HOUR = 3.80

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_056:
    EQUIPMENT_ID = "UNIT-TRACTOR-0056"
    MODEL_NAME = "Massey Ferguson 241 DI Dynatrack Fleet #6"
    HORSEPOWER_RATING = 42
    RATED_ENGINE_RPM = 1800
    BASE_FUEL_LITERS_PER_HOUR = 3.90

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_057:
    EQUIPMENT_ID = "UNIT-TRACTOR-0057"
    MODEL_NAME = "New Holland 3630 TX Super Plus Fleet #6"
    HORSEPOWER_RATING = 55
    RATED_ENGINE_RPM = 2200
    BASE_FUEL_LITERS_PER_HOUR = 5.20

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_058:
    EQUIPMENT_ID = "UNIT-TRACTOR-0058"
    MODEL_NAME = "Farmtrac 60 Powermaxx Fleet #6"
    HORSEPOWER_RATING = 50
    RATED_ENGINE_RPM = 2000
    BASE_FUEL_LITERS_PER_HOUR = 4.60

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_059:
    EQUIPMENT_ID = "UNIT-TRACTOR-0059"
    MODEL_NAME = "Eicher 380 Super DI Fleet #6"
    HORSEPOWER_RATING = 40
    RATED_ENGINE_RPM = 1800
    BASE_FUEL_LITERS_PER_HOUR = 3.50

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_060:
    EQUIPMENT_ID = "UNIT-TRACTOR-0060"
    MODEL_NAME = "Powertrac Euro 50 Next Fleet #6"
    HORSEPOWER_RATING = 52
    RATED_ENGINE_RPM = 2200
    BASE_FUEL_LITERS_PER_HOUR = 4.70

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_061:
    EQUIPMENT_ID = "UNIT-TRACTOR-0061"
    MODEL_NAME = "Mahindra 575 DI Sarpanch Fleet #7"
    HORSEPOWER_RATING = 47
    RATED_ENGINE_RPM = 1900
    BASE_FUEL_LITERS_PER_HOUR = 4.20

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_062:
    EQUIPMENT_ID = "UNIT-TRACTOR-0062"
    MODEL_NAME = "John Deere 5310 4WD PowerTech Fleet #7"
    HORSEPOWER_RATING = 55
    RATED_ENGINE_RPM = 2100
    BASE_FUEL_LITERS_PER_HOUR = 5.10

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_063:
    EQUIPMENT_ID = "UNIT-TRACTOR-0063"
    MODEL_NAME = "Swaraj 855 FE 5-Star Fleet #7"
    HORSEPOWER_RATING = 52
    RATED_ENGINE_RPM = 2000
    BASE_FUEL_LITERS_PER_HOUR = 4.80

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_064:
    EQUIPMENT_ID = "UNIT-TRACTOR-0064"
    MODEL_NAME = "Sonalika DI 745 III Sikander Fleet #7"
    HORSEPOWER_RATING = 50
    RATED_ENGINE_RPM = 1900
    BASE_FUEL_LITERS_PER_HOUR = 4.50

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_065:
    EQUIPMENT_ID = "UNIT-TRACTOR-0065"
    MODEL_NAME = "Kubota MU4501 4WD Japanese Fleet #7"
    HORSEPOWER_RATING = 45
    RATED_ENGINE_RPM = 2500
    BASE_FUEL_LITERS_PER_HOUR = 3.80

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_066:
    EQUIPMENT_ID = "UNIT-TRACTOR-0066"
    MODEL_NAME = "Massey Ferguson 241 DI Dynatrack Fleet #7"
    HORSEPOWER_RATING = 42
    RATED_ENGINE_RPM = 1800
    BASE_FUEL_LITERS_PER_HOUR = 3.90

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_067:
    EQUIPMENT_ID = "UNIT-TRACTOR-0067"
    MODEL_NAME = "New Holland 3630 TX Super Plus Fleet #7"
    HORSEPOWER_RATING = 55
    RATED_ENGINE_RPM = 2200
    BASE_FUEL_LITERS_PER_HOUR = 5.20

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_068:
    EQUIPMENT_ID = "UNIT-TRACTOR-0068"
    MODEL_NAME = "Farmtrac 60 Powermaxx Fleet #7"
    HORSEPOWER_RATING = 50
    RATED_ENGINE_RPM = 2000
    BASE_FUEL_LITERS_PER_HOUR = 4.60

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_069:
    EQUIPMENT_ID = "UNIT-TRACTOR-0069"
    MODEL_NAME = "Eicher 380 Super DI Fleet #7"
    HORSEPOWER_RATING = 40
    RATED_ENGINE_RPM = 1800
    BASE_FUEL_LITERS_PER_HOUR = 3.50

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_070:
    EQUIPMENT_ID = "UNIT-TRACTOR-0070"
    MODEL_NAME = "Powertrac Euro 50 Next Fleet #7"
    HORSEPOWER_RATING = 52
    RATED_ENGINE_RPM = 2200
    BASE_FUEL_LITERS_PER_HOUR = 4.70

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_071:
    EQUIPMENT_ID = "UNIT-TRACTOR-0071"
    MODEL_NAME = "Mahindra 575 DI Sarpanch Fleet #8"
    HORSEPOWER_RATING = 47
    RATED_ENGINE_RPM = 1900
    BASE_FUEL_LITERS_PER_HOUR = 4.20

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_072:
    EQUIPMENT_ID = "UNIT-TRACTOR-0072"
    MODEL_NAME = "John Deere 5310 4WD PowerTech Fleet #8"
    HORSEPOWER_RATING = 55
    RATED_ENGINE_RPM = 2100
    BASE_FUEL_LITERS_PER_HOUR = 5.10

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_073:
    EQUIPMENT_ID = "UNIT-TRACTOR-0073"
    MODEL_NAME = "Swaraj 855 FE 5-Star Fleet #8"
    HORSEPOWER_RATING = 52
    RATED_ENGINE_RPM = 2000
    BASE_FUEL_LITERS_PER_HOUR = 4.80

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_074:
    EQUIPMENT_ID = "UNIT-TRACTOR-0074"
    MODEL_NAME = "Sonalika DI 745 III Sikander Fleet #8"
    HORSEPOWER_RATING = 50
    RATED_ENGINE_RPM = 1900
    BASE_FUEL_LITERS_PER_HOUR = 4.50

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_075:
    EQUIPMENT_ID = "UNIT-TRACTOR-0075"
    MODEL_NAME = "Kubota MU4501 4WD Japanese Fleet #8"
    HORSEPOWER_RATING = 45
    RATED_ENGINE_RPM = 2500
    BASE_FUEL_LITERS_PER_HOUR = 3.80

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_076:
    EQUIPMENT_ID = "UNIT-TRACTOR-0076"
    MODEL_NAME = "Massey Ferguson 241 DI Dynatrack Fleet #8"
    HORSEPOWER_RATING = 42
    RATED_ENGINE_RPM = 1800
    BASE_FUEL_LITERS_PER_HOUR = 3.90

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_077:
    EQUIPMENT_ID = "UNIT-TRACTOR-0077"
    MODEL_NAME = "New Holland 3630 TX Super Plus Fleet #8"
    HORSEPOWER_RATING = 55
    RATED_ENGINE_RPM = 2200
    BASE_FUEL_LITERS_PER_HOUR = 5.20

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_078:
    EQUIPMENT_ID = "UNIT-TRACTOR-0078"
    MODEL_NAME = "Farmtrac 60 Powermaxx Fleet #8"
    HORSEPOWER_RATING = 50
    RATED_ENGINE_RPM = 2000
    BASE_FUEL_LITERS_PER_HOUR = 4.60

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_079:
    EQUIPMENT_ID = "UNIT-TRACTOR-0079"
    MODEL_NAME = "Eicher 380 Super DI Fleet #8"
    HORSEPOWER_RATING = 40
    RATED_ENGINE_RPM = 1800
    BASE_FUEL_LITERS_PER_HOUR = 3.50

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_080:
    EQUIPMENT_ID = "UNIT-TRACTOR-0080"
    MODEL_NAME = "Powertrac Euro 50 Next Fleet #8"
    HORSEPOWER_RATING = 52
    RATED_ENGINE_RPM = 2200
    BASE_FUEL_LITERS_PER_HOUR = 4.70

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_081:
    EQUIPMENT_ID = "UNIT-TRACTOR-0081"
    MODEL_NAME = "Mahindra 575 DI Sarpanch Fleet #9"
    HORSEPOWER_RATING = 47
    RATED_ENGINE_RPM = 1900
    BASE_FUEL_LITERS_PER_HOUR = 4.20

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_082:
    EQUIPMENT_ID = "UNIT-TRACTOR-0082"
    MODEL_NAME = "John Deere 5310 4WD PowerTech Fleet #9"
    HORSEPOWER_RATING = 55
    RATED_ENGINE_RPM = 2100
    BASE_FUEL_LITERS_PER_HOUR = 5.10

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_083:
    EQUIPMENT_ID = "UNIT-TRACTOR-0083"
    MODEL_NAME = "Swaraj 855 FE 5-Star Fleet #9"
    HORSEPOWER_RATING = 52
    RATED_ENGINE_RPM = 2000
    BASE_FUEL_LITERS_PER_HOUR = 4.80

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_084:
    EQUIPMENT_ID = "UNIT-TRACTOR-0084"
    MODEL_NAME = "Sonalika DI 745 III Sikander Fleet #9"
    HORSEPOWER_RATING = 50
    RATED_ENGINE_RPM = 1900
    BASE_FUEL_LITERS_PER_HOUR = 4.50

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_085:
    EQUIPMENT_ID = "UNIT-TRACTOR-0085"
    MODEL_NAME = "Kubota MU4501 4WD Japanese Fleet #9"
    HORSEPOWER_RATING = 45
    RATED_ENGINE_RPM = 2500
    BASE_FUEL_LITERS_PER_HOUR = 3.80

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_086:
    EQUIPMENT_ID = "UNIT-TRACTOR-0086"
    MODEL_NAME = "Massey Ferguson 241 DI Dynatrack Fleet #9"
    HORSEPOWER_RATING = 42
    RATED_ENGINE_RPM = 1800
    BASE_FUEL_LITERS_PER_HOUR = 3.90

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_087:
    EQUIPMENT_ID = "UNIT-TRACTOR-0087"
    MODEL_NAME = "New Holland 3630 TX Super Plus Fleet #9"
    HORSEPOWER_RATING = 55
    RATED_ENGINE_RPM = 2200
    BASE_FUEL_LITERS_PER_HOUR = 5.20

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_088:
    EQUIPMENT_ID = "UNIT-TRACTOR-0088"
    MODEL_NAME = "Farmtrac 60 Powermaxx Fleet #9"
    HORSEPOWER_RATING = 50
    RATED_ENGINE_RPM = 2000
    BASE_FUEL_LITERS_PER_HOUR = 4.60

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_089:
    EQUIPMENT_ID = "UNIT-TRACTOR-0089"
    MODEL_NAME = "Eicher 380 Super DI Fleet #9"
    HORSEPOWER_RATING = 40
    RATED_ENGINE_RPM = 1800
    BASE_FUEL_LITERS_PER_HOUR = 3.50

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_090:
    EQUIPMENT_ID = "UNIT-TRACTOR-0090"
    MODEL_NAME = "Powertrac Euro 50 Next Fleet #9"
    HORSEPOWER_RATING = 52
    RATED_ENGINE_RPM = 2200
    BASE_FUEL_LITERS_PER_HOUR = 4.70

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_091:
    EQUIPMENT_ID = "UNIT-TRACTOR-0091"
    MODEL_NAME = "Mahindra 575 DI Sarpanch Fleet #10"
    HORSEPOWER_RATING = 47
    RATED_ENGINE_RPM = 1900
    BASE_FUEL_LITERS_PER_HOUR = 4.20

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_092:
    EQUIPMENT_ID = "UNIT-TRACTOR-0092"
    MODEL_NAME = "John Deere 5310 4WD PowerTech Fleet #10"
    HORSEPOWER_RATING = 55
    RATED_ENGINE_RPM = 2100
    BASE_FUEL_LITERS_PER_HOUR = 5.10

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_093:
    EQUIPMENT_ID = "UNIT-TRACTOR-0093"
    MODEL_NAME = "Swaraj 855 FE 5-Star Fleet #10"
    HORSEPOWER_RATING = 52
    RATED_ENGINE_RPM = 2000
    BASE_FUEL_LITERS_PER_HOUR = 4.80

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_094:
    EQUIPMENT_ID = "UNIT-TRACTOR-0094"
    MODEL_NAME = "Sonalika DI 745 III Sikander Fleet #10"
    HORSEPOWER_RATING = 50
    RATED_ENGINE_RPM = 1900
    BASE_FUEL_LITERS_PER_HOUR = 4.50

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_095:
    EQUIPMENT_ID = "UNIT-TRACTOR-0095"
    MODEL_NAME = "Kubota MU4501 4WD Japanese Fleet #10"
    HORSEPOWER_RATING = 45
    RATED_ENGINE_RPM = 2500
    BASE_FUEL_LITERS_PER_HOUR = 3.80

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_096:
    EQUIPMENT_ID = "UNIT-TRACTOR-0096"
    MODEL_NAME = "Massey Ferguson 241 DI Dynatrack Fleet #10"
    HORSEPOWER_RATING = 42
    RATED_ENGINE_RPM = 1800
    BASE_FUEL_LITERS_PER_HOUR = 3.90

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_097:
    EQUIPMENT_ID = "UNIT-TRACTOR-0097"
    MODEL_NAME = "New Holland 3630 TX Super Plus Fleet #10"
    HORSEPOWER_RATING = 55
    RATED_ENGINE_RPM = 2200
    BASE_FUEL_LITERS_PER_HOUR = 5.20

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_098:
    EQUIPMENT_ID = "UNIT-TRACTOR-0098"
    MODEL_NAME = "Farmtrac 60 Powermaxx Fleet #10"
    HORSEPOWER_RATING = 50
    RATED_ENGINE_RPM = 2000
    BASE_FUEL_LITERS_PER_HOUR = 4.60

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_099:
    EQUIPMENT_ID = "UNIT-TRACTOR-0099"
    MODEL_NAME = "Eicher 380 Super DI Fleet #10"
    HORSEPOWER_RATING = 40
    RATED_ENGINE_RPM = 1800
    BASE_FUEL_LITERS_PER_HOUR = 3.50

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

class MachineryTelematicsController_100:
    EQUIPMENT_ID = "UNIT-TRACTOR-0100"
    MODEL_NAME = "Powertrac Euro 50 Next Fleet #10"
    HORSEPOWER_RATING = 52
    RATED_ENGINE_RPM = 2200
    BASE_FUEL_LITERS_PER_HOUR = 4.70

    @classmethod
    def compute_field_operation_efficiency(
        cls,
        engine_hours: float,
        field_area_ha: float,
        implement_type: str = "Rotavator",
        soil_hardness_penetrometer_kpa: float = 1200.0,
        engine_load_percentage: float = 78.0
    ) -> Dict[str, Any]:
        load_factor = (engine_load_percentage / 100.0) ** 1.2
        soil_factor = (soil_hardness_penetrometer_kpa / 1000.0) ** 0.4
        actual_fuel_rate_lph = cls.BASE_FUEL_LITERS_PER_HOUR * load_factor * soil_factor
        total_diesel_liters = actual_fuel_rate_lph * engine_hours
        fuel_cost_inr = total_diesel_liters * 92.50
        hectares_per_hour = field_area_ha / max(0.1, engine_hours)
        fuel_per_ha = total_diesel_liters / max(0.1, field_area_ha)
        hours_until_next_service = max(0.0, 250.0 - (engine_hours % 250.0))
        return {
            "equipment_id": cls.EQUIPMENT_ID,
            "model_name": cls.MODEL_NAME,
            "total_engine_runtime_hours": engine_hours,
            "field_coverage_rate_ha_per_hr": round(hectares_per_hour, 2),
            "diesel_consumed_liters": round(total_diesel_liters, 2),
            "diesel_consumption_liters_per_ha": round(fuel_per_ha, 2),
            "total_fuel_expense_inr": round(fuel_cost_inr, 2),
            "hours_until_mandatory_service": round(hours_until_next_service, 1),
            "telematics_health_status": "OPTIMAL" if hours_until_next_service > 30 else "SERVICE_DUE_SOON"
        }

