"""
Assistant Router - Context-Aware Multilingual Agri-AI Chatbot API
"""

from fastapi import APIRouter
from backend.app.models.schemas import ChatRequest, ChatResponse
from backend.app.services.chatbot_service import AgriChatbotService

router = APIRouter(prefix="/api/assistant", tags=["Agri-AI Assistant"])

@router.post("/chat", response_model=ChatResponse)
def chat_with_agri_assistant(request: ChatRequest):
    """Interacts with the multilingual agronomic advisory AI assistant"""
    return AgriChatbotService.get_response(request)
