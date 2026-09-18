from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from lia_core.agents.orchestrator import LifeOrchestrator, OrchestrationResult

app = FastAPI(
    title="LIA — Life Intelligence Assistant API",
    description="Motor de orquestación personal impulsado por micro-agentes asíncronos.",
    version="1.1.0"
)

orchestrator = LifeOrchestrator()

class PromptRequest(BaseModel):
    prompt: str
    user_id: str = "default_user"

@app.get("/")
def health_check():
    return {"status": "online", "system": "LIA Core Engine", "version": "1.1.0"}

@app.post("/v1/orchestrate", response_model=OrchestrationResult)
async def orchestrate_user_intent(request: PromptRequest):
    if not request.prompt.strip():
        raise HTTPException(status_code=400, detail="El prompt no puede estar vacío.")
    
    return await orchestrator.parse_and_execute(request.prompt)
