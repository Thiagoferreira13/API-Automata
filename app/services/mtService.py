"""
Service para manipulação de Máquinas de Turing (MT).
Implementa operações de criação, teste e visualização de MTs.
"""
from automata.tm.dtm import DTM
from schemas.mtSchema import mtInput, mtInfo
from graphviz import Digraph

mtAtual: DTM | None = None

def criarMt(mt_input: mtInput):
    """
    Cria uma nova Máquina de Turing.

    Args:
        mt_input (mtInput): Dados da MT
            - estados: Conjunto de estados
            - simbolos_entrada: Alfabeto de entrada
            - simbolos_fita: Alfabeto da fita
            - transicoes: Função de transição
            - estado_inicial: Estado inicial
            - simbolo_branco: Símbolo em branco
            - estados_finais: Estados finais

    Returns:
        dict: Mensagem de sucesso/erro
    """
    global mtAtual
    mtAtual = DTM(
        states = mt_input.estados,
        input_symbols = mt_input.simbolos_entrada,
        tape_symbols = mt_input.simbolos_fita,
        transitions = mt_input.transicoes,
        initial_state = mt_input.estado_inicial,
        blank_symbol = mt_input.simbolo_branco,
        final_states = mt_input.estados_finais
    )

    return {"mensagem": "MT criada com sucesso"}

def testarString(input_string: str) -> dict:
    """
    Verifica se uma string é aceita pela MT atual.

    Args:
        input_string (str): String a ser testada

    Returns:
        dict: Resultado do teste contendo:
            - string: String testada
            - aceita: Booleano indicando aceitação
            - fita_final: Conteúdo final da fita
            - mensagem: Descrição textual do resultado
    """
    if mtAtual is None:
        return {"erro": "Nenhuma MT foi criada ainda"}
    
    try:
        # Executa a MT passo a passo
        config = mtAtual.read_input_stepwise(input_string)
        
        # Variável para armazenar a última configuração válida
        final_config = None
        
        # Percorre até o estado final ou até a MT parar
        try:
            for final_config in config:
                pass
        except Exception:
            # Se houver exceção durante a execução, usa a última configuração válida
            pass

        # Se não conseguimos obter nenhuma configuração, a string é rejeitada
        if final_config is None:
            return {
                "string": input_string,
                "aceita": False,
                "fita_final": input_string,  # Retorna a string original como estava na fita
                "mensagem": "String rejeitada"
            }

        # Obtém o conteúdo final da fita
        fita_final = "".join(final_config.tape)
        aceita = final_config.state in mtAtual.final_states

        return {
            "string": input_string,
            "aceita": aceita,
            "fita_final": fita_final,
            "mensagem": "String aceita" if aceita else "String rejeitada"
        }
    except Exception as e:
        return {"erro": f"Erro ao processar string: {str(e)}"}

def getMtInfo() -> mtInfo:
    """
    Obtém informações da MT atual.

    Returns:
        mtInfo: Dados da MT
            - estados: Conjunto de estados
            - simbolos_fita: Alfabeto da fita
            - simbolos_entrada: Alfabeto de entrada
            - transicoes: Função de transição
            - estado_inicial: Estado inicial
            - estados_finais: Estados finais
            - simbolo_branco: Símbolo em branco

    Raises:
        Exception: Se nenhuma MT foi criada
    """
    if mtAtual is None:
        return {"erro": "Nenhuma MT foi criada ainda"}
    
    return mtInfo(
        estados = mtAtual.states,
        simbolos_fita = mtAtual.tape_symbols,
        simbolos_entrada = mtAtual.input_symbols,
        transicoes = mtAtual.transitions,
        estado_inicial = mtAtual.initial_state,
        estados_finais = mtAtual.final_states,
        simbolo_branco = mtAtual.blank_symbol
    )



def visualizarMt():
    """
    Gera visualização gráfica da MT atual.

    Returns:
        dict: Mensagem de sucesso/erro

    Notes:
        - Gera arquivo PNG com diagrama da MT
        - Estados finais são representados com círculo duplo
        - Transições mostram símbolo lido/escrito e direção
    """
    if mtAtual is None:
        return {"erro": "Nenhuma MT foi criada ainda"}
    
    dot = Digraph()
    dot.attr(rankdir="LR")  # Layout da esquerda para a direita

    # Indicação do estado inicial
    dot.node("", shape="none")
    dot.edge("", mtAtual.initial_state, label="")

    # Configuração dos nós
    for estado in mtAtual.states:
        if estado in mtAtual.final_states:
            dot.node(estado, estado, shape="doublecircle")
        else:
            dot.node(estado, estado, shape="circle")

    # Adiciona as transições agrupando as que têm o mesmo destino
    transicoes_formatadas = {}
    
    for estado, trans_by_symbol in mtAtual.transitions.items():
        for symbol, (next_state, write_symbol, direction) in trans_by_symbol.items():
            label = f"{symbol}/{write_symbol},{direction}"
            
            if (estado, next_state) in transicoes_formatadas:
                transicoes_formatadas[(estado, next_state)].append(label)
            else:
                transicoes_formatadas[(estado, next_state)] = [label]

    # Adiciona as transições sem sobreposição
    for (estado, next_state), labels in transicoes_formatadas.items():
        dot.edge(estado, next_state, label="\n".join(labels), constraint="false", minlen="2")

    # Salva o arquivo
    dot.render("mt_visualization", format="png", cleanup=True)
    return {"mensagem": "Visualização da MT gerada com sucesso"}
