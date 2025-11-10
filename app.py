import streamlit as st
import pandas as pd
import plotly.express as px
from utils_mongo import conectar_mongo, obtener_datos
from lambda_batch import procesar_batch
from lambda_speed import recomendacion_rapida

# --- Configuración general ---
st.set_page_config(page_title="🏋️ Sistema Recomendador de Deportes (Lambda + MongoDB)", layout="wide")

# --- Conexión a MongoDB ---
MONGO_URI = "mongodb+srv://freddy_db_user:freddy1991@cluster0.fjs355s.mongodb.net/"
coleccion = conectar_mongo(MONGO_URI, "deportes_db", "deportes")
df = obtener_datos(coleccion)

st.title("🏋️ Sistema Recomendador de Deportes")
st.markdown("### Arquitectura Lambda + MongoDB Atlas + Streamlit Cloud")

# --- Capa Batch ---
st.subheader("📊 Capa Batch: Procesamiento histórico")
resumen = procesar_batch(df)
fig = px.bar(resumen, x="tipo", y="cantidad_deportes", title="Cantidad de deportes por tipo")
st.plotly_chart(fig, use_container_width=True)

# --- Capa Speed (Tiempo real) ---
st.subheader("⚡ Capa Speed: Recomendaciones en tiempo real")

col1, col2, col3 = st.columns(3)
with col1:
    tipo = st.selectbox("Tipo de deporte", ["", "Individual", "Grupal"])
with col2:
    categoria = st.selectbox("Categoría", ["", "Exterior", "Interior", "Piscina", "Nieve", "Urbano"])
with col3:
    dificultad = st.selectbox("Nivel de dificultad", ["", "Fácil", "Media"])

if st.button("🎯 Obtener recomendaciones"):
    recs = recomendacion_rapida(df, tipo, categoria, dificultad)
    if recs.empty:
        st.warning("No se encontraron coincidencias con esos filtros.")
    else:
        st.success("Recomendaciones encontradas:")
        st.dataframe(recs, use_container_width=True)

# --- Información adicional ---
st.markdown("---")
st.markdown("Desarrollado con 🧠 Arquitectura Lambda + MongoDB + Streamlit Cloud")
