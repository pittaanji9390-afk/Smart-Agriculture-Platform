"""
Micro-Climate Numerical Weather Downscaler & Agro-Meteorological Advisory Engine
"""
import math
from typing import Dict, Any, List

class AgroMeteorologicalGridCell_001:
    GRID_ID = "WEATHER-CELL-0001"
    ELEVATION_METERS = 120.0
    LATITUDE_DEG = 12.0000
    LONGITUDE_DEG = 72.0000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_002:
    GRID_ID = "WEATHER-CELL-0002"
    ELEVATION_METERS = 165.0
    LATITUDE_DEG = 12.8000
    LONGITUDE_DEG = 72.7000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_003:
    GRID_ID = "WEATHER-CELL-0003"
    ELEVATION_METERS = 210.0
    LATITUDE_DEG = 13.6000
    LONGITUDE_DEG = 73.4000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_004:
    GRID_ID = "WEATHER-CELL-0004"
    ELEVATION_METERS = 255.0
    LATITUDE_DEG = 14.4000
    LONGITUDE_DEG = 74.1000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_005:
    GRID_ID = "WEATHER-CELL-0005"
    ELEVATION_METERS = 300.0
    LATITUDE_DEG = 15.2000
    LONGITUDE_DEG = 74.8000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_006:
    GRID_ID = "WEATHER-CELL-0006"
    ELEVATION_METERS = 345.0
    LATITUDE_DEG = 16.0000
    LONGITUDE_DEG = 75.5000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_007:
    GRID_ID = "WEATHER-CELL-0007"
    ELEVATION_METERS = 390.0
    LATITUDE_DEG = 16.8000
    LONGITUDE_DEG = 76.2000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_008:
    GRID_ID = "WEATHER-CELL-0008"
    ELEVATION_METERS = 435.0
    LATITUDE_DEG = 17.6000
    LONGITUDE_DEG = 76.9000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_009:
    GRID_ID = "WEATHER-CELL-0009"
    ELEVATION_METERS = 480.0
    LATITUDE_DEG = 18.4000
    LONGITUDE_DEG = 77.6000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_010:
    GRID_ID = "WEATHER-CELL-0010"
    ELEVATION_METERS = 525.0
    LATITUDE_DEG = 19.2000
    LONGITUDE_DEG = 78.3000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_011:
    GRID_ID = "WEATHER-CELL-0011"
    ELEVATION_METERS = 570.0
    LATITUDE_DEG = 20.0000
    LONGITUDE_DEG = 79.0000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_012:
    GRID_ID = "WEATHER-CELL-0012"
    ELEVATION_METERS = 615.0
    LATITUDE_DEG = 20.8000
    LONGITUDE_DEG = 79.7000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_013:
    GRID_ID = "WEATHER-CELL-0013"
    ELEVATION_METERS = 660.0
    LATITUDE_DEG = 21.6000
    LONGITUDE_DEG = 80.4000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_014:
    GRID_ID = "WEATHER-CELL-0014"
    ELEVATION_METERS = 705.0
    LATITUDE_DEG = 22.4000
    LONGITUDE_DEG = 81.1000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_015:
    GRID_ID = "WEATHER-CELL-0015"
    ELEVATION_METERS = 750.0
    LATITUDE_DEG = 23.2000
    LONGITUDE_DEG = 81.8000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_016:
    GRID_ID = "WEATHER-CELL-0016"
    ELEVATION_METERS = 795.0
    LATITUDE_DEG = 24.0000
    LONGITUDE_DEG = 82.5000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_017:
    GRID_ID = "WEATHER-CELL-0017"
    ELEVATION_METERS = 840.0
    LATITUDE_DEG = 24.8000
    LONGITUDE_DEG = 83.2000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_018:
    GRID_ID = "WEATHER-CELL-0018"
    ELEVATION_METERS = 885.0
    LATITUDE_DEG = 25.6000
    LONGITUDE_DEG = 83.9000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_019:
    GRID_ID = "WEATHER-CELL-0019"
    ELEVATION_METERS = 930.0
    LATITUDE_DEG = 12.0000
    LONGITUDE_DEG = 84.6000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_020:
    GRID_ID = "WEATHER-CELL-0020"
    ELEVATION_METERS = 975.0
    LATITUDE_DEG = 12.8000
    LONGITUDE_DEG = 85.3000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_021:
    GRID_ID = "WEATHER-CELL-0021"
    ELEVATION_METERS = 1020.0
    LATITUDE_DEG = 13.6000
    LONGITUDE_DEG = 72.0000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_022:
    GRID_ID = "WEATHER-CELL-0022"
    ELEVATION_METERS = 1065.0
    LATITUDE_DEG = 14.4000
    LONGITUDE_DEG = 72.7000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_023:
    GRID_ID = "WEATHER-CELL-0023"
    ELEVATION_METERS = 1110.0
    LATITUDE_DEG = 15.2000
    LONGITUDE_DEG = 73.4000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_024:
    GRID_ID = "WEATHER-CELL-0024"
    ELEVATION_METERS = 1155.0
    LATITUDE_DEG = 16.0000
    LONGITUDE_DEG = 74.1000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_025:
    GRID_ID = "WEATHER-CELL-0025"
    ELEVATION_METERS = 1200.0
    LATITUDE_DEG = 16.8000
    LONGITUDE_DEG = 74.8000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_026:
    GRID_ID = "WEATHER-CELL-0026"
    ELEVATION_METERS = 120.0
    LATITUDE_DEG = 17.6000
    LONGITUDE_DEG = 75.5000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_027:
    GRID_ID = "WEATHER-CELL-0027"
    ELEVATION_METERS = 165.0
    LATITUDE_DEG = 18.4000
    LONGITUDE_DEG = 76.2000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_028:
    GRID_ID = "WEATHER-CELL-0028"
    ELEVATION_METERS = 210.0
    LATITUDE_DEG = 19.2000
    LONGITUDE_DEG = 76.9000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_029:
    GRID_ID = "WEATHER-CELL-0029"
    ELEVATION_METERS = 255.0
    LATITUDE_DEG = 20.0000
    LONGITUDE_DEG = 77.6000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_030:
    GRID_ID = "WEATHER-CELL-0030"
    ELEVATION_METERS = 300.0
    LATITUDE_DEG = 20.8000
    LONGITUDE_DEG = 78.3000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_031:
    GRID_ID = "WEATHER-CELL-0031"
    ELEVATION_METERS = 345.0
    LATITUDE_DEG = 21.6000
    LONGITUDE_DEG = 79.0000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_032:
    GRID_ID = "WEATHER-CELL-0032"
    ELEVATION_METERS = 390.0
    LATITUDE_DEG = 22.4000
    LONGITUDE_DEG = 79.7000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_033:
    GRID_ID = "WEATHER-CELL-0033"
    ELEVATION_METERS = 435.0
    LATITUDE_DEG = 23.2000
    LONGITUDE_DEG = 80.4000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_034:
    GRID_ID = "WEATHER-CELL-0034"
    ELEVATION_METERS = 480.0
    LATITUDE_DEG = 24.0000
    LONGITUDE_DEG = 81.1000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_035:
    GRID_ID = "WEATHER-CELL-0035"
    ELEVATION_METERS = 525.0
    LATITUDE_DEG = 24.8000
    LONGITUDE_DEG = 81.8000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_036:
    GRID_ID = "WEATHER-CELL-0036"
    ELEVATION_METERS = 570.0
    LATITUDE_DEG = 25.6000
    LONGITUDE_DEG = 82.5000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_037:
    GRID_ID = "WEATHER-CELL-0037"
    ELEVATION_METERS = 615.0
    LATITUDE_DEG = 12.0000
    LONGITUDE_DEG = 83.2000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_038:
    GRID_ID = "WEATHER-CELL-0038"
    ELEVATION_METERS = 660.0
    LATITUDE_DEG = 12.8000
    LONGITUDE_DEG = 83.9000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_039:
    GRID_ID = "WEATHER-CELL-0039"
    ELEVATION_METERS = 705.0
    LATITUDE_DEG = 13.6000
    LONGITUDE_DEG = 84.6000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_040:
    GRID_ID = "WEATHER-CELL-0040"
    ELEVATION_METERS = 750.0
    LATITUDE_DEG = 14.4000
    LONGITUDE_DEG = 85.3000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_041:
    GRID_ID = "WEATHER-CELL-0041"
    ELEVATION_METERS = 795.0
    LATITUDE_DEG = 15.2000
    LONGITUDE_DEG = 72.0000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_042:
    GRID_ID = "WEATHER-CELL-0042"
    ELEVATION_METERS = 840.0
    LATITUDE_DEG = 16.0000
    LONGITUDE_DEG = 72.7000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_043:
    GRID_ID = "WEATHER-CELL-0043"
    ELEVATION_METERS = 885.0
    LATITUDE_DEG = 16.8000
    LONGITUDE_DEG = 73.4000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_044:
    GRID_ID = "WEATHER-CELL-0044"
    ELEVATION_METERS = 930.0
    LATITUDE_DEG = 17.6000
    LONGITUDE_DEG = 74.1000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_045:
    GRID_ID = "WEATHER-CELL-0045"
    ELEVATION_METERS = 975.0
    LATITUDE_DEG = 18.4000
    LONGITUDE_DEG = 74.8000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_046:
    GRID_ID = "WEATHER-CELL-0046"
    ELEVATION_METERS = 1020.0
    LATITUDE_DEG = 19.2000
    LONGITUDE_DEG = 75.5000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_047:
    GRID_ID = "WEATHER-CELL-0047"
    ELEVATION_METERS = 1065.0
    LATITUDE_DEG = 20.0000
    LONGITUDE_DEG = 76.2000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_048:
    GRID_ID = "WEATHER-CELL-0048"
    ELEVATION_METERS = 1110.0
    LATITUDE_DEG = 20.8000
    LONGITUDE_DEG = 76.9000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_049:
    GRID_ID = "WEATHER-CELL-0049"
    ELEVATION_METERS = 1155.0
    LATITUDE_DEG = 21.6000
    LONGITUDE_DEG = 77.6000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_050:
    GRID_ID = "WEATHER-CELL-0050"
    ELEVATION_METERS = 1200.0
    LATITUDE_DEG = 22.4000
    LONGITUDE_DEG = 78.3000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_051:
    GRID_ID = "WEATHER-CELL-0051"
    ELEVATION_METERS = 120.0
    LATITUDE_DEG = 23.2000
    LONGITUDE_DEG = 79.0000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_052:
    GRID_ID = "WEATHER-CELL-0052"
    ELEVATION_METERS = 165.0
    LATITUDE_DEG = 24.0000
    LONGITUDE_DEG = 79.7000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_053:
    GRID_ID = "WEATHER-CELL-0053"
    ELEVATION_METERS = 210.0
    LATITUDE_DEG = 24.8000
    LONGITUDE_DEG = 80.4000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_054:
    GRID_ID = "WEATHER-CELL-0054"
    ELEVATION_METERS = 255.0
    LATITUDE_DEG = 25.6000
    LONGITUDE_DEG = 81.1000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_055:
    GRID_ID = "WEATHER-CELL-0055"
    ELEVATION_METERS = 300.0
    LATITUDE_DEG = 12.0000
    LONGITUDE_DEG = 81.8000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_056:
    GRID_ID = "WEATHER-CELL-0056"
    ELEVATION_METERS = 345.0
    LATITUDE_DEG = 12.8000
    LONGITUDE_DEG = 82.5000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_057:
    GRID_ID = "WEATHER-CELL-0057"
    ELEVATION_METERS = 390.0
    LATITUDE_DEG = 13.6000
    LONGITUDE_DEG = 83.2000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_058:
    GRID_ID = "WEATHER-CELL-0058"
    ELEVATION_METERS = 435.0
    LATITUDE_DEG = 14.4000
    LONGITUDE_DEG = 83.9000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_059:
    GRID_ID = "WEATHER-CELL-0059"
    ELEVATION_METERS = 480.0
    LATITUDE_DEG = 15.2000
    LONGITUDE_DEG = 84.6000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_060:
    GRID_ID = "WEATHER-CELL-0060"
    ELEVATION_METERS = 525.0
    LATITUDE_DEG = 16.0000
    LONGITUDE_DEG = 85.3000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_061:
    GRID_ID = "WEATHER-CELL-0061"
    ELEVATION_METERS = 570.0
    LATITUDE_DEG = 16.8000
    LONGITUDE_DEG = 72.0000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_062:
    GRID_ID = "WEATHER-CELL-0062"
    ELEVATION_METERS = 615.0
    LATITUDE_DEG = 17.6000
    LONGITUDE_DEG = 72.7000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_063:
    GRID_ID = "WEATHER-CELL-0063"
    ELEVATION_METERS = 660.0
    LATITUDE_DEG = 18.4000
    LONGITUDE_DEG = 73.4000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_064:
    GRID_ID = "WEATHER-CELL-0064"
    ELEVATION_METERS = 705.0
    LATITUDE_DEG = 19.2000
    LONGITUDE_DEG = 74.1000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_065:
    GRID_ID = "WEATHER-CELL-0065"
    ELEVATION_METERS = 750.0
    LATITUDE_DEG = 20.0000
    LONGITUDE_DEG = 74.8000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_066:
    GRID_ID = "WEATHER-CELL-0066"
    ELEVATION_METERS = 795.0
    LATITUDE_DEG = 20.8000
    LONGITUDE_DEG = 75.5000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_067:
    GRID_ID = "WEATHER-CELL-0067"
    ELEVATION_METERS = 840.0
    LATITUDE_DEG = 21.6000
    LONGITUDE_DEG = 76.2000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_068:
    GRID_ID = "WEATHER-CELL-0068"
    ELEVATION_METERS = 885.0
    LATITUDE_DEG = 22.4000
    LONGITUDE_DEG = 76.9000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_069:
    GRID_ID = "WEATHER-CELL-0069"
    ELEVATION_METERS = 930.0
    LATITUDE_DEG = 23.2000
    LONGITUDE_DEG = 77.6000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_070:
    GRID_ID = "WEATHER-CELL-0070"
    ELEVATION_METERS = 975.0
    LATITUDE_DEG = 24.0000
    LONGITUDE_DEG = 78.3000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_071:
    GRID_ID = "WEATHER-CELL-0071"
    ELEVATION_METERS = 1020.0
    LATITUDE_DEG = 24.8000
    LONGITUDE_DEG = 79.0000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_072:
    GRID_ID = "WEATHER-CELL-0072"
    ELEVATION_METERS = 1065.0
    LATITUDE_DEG = 25.6000
    LONGITUDE_DEG = 79.7000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_073:
    GRID_ID = "WEATHER-CELL-0073"
    ELEVATION_METERS = 1110.0
    LATITUDE_DEG = 12.0000
    LONGITUDE_DEG = 80.4000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_074:
    GRID_ID = "WEATHER-CELL-0074"
    ELEVATION_METERS = 1155.0
    LATITUDE_DEG = 12.8000
    LONGITUDE_DEG = 81.1000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_075:
    GRID_ID = "WEATHER-CELL-0075"
    ELEVATION_METERS = 1200.0
    LATITUDE_DEG = 13.6000
    LONGITUDE_DEG = 81.8000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_076:
    GRID_ID = "WEATHER-CELL-0076"
    ELEVATION_METERS = 120.0
    LATITUDE_DEG = 14.4000
    LONGITUDE_DEG = 82.5000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_077:
    GRID_ID = "WEATHER-CELL-0077"
    ELEVATION_METERS = 165.0
    LATITUDE_DEG = 15.2000
    LONGITUDE_DEG = 83.2000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_078:
    GRID_ID = "WEATHER-CELL-0078"
    ELEVATION_METERS = 210.0
    LATITUDE_DEG = 16.0000
    LONGITUDE_DEG = 83.9000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_079:
    GRID_ID = "WEATHER-CELL-0079"
    ELEVATION_METERS = 255.0
    LATITUDE_DEG = 16.8000
    LONGITUDE_DEG = 84.6000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_080:
    GRID_ID = "WEATHER-CELL-0080"
    ELEVATION_METERS = 300.0
    LATITUDE_DEG = 17.6000
    LONGITUDE_DEG = 85.3000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_081:
    GRID_ID = "WEATHER-CELL-0081"
    ELEVATION_METERS = 345.0
    LATITUDE_DEG = 18.4000
    LONGITUDE_DEG = 72.0000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_082:
    GRID_ID = "WEATHER-CELL-0082"
    ELEVATION_METERS = 390.0
    LATITUDE_DEG = 19.2000
    LONGITUDE_DEG = 72.7000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_083:
    GRID_ID = "WEATHER-CELL-0083"
    ELEVATION_METERS = 435.0
    LATITUDE_DEG = 20.0000
    LONGITUDE_DEG = 73.4000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_084:
    GRID_ID = "WEATHER-CELL-0084"
    ELEVATION_METERS = 480.0
    LATITUDE_DEG = 20.8000
    LONGITUDE_DEG = 74.1000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_085:
    GRID_ID = "WEATHER-CELL-0085"
    ELEVATION_METERS = 525.0
    LATITUDE_DEG = 21.6000
    LONGITUDE_DEG = 74.8000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_086:
    GRID_ID = "WEATHER-CELL-0086"
    ELEVATION_METERS = 570.0
    LATITUDE_DEG = 22.4000
    LONGITUDE_DEG = 75.5000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_087:
    GRID_ID = "WEATHER-CELL-0087"
    ELEVATION_METERS = 615.0
    LATITUDE_DEG = 23.2000
    LONGITUDE_DEG = 76.2000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_088:
    GRID_ID = "WEATHER-CELL-0088"
    ELEVATION_METERS = 660.0
    LATITUDE_DEG = 24.0000
    LONGITUDE_DEG = 76.9000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_089:
    GRID_ID = "WEATHER-CELL-0089"
    ELEVATION_METERS = 705.0
    LATITUDE_DEG = 24.8000
    LONGITUDE_DEG = 77.6000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_090:
    GRID_ID = "WEATHER-CELL-0090"
    ELEVATION_METERS = 750.0
    LATITUDE_DEG = 25.6000
    LONGITUDE_DEG = 78.3000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_091:
    GRID_ID = "WEATHER-CELL-0091"
    ELEVATION_METERS = 795.0
    LATITUDE_DEG = 12.0000
    LONGITUDE_DEG = 79.0000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_092:
    GRID_ID = "WEATHER-CELL-0092"
    ELEVATION_METERS = 840.0
    LATITUDE_DEG = 12.8000
    LONGITUDE_DEG = 79.7000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_093:
    GRID_ID = "WEATHER-CELL-0093"
    ELEVATION_METERS = 885.0
    LATITUDE_DEG = 13.6000
    LONGITUDE_DEG = 80.4000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_094:
    GRID_ID = "WEATHER-CELL-0094"
    ELEVATION_METERS = 930.0
    LATITUDE_DEG = 14.4000
    LONGITUDE_DEG = 81.1000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_095:
    GRID_ID = "WEATHER-CELL-0095"
    ELEVATION_METERS = 975.0
    LATITUDE_DEG = 15.2000
    LONGITUDE_DEG = 81.8000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_096:
    GRID_ID = "WEATHER-CELL-0096"
    ELEVATION_METERS = 1020.0
    LATITUDE_DEG = 16.0000
    LONGITUDE_DEG = 82.5000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_097:
    GRID_ID = "WEATHER-CELL-0097"
    ELEVATION_METERS = 1065.0
    LATITUDE_DEG = 16.8000
    LONGITUDE_DEG = 83.2000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_098:
    GRID_ID = "WEATHER-CELL-0098"
    ELEVATION_METERS = 1110.0
    LATITUDE_DEG = 17.6000
    LONGITUDE_DEG = 83.9000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_099:
    GRID_ID = "WEATHER-CELL-0099"
    ELEVATION_METERS = 1155.0
    LATITUDE_DEG = 18.4000
    LONGITUDE_DEG = 84.6000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

class AgroMeteorologicalGridCell_100:
    GRID_ID = "WEATHER-CELL-0100"
    ELEVATION_METERS = 1200.0
    LATITUDE_DEG = 19.2000
    LONGITUDE_DEG = 85.3000

    @classmethod
    def forecast_microclimate_advisory(
        cls,
        synoptic_t_max_c: float,
        synoptic_t_min_c: float,
        synoptic_rh_pct: float,
        synoptic_wind_speed_kmh: float,
        canopy_closure_fraction: float = 0.75
    ) -> Dict[str, Any]:
        elevation_offset_c = (cls.ELEVATION_METERS / 1000.0) * -6.5
        local_t_max = synoptic_t_max_c + elevation_offset_c
        local_t_min = synoptic_t_min_c + elevation_offset_c
        canopy_t_max = local_t_max - (canopy_closure_fraction * 2.2)
        canopy_t_min = local_t_min + (canopy_closure_fraction * 1.8)
        es = 0.6108 * math.exp((17.27 * canopy_t_max) / (canopy_t_max + 237.3))
        ea = es * (synoptic_rh_pct / 100.0)
        vpd = max(0.1, es - ea)
        heat_stress = canopy_t_max >= 35.0
        frost_risk = canopy_t_min <= 3.5
        delta_t = canopy_t_max - (canopy_t_max * (synoptic_rh_pct / 100.0)**0.5)
        spray_suitable = (2.0 <= delta_t <= 8.0) and (synoptic_wind_speed_kmh < 15.0)
        return {
            "grid_cell_id": cls.GRID_ID,
            "elevation_m": cls.ELEVATION_METERS,
            "adjusted_canopy_temp_max_c": round(canopy_t_max, 1),
            "adjusted_canopy_temp_min_c": round(canopy_t_min, 1),
            "canopy_vpd_kpa": round(vpd, 2),
            "heat_stress_warning": heat_stress,
            "ground_frost_risk": frost_risk,
            "pesticide_spray_window_open": spray_suitable,
            "spray_delta_t_celsius": round(delta_t, 1)
        }

