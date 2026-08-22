/**
 * Main Application Bootstrap and View Controller
 */

function switchTab(tabId) {
    document.querySelectorAll(".tab-content").forEach(el => el.classList.add("hidden"));
    document.querySelectorAll(".nav-tab").forEach(el => el.classList.remove("active"));

    const target = document.getElementById(`tab-content-${tabId}`);
    if (target) target.classList.remove("hidden");

    const navBtn = document.getElementById(`nav-${tabId}`);
    if (navBtn) navBtn.classList.add("active");

    if (tabId === "irrigation") fetchIrrigationStatus();
    if (tabId === "market") fetchMandiPrices();
}

function handleZoneChange(e) {
    selectedZoneId = e.target.value;
}

document.addEventListener("DOMContentLoaded", () => {
    // Start telemetry streaming
    startTelemetryStream();

    // Event Listeners
    const zoneSelect = document.getElementById("zone-selector");
    if (zoneSelect) zoneSelect.addEventListener("change", handleZoneChange);

    const cropForm = document.getElementById("form-crop-rec");
    if (cropForm) cropForm.addEventListener("submit", handleCropRecommendationSubmit);

    const fertForm = document.getElementById("form-fertilizer");
    if (fertForm) fertForm.addEventListener("submit", handleFertilizerSubmit);

    const diseaseForm = document.getElementById("form-disease-diag");
    if (diseaseForm) diseaseForm.addEventListener("submit", handleDiseaseDiagnosisSubmit);

    const langSelect = document.getElementById("language-selector");
    if (langSelect) langSelect.addEventListener("change", (e) => setLanguage(e.target.value));

    // Chat enter trigger
    const chatInput = document.getElementById("chat-input");
    if (chatInput) {
        chatInput.addEventListener("keydown", (e) => {
            if (e.key === "Enter") sendChatMessage();
        });
    }

    // Set initial calculations
    calculateFarmProfit();
});
