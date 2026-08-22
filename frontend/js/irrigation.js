/**
 * Precision Irrigation Controller Module
 */

async function fetchIrrigationStatus() {
    try {
        const res = await fetch("/api/irrigation/status");
        const zones = await res.json();
        renderIrrigationCards(zones);
    } catch (err) {
        console.error("Failed to load irrigation status", err);
    }
}

function renderIrrigationCards(zones) {
    const container = document.getElementById("irrigation-zones-container");
    if (!container) return;

    container.innerHTML = "";
    zones.forEach(z => {
        const isValveOpen = z.valve_open;
        const card = document.createElement("div");
        card.className = "glass-card p-5 relative overflow-hidden flex flex-col justify-between";
        
        card.innerHTML = `
            <div>
                <div class="flex items-center justify-between mb-3">
                    <span class="text-xs font-semibold px-2 py-0.5 rounded bg-slate-700 text-emerald-400">${z.zone_id}</span>
                    <span class="px-2.5 py-1 text-xs font-bold rounded-full ${isValveOpen ? 'bg-blue-500/20 text-blue-400 border border-blue-500/40 animate-pulse' : 'bg-slate-700 text-slate-400'}">
                        ${isValveOpen ? '💧 IRRIGATING' : 'IDLE'}
                    </span>
                </div>
                <h4 class="font-bold text-slate-100 text-base mb-1">${z.zone_name}</h4>
                <p class="text-xs text-slate-400 mb-4">Mode: <span class="text-emerald-400 font-semibold">${z.mode}</span> | Next: ${z.next_scheduled_run}</p>
                
                <div class="space-y-2 text-xs mb-5">
                    <div class="flex justify-between text-slate-300">
                        <span>Current Moisture:</span>
                        <span class="font-semibold ${z.current_moisture_pct < z.moisture_threshold_pct ? 'text-red-400' : 'text-emerald-400'}">${z.current_moisture_pct}%</span>
                    </div>
                    <div class="flex justify-between text-slate-300">
                        <span>Auto-Trigger Threshold:</span>
                        <span class="font-semibold text-slate-200">${z.moisture_threshold_pct}%</span>
                    </div>
                    <div class="flex justify-between text-slate-300">
                        <span>Total Water Applied:</span>
                        <span class="font-semibold text-blue-400">${z.water_applied_liters.toLocaleString()} Liters</span>
                    </div>
                    <div class="flex justify-between text-slate-300">
                        <span>Reference ET0 Rate:</span>
                        <span class="font-semibold text-amber-400">${z.et0_rate_mm_day} mm/day</span>
                    </div>
                </div>
            </div>

            <div class="flex gap-2">
                ${isValveOpen 
                    ? `<button onclick="sendIrrigationAction('${z.zone_id}', 'STOP')" class="flex-1 py-2 px-3 bg-red-600/80 hover:bg-red-600 text-white rounded-lg text-xs font-semibold transition">Stop Pump</button>`
                    : `<button onclick="sendIrrigationAction('${z.zone_id}', 'START', 15)" class="flex-1 py-2 px-3 bg-emerald-600 hover:bg-emerald-500 text-white rounded-lg text-xs font-semibold transition">Start Pump (15m)</button>`
                }
                <button onclick="sendIrrigationAction('${z.zone_id}', 'AUTO_SCHEDULE')" class="py-2 px-3 bg-slate-700 hover:bg-slate-600 text-slate-200 rounded-lg text-xs font-semibold transition">Auto</button>
            </div>
        `;
        container.appendChild(card);
    });
}

async function sendIrrigationAction(zoneId, action, duration = 15) {
    try {
        const res = await fetch("/api/irrigation/control", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                zone_id: zoneId,
                action: action,
                duration_minutes: duration
            })
        });
        const result = await res.json();
        fetchIrrigationStatus();
    } catch (err) {
        console.error("Irrigation action error:", err);
    }
}
