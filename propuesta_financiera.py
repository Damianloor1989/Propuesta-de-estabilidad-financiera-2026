import streamlit as st
import pandas as pd
import numpy as np

# 1. CONFIGURACIÓN DE IDENTIDAD VISUAL
st.set_page_config(page_title="Propuesta Ejecutiva - Asistente de Crédito", layout="wide")

st.markdown("""
<style>
    .main { background-color: #f0f2f6; }
    .stMetric { background-color: #ffffff; padding: 20px; border-radius: 15px; border: 1px solid #d1d5db; box-shadow: 0px 4px 6px rgba(0,0,0,0.05); }
    h1, h2, h3 { color: #1e3a8a; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    .justificacion { background-color: #e0f2fe; padding: 20px; border-radius: 10px; border-left: 5px solid #0369a1; }
</style>
""", unsafe_allow_html=True)

# 2. ENCABEZADO PERSONALIZADO
st.title("💼 Plan de Fortalecimiento y Estabilidad Financiera")
st.subheader("Solicitante: [Damian Loor Guerrero")
st.markdown("**Cargo:** Asistente de Crédito | **Trayectoria:** 13 años de servicio ininterrumpido")
st.markdown("---")

# 3. SECCIÓN DE LOGROS (Puntos de personalización manual)
st.header("📈 Rendimiento y Aporte Técnico")
col_logro1, col_logro2, col_logro3 = st.columns(3)

with col_logro1:
    st.metric(label="Experiencia", value="13 Años", delta="Estabilidad")
with col_logro2:
    st.metric(label="Efectividad", value="98%", delta="Precisión")
with col_logro3:
    st.metric(label="Gestión", value="Manabí", delta="Dominio Regional")


# 4. BARRA LATERAL: PARÁMETROS FINANCIEROS (Cambios manuales aquí)
st.sidebar.header("⚙️ Configuración de la Propuesta")

st.sidebar.subheader("Laboral")
salario_base = st.sidebar.number_input("Salario Actual ($)", value=750.0) # CAMBIAR AQUÍ
pct_aumento = st.sidebar.slider("Aumento solicitado (%)", 5, 15, 6) # CAMBIAR AQUÍ
salario_nuevo = salario_base * (1 + pct_aumento / 100)

st.sidebar.subheader("Crédito Hipotecario")
tipo_tabla = st.sidebar.selectbox("Tabla de Amortización", ["Francesa (Cuota Fija)", "Alemana (Amortización Fija)"])
monto_credito = st.sidebar.number_input("Monto Solicitado ($)", value=50000.0) # CAMBIAR AQUÍ
tasa_anual = st.sidebar.slider("Tasa de Interés (%)", 8.5, 12.0, 9.5)
plazo_anios = st.sidebar.slider("Plazo (Años)", 5, 25, 20)

st.sidebar.subheader("Seguros de Ley")
seguro_desgravamen = st.sidebar.number_input("Tasa Desgravamen (%)", value=0.05, format="%.3f")
seguro_incendio = st.sidebar.number_input("Tasa Incendio/Aliados (%)", value=0.02, format="%.3f")

# 5. LÓGICA DE AMORTIZACIÓN Y SEGUROS
i = (tasa_anual / 100) / 12
n = plazo_anios * 12
seguro_fijo = monto_credito * ((seguro_desgravamen + seguro_incendio) / 100)

if "Francesa" in tipo_tabla:
    cuota_base = (monto_credito * i) / (1 - (1 + i)**-n)
    cuota_inicial_total = cuota_base + seguro_fijo
else: # Alemana
    cuota_inicial_total = (monto_credito / n) + (monto_credito * i) + seguro_fijo

# 6. ANÁLISIS DE CAPACIDAD DE PAGO (56% de relación actual)
st.header("🔄 Optimización del Riesgo Financiero")
c1, c2 = st.columns(2)

with c1:
    st.subheader("Situación Sin Consolidar")
    st.metric("Relación Cuota/Ingreso Actual", "56%", delta="Exceso de carga", delta_color="inverse")
    st.write("La carga actual dispersa compromete el flujo de caja personal.")

with c2:
    relacion_nueva = (cuota_inicial_total / salario_nuevo) * 100
    st.subheader("Situación Proyectada")
    st.metric("Nueva Relación Cuota/Ingreso", f"{relacion_nueva:.1f}%", delta=f"{relacion_nueva - 56:.1f}% Mejora")
    if relacion_nueva < 40:
        st.success("✅ Nivel de riesgo Manejable.")

# 7. JUSTIFICACIÓN Y CIERRE
st.markdown("---")
st.markdown(f"""
<div class="justificacion">
    <h3>Justificación Técnica</h3>
    <p>Tras 13 años de experiencia en la institución, presento este análisis de viabilidad para unificar pasivos y mejorar mi vivienda. 
    Al reducir mi carga financiera del <b>56%</b> a un <b>{relacion_nueva:.1f}%</b>, garantizo el cumplimiento puntual de mis obligaciones 
    y refuerzo mi compromiso a largo plazo con la Institucion.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align: center; color: gray; font-size: 0.8em; margin-top: 30px;">
    <i>Generado mediante análisis técnico de crédito y herramientas de automatización Python.</i>
</div>
""", unsafe_allow_html=True)
