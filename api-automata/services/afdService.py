"""
Service para manipulação de Autômatos Finitos Determinísticos (AFD).
Implementa operações de criação, teste e visualização de AFDs.
"""

from automata.fa.dfa import DFA
from schemas.afdSchema import afdInput, afdInfo
from graphviz import Digraph

afdAtual: DFA | None = None

def criarAfd(afd_input: afdInput):
    """
    Cria um novo Autômato Finito Determinístico (AFD).

    Args:
        afd_input (afdInput): Dados do AFD
            - estados: Conjunto de estados (set)
            - simbolos: Alfabeto de entrada (set)
            - transicoes: Dicionário de transições {estado: {símbolo: estado_destino}}
            - estado_inicial: Estado inicial (str)
            - estados_finais: Conjunto de estados de aceitação (set)

    Returns:
        dict: Mensagem de sucesso/erro
    """
    global afdAtual
    afdAtual = DFA(

        states = afd_input.estados,
        input_symbols = afd_input.simbolos,
        transitions = afd_input.transicoes,
        initial_state = afd_input.estado_inicial,
        final_states = afd_input.estados_finais
    )

    return {"mensagem": "AFD criado com sucesso"}



def testarString(input_string: str) -> dict:
    """
    Cria um novo Autômato Finito Determinístico (AFD).

    Args:
        afd_input (afdInput): Dados do AFD
            - estados: Conjunto de estados (set)
            - simbolos: Alfabeto de entrada (set)
            - transicoes: Dicionário de transições {estado: {símbolo: estado_destino}}
            - estado_inicial: Estado inicial (str)
            - estados_finais: Conjunto de estados de aceitação (set)

    Returns:
        dict: Mensagem de sucesso/erro
    """
    if afdAtual is None:
        return {"erro": "Nenhum AFD foi criado ainda"}
    
    try:
        aceita = afdAtual.accepts_input(input_string)
        return {
            "string": input_string,
            "aceita": aceita,
            "mensagem": "String aceita" if aceita else "String rejeitada"
        }
    except Exception as e:
        return {"erro": f"Erro ao processar string: {str(e)}"}
    


def getAfdInfo() -> afdInfo:
    """
    Obtém informações detalhadas do AFD atual.

    Returns:
        afdInfo: Dados do AFD contendo:
            - estados: Conjunto de estados
            - simbolos: Alfabeto de entrada
            - transicoes: Regras de transição
            - estado_inicial: Estado inicial
            - estados_finais: Estados de aceitação

    Raises:
        Exception: Se nenhum AFD foi criado
    """
    if afdAtual is None:
        return {"erro": "Nenhum AFD foi criado ainda"}
    
    print(afdAtual)
    return afdInfo(
        estados = afdAtual.states,
        simbolos = afdAtual.input_symbols,
        transicoes = afdAtual.transitions,
        estado_inicial = afdAtual.initial_state,
        estados_finais = afdAtual.final_states
    )



def visualizarAfd():
    """
    Obtém informações detalhadas do AFD atual.

    Returns:
        afdInfo: Dados do AFD contendo:
            - estados: Conjunto de estados
            - simbolos: Alfabeto de entrada
            - transicoes: Regras de transição
            - estado_inicial: Estado inicial
            - estados_finais: Estados de aceitação

    Raises:
        Exception: Se nenhum AFD foi criado
    """
    if afdAtual is None:
        return {"erro": "Nenhum AFD foi criado ainda"}
    
    dot = Digraph()

    # Indicação do estado inicial
    dot.node("", shape = "none")  # Nó invisível para a seta inicial
    dot.edge("", afdAtual.initial_state, label = "")  # A seta inicial aponta para o estado inicial

    # Configuração dos nós
    for estado in afdAtual.states:
        if estado in afdAtual.final_states:
            dot.node(estado, estado, shape = "doublecircle")
        else:
            dot.node(estado, estado, shape="circle")

    # Adiciona as transições
    for estado, transicoes in afdAtual.transitions.items():
        for simbolo, destino in transicoes.items():
            dot.edge(estado, destino, label = simbolo)

    # Salva o arquivo
    dot.render("afd_visualization", format="png", cleanup = True)
    return {"mensagem": "Visualização do AFD gerada com sucesso"}
