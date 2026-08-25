"""
Machinery Telematics Units - Batch 1
"""
from typing import Dict, Any

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

