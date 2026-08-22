"""
Database Models for SQLite / PostgreSQL
"""

from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class DBTelemetryLog(Base):
    __tablename__ = "telemetry_logs"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    zone_id = Column(String(50), index=True)
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)
    soil_moisture_10cm = Column(Float)
    soil_moisture_30cm = Column(Float)
    soil_moisture_60cm = Column(Float)
    soil_temperature = Column(Float)
    soil_ph = Column(Float)
    nitrogen_ppm = Column(Float)
    phosphorus_ppm = Column(Float)
    potassium_ppm = Column(Float)
    ambient_temperature = Column(Float)
    relative_humidity = Column(Float)
    solar_radiation_w_m2 = Column(Float)
    precipitation_mm = Column(Float)
    vpd_kpa = Column(Float)
    battery_level_pct = Column(Float)

class DBIrrigationLog(Base):
    __tablename__ = "irrigation_events"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    zone_id = Column(String(50), index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    action = Column(String(50))
    duration_minutes = Column(Integer)
    water_liters = Column(Float)
    trigger_reason = Column(String(200))

class DBCropCycle(Base):
    __tablename__ = "crop_cycles"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    zone_id = Column(String(50), unique=True)
    crop_name = Column(String(100))
    variety = Column(String(100))
    sowing_date = Column(DateTime)
    stage = Column(String(50))
    target_yield_kg = Column(Float)
