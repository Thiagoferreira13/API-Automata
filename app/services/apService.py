"""
Service para manipulação de Autômatos com Pilha (AP).
Implementa operações de criação, teste e visualização de APs.
"""

from automata.pda.dpda import DPDA
from schemas.apSchema import apInput, apInfo
from graphviz import Digraph

apAtual: DPDA | None = None

def criarAp(ap_input: apInput):
    """
    Cria um novo Autômato com Pilha (AP) Determinístico.

    Args:
        ap_input (apInput): Dados do AP
        - estados: Conjunto de estados
        - simbolos_entrada: Alfabeto de entrada
        - simbolos_pilha: Alfabeto da pilha
        - transitions: Função de transição (dict hierárquico)
        - estado_inicial: Estado inicial
        - simbolo_inicial_pilha: Símbolo inicial da pilha
        - estados_finais: Estados finais

    Returns:
        dict: Mensagem de sucesso/erro
    """
    global apAtual
    apAtual = DPDA(
        states = ap_input.estados,
        input_symbols = ap_input.simbolos_entrada,
        stack_symbols = ap_input.simbolos_pilha,
        transitions = ap_input.transitions,
        initial_state = ap_input.estado_inicial,
        initial_stack_symbol = ap_input.simbolo_inicial_pilha,
        final_states = ap_input.estados_finais
    )

    return {"mensagem": "AP criado com sucesso"}

def testarString(input_string: str) -> dict:
    """
    Verifica se uma string é aceita pelo AP atual.

    Args:
    input_string (str): String a ser testada

    Returns:
        dict: Resultado do teste com:
            - string: String testada
            - aceita: Booleano indicando aceitação
            - mensagem: Descrição textual do resultado

    Raises:
        Exception: Se ocorrer erro durante o processamento
    """
    if apAtual is None:
        return {"erro": "Nenhum AP foi criado ainda"}
    
    try:
        aceita = apAtual.accepts_input(input_string)
        return {
            "string": input_string,
            "aceita": aceita,
            "mensagem": "String aceita" if aceita else "String rejeitada"
        }
    except Exception as e:
        return {"erro": f"Erro ao processar string: {str(e)}"}

def getApInfo() -> apInfo:
    """
    Obtém informações detalhadas do AP atual.

    Returns:
    apInfo: Dados do AP contendo:
        - estados: Conjunto de estados
        - simbolos_entrada: Alfabeto de entrada
        - simbolos_pilha: Alfabeto da pilha
        - transitions: Regras de transição
        - estado_inicial: Estado inicial
        - estados_finais: Estados de aceitação
        - simbolo_inicial_pilha: Símbolo inicial da pilha

    Raises:
        Exception: Se nenhum AP foi criado
    """
    if apAtual is None:
        return {"erro": "Nenhum AP foi criado ainda"}
    
    return apInfo(
        estados = apAtual.states,
        simbolos_entrada = apAtual.input_symbols,
        simbolos_pilha = apAtual.stack_symbols,
        transitions = apAtual.transitions,
        estado_inicial = apAtual.initial_state,
        estados_finais = apAtual.final_states,
        simbolo_inicial_pilha = apAtual.initial_stack_symbol
    )

def visualizarAp():
    """
    Gera uma visualização gráfica do AP usando Graphviz.

    Returns:
    dict: Mensagem de sucesso/erro

    Notes:
    - Cria arquivo PNG 'ap_visualization.png'
    - Estados finais têm círculo duplo
    - Transições mostram: símbolo_entrada,símbolo_pilha_pop/símbolos_pilha_push
    - Layout horizontal para melhor organização
    """
    if apAtual is None:
        return {"erro": "Nenhum AP foi criado ainda"}
    
    dot = Digraph()
    dot.attr(rankdir="LR")  # Organiza os estados horizontalmente para evitar sobreposição

    # Indicação do estado inicial
    dot.node("", shape="none")
    dot.edge("", apAtual.initial_state, label="")

    # Configuração dos nós
    for estado in apAtual.states:
        if estado in apAtual.final_states:
            dot.node(estado, estado, shape="doublecircle")
        else:
            dot.node(estado, estado, shape="circle")

    # Agrupamento de transições para evitar sobreposição de setas
    transicoes_formatadas = {}

    for estado, trans_by_input in apAtual.transitions.items():
        for input_symbol, trans_by_stack in trans_by_input.items():
            for stack_symbol, (next_state, stack_push) in trans_by_stack.items():
                label = f"{input_symbol},{stack_symbol}/{','.join(stack_push)}"

                if (estado, next_state) in transicoes_formatadas:
                    transicoes_formatadas[(estado, next_state)].append(label)
                else:
                    transicoes_formatadas[(estado, next_state)] = [label]

    # Adiciona as transições ao grafo de forma mais organizada
    for (estado, next_state), labels in transicoes_formatadas.items():
        dot.edge(estado, next_state, label="\n".join(labels), constraint="false", minlen="2")

    # Salva o arquivo
    dot.render("ap_visualization", format="png", cleanup=True)
    return {"mensagem": "Visualização do AP gerada com sucesso"}