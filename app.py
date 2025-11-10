import streamlit as st
import pandas as pd
import plotly.express as px
from utils_mongo import conectar_mongo, obtener_datos
from lambda_batch import procesar_batch
from lambda_speed import recomendacion_rapida

# ---------------------------
# 🧩 CONFIGURACIÓN GENERAL
# ---------------------------
st.set_page_config(
    page_title="🏋️ Sistema Recomendador de Deportes (Lambda + MongoDB)",
    layout="wide",
    page_icon="🏅"
)

st.title("🏋️ Sistema Recomendador de Deportes")
st.markdown("### Arquitectura Lambda + MongoDB Atlas + Streamlit Cloud")

# ---------------------------
# 🔗 CONEXIÓN A MONGODB
# ---------------------------
try:
    # 🔒 La URI se almacena en los secretos de Streamlit Cloud (/.streamlit/secrets.toml)
    MONGO_URI = st.secrets["mongodb+srv://freddy_db_user:freddy1991@cluster0.fjs355s.mongodb.net/"]["mongodb+srv://freddy_db_user:freddy1991@cluster0.fjs355s.mongodb.net/"]

    # Conectar con la base de datos y colección correctas
    coleccion = conectar_mongo(MONGO_URI, "recomendador_Deportes", "Deportes")
    df = obtener_datos(coleccion)

    if df.empty:
        st.warning("⚠️ No se encontraron datos en la colección de MongoDB.")
    else:
        st.success("✅ Conexión exitosa con MongoDB.")

except Exception as e:
    st.error(f"❌ Error al conectar con MongoDB: {e}")
    st.stop()

# ---------------------------
# 🧮 CAPA BATCH (Procesamiento histórico)
# ---------------------------
st.subheader("📊 Capa Batch: Procesamiento histórico")

try:
    resumen = procesar_batch(df)
    if resumen.empty:
        st.warning("No se pudo generar el resumen de datos.")
    else:
        fig = px.bar(
            resumen,
            x="tipo",
            y="cantidad_deportes",
            title="Cantidad de deportes por tipo",
            color="tipo",
            text_auto=True
        )
        st.plotly_chart(fig, use_container_width=True)
except Exception as e:
    st.error(f"Error en el procesamiento batch: {e}")

# ---------------------------
# ⚡ CAPA SPEED (Recomendaciones en tiempo real)
# ---------------------------
st.subheader("⚡ Capa Speed: Recomendaciones en tiempo real")

col1, col2, col3 = st.columns(3)

with col1:
    tipo = st.selectbox("Tipo de deporte", ["", "Individual", "Grupal"])
with col2:
    categoria = st.selectbox("Categoría", ["", "Exterior", "Interior", "Piscina", "Nieve", "Urbano"])
with col3:
    dificultad = st.selectbox("Nivel de dificultad", ["", "Fácil", "Media"])

if st.button("🎯 Obtener recomendaciones"):
    try:
        recs = recomendacion_rapida(df, tipo, categoria, dificultad)
        if recs.empty:
            st.warning("No se encontraron coincidencias con esos filtros.")
        else:
            st.success(f"🎉 Se encontraron {len(recs)} recomendaciones:")
            st.dataframe(recs, use_container_width=True)
    except Exception as e:
        st.error(f"Error al generar las recomendaciones: {e}")

# ---------------------------
# 🧾 INFORMACIÓN ADICIONAL
# ---------------------------
st.markdown("---")
st.markdown("Desarrollado con 🧠 Arquitectura Lambda + MongoDB + Streamlit Cloud")
st.caption("© 2025 - Proyecto educativo de recomendación de deportes")
