# Smart Agriculture Platform (AgriSphere OS) 🌱🚜

An enterprise-grade, full-stack Precision Agriculture & IoT Farm Intelligence Platform designed for high-density IoT telemetry ingestion, satellite remote sensing (NDVI/EVI), AI agronomic decision-support (Crop & Fertilizer recommendation, Disease Vision Diagnosis), precision automated irrigation, and farm ERP with live Mandi market pricing.

---

## 🌟 Key Features & Capabilities

### 1. 📡 IoT Telemetry & Sensor Monitoring
- **Real-Time Environmental & Soil Telemetry**: Ingests continuous readings for Soil Moisture (10cm, 30cm, 60cm depths), Ambient Temperature, Relative Humidity, Soil pH, Nitrogen (N), Phosphorus (P), Potassium (K), Solar Irradiance, and Precipitation.
- **Edge Gateway & Protocols**: Built-in support for Modbus RS-485, LoRaWAN SX1262, MQTT v5, and WebSocket live streams with Kalman filtering for noise reduction.
- **Zone Health Heatmaps**: Multi-depth volumetric water content calculation and Vapor Pressure Deficit (VPD) analysis.

### 2. 🤖 AI / Machine Learning Agronomic Suite
- **Crop Recommendation Engine**: Multi-variate ensemble model evaluating soil nutrients, pH, elevation, and historical climate indices to recommend the most profitable and climate-resilient crops.
- **Precision Fertilizer Advisor**: Calculates precise elemental NPK deficits and converts them into optimized schedules of chemical (Urea, DAP, MOP) and organic amendments.
- **Leaf Disease Computer Vision Doctor**: Multi-crop pathogen diagnosis engine identifying foliar diseases across Tomato, Potato, Corn, Rice, Wheat, Cotton, and Grape, with instant chemical and organic remedy prescriptions.
- **Micro-Climate Yield & Harvest Predictor**: Phenology stage tracking (BBCH scale) and harvest date optimization based on GDD (Growing Degree Days).

### 3. 💧 Precision Automated Irrigation & Water Conservation
- **FAO-56 Penman-Monteith Evapotranspiration ($ET_0$)**: Hourly and daily reference evapotranspiration modeling with dual-crop coefficient ($K_{cb} + K_e$).
- **Smart Irrigation Automation**: Closed-loop PLC solenoid valve triggering based on dynamic soil water depletion thresholds and 48-hour precipitation forecasting.

### 4. 🛰️ GIS & Satellite Remote Sensing
- **Field Parcel Mapping**: PostGIS geospatial boundaries with acreage and elevation profiles.
- **Vegetation Indices**: Automated computation of NDVI (Normalized Difference Vegetation Index), EVI, and NDWI from Copernicus Sentinel-2 satellite imagery.

### 5. 🌾 Farm ERP & Mandi Market Intelligence
- **Commodity Price Trends**: Real-time national APMC Mandi commodity rates, price wave forecasting, and optimal market destination recommendations.
- **Crop Budgeting & P&L**: Input cost ledger, labor tracking, and profit per acre calculator.

### 6. 🌐 Multilingual Agronomist Web Portal & Mobile Interface
- **Interactive UI**: Real-time dials, WebGL time-series charts, disease diagnostic image uploader, and interactive irrigation valve switches.
- **Multilingual Localization**: Native support for **English**, **Hindi (हिन्दी)**, and **Telugu (తెలుగు)**.

---

## 🏗️ Project Architecture

```
Smart-Agriculture-Platform/
├── backend/
│   ├── app/
│   │   ├── main.py                  # FastAPI server & WebSocket streaming hub
│   │   ├── config.py                # System settings & environment configuration
│   │   ├── database.py              # SQLite / PostgreSQL persistence engine
│   │   ├── models/                  # Pydantic schemas & DB models
│   │   │   ├── schemas.py           # Telemetry, advisory, and market schemas
│   │   │   └── orm_models.py        # SQLAlchemy entities
│   │   ├── services/
│   │   │   ├── ml_engine.py         # Crop recommendation & fertilizer calculation
│   │   │   ├── disease_engine.py    # Vision diagnostic & symptom rule engine
│   │   │   ├── irrigation_engine.py # FAO-56 Penman-Monteith ET0 & valve scheduler
│   │   │   ├── iot_simulator.py     # Live multi-zone sensor telemetry generator
│   │   │   ├── market_service.py    # Mandi commodity rates & price forecasting
│   │   │   └── chatbot_service.py   # Multi-lingual Agri-AI consulting assistant
│   │   └── routers/
│   │       ├── telemetry.py         # Sensor endpoints & live streams
│   │       ├── analytics.py         # AI recommendations & vision diagnostics
│   │       ├── irrigation.py        # Pump controls & valve schedules
│   │       ├── market.py            # Mandi rates & economics
│   │       └── assistant.py         # Agri-AI chat endpoints
│   ├── data/                        # Seed data for crops, fertilizers, diseases, and APMCs
│   └── requirements.txt             # Python dependencies
├── edge-gateway/
│   ├── firmware/                    # ESP32 / C++ drivers for NPK RS485 & LoRaWAN
│   └── gateway_daemon/              # Modbus & MQTT edge gateway scripts
├── frontend/
│   ├── index.html                   # Modern agricultural dashboard application
│   ├── css/
│   │   └── styles.css               # Agricultural dashboard theme and styles
│   ├── js/
│   │   ├── app.js                   # Application state & view router
│   │   ├── telemetry.js             # Live Chart.js telemetry visualizers
│   │   ├── irrigation.js            # Pump and valve automation controllers
│   │   ├── advisory.js              # Crop advisor & leaf disease scanner
│   │   ├── market.js                # Mandi trends & economic calculators
│   │   ├── chatbot.js               # Multi-lingual Agri-Bot assistant
│   │   └── i18n.js                  # Localization (English, Hindi, Telugu)
│   └── assets/                      # Icons and UI assets
├── tests/                           # Unit & integration test suites
│   ├── test_ml_models.py
│   ├── test_irrigation.py
│   └── test_api_endpoints.py
├── run_server.py                    # One-click startup script
├── .gitignore                       # Git ignore configuration
└── README.md                        # Documentation
```

---

## 🚀 Quick Start

### 1. Prerequisites
- **Python 3.10+** (Recommended: Python 3.11 or 3.12+)
- **Modern Web Browser** (Chrome, Edge, Firefox, Safari)

### 2. Installation
Clone the repository and install the backend dependencies:

```bash
git clone https://github.com/pittaanji9390-afk/Smart-Agriculture-Platform.git
cd Smart-Agriculture-Platform
pip install -r backend/requirements.txt
```

### 3. Launch the Platform
Start the unified platform (FastAPI Backend + Live IoT Simulator + Web Dashboard):

```bash
python run_server.py
```

Open your browser and navigate to:
```
http://localhost:8000
```

Interactive API documentation is available at:
```
http://localhost:8000/docs
```

---

## 🧪 Running Tests

Execute the automated test suite:

```bash
pytest tests/ -v
```

---

## 📜 License
This project is licensed under the MIT License.
