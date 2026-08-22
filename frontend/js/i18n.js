/**
 * Internationalization (i18n) Module
 * Supports English, Hindi (हिन्दी), and Telugu (తెలుగు)
 */

const TRANSLATIONS = {
    en: {
        app_title: "AgriSphere OS",
        app_subtitle: "Enterprise Precision Agriculture & Farm Intelligence",
        tab_telemetry: "IoT Telemetry",
        tab_irrigation: "Smart Irrigation",
        tab_crop_advisor: "Crop & Fertilizer Advisor",
        tab_disease_doctor: "Leaf Disease Doctor",
        tab_market: "Mandi Market & Economics",
        system_online: "IoT Gateway Online",
        select_zone: "Select Field Zone:",
        soil_moisture: "Soil Moisture",
        soil_temp: "Soil Temperature",
        soil_ph: "Soil pH",
        nutrients_npk: "NPK Nutrients (mg/kg)",
        ambient_temp: "Air Temp",
        humidity: "Humidity",
        solar_radiation: "Solar Radiation",
        vpd: "Vapor Pressure Deficit",
        health_status: "Health Status",
        irrigation_controller: "Smart Automated Irrigation",
        valve_status: "Valve Status",
        valve_open: "VALVE OPEN",
        valve_closed: "VALVE CLOSED",
        auto_mode: "Closed-Loop AUTO Mode",
        manual_override: "Manual Override",
        open_valve: "Start Pump (15 Min)",
        close_valve: "Stop Pump",
        water_applied: "Total Water Applied",
        et0_evapotranspiration: "Reference ET0 Rate",
        crop_recommendation_title: "AI Crop Compatibility Recommender",
        crop_desc: "Enter soil and climate parameters to discover the most profitable and high-yielding crops.",
        btn_recommend: "Run AI Crop Recommendation",
        fertilizer_planner: "Nutrient & Fertilizer Scheduler",
        btn_calc_fertilizer: "Calculate Precise Fertilizer Dosing",
        disease_title: "Leaf Disease Computer Vision Diagnostic",
        upload_leaf: "Upload Leaf Photo",
        or_select_symptoms: "Or Select Observed Symptoms",
        diagnose_btn: "Diagnose Plant Health",
        mandi_title: "Live APMC Mandi Market Prices",
        commodity: "Commodity",
        market_name: "Market / APMC",
        modal_price: "Modal Price (₹/Qtl)",
        price_trend: "Trend",
        ask_assistant: "Agri-AI Assistant",
        chat_placeholder: "Ask about crops, diseases, fertilizers, or water...",
        send_btn: "Send"
    },
    hi: {
        app_title: "एग्रीस्फेयर (AgriSphere)",
        app_subtitle: "स्मार्ट कृषि और फार्म इंटेलिजेंस प्लेटफॉर्म",
        tab_telemetry: "सेंसर टेलीमेट्री",
        tab_irrigation: "स्मार्ट सिंचाई",
        tab_crop_advisor: "फसल व खाद सलाहकार",
        tab_disease_doctor: "पत्ती रोग डॉक्टर",
        tab_market: "मंडी भाव और आय",
        system_online: "गेटवे ऑनलाइन",
        select_zone: "खेत क्षेत्र चुनें:",
        soil_moisture: "मिट्टी की नमी",
        soil_temp: "मिट्टी का तापमान",
        soil_ph: "मिट्टी का पीएच",
        nutrients_npk: "एनपीके पोषक तत्व",
        ambient_temp: "हवा का तापमान",
        humidity: "आर्द्रता (नमी)",
        solar_radiation: "सौर विकिरण",
        vpd: "वाष्प दबाव घाटा (VPD)",
        health_status: "फसल स्थिति",
        irrigation_controller: "स्वचालित स्मार्ट सिंचाई",
        valve_status: "वाल्व स्थिति",
        valve_open: "वाल्व खुला है",
        valve_closed: "वाल्व बंद है",
        auto_mode: "ऑटो मोड",
        manual_override: "मैनुअल नियंत्रण",
        open_valve: "पंप चालू करें (15 मिनट)",
        close_valve: "पंप बंद करें",
        water_applied: "कुल प्रयुक्त जल",
        et0_evapotranspiration: "वाष्पीकरण दर (ET0)",
        crop_recommendation_title: "एआई फसल सिफारिश प्रणाली",
        crop_desc: "मिट्टी व मौसम विवरण दर्ज करें और सर्वोत्तम फसल की सिफारिश प्राप्त करें।",
        btn_recommend: "फसल की सिफारिश देखें",
        fertilizer_planner: "सटीक खाद अनुसूची कैलकुलेटर",
        btn_calc_fertilizer: "खाद की मात्रा की गणना करें",
        disease_title: "पौधे के रोग की जांच (कंप्यूटर विजन)",
        upload_leaf: "पत्ती की फोटो अपलोड करें",
        or_select_symptoms: "या देखे गए लक्षण चुनें",
        diagnose_btn: "रोग का निदान करें",
        mandi_title: "लाइव कृषि उपज मंडी भाव",
        commodity: "फसल / जींस",
        market_name: "मंडी का नाम",
        modal_price: "मॉडल भाव (₹/क्विंटल)",
        price_trend: "रुझान",
        ask_assistant: "कृषि-एआई सहायक",
        chat_placeholder: "फसल, खाद, सिंचाई या बीमारी के बारे में पूछें...",
        send_btn: "भेजें"
    },
    te: {
        app_title: "అగ్రిస్ఫియర్ (AgriSphere)",
        app_subtitle: "స్మార్ట్ వ్యవసాయ మరియు క్షేత్ర నిర్వహణ వేదిక",
        tab_telemetry: "సెన్సార్ టెలిమెట్రీ",
        tab_irrigation: "స్మార్ట్ నీటిపారుదల",
        tab_crop_advisor: "పంట & ఎరువుల సలహాదారు",
        tab_disease_doctor: "ఆకు తెగుళ్ల నివారణ",
        tab_market: "మార్కెట్ ధరలు & లాభాలు",
        system_online: "సిస్టమ్ ఆన్‌లైన్",
        select_zone: "పొలం జోన్ ఎంచుకోండి:",
        soil_moisture: "నేల తేమ శాతం",
        soil_temp: "నేల ఉష్ణోగ్రత",
        soil_ph: "నేల pH విలువ",
        nutrients_npk: "NPK పోషకాలు (mg/kg)",
        ambient_temp: "వాతావరణ ఉష్ణోగ్రత",
        humidity: "గాలిలో తేమ",
        solar_radiation: "సూర్యరశ్మి తీవ్రత",
        vpd: "బాష్పీభవన లోటు (VPD)",
        health_status: "పంట ఆరోగ్యం",
        irrigation_controller: "ఆటోమేటిక్ స్మార్ట్ నీటిపారుదల",
        valve_status: "వాల్వ్ స్థితి",
        valve_open: "వాల్వ్ తెరిచి ఉంది",
        valve_closed: "వాల్వ్ మూసి ఉంది",
        auto_mode: "ఆటోమేటిక్ మోడ్",
        manual_override: "మాన్యువల్ నియంత్రణ",
        open_valve: "పంప్ ప్రారంభించు (15 నిమి)",
        close_valve: "పంప్ ఆపు",
        water_applied: "వాడిన మొత్తం నీరు",
        et0_evapotranspiration: "బాష్పోత్సేకం రేటు (ET0)",
        crop_recommendation_title: "AI పంట సిఫార్సు విధానం",
        crop_desc: "నేల మరియు వాతావరణ వివరాలను నమోదు చేసి అనువైన పంటలను తెలుసుకోండి.",
        btn_recommend: "పంట సిఫార్సును పొందండి",
        fertilizer_planner: "ఎరువుల మోతాదు ప్రణాళిక",
        btn_calc_fertilizer: "ఎరువుల పరిమాణాన్ని లెక్కించు",
        disease_title: "ఆకు తెగుళ్ల నిర్ధారణ (AI విజన్)",
        upload_leaf: "ఆకు ఫోటో అప్‌లోడ్ చేయండి",
        or_select_symptoms: "లేదా కనిపించిన లక్షణాలను ఎంచుకోండి",
        diagnose_btn: "తెగులును గుర్తించు",
        mandi_title: "లైవ్ వ్యవసాయ మార్కెట్ ధరలు",
        commodity: "పంట / సరుకు",
        market_name: "మార్కెట్ పేరు",
        modal_price: "ధర (₹/క్వింటాలు)",
        price_trend: "ధర సరళి",
        ask_assistant: "వ్యవసాయ AI సహాయకుడు",
        chat_placeholder: "పంటలు, ఎరువులు, నీటిపారుదల గురించి అడగండి...",
        send_btn: "పంపు"
    }
};

let currentLang = "en";

function setLanguage(lang) {
    if (!TRANSLATIONS[lang]) return;
    currentLang = lang;
    document.querySelectorAll("[data-i18n]").forEach(el => {
        const key = el.getAttribute("data-i18n");
        if (TRANSLATIONS[lang][key]) {
            el.textContent = TRANSLATIONS[lang][key];
        }
    });
    
    document.querySelectorAll("[data-i18n-placeholder]").forEach(el => {
        const key = el.getAttribute("data-i18n-placeholder");
        if (TRANSLATIONS[lang][key]) {
            el.placeholder = TRANSLATIONS[lang][key];
        }
    });
}
