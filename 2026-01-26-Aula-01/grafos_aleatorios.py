import marimo

__generated_with = "0.19.6"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    import networkx as nx
    import matplotlib.pyplot as plt
    import random
    return mo, nx, plt, random


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Créditos:

    O código apresentado nesse notebook foi inteiramente digitado por [Dickson Souza](https://www.linkedin.com/in/disouzam/) baseado na aula 01 do curso Introdução às Redes Complexas, ofertado pela USP, e ministrado pelos professores [Camilo Rodrigues Neto](https://www.linkedin.com/in/camilo-rodrigues-neto-074aa265/) e [Masayuki Hase](https://www.linkedin.com/in/masayuki-hase-3b26144/).

    As modificações foram feitas por Dickson Souza para adequação à preferências pessoais de desenvolvimento em Python.

    A aula pode ser acessada em https://www.youtube.com/live/qzgSoFtH6xs?si=cgpzwVSUb4GA--2o
    """)
    return


@app.cell
def _(mo):
    node_slider = mo.ui.slider(start=1, stop=100, label="Número de nós para o grafo", value=10)

    probability_slider = mo.ui.slider(start=0, stop=1, step=0.1, label="Probabilidade de formar uma aresta", value=0.5)
    return node_slider, probability_slider


@app.cell
def _(mo, node_slider, probability_slider):
    mo.vstack(
        [
            mo.hstack([node_slider, mo.md(f"Número de nós selecionado: {node_slider.value}")]),
            mo.hstack([probability_slider, mo.md(f"Probabilidade selecionada: {probability_slider.value}")])
        ]
    )
    return


@app.cell
def _(node_slider, probability_slider):
    # Número de nós
    nodes = node_slider.value

    # Probabilidade fixa de conexão entre nos 
    p = probability_slider.value
    return nodes, p


@app.cell
def _(nx, random):
    # Criar um grafo aleatório
    def gerar_grafo_aleatorio(nodes, probability):
        G = nx.Graph()
        G.add_nodes_from(range(nodes))

        for i in range(nodes):
            for j in range(i + 1, nodes):
                if random.random() < probability:
                    G.add_edge(i,j)

        return G
    return (gerar_grafo_aleatorio,)


@app.cell
def _(gerar_grafo_aleatorio, mo, nodes, nx, p, plt):
    G = gerar_grafo_aleatorio(nodes,p)

    # Desenhar o grafo
    plt.figure(figsize=(4,4))
    nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=700, font_size=12)
    plt.title(f"Grafo aleatório com {nodes} nós (p={p}")

    mo.mpl.interactive(plt.gcf())
    return (G,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Histograma do grau dos nós
    """)
    return


@app.cell
def _(G, plt):
    graus = [d for n, d in G.degree()]

    plt.figure(figsize=(6,4))
    plt.hist(graus, bins=range(0 , max(graus) + 2), color='blue', alpha=0.7, edgecolor='black', density=True)
    plt.xlabel('Grau')
    plt.ylabel('Frequência')
    plt.title('Histograma do grau dos nós')

    xticks = range(0, max(graus) + 1)

    if len(xticks) > 10:
        xticks = range(0, max(graus) + 1, 5)

    plt.xticks(xticks)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
    return


if __name__ == "__main__":
    app.run()
