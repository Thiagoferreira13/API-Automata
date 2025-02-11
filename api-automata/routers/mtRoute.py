"""
Router para manipulação de Máquinas de Turing (MT).
Fornece endpoints para criar, testar, visualizar e obter informações de MTs.

Endpoints:
    POST /criar: Cria nova MT determinística
    POST /testar: Testa string na MT atual
    GET /info: Obtém informações da MT atual 
    GET /visualizar: Gera visualização da MT atual
"""

from fastapi import APIRouter, HTTPException
from schemas.mtSchema import mtInput, StringInput
from services.mtService import criarMt, testarString, getMtInfo, visualizarMt
from fastapi.responses import FileResponse

router = APIRouter()

@router.post("/criar")
async def criar_mt(mt_input: mtInput):
    """
    Cria uma nova Máquina de Turing (MT) determinística.

    Parâmetros:
    - estados: Conjunto de estados (set)
    - simbolos_entrada: Alfabeto de entrada (set)
    - simbolos_fita: Alfabeto da fita (set)
    - transicoes: Função de transição (dict)
    - estado_inicial: Estado inicial (str)
    - estados_finais: Estados de aceitação (set)
    - simbolo_branco: Símbolo branco da fita (str)

    Retorna:
    - dict: Mensagem de sucesso/erro na criação

    Raises:
        HTTPException: Se ocorrer erro na validação dos parâmetros
    """
    return criarMt(mt_input)

@router.post("/testar")
async def testar_string(input_data: StringInput):
    """
    Testa o processamento de uma string pela MT atual.

    Parameters:
        input_data (StringInput): Dados para teste contendo:
            - input: String a ser processada na fita

    Returns:
        dict: Resultado do teste com:
            - string: String testada
            - aceita: Status de aceitação (bool)
            - fita_final: Conteúdo final da fita
            - mensagem: Descrição textual do resultado

    Raises:
        HTTPException: Se MT não existir ou erro no processamento
    """
    return testarString(input_data.input)

@router.get("/info")
async def get_info():
    """
    Obtém informações completas da MT atual.

    Returns:
        mtInfo: Estrutura com todos os dados da máquina contendo:
            - estados: Conjunto de estados
            - simbolos_entrada: Alfabeto de entrada
            - simbolos_fita: Alfabeto da fita
            - transicoes: Regras de transição
            - estado_inicial: Estado inicial
            - estados_finais: Estados finais
            - simbolo_branco: Símbolo branco

    Raises:
        HTTPException: Se nenhuma MT foi criada
    """
    return getMtInfo()

@router.get("/visualizar")
async def get_visualization():
    """
    Gera diagrama de estados da MT em formato PNG.

    Returns:
        FileResponse: Imagem PNG do diagrama

    Raises:
        HTTPException: 400 se nenhuma MT foi criada

    Notes:
        - Estados finais com círculo duplo
        - Transições mostram: símbolo_lido → símbolo_escrito,direção
        - Layout horizontal para melhor organização
        - Cabeçote de leitura/escrita representado nas transições
    """
    result = visualizarMt()
    if "erro" in result:
        raise HTTPException(status_code=400, detail=result["erro"])
    return FileResponse("mt_visualization.png")