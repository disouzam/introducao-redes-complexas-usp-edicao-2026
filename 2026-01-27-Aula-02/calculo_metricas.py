import marimo

__generated_with = "0.19.6"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Créditos:

    O código apresentado nesse notebook foi inteiramente digitado por [Dickson Souza](https://www.linkedin.com/in/disouzam/) baseado na aula 02 do curso Introdução às Redes Complexas, ofertado pela USP, e ministrado pelos professores [Camilo Rodrigues Neto](https://www.linkedin.com/in/camilo-rodrigues-neto-074aa265/) e [Masayuki Hase](https://www.linkedin.com/in/masayuki-hase-3b26144/).

    Introduzi algumas modificações para adaptação ao marimo, incluindo o uso de recursos interativos para seleção do número de nós usados para a criação do grafo completo.

    A aula pode ser acessada em [
    Aula 2 - Redes Homogêneas - terça, 27/1/2026, 14 h](https://www.youtube.com/watch?v=kWUXR1oOhJ0) - https://www.youtube.com/watch?v=kWUXR1oOhJ0
    """)
    return


@app.cell
def _():
    import networkx as nx
    import random
    import numpy as np
    return np, nx


@app.cell
def _(np):
    def criar_gerador_numeros_aleatorios(n_streams=1, user_seed=None):
        seed_sequence = np.random.SeedSequence(user_seed)
        seeds = seed_sequence.spawn(n_streams)

        if user_seed is not None:
            rng = np.random.default_rng(seeds[0])
        else:
            rng = np.random.default_rng()

        return rng
    return (criar_gerador_numeros_aleatorios,)


@app.cell
def _(criar_gerador_numeros_aleatorios, nx):
    def criar_grafo_completo(nos):
        G = nx.complete_graph(nos)
        return G


    def criar_grafo_aleatorio(nodes, probability, random_generator=None):
        G = nx.Graph()
        G.add_nodes_from(range(nodes))

        if random_generator is None:
            rng = criar_gerador_numeros_aleatorios()
        else:
            rng = random_generator

        for i in range(nodes):
            for j in range(i + 1, nodes):
                if rng.uniform(low=0, high=1) < probability:
                    G.add_edge(i, j)

        return G
    return criar_grafo_aleatorio, criar_grafo_completo


@app.cell
def _(nx):
    def calcular_caminho_minimo_medio(grafo):
        if nx.is_connected(grafo):
            return nx.average_shortest_path_length(grafo)
        else:
            return float("inf")


    def calcular_coeficiente_aglomeracao_medio(grafo):
        return nx.average_clustering(grafo)
    return (
        calcular_caminho_minimo_medio,
        calcular_coeficiente_aglomeracao_medio,
    )


@app.cell
def _():
    nos_referencia = 10
    return (nos_referencia,)


@app.cell
def _(
    calcular_caminho_minimo_medio,
    calcular_coeficiente_aglomeracao_medio,
    criar_grafo_completo,
    nos_referencia,
):
    grafo_completo = criar_grafo_completo(nos_referencia)
    print(f"Caminho minimo medio do grafo completo: {calcular_caminho_minimo_medio(grafo_completo)}")
    print(
        f"Coeficiente de aglomeração médio do grafo completo: {calcular_coeficiente_aglomeracao_medio(grafo_completo)}"
    )
    return


@app.cell
def _(
    calcular_caminho_minimo_medio,
    calcular_coeficiente_aglomeracao_medio,
    criar_grafo_aleatorio,
    nos_referencia,
):
    grafo_aleatorio = criar_grafo_aleatorio(nos_referencia, 0.1)
    print(
        f"Caminho minimo medio do grafo aleatório: {calcular_caminho_minimo_medio(grafo_aleatorio):.4f}"
    )
    print(
        f"Coeficiente de aglomeração médio do grafo aleatório: {calcular_coeficiente_aglomeracao_medio(grafo_aleatorio)}"
    )
    return


if __name__ == "__main__":
    app.run()
