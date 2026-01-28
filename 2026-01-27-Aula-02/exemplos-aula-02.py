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


if __name__ == "__main__":
    app.run()
