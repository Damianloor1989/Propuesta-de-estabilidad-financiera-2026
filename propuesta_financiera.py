import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# 1. CONFIGURACIÓN Y ESTILO
st.set_page_config(page_title="Propuesta Financiera - Consolidación BIESS", layout="wide")

st.markdown("""
<style>
    .main { background-color: #f8fafc; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 12px; border: 1px solid #e2e8f0; }
    h1, h2, h3 { color: #1e3a8a; }
    .seccion-biess { background-color: #eff6ff; padding: 20px; border-radius: 10px; border-left: 5px solid #2563eb; }
</style>
""", unsafe_allow_html=True)

# 2. ENCABEZADO
st.title("💼 Estrategia de Optimización Crediticia y Estabilidad Financiera")
st.subheader("Solicitante: Damian Loor | Asistente de Crédito (13 años)")
st.markdown("---")

# 3. PARÁMETROS DE ENTRADA (SIDEBAR)
st.sidebar.header("📊 Parámetros del Análisis")

# Datos Laborales
salario_base = st.sidebar.number_input("Salario Actual ($)", value=850.0)
pct_aumento = st.sidebar.slider("Aumento solicitado (%)", 5, 40, 15)
salario_nuevo = salario_base * (1 + pct_aumento / 100)

# Datos del Crédito Nuevo
st.sidebar.markdown("---")
st.sidebar.subheader("Nuevo Crédito Consolidado")
monto_solicitado = st.sidebar.number_input("Monto Total Proyectado ($)", value=30000.0)
plazo_anios = st.sidebar.slider("Plazo (Años)", 5, 25, 15)
tasa_anual = st.sidebar.slider("Tasa Interés Anual (%)", 8.0, 11.5, 9.5)
tipo_tabla = st.sidebar.selectbox("Sistema de Amortización", ["Francesa (Cuota Fija)", "Alemana (Cuota Decreciente)"])

# Seguros
tasa_seguros = st.sidebar.number_input("Seguros (Desgravamen + Incendio) % mensual", value=0.07, format="%.3f")

# --- CÁLCULOS FINANCIEROS ---
cuota_actual = 457.38  # VALOR EXACTO SOLICITADO
i = (tasa_anual / 100) / 12
n = plazo_anios * 12
seguro_mensual = monto_solicitado * (tasa_seguros / 100)

if "Francesa" in tipo_tabla:
    pago_mensual_base = (monto_solicitado * i) / (1 - (1 + i)**-n)
else:
    pago_mensual_base = (monto_solicitado / n) + (monto_solicitado * i)

cuota_nueva_total = pago_mensual_base + seguro_mensual

# 4. DASHBOARD DE INDICADORES
st.header("📈 Comparativa de Carga Financiera")
c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Cuota Actual Total", f"${cuota_actual:,.2f}", delta="Carga Dispersa", delta_color="inverse")
with c2:
    st.metric("Nueva Cuota Unificada", f"${cuota_nueva_total:,.2f}", delta=f"${cuota_nueva_total - cuota_actual:,.2f} Diferencia")
with c3:
    relacion_actual = (cuota_actual / salario_base) * 100
    relacion_nueva = (cuota_nueva_total / salario_nuevo) * 100
    st.metric("Relación Cuota/Ingreso", f"{relacion_nueva:.1f}%", delta=f"{relacion_nueva - 56:.1f}% vs Actual")

# 5. VISUALIZACIONES (GRÁFICOS)
st.markdown("---")
col_graf1, col_graf2 = st.columns(2)

with col_graf1:
    st.subheader("Comparativo de Flujo Mensual ($)")
    df_barras = pd.DataFrame({
        "Escenario": ["Situación Actual", "Propuesta Consolidada"],
        "Valor Mensual": [cuota_actual, cuota_nueva_total],
        "Color": ["#ef4444", "#22c55e"]
    })
    fig_bar = px.bar(df_barras, x="Escenario", y="Valor Mensual", color="Escenario",
                     color_discrete_map={"Situación Actual": "#ef4444", "Propuesta Consolidada": "#22c55e"})
    st.plotly_chart(fig_bar, use_container_width=True)

with col_graf2:
    st.subheader("Distribución del Plan de Inversión")
    # Plan de inversión personalizado para el BIESS
    inversion_data = {
        "Destino": ["Hipotecario BIESS", "Quirografarios BIESS", "Créditos Personales", "Mejoras Vivienda"],
        "Monto": [monto_solicitado * 0.50, monto_solicitado * 0.20, monto_solicitado * 0.15, monto_solicitado * 0.15]
    }
    fig_pie = px.pie(pd.DataFrame(inversion_data), values="Monto", names="Destino", hole=0.4,
                     color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig_pie, use_container_width=True)

# 6. DETALLE DEL PLAN DE INVERSIÓN (Tabla)
st.header("📋 Plan de Inversión Detallado")
st.markdown("""
Esta estrategia contempla la liquidación total de pasivos con el **BIESS** y otras instituciones, 
transformando deudas de corto plazo en una sola obligación hipotecaria de largo plazo.
""")

df_plan = pd.DataFrame(inversion_data)
df_plan["Monto"] = df_plan["Monto"].map("${:,.2f}".format)
st.table(df_plan)

# 7. CIERRE
st.markdown(f"""
<div class="seccion-biess">
    <h3>Sustento del Asistente de Crédito</h3>
    <p>Considerando mis 13 años de experiencia en el análisis de riesgos, esta operación reduce mi exposición financiera 
    del <b>56%</b> a un nivel óptimo del <b>{relacion_nueva:.1f}%</b>. Esto no solo mejora mi liquidez familiar, 
    sino que formaliza mi patrimonio como garantía ante la institución.</p>
</div>
""", unsafe_allow_html=True)
