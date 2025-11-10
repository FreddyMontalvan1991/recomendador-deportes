import pandas as pd

def recomendacion_rapida(df, tipo=None, categoria=None, dificultad=None):
    """
    Filtra y recomienda deportes en tiempo real según las preferencias del usuario.
    
    Parámetros:
    -----------
    df : pandas.DataFrame
        DataFrame con los datos de deportes (debe contener columnas como 'tipo', 'categoria', 'popularidad').
    tipo : str, opcional
        Tipo de deporte (por ejemplo: 'Grupal', 'Individual').
    categoria : str, opcional
        Categoría del deporte (por ejemplo: 'Exterior', 'Interior').
    dificultad : str, opcional
        Nivel de dificultad ('Fácil', 'Media'). 
        Se calcula de forma ficticia usando la popularidad.

    Retorna:
    --------
    pandas.DataFrame
        Subconjunto filtrado del DataFrame original (hasta 5 deportes).
    """

    if df.empty:
        print("⚠️ El DataFrame está vacío. No hay datos para recomendar.")
        return pd.DataFrame()

    filtrado = df.copy()

    # Filtros dinámicos según parámetros
    if tipo:
        filtrado = filtrado[filtrado["tipo"].str.lower() == tipo.lower()]
    
    if categoria:
        filtrado = filtrado[filtrado["categoria"].str.contains(categoria, case=False, na=False)]
    
    if dificultad:
        if "popularidad" not in filtrado.columns:
            print("⚠️ No se encontró la columna 'popularidad'. No se puede aplicar el filtro de dificultad.")
        else:
            if dificultad.lower() == "fácil":
                filtrado = filtrado[filtrado["popularidad"].str.lower() == "alta"]
            elif dificultad.lower() == "media":
                filtrado = filtrado[filtrado["popularidad"].str.lower() == "media"]
            else:
                print("⚠️ Dificultad no reconocida. Use 'Fácil' o 'Media'.")

    if filtrado.empty:
        print("⚠️ No se encontraron deportes con los criterios seleccionados.")
        return pd.DataFrame()

    # Selecciona hasta 5 recomendaciones aleatorias
    return filtrado.sample(min(5, len(filtrado))).reset_index(drop=True)
