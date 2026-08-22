/**
 * IoT Sensor Telemetry & Real-Time Charting Module
 */

let selectedZoneId = "ZONE-01";
let telemetryHistory = {
    labels: [],
    moisture: [],
    temp: [],
    humidity: []
};

let telemetryChart = null;

function initTelemetryChart() {
    const ctx = document.getElementById("telemetryChart");
    if (!ctx) return;

    telemetryChart = new Chart(ctx, {
        type: "line",
        data: {
            labels: telemetryHistory.labels,
            datasets: [
                {
                    label: "Soil Moisture 10cm (%)",
                    data: telemetryHistory.moisture,
                    borderColor: "#10b981",
                    backgroundColor: "rgba(16, 185, 129, 0.1)",
                    fill: true,
                    tension: 0.4,
                    borderWidth: 2
                },
                {
                    label: "Ambient Temp (°C)",
                    data: telemetryHistory.temp,
                    borderColor: "#f59e0b",
                    backgroundColor: "transparent",
                    tension: 0.4,
                    borderWidth: 2
                },
                {
                    label: "Humidity (%)",
                    data: telemetryHistory.humidity,
                    borderColor: "#3b82f6",
                    backgroundColor: "transparent",
                    tension: 0.4,
                    borderWidth: 2
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            animation: { duration: 400 },
            scales: {
                x: {
                    grid: { color: "rgba(255, 255, 255, 0.05)" },
                    ticks: { color: "#94a3b8" }
                },
                y: {
                    grid: { color: "rgba(255, 255, 255, 0.05)" },
                    ticks: { color: "#94a3b8" }
                }
            },
            plugins: {
                legend: { labels: { color: "#cbd5e1" } }
            }
        }
    });
}

function updateTelemetryUI(reading) {
    if (!reading) return;

    document.getElementById("val-moisture-10").textContent = `${reading.soil_moisture_10cm}%`;
    document.getElementById("val-moisture-30").textContent = `${reading.soil_moisture_30cm}%`;
    document.getElementById("val-soil-temp").textContent = `${reading.soil_temperature}°C`;
    document.getElementById("val-soil-ph").textContent = reading.soil_ph;
    document.getElementById("val-npk").textContent = `${reading.nitrogen_ppm} / ${reading.phosphorus_ppm} / ${reading.potassium_ppm}`;
    document.getElementById("val-air-temp").textContent = `${reading.ambient_temperature}°C`;
    document.getElementById("val-humidity").textContent = `${reading.relative_humidity}%`;
    document.getElementById("val-solar").textContent = `${reading.solar_radiation_w_m2} W/m²`;
    document.getElementById("val-vpd").textContent = `${reading.vpd_kpa} kPa`;
    
    const healthBadge = document.getElementById("badge-health");
    healthBadge.textContent = reading.health_status;
    if (reading.health_status.includes("OPTIMAL")) {
        healthBadge.className = "px-3 py-1 text-xs font-semibold rounded-full bg-emerald-500/20 text-emerald-400 border border-emerald-500/40";
    } else if (reading.health_status.includes("WARNING") || reading.health_status.includes("STRESS")) {
        healthBadge.className = "px-3 py-1 text-xs font-semibold rounded-full bg-amber-500/20 text-amber-400 border border-amber-500/40";
    } else {
        healthBadge.className = "px-3 py-1 text-xs font-semibold rounded-full bg-red-500/20 text-red-400 border border-red-500/40";
    }

    // Update Chart
    const timeStr = new Date(reading.timestamp).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' });
    telemetryHistory.labels.push(timeStr);
    telemetryHistory.moisture.push(reading.soil_moisture_10cm);
    telemetryHistory.temp.push(reading.ambient_temperature);
    telemetryHistory.humidity.push(reading.relative_humidity);

    if (telemetryHistory.labels.length > 15) {
        telemetryHistory.labels.shift();
        telemetryHistory.moisture.shift();
        telemetryHistory.temp.shift();
        telemetryHistory.humidity.shift();
    }

    if (telemetryChart) {
        telemetryChart.update();
    }
}

function startTelemetryStream() {
    initTelemetryChart();
    
    // Connect WebSocket
    const protocol = window.location.protocol === "https:" ? "wss:" : "ws:";
    const wsUrl = `${protocol}//${window.location.host}/api/telemetry/ws`;
    
    let ws = null;
    try {
        ws = new WebSocket(wsUrl);
        ws.onmessage = (event) => {
            const data = JSON.parse(event.data);
            const activeReading = data.zones.find(z => z.zone_id === selectedZoneId) || data.zones[0];
            updateTelemetryUI(activeReading);
        };
        ws.onerror = () => { fallbackPolling(); };
    } catch (e) {
        fallbackPolling();
    }
}

function fallbackPolling() {
    setInterval(async () => {
        try {
            const res = await fetch("/api/telemetry/current");
            const data = await res.json();
            const activeReading = data.zones.find(z => z.zone_id === selectedZoneId) || data.zones[0];
            updateTelemetryUI(activeReading);
        } catch (err) {
            console.error("Telemetry fetch error:", err);
        }
    }, 2500);
}
