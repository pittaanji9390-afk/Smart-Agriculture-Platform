"""
Multilingual Agri-AI Advisory Assistant
Provides contextual agronomic advice in English, Hindi (हिन्दी), and Telugu (తెలుగు).
"""

from typing import List, Dict, Any
from backend.app.models.schemas import ChatRequest, ChatResponse

AGRI_RESPONSES = {
    "en": {
        "greeting": "Hello! I am AgriSphere AI, your intelligent farming assistant. How can I assist you today with crops, pest management, soil nutrients, or irrigation?",
        "fertilizer": "For balanced nutrition, apply fertilizers based on soil test values. A general NPK ratio for cereals is 4:2:1, while legumes benefit from high phosphorus (1:2:1). Split your Nitrogen applications to avoid leaching!",
        "irrigation": "Smart irrigation is activated. Maintaining soil moisture between 40% to 65% ensures optimal root aeration and prevents blossom-end rot or fungal root rots. Water in the early morning to minimize evaporation.",
        "pest": "For foliar pests like aphids or whiteflies, use yellow sticky traps and spray Neem Oil (5ml/L). If fungal spots appear, apply Mancozeb or Trichoderma viride bio-fungicide immediately.",
        "weather": "Current weather is optimal for vegetative growth. Keep a check on high humidity levels (>80%) which may accelerate fungal blast or blight development.",
        "default": "Thank you for reaching out! To get the most accurate advice, you can use our AI Crop Recommendation Studio, upload a leaf photo for Disease Diagnosis, or check live Mandi prices on the dashboard."
    },
    "hi": {
        "greeting": "नमस्ते! मैं एग्रीस्फेयर एआई (AgriSphere AI) हूँ, आपका कृषि सलाहकार। मैं आज आपकी फसल, कीट नियंत्रण, मृदा पोषण या सिंचाई में कैसे सहायता कर सकता हूँ?",
        "fertilizer": "संतुलित पोषण के लिए मिट्टी की जांच के अनुसार खाद डालें। अनाज की फसलों के लिए 4:2:1 NPK अनुपात और दलहनी फसलों के लिए फास्फोरस युक्त खाद (1:2:1) उपयुक्त है। यूरिया को 2-3 किश्तों में दें।",
        "irrigation": "स्मार्ट सिंचाई प्रणाली चालू है। मिट्टी में 40% से 65% नमी बनाए रखना फसल की जड़ों के लिए सर्वोत्तम है। वाष्पीकरण कम करने के लिए सुबह या शाम को पानी दें।",
        "pest": "सफेद मक्खी या कीटों के लिए पीले चिपचिपे ट्रैप लगाएं और नीम का तेल (5 मिली/लीटर) छिड़कें। यदि फफूंद के धब्बे दिखें तो तुरंत मैंकोजेब (Mancozeb) का छिड़काव करें।",
        "weather": "वर्तमान मौसम फसलों की वृद्धि के लिए अनुकूल है। अधिक नमी (>80%) होने पर फफूंद जनित रोगों से बचाव के लिए सतर्क रहें।",
        "default": "धन्यवाद! अधिक सटीक जानकारी के लिए आप हमारे 'फसल सिफारिश', 'पत्ती रोग जांच', या 'लाइव मंडी भाव' मॉड्यूल का उपयोग कर सकते हैं।"
    },
    "te": {
        "greeting": "నమస్కారం! నేను అగ్రిస్ఫియర్ AI (AgriSphere AI), మీ వ్యవసాయ సలహాదారుని. పంటలు, ఎరువులు, తెగుళ్ల నివారణ లేదా నీటిపారుదల గురించి మీకు ఎలాంటి సహాయం కావాలి?",
        "fertilizer": "నేల పరీక్ష ఆధారంగా ఎరువులు వాడటం ఉత్తమం. వరి, మొక్కజొన్న వంటి పంటలకు 4:2:1 NPK నిష్పత్తిని వాడండి. నత్రజని (యూరియా) ఎరువును ఒకేసారి వేయకుండా 2-3 దఫాలుగా వేయండి.",
        "irrigation": "స్మార్ట్ నీటిపారుదల వ్యవస్థ ద్వారా తేమ 40%-65% ఉండేలా చూడండి. ఉదయం లేదా సాయంత్రం వేళల్లో డ్రిప్ ద్వారా నీరు అందించడం వల్ల నీరు ఆదా అవుతుంది.",
        "pest": "తెల్లదోమ లేదా పేనుబంక నివారణకు పసుపు రంగు జిగురు బోర్డులను అమర్చండి మరియు వేప నూనె (5ml/లీటరు) పిచికారీ చేయండి. ఆకులపై మచ్చలు వస్తే మాంకోజెబ్ మందును వాడండి.",
        "weather": "వాతావరణం పంట పెరుగుదలకు అనుకూలంగా ఉంది. గాలిలో తేమ ఎక్కువగా ఉన్నప్పుడు ఫంగస్ తెగుళ్లు రాకుండా ముందస్తు జాగ్రత్తలు తీసుకోండి.",
        "default": "ధన్యవాదాలు! ఖచ్చితమైన సమాచారం కోసం మా 'పంట సిఫార్సు', 'తెగుళ్ల నిర్ధారణ' లేదా 'మండీ ధరల' విభాగాన్ని చూడండి."
    }
}

class AgriChatbotService:
    @classmethod
    def get_response(cls, req: ChatRequest) -> ChatResponse:
        lang = req.language if req.language in ["en", "hi", "te"] else "en"
        msg = req.message.lower()
        kb = AGRI_RESPONSES[lang]
        
        # Simple intent matching
        if any(w in msg for w in ["hi", "hello", "namaste", "namaskaram", "హలో", "నమస్కారం", "नमस्ते"]):
            reply = kb["greeting"]
            actions = ["Recommend Best Crop", "Analyze Fertilizer Needs", "Check Live Soil Telemetry"]
        elif any(w in msg for w in ["fertilizer", "npk", "urea", "dap", "khad", "ఎరువులు", "ఖాద్", "nutrition"]):
            reply = kb["fertilizer"]
            actions = ["Open Fertilizer Calculator", "Check Soil Fertility Score"]
        elif any(w in msg for w in ["irrigation", "water", "pump", "pani", "నీరు", "పంపు", "moisture"]):
            reply = kb["irrigation"]
            actions = ["View Irrigation Zones", "Start Zone 3 Pump", "Set Moisture Threshold"]
        elif any(w in msg for w in ["pest", "disease", "leaf", "blight", "insect", "spot", "కీటకాలు", "తెగులు", "कीट", "रोग"]):
            reply = kb["pest"]
            actions = ["Upload Leaf Photo for Scan", "View Organic Remedies"]
        elif any(w in msg for w in ["weather", "rain", "forecast", "temp", "వాతావరణం", "मौसम", "barish"]):
            reply = kb["weather"]
            actions = ["View 7-Day Weather Forecast", "Check Frost/Heatwave Alerts"]
        else:
            reply = kb["default"]
            actions = ["Crop Recommendation", "Disease Doctor", "Live Mandi Prices"]
            
        return ChatResponse(
            reply=reply,
            language=lang,
            suggested_actions=actions
        )
