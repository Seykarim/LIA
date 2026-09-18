"""
Simuladores de conectores API de LIA para servicios de terceros
(Google Calendar, Open Banking API, Apple Healthkit, Smart Fridge IoT).
"""

class CalendarConnector:
    @staticmethod
    def get_free_slots():
        return ["2026-09-21 09:00", "2026-09-22 14:00", "2026-09-24 10:30"]

class BankingConnector:
    @staticmethod
    def get_pending_bills():
        return [{"id": "BILL-882", "service": "Energía/Luz", "amount": 142000, "due_date": "2026-09-25"}]

class HealthConnector:
    @staticmethod
    def get_water_reminder():
        return "Recordatorio de hidratación programado cada 2 horas."

class SmartHomeConnector:
    @staticmethod
    def get_fridge_inventory():
        return {"leche": "bajo", "huevos": "suficiente", "verduras": "crítico"}
