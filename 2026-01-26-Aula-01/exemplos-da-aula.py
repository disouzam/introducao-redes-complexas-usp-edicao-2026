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

    O código apresentado nesse notebook foi inteiramente digitado por [Dickson Souza](https://www.linkedin.com/in/disouzam/) baseado na aula 01 do curso Introdução às Redes Complexas, ofertado pela USP, e ministrado pelos professores [Camilo Rodrigues Neto](https://www.linkedin.com/in/camilo-rodrigues-neto-074aa265/) e [Masayuki Hase](https://www.linkedin.com/in/masayuki-hase-3b26144/).

    Introduzi algumas modificações para adaptação ao marimo, incluindo o uso de recursos interativos para seleção do número de nós usados para a criação do grafo completo.

    A aula pode ser acessada em https://www.youtube.com/live/qzgSoFtH6xs?si=cgpzwVSUb4GA--2o
    """)
    return


@app.cell
def _():
    import networkx as nx
    import matplotlib.pyplot as plt
    import numpy as np
    return np, nx, plt


@app.cell
def _(mo):
    node_slider = mo.ui.slider(start=1, stop=100000, label="Número de nós para o grafo", value=1000)
    return (node_slider,)


@app.cell
def _(mo, node_slider):
    mo.hstack([node_slider, mo.md(f"Número de nós selecionado: {node_slider.value}")])
    return


@app.cell
def _(node_slider):
    # Número de nós
    nodes = node_slider.value
    return (nodes,)


@app.cell
def _(nodes, nx):
    # Criar um grafo completo (todos os nós conectados entre si)
    G = nx.complete_graph(nodes)
    return (G,)


@app.cell
def _(G, mo, nodes, nx, plt):
    # Desenhar o grafo
    plt.figure(figsize=(4, 4))
    nx.draw(G, with_labels=True, node_color="lightblue", edge_color="gray", node_size=700, font_size=12)
    plt.title(f"Grafo completo com {nodes} nós")

    mo.mpl.interactive(plt.gcf())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Histograma do grau dos nós
    """)
    return


@app.cell
def _(G, np, plt):
    graus = [d for n, d in G.degree()]

    plt.figure(figsize=(6, 4))

    bins = np.arange(-0.5, max(graus) + 2.5)
    plt.hist(graus, bins=bins, color="blue", alpha=0.7, edgecolor="black", density=True, align="mid")
    plt.xlabel("Grau")
    plt.ylabel("Frequência")
    plt.title("Histograma do grau dos nós")

    step = 1
    factors = [1, 2, 5, 10]
    xticks = np.arange(-0.5, max(graus) + 2.5, step=step)

    base_step = step
    while len(xticks) > 10:
        for factor in factors:
            if factor == 1:
                base_step = step
            step = base_step * factor
            xticks = np.arange(-0.5, max(graus) + 2.5, step=step)

            if len(xticks) <= 10:
                break

    plt.xticks(xticks)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()
    return


if __name__ == "__main__":
    app.run()
