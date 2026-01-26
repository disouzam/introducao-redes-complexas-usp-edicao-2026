import marimo

__generated_with = "0.19.6"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    return (pd,)


@app.cell
def _(pd):
    # Criação da tabela de probabilidades
    distribuicao_probs = [0, 0.08, 0.16, 0.21, 0.18, 0.16, 0.10, 0.06, 0.03, 0.01, 0.01]

    distribuicao_probs_series = pd.Series(distribuicao_probs, name="Probabilidade do grau k")
    distribuicao_probs_series.index.name="k"

    print(distribuicao_probs_series)
    return (distribuicao_probs_series,)


@app.cell
def _(distribuicao_probs_series):
    # Soma das probabilidades
    total = distribuicao_probs_series.sum()
    print(f"A soma de P(0) + P(1) + P(2) + ... é igual a {total} como esperado para um espaço de probabilidades completo.") 
    return


@app.cell
def _(distribuicao_probs_series, pd):
    # Valor esperado (aka média) - Preparação
    distribuicao_probs_df = pd.DataFrame(distribuicao_probs_series)

    # Replicação do índice para a criação de uma coluna auxiliar
    distribuicao_probs_df["Grau k"] = distribuicao_probs_df.index

    # Coluna auxiliar para o cálculo do valor esperado
    distribuicao_probs_df["P(k)*k"] = distribuicao_probs_df["Probabilidade do grau k"] * distribuicao_probs_df["Grau k"]
    distribuicao_probs_df
    return (distribuicao_probs_df,)


@app.cell
def _(distribuicao_probs_df):
    # Valor esperado (aka média)
    valor_esperado = distribuicao_probs_df["P(k)*k"].sum()
    print(f"O valor esperado (aka média) para o número de graus é igual {valor_esperado}.")
    return


if __name__ == "__main__":
    app.run()
