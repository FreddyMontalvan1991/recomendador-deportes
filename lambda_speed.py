import pandas as pd

def recomendacion_rapida(df, tipo=None, categoria=None, dificultad=None):
    """Filtra deportes en tiempo real según las preferencias del usuario."""
    filtrado = df.copy()
    if tipo:
        filtrado = filtrado[filtrado["tipo"].str.lower() == tipo.lower()]
    if categoria:
        filtrado = filtrado[filtrado["categoria"].str.contains(categoria, case=False)]
    if dificultad:
        # Dificultad ficticia calculada por popularidad
        if dificultad == "Fácil":
            filtrado = filtrado[filtrado["popularidad"].isin(["Alta"])]
        elif dificultad == "Media":
            filtrado = filtrado[filtrado["popularidad"].isin(["Media"])]
    return filtrado.sample(min(5, len(filtrado)))
