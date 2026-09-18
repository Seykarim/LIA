import asyncio
import time
from typing import List, Dict, Any
from pydantic import BaseModel, Field

class AgentIntent(BaseModel):
    category: str = Field(..., description="Categoría del agente asignado")
    action: str = Field(..., description="Acción específica a ejecutar")
    details: str = Field(..., description="Detalles contextuales extraídos")
    priority: int = Field(default=1, description="Nivel de prioridad de ejecución (1-5)")
    requires_confirmation: bool = Field(default=False)

class OrchestrationResult(BaseModel):
    raw_prompt: str
    parsed_intents_count: int
    execution_time_ms: float
    execution_plan: List[Dict[str, Any]]

class LifeOrchestrator:
    """
    Motor de Orquestación Asíncrono de LIA.
    Procesa intenciones en paralelo y emite respuestas validadas con Pydantic.
    """
    def __init__(self):
        self.categories = ["agenda", "finanzas", "salud", "hogar_compras", "documentos"]

    def _extract_intents(self, text: str) -> List[AgentIntent]:
        intents = []
        text_lower = text.lower()

        if any(w in text_lower for w in ["organíza", "semana", "agenda", "reunión", "tiempo"]):
            intents.append(AgentIntent(
                category="agenda",
                action="OPTIMIZE_WEEK",
                details="Optimizar bloques de tiempo y consolidar prioridades de la semana",
                priority=1
            ))

        if any(w in text_lower for w in ["paga", "factura", "luz", "banco", "dinero", "saldo"]):
            intents.append(AgentIntent(
                category="finanzas",
                action="SCHEDULE_PAYMENT",
                details="Programar pago de servicio público (Luz/Energía)",
                priority=2,
                requires_confirmation=True
            ))

        if any(w in text_lower for w in ["médico", "cita", "doctor", "salud", "examen"]):
            intents.append(AgentIntent(
                category="salud",
                action="BOOK_APPOINTMENT",
                details="Buscar disponibilidad en agenda médica y reservar cita",
                priority=1
            ))

        if any(w in text_lower for w in ["mercado", "nevera", "compras", "despensa"]):
            intents.append(AgentIntent(
                category="hogar_compras",
                action="GENERATE_SMART_LIST",
                details="Cruzar inventario de la nevera con la lista de faltantes",
                priority=3
            ))

        if not intents:
            intents.append(AgentIntent(
                category="general",
                action="PROCESS_NLP",
                details=f"Procesar instrucción no estructurada: '{text}'",
                priority=4
            ))

        return sorted(intents, key=lambda x: x.priority)

    async def _execute_agent_task(self, intent: AgentIntent) -> Dict[str, Any]:
        start_time = time.time()
        await asyncio.sleep(0.05)  # Simulación de latencia I/O de micro-agente
        elapsed = round((time.time() - start_time) * 1000, 2)

        status = "PENDING_USER_CONFIRMATION" if intent.requires_confirmation else "EXECUTED_SUCCESSFULLY"
        return {
            "intent": intent.model_dump(),
            "status": status,
            "latency_ms": elapsed,
            "response": f"Agente [{intent.category.upper()}] completó la acción '{intent.action}'."
        }

    async def parse_and_execute(self, user_prompt: str) -> OrchestrationResult:
        start_total = time.time()
        intents = self._extract_intents(user_prompt)

        # Ejecución paralela con asyncio.gather
        tasks = [self._execute_agent_task(intent) for intent in intents]
        results = await asyncio.gather(*tasks)

        total_time = round((time.time() - start_total) * 1000, 2)

        return OrchestrationResult(
            raw_prompt=user_prompt,
            parsed_intents_count=len(intents),
            execution_time_ms=total_time,
            execution_plan=results
        )
