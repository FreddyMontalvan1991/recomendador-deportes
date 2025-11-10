import pandas as pd

def procesar_batch(df):
    """
    Procesa los datos históricos de deportes para crear un resumen
    agrupado por tipo de deporte, popularidad o cualquier otra categoría.
    """

    if df.empty:
        print("⚠️ El DataFrame está vacío. No hay datos para procesar.")
        return pd.DataFrame()

    # Verificamos que las columnas esperadas existan
    columnas_requeridas = {"tipo", "nombre"}
    if not columnas_requeridas.issubset(df.columns):
        raise ValueError(f"Faltan columnas requeridas: {columnas_requeridas - set(df.columns)}")

    # Agrupamos por tipo de deporte y contamos la cantidad
    resumen = (
        df.groupby("tipo")
        .agg(cantidad_deportes=("nombre", "count"))
        .reset_index()
        .sort_values("cantidad_deportes", ascending=False)
    )

    return resumen
