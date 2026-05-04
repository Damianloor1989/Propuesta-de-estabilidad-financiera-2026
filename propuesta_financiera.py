import streamlit as st
import pandas as pd
import numpy as np

# Configuración de página con estilo profesional
st.set_page_config(page_title="Propuesta de Crecimiento y Estabilidad Financiera", layout="wide")

# Estilos CSS personalizados para un look financiero
st.markdown("""
<style>
    .main { background-color: #f8f9fa; }
    .stMetric { 
        background-color: #ffffff; 
        padding: 20px; 
        border-radius: 12px; 
        border: 1px solid #e0e0e0;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
    }
    h1, h2 { color: #1e3a8a; }
</style>
""", unsafe_allow_html=True)


# Encabezado
st.title("💼 Propuesta de Evolución Salarial y Estabilidad Patrimonial")
st.subheader("Presentado por: Damian Loor Guerrero - Asistente de Crédito")
st.markdown(f"**Trayectoria Institucional:** 13 años de compromiso y resultados.")

st.markdown("---")

# --- SECCIÓN 1: TRAYECTORIA Y VALOR ---
st.header("📈 Rendimiento y Aporte de Experiencia")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Servicios prestados por", value="13 Años", delta="INTEGRIDAD Y ENTREGA")
with col2:
    st.metric(label="Eficiencia Operativa", value="98%", delta="Precisión en Dictámenes")
with col3:
    st.metric(label="Procesos cumplidos a Cabalidad", value="OPERATIVOS", delta="Cero errores críticos")

st.info("""
**Logros Técnicos Recientes:**
* Aprendizaje y Adaptacion rapida a cambios en procesos.
* Optimización del flujo de carga de microcréditos en el sistema interno.
* Creacion de Orden de Archivo desde cero.
""")

# --- SECCIÓN 2: SIMULADOR FINANCIERO ---
st.sidebar.header("⚙️ Parámetros de la Propuesta")
st.sidebar.markdown("---")
salario_actual = st.sidebar.number_input("Salario Mensual Actual ($)", value=750.0)
incremento = st.sidebar.slider("Ajuste Salarial Propuesto (%)", 5, 15, 6)
salario_nuevo = salario_actual * (1 + incremento/100)

st.sidebar.markdown("---")
st.sidebar.subheader("Datos del Crédito")
monto_solicitado = st.sidebar.number_input("Monto Hipotecario ($)", value=33000.0)
plazo = st.sidebar.slider("Plazo (Años)", 5, 25, 20)
tasa = st.sidebar.slider("Tasa de Interés (%)", 4.0, 11.5, 8.69)

# Cálculo de Cuota (Sistema Francés)
r = (tasa / 100) / 12
n = plazo * 12
cuota = (monto_solicitado * r) / (1 - (1 + r)**-n)

st.header("📑 Análisis de Viabilidad y Consolidación")

c1, c2 = st.columns([2, 1])

with c1:
    st.subheader("Impacto en el Flujo de Caja")
    # Simulación de deudas actuales (ejemplo ajustable)
    deudas_actuales = 457.38 
    df_comp = pd.DataFrame({
        "Escenario": ["Actual (Deudas Dispersas)", "Propuesto (Cuota Única)"],
        "Carga Financiera Mensual ($)": [deudas_actuales, cuota]
    })
    st.bar_chart(df_comp.set_index("Escenario"))

with c2:
    st.subheader("Resumen Económico")
    st.write(f"**Nuevo Salario:** ${salario_nuevo:,.2f}")
    st.write(f"**Cuota Unificada:** ${cuota:,.2f}")
    relacion = (cuota / salario_nuevo) * 100
    st.metric("Relación Cuota/Ingreso", f"{relacion:.1f}%", "- Optimizada")
    st.caption("Una relación menor al 40% garantiza solvencia y bajo riesgo para la institución.")

# --- SECCIÓN 3: PROYECTO DE MEJORA ---
st.header("🏠 Inversión en Activo Fijo (Garantía)")
st.write("El crédito permitirá consolidar pasivos y mejorar el inmueble, aumentando la plusvalía de la garantía hipotecaria:")

mejoras = {
    "Rubro de Inversión": ["Consolidación de Deudas Largo Plazo (Hipiteca BIESS)", "Consolidación de Deudas Corto Plazo (CREDITO PERSONAL Y QUIROGRAFARIOS)","Remodelación Vivienda", "Gastos Legales"],
    "Monto Estimado ($)": [monto_solicitado*0.61, monto_solicitado*0.27, monto_solicitado*0.1, monto_solicitado*0.02]
}
st.table(pd.DataFrame(mejoras))

st.markdown("---")
st.markdown("""
<div style="text-align: center;">
    <p><i>"Mi objetivo es alinear mi estabilidad economica familiar con mi proyección profesional a largo plazo en esta institución."</i></p>
</div>
""", unsafe_allow_html=True)
