/**
 * AI Crop & Fertilizer Advisory Studio & Leaf Disease Doctor
 */

async function handleCropRecommendationSubmit(e) {
    e.preventDefault();
    const btn = document.getElementById("btn-run-crop-rec");
    btn.textContent = "Analyzing Soil & Climate...";
    btn.disabled = true;

    const payload = {
        nitrogen: parseFloat(document.getElementById("input-rec-n").value),
        phosphorus: parseFloat(document.getElementById("input-rec-p").value),
        potassium: parseFloat(document.getElementById("input-rec-k").value),
        temperature: parseFloat(document.getElementById("input-rec-temp").value),
        humidity: parseFloat(document.getElementById("input-rec-hum").value),
        ph: parseFloat(document.getElementById("input-rec-ph").value),
        rainfall: parseFloat(document.getElementById("input-rec-rain").value)
    };

    try {
        const res = await fetch("/api/analytics/crop-recommendation", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });
        const data = await res.json();
        renderCropResults(data);
    } catch (err) {
        console.error("Crop recommendation failed", err);
    } finally {
        btn.textContent = "Run AI Crop Recommendation";
        btn.disabled = false;
    }
}

function renderCropResults(data) {
    const container = document.getElementById("crop-results-container");
    container.classList.remove("hidden");
    
    document.getElementById("fertility-score").textContent = `${data.soil_fertility_index} / 100`;
    document.getElementById("fertility-grade").textContent = data.soil_health_grade;
    document.getElementById("limiting-nutrients").textContent = data.limiting_nutrients.join(", ");

    const list = document.getElementById("crop-matches-list");
    list.innerHTML = "";

    data.recommended_crops.forEach((c, idx) => {
        const card = document.createElement("div");
        card.className = "p-4 bg-slate-800/80 border border-slate-700 rounded-xl flex flex-col justify-between";
        card.innerHTML = `
            <div>
                <div class="flex items-center justify-between mb-2">
                    <span class="text-lg font-bold text-emerald-400">#${idx + 1} ${c.crop}</span>
                    <span class="px-2.5 py-1 text-xs font-bold rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/40">
                        ${c.confidence_score}% Match
                    </span>
                </div>
                <p class="text-xs text-slate-300 mb-3">${c.description}</p>
                <div class="grid grid-cols-2 gap-2 text-xs text-slate-400 mb-3 bg-slate-900/50 p-2.5 rounded-lg">
                    <div>⏱️ Duration: <span class="text-slate-200 font-semibold">${c.growing_duration_days} Days</span></div>
                    <div>🌾 Exp Yield: <span class="text-slate-200 font-semibold">${c.estimated_yield_per_acre_kg} kg/acre</span></div>
                    <div>🌡️ Temp: <span class="text-slate-200">${c.ideal_conditions.optimum_temp}</span></div>
                    <div>🧪 NPK: <span class="text-slate-200">${c.ideal_conditions.ideal_n_p_k}</span></div>
                </div>
                <div class="text-xs text-amber-300/90 bg-amber-950/30 border border-amber-800/40 p-2 rounded">
                    <strong>Fertilizer Strategy:</strong> ${c.fertilizer_guideline}
                </div>
            </div>
            <button onclick="prefillFertilizerPlanner('${c.crop}')" class="mt-3 w-full py-1.5 bg-slate-700 hover:bg-emerald-600 text-xs font-semibold rounded transition text-slate-200 hover:text-white">
                Generate Fertilizer Schedule →
            </button>
        `;
        list.appendChild(card);
    });
}

function prefillFertilizerPlanner(cropName) {
    document.getElementById("fert-crop-select").value = cropName;
    document.getElementById("fertilizer-section").scrollIntoView({ behavior: 'smooth' });
}

async function handleFertilizerSubmit(e) {
    e.preventDefault();
    const payload = {
        crop_name: document.getElementById("fert-crop-select").value,
        field_area_acres: parseFloat(document.getElementById("fert-acres").value),
        current_n: parseFloat(document.getElementById("fert-curr-n").value),
        current_p: parseFloat(document.getElementById("fert-curr-p").value),
        current_k: parseFloat(document.getElementById("fert-curr-k").value)
    };

    try {
        const res = await fetch("/api/analytics/fertilizer-plan", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });
        const data = await res.json();
        renderFertilizerResults(data);
    } catch (err) {
        console.error("Fertilizer calculation failed", err);
    }
}

function renderFertilizerResults(data) {
    const container = document.getElementById("fertilizer-results-container");
    container.classList.remove("hidden");

    document.getElementById("total-urea").textContent = `${data.total_urea_needed_kg} kg`;
    document.getElementById("total-dap").textContent = `${data.total_dap_needed_kg} kg`;
    document.getElementById("total-mop").textContent = `${data.total_mop_needed_kg} kg`;
    document.getElementById("total-fym").textContent = `${data.total_organic_manure_kg} kg`;

    const tableBody = document.getElementById("fert-schedule-table");
    tableBody.innerHTML = "";

    data.application_schedule.forEach(s => {
        const row = document.createElement("tr");
        row.className = "border-b border-slate-800 text-xs";
        row.innerHTML = `
            <td class="py-3 px-2 font-semibold text-slate-200">${s.stage_name} <br><span class="text-slate-400 font-normal">Day ${s.days_after_sowing}</span></td>
            <td class="py-3 px-2 text-emerald-400 font-bold">${s.urea_kg} kg</td>
            <td class="py-3 px-2 text-blue-400 font-bold">${s.dap_kg} kg</td>
            <td class="py-3 px-2 text-amber-400 font-bold">${s.mop_kg} kg</td>
            <td class="py-3 px-2 text-slate-300">${s.instructions}</td>
        `;
        tableBody.appendChild(row);
    });
}

// Leaf Disease Diagnosis
async function handleDiseaseDiagnosisSubmit(e) {
    e.preventDefault();
    const symptoms = [];
    document.querySelectorAll(".symptom-check:checked").forEach(cb => symptoms.push(cb.value));

    const payload = {
        crop_name: document.getElementById("disease-crop").value,
        symptoms_observed: symptoms.length > 0 ? symptoms : ["brown spots", "yellow halo"],
        affected_parts: ["Leaves", "Stem"]
    };

    try {
        const res = await fetch("/api/analytics/disease-diagnosis", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });
        const data = await res.json();
        renderDiseaseResults(data);
    } catch (err) {
        console.error("Disease diagnosis failed", err);
    }
}

async function handleLeafUpload(input) {
    if (!input.files || !input.files[0]) return;
    const file = input.files[0];

    const formData = new FormData();
    formData.append("file", file);
    formData.append("crop_hint", document.getElementById("disease-crop").value);

    try {
        const res = await fetch("/api/analytics/scan-leaf", {
            method: "POST",
            body: formData
        });
        const data = await res.json();
        renderDiseaseResults(data);
    } catch (err) {
        console.error("Leaf photo diagnosis error:", err);
    }
}

function renderDiseaseResults(data) {
    const container = document.getElementById("disease-results-container");
    container.classList.remove("hidden");

    document.getElementById("disease-name").textContent = data.disease_name;
    document.getElementById("disease-causal").textContent = data.causal_agent;
    document.getElementById("disease-confidence").textContent = `${data.confidence_pct}% Confidence`;
    document.getElementById("disease-summary").textContent = data.symptom_summary;

    const chemList = document.getElementById("disease-chem-treatments");
    chemList.innerHTML = "";
    data.chemical_treatments.forEach(c => {
        const item = document.createElement("li");
        item.className = "text-xs text-slate-300 mb-2";
        item.innerHTML = `<strong>${c.name}:</strong> ${c.dosage} (${c.timing})`;
        chemList.appendChild(item);
    });

    const orgList = document.getElementById("disease-organic-remedies");
    orgList.innerHTML = "";
    data.organic_remedies.forEach(o => {
        const item = document.createElement("li");
        item.className = "text-xs text-slate-300 mb-1";
        item.textContent = `🌿 ${o}`;
        orgList.appendChild(item);
    });
}
