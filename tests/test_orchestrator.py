import pytest
import asyncio
from lia_core.agents.orchestrator import LifeOrchestrator

@pytest.mark.asyncio
async def test_orchestrator_multi_intent():
    orchestrator = LifeOrchestrator()
    prompt = "Organízame la semana, recuérdame pagar la luz y reserva cita con el médico"
    
    result = await orchestrator.parse_and_execute(prompt)
    
    assert result.parsed_intents_count == 3
    assert result.execution_time_ms > 0
    assert len(result.execution_plan) == 3

@pytest.mark.asyncio
async def test_orchestrator_confirmation_flag():
    orchestrator = LifeOrchestrator()
    prompt = "Paga la factura de energía"
    
    result = await orchestrator.parse_and_execute(prompt)
    
    finanzas_item = next(item for item in result.execution_plan if item['intent']['category'] == 'finanzas')
    assert finanzas_item['status'] == "PENDING_USER_CONFIRMATION"
