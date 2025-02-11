"""
API para manipulação de autômatos e máquinas de Turing.
Fornece endpoints para criar, testar e visualizar AFDs, APs e MTs.
"""

from fastapi import FastAPI
from routers.afdRoute import router as afd_router
from routers.apRoute import router as ap_router
from routers.mtRoute import router as mt_router

app = FastAPI(
    title="Automata API",
    description="API para manipulação de Autômatos Finitos Deterministicos, Automatos Com Pilha e Maquinas de Turing",
    version="1.0.0"
)

# Registra as rotas para cada tipo de autômato
app.include_router(afd_router, prefix = "/api/afd", tags = ["Autômatos Finitos"])
app.include_router(ap_router, prefix = "/api/ap", tags = ["Autômatos com Pilha"])
app.include_router(mt_router, prefix = "/api/mt", tags = ["Maquinas de Turing"])


@app.get("/")
async def root():
    """Rota principal que verifica se a API está funcionando."""
    return {"message": "Rodando API"}