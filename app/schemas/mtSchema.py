from pydantic import BaseModel
from typing import Dict, Set, Tuple

class mtInput(BaseModel):
    estados: Set[str]
    simbolos_fita: Set[str]
    simbolos_entrada: Set[str]
    transicoes: Dict[str, Dict[str, Tuple[str, str, str]]]
    estado_inicial: str
    estados_finais: Set[str]
    simbolo_branco: str

class StringInput(BaseModel):
    input: str

class mtInfo(BaseModel):
    estados: Set[str]
    simbolos_fita: Set[str]
    simbolos_entrada: Set[str]
    transicoes: Dict[str, Dict[str, Tuple[str, str, str]]]
    estado_inicial: str
    estados_finais: Set[str]
    simbolo_branco: str