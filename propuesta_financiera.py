import streamlit as st
import pandas as pd
import numpy as np

# Configuración de página
st.set_page_config(page_title="Propuesta Financiera Avanzada", layout="wide")

# Estilos CSS
st.markdown("""
<style>
    .main { background-color: #f4f7f6; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; border: 1px solid #d1d5db; }
    h1, h2, h3 { color: #064e3b; }
</style>
""", unsafe_allow_html=True)

st.title("📊 Análisis de Consolidación y Estabilidad Financiera")
st.markdown(f"**Postulante:** Asistente de Crédito (13 años de trayectoria)")
st.markdown("---")

# --- SIDEBAR: PARÁMETROS BANCARIOS REALES ---
st.sidebar.header("⚙️ Configuración del Crédito")
tipo_tabla = st.sidebar.selectbox("Tipo de Amortización", ["Francesa (Cuota Fija)", "Alemana (Cuota Decreciente)"])

monto = st.sidebar.number_input("Monto del Crédito ($)", value=25000.0)
plazo_años = st.sidebar.slider("Plazo (Años)", 5, 25, 15)
tasa_anual = st.sidebar.slider("Tasa de Interés Anual (%)", 8.0, 11.5, 9.5)

st.sidebar.subheader("🛡️ Seguros Obligatorios")
tasa_desgravamen = st.sidebar.number_input("Tasa Desgravamen Mensual (%)", value=0.05, format="%.3f")
tasa_incendio = st.sidebar.number_input("Tasa Incendio/Aliados Mensual (%)", value=0.02, format="%.3f")

salario_propuesto = st.sidebar.number_input("Salario Propuesto ($)", value=1200.0)

# --- CÁLCULOS FINANCIEROS ---
n = plazo_años * 12
i = (tasa_anual / 100) / 12
seguro_mensual = monto * ((tasa_desgravamen + tasa_incendio) / 100)

if "Francesa" in tipo_tabla:
    cuota_base = (monto * i) / (1 - (1 + i)**-n)
    cuota_total_inicial = cuota_base + seguro_mensual
else: # Alemana
    amortizacion_fija = monto / n
    interes_inicial = monto * i
    cuota_total_inicial = amortizacion_fija + interes_inicial + seguro_mensual

# --- SECCIÓN 1: COMPARATIVA DE CAPACIDAD DE PAGO ---
st.header("🔄 Optimización del Endeudamiento")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Situación Actual")
    st.metric("Relación Cuota/Ingreso Actual", "56%", delta="Exceso de carga", delta_color="inverse")
    st.warning("⚠️ La carga financiera actual limita la capacidad de ahorro y estabilidad.")

with col2:
    relacion_nueva = (cuota_total_inicial / salario_propuesto) * 100
    st.subheader("Situación Proyectada")
    st.metric("Nueva Relación Cuota/Ingreso", f"{relacion_nueva:.1f}%", delta=f"{relacion_nueva - 56:.1f}% Mejora", delta_color="normal")
    if relacion_nueva < 40:
        st.success("✅ Relación óptima bajo estándares bancarios (<40%).")

# --- SECCIÓN 2: TABLA DE AMORTIZACIÓN ---
st.header(f"📅 Proyección de Pagos ({tipo_tabla})")

# Generar Tabla
tabla_data = []
saldo = monto
for mes in range(1, n + 1):
    interes_mes = saldo * i
    seguros_mes = saldo * ((tasa_desgravamen + tasa_incendio) / 100) # Ajustado al saldo insoluto
    
    if "Francesa" in tipo_tabla:
        cuota_capital = cuota_base - interes_mes
    else:
        cuota_capital = monto / n
    
    pago_total = cuota_capital + interes_mes + seguros_mes
    saldo -= cuota_capital
    
    if mes <= 12: # Solo mostrar el primer año por brevedad
        tabla_data.append([mes, cuota_capital, interes_mes, seguros_mes, pago_total, max(saldo, 0)])

df_tabla = pd.DataFrame(tabla_data, columns=["Mes", "Capital ($)", "Interés ($)", "Seguros ($)", "Cuota Total ($)", "Saldo Pendiente ($)"])
st.write("**Proyección del Primer Año:**")
st.table(df_tabla.style.format("{:.2f}"))

# --- SECCIÓN 3: JUSTIFICACIÓN ---
st.markdown("---")
st.subheader("📝 Sustento Técnico")
st.write(f"""
Esta propuesta busca reducir mi exposición financiera del **56% actual** a un manejable **{relacion_nueva:.1f}%**. 
Al consolidar deudas mediante un crédito hipotecario con seguros de ley (Desgravamen e Incendio), 
garantizo la cobertura total de la operación y la protección del patrimonio que sirve como garantía institucional.
""")

st.markdown("""
<div style="text-align: center; padding: 20px;">
    <p><i>13 años de experiencia respaldan mi capacidad para gestionar este compromiso con responsabilidad.</i></p>
</div>
""", unsafe_allow_html=True)
