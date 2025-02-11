from pydantic import BaseModel
from typing import Dict, Set, List


class apInput(BaseModel):
    estados: Set[str]
    simbolos_entrada: Set[str]
    simbolos_pilha: Set[str]
    transitions: Dict[str, Dict[str, Dict[str, list]]]  
    estado_inicial: str
    estados_finais: Set[str]
    simbolo_inicial_pilha: str

class StringInput(BaseModel):
    input: str

class apInfo(BaseModel):
    estados: Set[str]
    simbolos_entrada: Set[str]
    simbolos_pilha: Set[str]
    transitions: Dict[str, Dict[str, Dict[str, list]]]
    estado_inicial: str
    estados_finais: Set[str]
    simbolo_inicial_pilha: str