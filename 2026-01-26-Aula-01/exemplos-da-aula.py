import marimo

__generated_with = "0.19.6"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    return


@app.cell
def _():
    import networkx as nx
    import matplotlib.pyplot as plt
    return nx, plt


@app.cell
def _():
    # Número de nós
    nodes = 10
    return (nodes,)


@app.cell
def _(nodes, nx):
    # Criar um grafo completo (todos os nós conectados entre si)
    G = nx.complete_graph(nodes)
    return (G,)


@app.cell
def _(G, nodes, nx, plt):
    # Desenhar o grafo
    plt.figure(figsize=(6,6))
    nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=700, font_size=12)
    plt.title(f"Grafo completo com {nodes} nós")
    plt.show()
    return


if __name__ == "__main__":
    app.run()
