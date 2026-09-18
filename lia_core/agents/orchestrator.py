import asyncio
import re
from typing import List, Dict, Any

class AgentIntent:
    def __init__(self, category: str, action: str, details: str, requires_confirmation: bool = False):
        self.category = category
        self.action = action
        self.details = details
        self.requires_confirmation = requires_confirmation

    def to_dict(self) -> Dict[str, Any]:
        return {
            "category": self.category,
            "action": self.action,
            "details": self.details,
            "requires_confirmation": self.requires_confirmation
        }

class LifeOrchestrator:
    """
    Núcleo de Orquestación de LIA:
    Parsea lenguaje natural compuesto y distribuye tareas a micro-agentes locales/nube.
    """
    def __init__(self):
        self.categories = ["agenda", "finanzas", "salud", "hogar_compras", "documentos"]

    async def parse_and_execute(self, user_prompt: str) -> Dict[str, Any]:
        intents = self._extract_intents(user_prompt)
        execution_results = []

        for intent in intents:
            result = await self._route_to_agent(intent)
            execution_results.append(result)

        return {
            "raw_prompt": user_prompt,
            "parsed_intents_count": len(intents),
            "execution_plan": execution_results
        }

    def _extract_intents(self, text: str) -> List[AgentIntent]:
        intents = []
        text_lower = text.lower()

        # Detección de intenciones de Agenda / Calendario
        if "organíza" in text_lower or "semana" in text_lower or "agenda" in text_lower:
            intents.append(AgentIntent("agenda", "OPTIMIZE_WEEK", "Optimizar bloques de tiempo y consolidar prioridades de la semana"))

        # Detección de Finanzas
        if "paga" in text_lower or "factura" in text_lower or "luz" in text_lower or "banco" in text_lower:
            intents.append(AgentIntent("finanzas", "SCHEDULE_PAYMENT", "Programar pago de servicio público (Luz)", requires_confirmation=True))

        # Detección de Salud
        if "médico" in text_lower or "cita" in text_lower or "doctor" in text_lower:
            intents.append(AgentIntent("salud", "BOOK_APPOINTMENT", "Buscar disponibilidad y agendar cita médica"))

        # Detección de Inventario / Mercado
        if "mercado" in text_lower or "nevera" in text_lower or "compras" in text_lower:
            intents.append(AgentIntent("hogar_compras", "GENERATE_SMART_LIST", "Cruzar inventario de nevera con lista de compras faltantes"))

        # Fallback si no hay reglas explícitas coincidentes
        if not intents:
            intents.append(AgentIntent("general", "PROCESS_NLP", f"Procesar instrucción general: '{text}'"))

        return intents

    async def _route_to_agent(self, intent: AgentIntent) -> Dict[str, Any]:
        await asyncio.sleep(0.1) # Simulación de ejecución asíncrona de agente
        status = "PENDING_CONFIRMATION" if intent.requires_confirmation else "EXECUTED_SUCCESSFULLY"
        return {
            "intent": intent.to_dict(),
            "status": status,
            "response": f"Agente [{intent.category.upper()}] -> {intent.action}: Completo."
        }
