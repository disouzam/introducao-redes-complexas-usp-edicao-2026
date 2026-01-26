import marimo

__generated_with = "0.19.6"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    return mo, pd


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Criação da tabela de probabilidades
    """)
    return


@app.cell
def _(pd):
    distribuicao_probs = [0, 0.25, 0.16, 0.12, 0.10, 0.08, 0.07, 0.06, 0.06, 0.05, 0.05]

    distribuicao_probs_series = pd.Series(distribuicao_probs, name="Probabilidade do grau k")
    distribuicao_probs_series.index.name="k"
    distribuicao_probs_series
    return (distribuicao_probs_series,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Soma das probabilidades
    """)
    return


@app.cell
def _(distribuicao_probs_series):
    total = distribuicao_probs_series.sum()
    print(f"A soma de P(0) + P(1) + P(2) + ... é igual a {total:.2f} como esperado para um espaço de probabilidades completo.") 
    return (total,)


@app.cell(hide_code=True)
def _(mo, total):
    mo.md(f"""
    ## A soma de P(0) + P(1) + P(2) + ... é igual a **{total:.2f}** como esperado para um espaço de probabilidades completo.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Valor esperado (aka média) - Preparação
    """)
    return


@app.cell
def _(distribuicao_probs_series, pd):
    distribuicao_probs_df = pd.DataFrame(distribuicao_probs_series)

    # Replicação do índice para a criação de uma coluna auxiliar
    distribuicao_probs_df["Grau k"] = distribuicao_probs_df.index

    # Coluna auxiliar para o cálculo do valor esperado
    distribuicao_probs_df["P(k)*k"] = distribuicao_probs_df["Probabilidade do grau k"] * distribuicao_probs_df["Grau k"]
    distribuicao_probs_df
    return (distribuicao_probs_df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Valor esperado (aka média)
    """)
    return


@app.cell
def _(distribuicao_probs_df):
    valor_esperado = distribuicao_probs_df["P(k)*k"].sum()
    print(f"O valor esperado (aka média) para o número de graus é igual {valor_esperado}.")
    return (valor_esperado,)


@app.cell(hide_code=True)
def _(mo, valor_esperado):
    mo.md(f"""
    ## O valor esperado (aka média) para o número de graus é igual **{valor_esperado}**.
    """)
    return


if __name__ == "__main__":
    app.run()
