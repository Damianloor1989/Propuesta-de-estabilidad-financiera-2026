import streamlit as st
import pandas as pd
import plotly.express as px

# 1. CONFIGURACIÓN Y ESTILO
st.set_page_config(page_title="Propuesta Financiera Consolidacion Biess", layout="wide")

st.markdown("""
<style>
    .main { background-color: #f8fafc; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 12px; border: 1px solid #e2e8f0; }
    .benefit-card { background-color: #f0fdf4; padding: 20px; border-radius: 10px; border-left: 5px solid #16a34a; margin-bottom: 20px; }
    .salary-card { background-color: #fff7ed; padding: 20px; border-radius: 10px; border-left: 5px solid #ea580c; }
    h1, h2, h3 { color: #1e3a8a; }
</style>
""", unsafe_allow_html=True)

# 2. ENCABEZADO
st.title("💼 Propuesta de Optimización y Estabilidad Financiera")
st.subheader("Solicitante: Damian Loor Guerrero | Asistente de Crédito (13 años)")
st.markdown("---")

# 3. PARÁMETROS DE ENTRADA (SIDEBAR)
st.sidebar.header("📊 Parámetros del Análisis")

# Salario con salto de 100 en 100 o manual
salario_base = st.sidebar.number_input("Salario Actual ($)", value=750.0, step=50.0)
# Crédito con salto de 1000 en 1000
monto_solicitado = st.sidebar.number_input("Monto Total Proyectado ($)", value=33000.0, step=1000.0)

pct_aumento = st.sidebar.slider("Aumento solicitado (%)", 5, 15, 6)
salario_nuevo = salario_base * (1 + pct_aumento / 100)

st.sidebar.markdown("---")
plazo_anios = st.sidebar.slider("Plazo (Años)", 5, 30, 20)
tasa_anual = st.sidebar.slider("Tasa Interés Anual (%)", 3.0, 11.0, 8.6)
tipo_tabla = st.sidebar.selectbox("Sistema de Amortización", ["Francesa (Cuota Fija)", "Alemana (Cuota Decreciente)"])
tasa_seguros = st.sidebar.number_input("Seguros % mensual", value=0.07, format="%.3f")

# --- CÁLCULOS ---
cuota_actual = 457.38 
i = (tasa_anual / 100) / 12
n = plazo_anios * 12
seguro_mensual = monto_solicitado * (tasa_seguros / 100)

if "Francesa" in tipo_tabla:
    pago_mensual_base = (monto_solicitado * i) / (1 - (1 + i)**-n)
else:
    pago_mensual_base = (monto_solicitado / n) + (monto_solicitado * i)

cuota_nueva_total = pago_mensual_base + seguro_mensual

# 4. SECCIÓN: MEJORA SALARIAL
st.header("💵 Análisis de Mejora Salarial")
col_s1, col_s2, col_s3 = st.columns(3)

with col_s1:
    st.metric("Salario Actual", f"${salario_base:,.2f}")
with col_s2:
    st.metric("Salario Propuesto", f"${salario_nuevo:,.2f}", delta=f"+{pct_aumento}%")
with col_s3:
    st.metric("Incremento Neto", f"${salario_nuevo - salario_base:,.2f}")

st.markdown(f"""
<div class="salary-card">
    <p>
        <b>Impacto del Ajuste:</b> Este incremento y Crédito Hipotecario permite que la nueva relación cuota/ingreso sea de 
        <b>{(cuota_nueva_total/salario_nuevo)*100:.1f}%</b>, garantizando una mejora en mi ingreso neto mensual ya que al momento esta en el 56%.
    </p>
    <hr style="border: 0; border-top: 1px solid #eee; margin: 10px 0;">
    <p>
        <b>Cambio en plan de datos móviles:</b> Ajuste en el subsidio del 50% del plan de datos móviles al 100% por llamadas a Referencias vía WhatsApp.
    </p>
</div>
""", unsafe_allow_html=True)

# 5. VISUALIZACIONES (GRÁFICOS)
st.markdown("---")
col_graf1, col_graf2 = st.columns(2)

with col_graf1:
    st.subheader("Reducción de Carga Financiera ($)")
    fig_bar = px.bar(x=["Actual", "Propuesta"], y=[cuota_actual, cuota_nueva_total], 
                     color=["Actual", "Propuesta"], color_discrete_map={"Actual": "#ef4444", "Propuesta": "#22c55e"})
    st.plotly_chart(fig_bar, use_container_width=True)

with col_graf2:
    st.subheader("Distribución del Crédito")
    inversion_data = {"Destino": ["BIESS Hipotecario", "Quirografarios y Personal", "Mejoras y Costos Legales"], 
                      "Monto": [monto_solicitado*0.63, monto_solicitado*0.27, monto_solicitado*0.1]}
    fig_pie = px.pie(pd.DataFrame(inversion_data), values="Monto", names="Destino", hole=0.4)
    st.plotly_chart(fig_pie, use_container_width=True)

# 6. BENEFICIOS PARA LA INSTITUCIÓN
st.header("🤝 Valor Agregado para la Institución")
st.markdown("""
<div class="benefit-card">
    <h4>¿Por qué esta propuesta es beneficiosa para la Institucion?</h4>
    <ul>
        <li><b>Talento Humano:</b> Asegura la permanencia de un Asistente de Crédito con experiencia.</li>
        <li><b>Mitigación de Riesgos:</b> La consolidación elimina el estrés financiero del colaborador, aumentando la productividad y el enfoque.</li>
        <li><b>Garantía Real:</b> El crédito es de bajo riesgo ya que se respalda con un activo fijo (vivienda).</li>
</div>
""", unsafe_allow_html=True)

st.info("Nota: Los cálculos incluyen Seguros de Desgravamen e Incendio los mismos que se pueden ajustar al % que estipule la Institucion.")
