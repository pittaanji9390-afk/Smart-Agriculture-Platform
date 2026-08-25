"""
Machinery Telematics Units - Batch 4
"""
from typing import Dict, Any

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

