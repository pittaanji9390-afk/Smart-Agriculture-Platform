# Changelog

All notable changes to the **AgriSphere OS (Smart Agriculture Platform)** project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [2.5.0] - 2026-08-25

### Added
- **IPCC Tier-2 Carbon Sequestration Accounting**: Added models for soil organic carbon (SOC) stock changes, biochar persistence, and verifiable carbon credit ($tCO_2e$) monetization.
- **National Crop Varietal Gene Bank Registry**: Genomic accession records with QTL markers for submergence (*Sub1A*), heat stress (*TaHsfA2d*), and rust resistance (*Yr17*, *Lr37*, *Sr38*).
- **Farm Machinery CAN-Bus / ISOBUS Telematics**: Fuel consumption per hectare optimizer, implement load dynamics, and 250-hour service cycle health tracking.
- **Micro-Climate Numerical Weather Downscaler**: Adiabatic lapse rate downscaling, intra-canopy thermal buffering, frost risk detection, and Delta-T ($\Delta T$) spray window indicators.
- **Continuous Integration Pipeline**: Added `.github/workflows/ci.yml` supporting multi-version Python testing, code coverage artifact uploads, linting (Ruff, Flake8, Black), type checking (Mypy), and dependency security scanning (`pip-audit`).
- **Containerization Support**: Added production multi-stage `Dockerfile` and `docker-compose.yml` orchestrating FastAPI with Redis.
- **Supply Chain Management**: Pinned root `requirements.lock`, root `pyproject.toml`, `package.json`, and Dependabot configuration.

---

## [2.0.0] - 2026-08-22

### Added
- **National Agronomic Registries**: Comprehensive 750+ district soil profiles, 250+ crop dossiers, and 200+ plant pathology compendiums.
- **GIS Remote Sensing & Spatial Matrix Suite**: 25+ multispectral vegetation indices (NDVI, NDRE, EVI, SAVI, GNDVI, NDWI, MSI), IDW spatial heatmap interpolation, and PostGIS boundary validation.
- **Precision Irrigation Engine**: Full FAO-56 Penman-Monteith dual-crop coefficient ($K_{cb} + K_e$) water balance and A/B tank fertigation recipe optimizer.
- **APMC Mandi Intelligence**: 300+ terminal market registry with historical MSP time-series, modal price distributions, and price volatility analytics.
- **Offline-First Mobile Scout Platform**: React Native on-device camera leaf vision scanner, WatermelonDB offline schema, and GPS geofencing.

---

## [1.1.0] - 2026-08-22

### Added
- **Embedded C++ Hardware Suite**: Drivers for Modbus RS-485 7-in-1 NPK probes, SHT30 air temperature/humidity, SDI-12 protocol, and CayenneLPP byte serializers.
- **Edge Gateway Daemon**: Local SQLite store-and-forward queue, 1D Kalman noise filtering, and Modbus TCP/MQTT v5 adapters.
- **Multilingual Support**: Added complete localization dictionary for English, Hindi (हिन्दी), and Telugu (తెలుగు).

---

## [1.0.0] - 2026-08-22

### Added
- Initial project architecture and repository setup.
- FastAPI REST backend with WebSocket live telemetry streaming on `/api/telemetry/ws`.
- Core ML models for crop recommendation, fertilizer calculation, and leaf disease diagnosis.
- Interactive Single Page Application (SPA) dashboard with real-time Chart.js charts.
