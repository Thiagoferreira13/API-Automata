from pydantic import BaseModel
from typing import Dict, Set

class afdInput(BaseModel):
    estados: Set[str]
    simbolos: Set[str]
    transicoes: Dict[str, Dict[str, str]]
    estado_inicial: str
    estados_finais: Set[str]


class StringInput(BaseModel):
    input: str


class afdInfo(BaseModel):
    estados: Set[str]
    simbolos: Set[str]
    transicoes: Dict[str, Dict[str, str]]
    estado_inicial: str
    estados_finais: Set[str]