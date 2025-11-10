import pandas as pd

def procesar_batch(df):
    """
    Procesa los datos históricos para crear un resumen
    (por ejemplo, popularidad y tipos de deportes).
    """
    resumen = (
        df.groupby("tipo")
        .agg({"nombre": "count"})
        .rename(columns={"nombre": "cantidad_deportes"})
        .reset_index()
    )
    return resumen
