# 🏗️ AgriSphere OS - System Architecture & Engineering Specifications

This document provides a comprehensive technical blueprint of the **AgriSphere OS (Smart Agriculture Platform)** architecture, telemetry pipelines, agronomic AI engines, and infrastructure topology.

---

## 🌐 1. High-Level System Architecture

```mermaid
graph TB
    subgraph Edge Layer [📡 IoT Edge Gateway & Sensor Field Nodes]
        Modbus["RS-485 Modbus 7-in-1 NPK Sensors"]
        SDI12["SDI-12 Soil Moisture & Temp Probes"]
        SHT30["SHT30 Air Temp & Humidity"]
        ADC420["4-20mA Current Loop Transducers"]
        LoRa["LoRaWAN / ESP32 Field Nodes"]
        EdgeDaemon["Edge Gateway Daemon\n(Kalman Filter + SQLite Store-and-Forward)"]
        
        Modbus --> EdgeDaemon
        SDI12 --> EdgeDaemon
        SHT30 --> EdgeDaemon
        ADC420 --> EdgeDaemon
        LoRa --> EdgeDaemon
    end

    subgraph Ingestion & Backend Layer [⚙️ FastAPI Application Core]
        WS["WebSocket Telemetry Streamer\n(/api/telemetry/ws)"]
        REST["REST API Endpoints\n(/api/analytics, /api/irrigation, /api/market)"]
        Metrics["Prometheus Exporter & Health Probes\n(/metrics, /health, /ready)"]
        Log["Structured JSON Logger & Sentry SDK"]
        
        EdgeDaemon -->|MQTT v5 / WebSocket| WS
        EdgeDaemon -->|HTTP POST JSON| REST
    end

    subgraph Agronomic & AI Computation Engines [🌾 Intelligence Subsystems]
        FAO56["FAO-56 Dual-Crop Penman-Monteith\nIrrigation Engine"]
        SoilDB["National District Soil DB\n(750+ Districts)"]
        Pathology["Plant Pathology & IPM Database\n(200+ Pathogens)"]
        GeneBank["Varietal Gene Bank Registry\n(250+ Cultivars & QTLs)"]
        Carbon["IPCC Tier-2 Carbon Accounting\n(SOC & tCO2e Credits)"]
        GIS["Multispectral Remote Sensing\n(25+ Indices: NDVI/EVI/SAVI/IDW)"]
        Telematics["ISOBUS CAN-Bus Fleet Telematics\n(Fuel & Engine Lifecycle)"]
        
        REST <--> FAO56
        REST <--> SoilDB
        REST <--> Pathology
        REST <--> GeneBank
        REST <--> Carbon
        REST <--> GIS
        REST <--> Telematics
    end

    subgraph Client Presentation Layer [💻 User Interfaces]
        WebPortal["Interactive SPA Web Dashboard\n(Chart.js + Tailwind + i18n Trilingual)"]
        MobileApp["Offline-First Mobile Scout\n(React Native + WatermelonDB + GPS)"]
        
        WS --> WebPortal
        REST <--> WebPortal
        REST <--> MobileApp
    end
```

---

## 📡 2. End-to-End Telemetry Pipeline

1. **Sensor Interfacing**: RS-485 Modbus RTU, SDI-12 v1.4, and 4-20mA current loop sensors sample field parameters every 2.5 seconds.
2. **Noise Reduction & Anomaly Detection**: 1D Kalman filters smooth analog sensor jitter while variance threshold algorithms detect frozen or drifting probe signals.
3. **Edge Resilience**: If WAN connectivity is interrupted, the edge buffer preserves telemetry packets in local SQLite storage and bursts data upstream once reconnecting.
4. **Real-Time Distribution**: The FastAPI backend broadcasts multi-zone sensor streams via asynchronous WebSockets to connected dashboards in sub-50ms latency.

---

## 💧 3. Precision Irrigation Water Balance Math

The irrigation controller computes root zone depletion ($D_{r,i}$) on a daily time-step:

$$D_{r,i} = D_{r,i-1} - (P_i - RO_i) - I_i - CR_i + ET_{c,i} + DP_i$$

Where:
- $ET_{c,i} = (K_{cb} + K_e) \cdot ET_0$
- $ET_0$: FAO-56 Reference Evapotranspiration computed via Penman-Monteith energy balance equation.
- $K_{cb}$: Basal crop coefficient.
- $K_e$: Soil evaporation coefficient.
- Soil Water Stress Coefficient: $K_s = \frac{TAW - D_r}{(1 - p) \cdot TAW}$.

---

## 📊 4. Observability, Logging & Health Probes

| Endpoint | Protocol | Purpose | Expected Output |
| :--- | :---: | :--- | :--- |
| `/health` | HTTP GET | Liveness probe for Kubernetes / Docker | `{"status": "healthy", "timestamp": ...}` |
| `/ready` | HTTP GET | Readiness probe for traffic routing | `{"status": "ready", "database": "ready"}` |
| `/metrics` | HTTP GET | Prometheus scraper endpoint | Prometheus text format with request counts & latency |
| `/api/telemetry/ws` | WebSocket | Real-time sensor streaming | JSON Telemetry Packets |
