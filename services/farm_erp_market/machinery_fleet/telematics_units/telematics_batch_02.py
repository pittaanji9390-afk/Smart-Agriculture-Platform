"""
Machinery Telematics Units - Batch 2
"""
from typing import Dict, Any

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

