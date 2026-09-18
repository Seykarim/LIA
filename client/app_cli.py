import asyncio
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lia_core.agents.orchestrator import LifeOrchestrator

async def main():
    orchestrator = LifeOrchestrator()
    print("=" * 65)
    print("🤖 LIA — Life Intelligence Assistant (Console Mode)")
    print("   'Una capa de orquestación para tu vida digital'")
    print("=" * 65)

    default_prompt = "Organízame la semana, recuérdame pagar la luz, agenda cita con el médico y haz la lista del mercado según lo que hay en la nevera."
    
    print(f"\n[Usuario]: {default_prompt}\n")
    print("⚡ LIA analizando intención, dividiendo en agentes y ejecutando...\n")

    result = await orchestrator.parse_and_execute(default_prompt)

    print(f"📊 Intenciones detectadas: {result['parsed_intents_count']}\n")
    for idx, item in enumerate(result['execution_plan'], 1):
        intent = item['intent']
        status = item['status']
        print(f"{idx}. Categoría: [{intent['category'].upper()}]")
        print(f"   Acción: {intent['action']}")
        print(f"   Detalle: {intent['details']}")
        print(f"   Estado: {status}")
        if intent['requires_confirmation']:
            print("   ⚠️  [Requiere confirmación en un toque en la App/Wearable]")
        print("-" * 55)

if __name__ == "__main__":
    asyncio.run(main())
