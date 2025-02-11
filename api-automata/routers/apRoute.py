"""
Router para manipulação de Autômatos com Pilha (AP).
Fornece endpoints para criar, testar, visualizar e obter informações de APs.

Endpoints:
    POST /criar: Cria novo AP determinístico
    POST /testar: Testa string no AP atual
    GET /info: Obtém informações do AP atual 
    GET /visualizar: Gera visualização do AP atual
"""

from fastapi import APIRouter, HTTPException
from schemas.apSchema import apInput, StringInput
from services.apService import criarAp, testarString, getApInfo, visualizarAp
from fastapi.responses import FileResponse

router = APIRouter()

@router.post("/criar")
async def criar_ap(ap_input: apInput):
    """
    Cria um novo Autômato com Pilha (AP) Determinístico.

    Parâmetros:
    - estados: Conjunto de estados (set)
    - simbolos_entrada: Alfabeto de entrada (set)
    - simbolos_pilha: Alfabeto da pilha (set)
    - transitions: Função de transição hierárquica (dict)
    - estado_inicial: Estado inicial (str)
    - simbolo_inicial_pilha: Símbolo inicial da pilha (str)
    - estados_finais: Conjunto de estados finais (set)

    Retorna:
    - dict: Mensagem de sucesso/erro na criação
    """
    return criarAp(ap_input)

@router.post("/testar")
async def testar_string(input_data: StringInput):
    """
    Testa se uma string é aceita pelo AP atual.

    Parameters:
        input_data (StringInput): Dados para teste contendo:
            - input: String a ser processada pelo autômato

    Returns:
        dict: Resultado do teste com:
            - string: String testada
            - aceita: Status de aceitação (bool)
            - mensagem: Descrição textual do resultado

    Raises:
        HTTPException: Se ocorrer erro no processamento
    """
    return testarString(input_data.input)

@router.get("/info")
async def get_info():
    """
    Obtém informações completas do AP atual.

    Returns:
        apInfo: Estrutura com todos os dados do autômato contendo:
            - estados: Conjunto de estados
            - simbolos_entrada: Alfabeto de entrada
            - simbolos_pilha: Alfabeto da pilha
            - transitions: Regras de transição
            - estado_inicial: Estado inicial
            - estados_finais: Estados finais
            - simbolo_inicial_pilha: Símbolo inicial da pilha

    Raises:
        HTTPException: Se nenhum AP foi criado
    """
    return getApInfo()

@router.get("/visualizar")
async def get_visualization():
    """
    Gera diagrama do AP no formato PNG.

    Returns:
        FileResponse: Imagem PNG do autômato

    Raises:
        HTTPException: 400 se nenhum AP foi criado

    Notes:
        - Estados finais têm círculo duplo
        - Transições mostram: símbolo_entrada,pop_pilha/push_pilha
        - Layout horizontal para melhor visualização
    """
    result = visualizarAp()
    if "erro" in result:
        raise HTTPException(status_code=400, detail=result["erro"])
    return FileResponse("ap_visualization.png")