"""
Farm Operations & Sowing-to-Harvest Crop Cycle Lifecycle Manager
Tracks agricultural operations, labor allocations, spray logs, and harvest milestones.
"""

from typing import List, Dict, Any, Optional
from datetime import datetime, timedelta

class CropCycleLifecycleManager:
    def __init__(self):
        self.crop_cycles: Dict[str, Dict[str, Any]] = {
            "CYCLE-2026-PADDY-01": {
                "id": "CYCLE-2026-PADDY-01",
                "plot_id": "ZONE-01",
                "crop": "Rice (Basmati)",
                "variety": "Pusa Basmati 1509",
                "sowing_date": "2026-06-15",
                "expected_harvest": "2026-10-25",
                "status": "IN_PROGRESS",
                "stage": "Panicle Initiation",
                "total_expenses_inr": 34500.0,
                "activities_completed": [
                    {"date": "2026-06-15", "activity": "Nursery Sowing", "labor_hours": 16, "cost_inr": 4000},
                    {"date": "2026-07-08", "activity": "Transplanting", "labor_hours": 40, "cost_inr": 12000},
                    {"date": "2026-07-25", "activity": "Basal Fertilizer Application (DAP + Zinc)", "labor_hours": 8, "cost_inr": 8500},
                    {"date": "2026-08-12", "activity": "First Top Dressing (Urea)", "labor_hours": 6, "cost_inr": 4000}
                ],
                "upcoming_tasks": [
                    {"due_date": "2026-08-28", "task": "Foliar spray of Tricyclazole for Blast Prevention", "priority": "HIGH"},
                    {"due_date": "2026-09-10", "task": "Potassium application at heading stage", "priority": "MEDIUM"},
                    {"due_date": "2026-10-15", "task": "Pre-harvest field drainage", "priority": "CRITICAL"}
                ]
            }
        }

    def add_activity_log(self, cycle_id: str, activity_name: str, labor_hours: int, cost_inr: float) -> bool:
        if cycle_id in self.crop_cycles:
            self.crop_cycles[cycle_id]["activities_completed"].append({
                "date": datetime.now().strftime("%Y-%m-%d"),
                "activity": activity_name,
                "labor_hours": labor_hours,
                "cost_inr": cost_inr
            })
            self.crop_cycles[cycle_id]["total_expenses_inr"] += cost_inr
            return True
        return False

    def get_cycle_summary(self, cycle_id: str) -> Optional[Dict[str, Any]]:
        return self.crop_cycles.get(cycle_id)
