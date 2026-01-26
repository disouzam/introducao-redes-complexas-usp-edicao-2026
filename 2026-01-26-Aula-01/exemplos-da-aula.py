import marimo

__generated_with = "0.19.6"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import networkx as nx
    import matplotlib.pyplot as plt
    return nx, plt


@app.cell
def _(mo):
    node_slider = mo.ui.slider(start=1, stop=100, label="Número de nós para o grafo", value=10)
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
    plt.figure(figsize=(4,4))
    nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=700, font_size=12)
    plt.title(f"Grafo completo com {nodes} nós")

    mo.mpl.interactive(plt.gcf())
    return


if __name__ == "__main__":
    app.run()
