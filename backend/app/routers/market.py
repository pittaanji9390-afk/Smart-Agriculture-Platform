"""
Market Router - APMC Mandi Commodity Rates & Price Trends
"""

from fastapi import APIRouter
from backend.app.models.schemas import MandiMarketResponse
from backend.app.services.market_service import MandiMarketService

router = APIRouter(prefix="/api/market", tags=["Mandi Intelligence"])

@router.get("/prices", response_model=MandiMarketResponse)
def get_mandi_prices():
    """Retrieve real-time APMC Mandi commodity rates, modal price, and daily fluctuations"""
    return MandiMarketService.get_live_mandi_prices()
