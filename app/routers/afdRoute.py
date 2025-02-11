"""
Router para manipulação de Autômatos Finitos Determinísticos (AFD).
Fornece endpoints para criar, testar, visualizar e obter informações de AFDs.

Endpoints:
    POST /criar: Cria novo AFD
    POST /testar: Testa string no AFD atual
    GET /info: Obtém informações do AFD atual 
    GET /visualizar: Gera visualização do AFD atual
"""

from fastapi import APIRouter, HTTPException
from schemas.afdSchema import afdInput, StringInput
from services.afdService import criarAfd, testarString, getAfdInfo, visualizarAfd
from fastapi.responses import FileResponse

router = APIRouter()  

@router.post("/criar")
async def criar_afd(afd_input: afdInput):
    """
    Cria um novo Autômato Finito Determinístico (AFD).
    
    Parâmetros:
    - estados: Conjunto de estados do autômato
    - simbolos: Alfabeto de entrada do autômato
    - transicoes: Função de transição do autômato
    - estado_inicial: Estado inicial do autômato
    - estados_finais: Conjunto de estados finais do autômato
    
    Retorna:
    - Mensagem de sucesso ou erro na criação do AFD
    """
    return criarAfd(afd_input)


@router.post("/testar")
async def testar_string(input_data: StringInput):
    """
    Testa se uma string é aceita pelo AFD atual.
    
    Parameters:
        input_data (StringInput): Dados para teste
            - input: String a ser testada no autômato
    
    Returns:
        dict: Resultado do teste contendo:
            - string: String testada
            - aceita: Booleano indicando aceitação
            - mensagem: Descrição do resultado
    """
    return testarString(input_data.input)


@router.get("/info")
async def get_info():
    """
    Obtém informações do AFD atual.
    
    Returns:
        afdInfo: Informações completas do AFD
            - estados: Conjunto de estados
            - simbolos: Alfabeto
            - transicoes: Função de transição
            - estado_inicial: Estado inicial
            - estados_finais: Estados finais
    """
    return getAfdInfo()



@router.get("/visualizar")
async def get_visualization():
    """
    Gera visualização gráfica do AFD atual.
    
    Returns:
        FileResponse: Imagem PNG do diagrama do AFD
    
    Raises:
        HTTPException: Se nenhum AFD foi criado
    """
    result = visualizarAfd()
    if "erro" in result:
        raise HTTPException(status_code = 400, detail = result["erro"])
    return FileResponse("afd_visualization.png")