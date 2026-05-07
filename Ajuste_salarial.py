import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Propuesta de Analisis y Ajuste Salarial", layout="wide")

st.markdown("""
<style>
    .main { background-color: #f8fafc; }
    .stMetric { background-color: #ffffff; padding: 20px; border-radius: 12px; border: 1px solid #cbd5e1; }
    .card-valor { background-color: #eff6ff; padding: 25px; border-radius: 10px; border-left: 6px solid #1e40af; }
    .card-retencion { background-color: #f0fdf4; padding: 25px; border-radius: 10px; border-left: 6px solid #16a34a; }
</style>
""", unsafe_allow_html=True)

st.title("🚀 Propuesta de Ajuste Salarial")
st.subheader("Análisis Técnico de Trayectoria - 13 Años de Experiencia")
st.markdown("---")

# SIDEBAR PARA AJUSTES
st.sidebar.header("📊 Variables de la Propuesta")
salario_base = st.sidebar.number_input("Remuneración Actual ($)", value=750.0, step=50.0)
pct_aumento = st.sidebar.slider("Ajuste Sugerido (%)", 5, 15, 6)
salario_nuevo = salario_base * (1 + pct_aumento / 100)

# MÉTRICAS DE IMPACTO
st.header("📈 Impacto del Ajuste Salarial")
c1, c2, c3 = st.columns(3)
with c1:
    st.metric("Salario Actual", f"${salario_base:,.2f}")
with c2:
    st.metric("Salario Propuesto", f"${salario_nuevo:,.2f}", delta=f"+{pct_aumento}%")
with c3:
    st.metric("Incremento Neto Mensual", f"${salario_nuevo - salario_base:,.2f}")

st.markdown("---")

# SECCIÓN DE VALOR AGREGADO
col_left, col_right = st.columns(2)

with col_left:
    st.markdown("""
    <div class="card-valor">
        <h3>💡 Valor Técnico y Operativo</h3>
        <ul>
            <li><b>Manejo de flujo operativo:</b> Ingreso, verificacion y procesamiento de operaciones de creditos individual Rural (90 operaciones promedio actualmente).</li>
            <li><b>Dominio de sistema financiero Orion:</b> 11 años asistiendo las cartera de 5 asesores con desembolsos promedio de los 11 años de 180 operaciones de credito mensuales .</li>
            <li><b>Eficiencia:</b> Adaptacion rapida y continua a nuevos procesos y mayor responsabilidad y carga laboral.</li>
<li><b>Predisposicion:</b> Desempeño con la mejor actitud y aptitud para con las directrices y recomendaciones recibidas desde el primer dia hasta el presente .</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col_right:
    st.markdown("""
    <div class="card-retencion">
        <h3>🤝 Beneficios para la Empresa</h3>
        <ul>
            <li><b>Retención de Conocimiento:</b> Continuidad de un pilar de la memoria institucional del banco.</li>
            <li><b>Liderazgo Senior:</b> Mentoría interna para analistas junior basada en experiencia probada.</li>
            <li><b>Innovación:</b> Capacidad de implementar soluciones tecnológicas sin costo externo de consultoría.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# GRÁFICO DE CRECIMIENTO PROFESIONAL
st.subheader("Proyección de Valor Institucional")
df_crecimiento = pd.DataFrame({
    "Año": ["2013", "2018", "2023", "2026 (Proyectado)"],
    "Valor para la Empresa": [20, 50, 85, 100]
})
fig = px.line(df_crecimiento, x="Año", y="Valor para la Empresa", markers=True, title="Curva de Especialización y Seniority")
st.plotly_chart(fig, use_container_width=True)

st.info("Nota: Esta propuesta busca nivelar la compensación con la alta especialización técnica demostrada durante más de una década.")
