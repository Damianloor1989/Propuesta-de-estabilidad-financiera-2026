import streamlit as st
import pandas as pd
import plotly.express as px

# 1. CONFIGURACIÓN Y ESTILO
st.set_page_config(page_title="Propuesta de Ajuste Salarial 2026", layout="wide")

st.markdown("""
<style>
    .main { background-color: #f8fafc; }
    .stMetric { background-color: #ffffff; padding: 20px; border-radius: 12px; border: 1px solid #cbd5e1; }
    .card-sustento { background-color: #f1f5f9; padding: 20px; border-radius: 10px; border-left: 6px solid #1e3a8a; }
    .card-beneficio { background-color: #f0fdf4; padding: 20px; border-radius: 10px; border-left: 6px solid #16a34a; }
    .card-peticion { background-color: #fffbeb; padding: 20px; border-radius: 10px; border-left: 6px solid #d97706; }
    h1, h2, h3 { color: #1e3a8a; }
</style>
""", unsafe_allow_html=True)

st.title("🚀 Propuesta de Estabilidad Profesional y Fortalecimiento Operativo")
st.markdown("---")

# 1. MI LABOR Y SUSTENTO DEL AUMENTO
st.header("1. Valor Técnico y Operativo (Sustento)")
col_t1, col_t2 = st.columns(2)

with col_t1:
    st.markdown("""
    <div class="card-sustento">
        <h4>💪 Capacidad de Gestión y Flujo</h4>
        <ul>
            <li><b>Manejo de Flujo Operativo Rural:</b> Ingreso, verificación y procesamiento de un promedio de <b>90 operaciones mensuales</b> actualmente.</li>
            <li><b>Dominio del Sistema Orion:</b> 11 años de experiencia técnica asistiendo las carteras de 5 y hasta 6 asesores de credito.</li>
            <li><b> Historico Desembolsos:</b> Gestión de una parte del proceso de un promedio de <b>180 operaciones de crédito mensuales</b> durante más de una década.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col_t2:
    st.markdown("""
    <div class="card-sustento">
        <h4>📈 Eficiencia y Predisposición</h4>
        <ul>
            <li><b>Adaptación Continua:</b> Capacidad probada para absorber nuevos procesos y mayores cargas laborales de forma rápida.</li>
            <li><b>Actitud Institucional:</b> Desempeño con la mejor aptitud y alineación total a las directrices recibidas desde el primer día.</li>
            <li><b>Antiguedad:</b> 13 años de experiencia que garantizan un minimo de errores en el ciclo del crédito.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# 2. BENEFICIOS (PERSONALES Y PARA LA INSTITUCIÓN)
st.markdown("---")
st.header("2. Matriz de Beneficios")
b_col1, b_col2 = st.columns(2)

with b_col1:
    st.markdown("""
    <div class="card-beneficio">
        <h4>🤝 Para la Institución</h4>
        <ul>
            <li><b>Seguridad Operativa:</b> Reducción de riesgos operativos mediante el manejo correcto de las diferentes herramientas tecnologicas de la institucion.</li>
            <li><b>Productividad Alta:</b> Procesamiento ágil de diferentes tareas requeridas (5 asesores simultáneos).</li>
            <li><b>Cero Costo de Formación:</b> Conocimiento totalmente operativo y actualizado en sistemas internos.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with b_col2:
    st.markdown("""
    <div class="card-beneficio">
        <h4>👤 Para el Colaborador</h4>
        <ul>
            <li>Reconocimiento al desempeño y la lealtad de largo plazo.</li>
            <li>Compensación alineada a la alta carga operativa actual.</li>
            <li>Herramientas para garantizar la eficiencia (Conectividad móvil).</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# 3. PETICIÓN CON VALORES Y GRÁFICOS
st.markdown("---")
st.header("3. Propuesta Económica y Requerimiento Operativo")

# Sidebar para interactividad
st.sidebar.header("Variables de la Propuesta")
aumento_pct = st.sidebar.slider("Ajuste Salarial (%)", 10, 30, 15)
salario_base = 850.0  # Puedes ajustar tu sueldo base real aquí
salario_nuevo = salario_base * (1 + aumento_pct/100)

# Petición específica del Plan de Datos
subsidio_datos = st.sidebar.radio("Subsidio Plan de Datos (Referencias WhatsApp)", 
                                  ["Sin subsidio", "50% ($5)", "100% ($10)"], index=2)

p1, p2, p3 = st.columns(3)
with p1:
    st.metric("Salario Propuesto", f"${salario_nuevo:,.2f}", delta=f"+{aumento_pct}%")
with p2:
    st.metric("Subsidio Móvil", f"{subsidio_datos}")
with p3:
    costo_datos = 10 if "100%" in subsidio_datos else (5 if "50%" in subsidio_datos else 0)
    st.metric("Total Compensación", f"${salario_nuevo + costo_datos:,.2f}")

# Gráficos
st.markdown("### Visualización de Impacto Operativo")
g_col1, g_col2 = st.columns(2)

with g_col1:
    # Gráfico de barras de operaciones
    df_ops = pd.DataFrame({
        "Actividad": ["Rural Individual (Actual)", "Promedio Orion (Histórico)"],
        "Operaciones Mensuales": [90, 180]
    })
    fig_ops = px.bar(df_ops, x="Actividad", y="Operaciones Mensuales", color="Actividad", 
                     text_auto=True, title="Volumen de Gestión Mensual")
    st.plotly_chart(fig_ops, use_container_width=True)

with g_col2:
    # Gráfico de eficiencia con/sin datos
    df_ef = pd.DataFrame({
        "Condición": ["Sin Plan de Datos", "Con Plan de Datos (100%)"],
        "Eficiencia en Validación": [60, 100]
    })
    fig_ef = px.line(df_ef, x="Condición", y="Eficiencia en Validación", markers=True, 
                     title="Impacto del Plan de Datos en Verificación de Referencias")
    st.plotly_chart(fig_ef, use_container_width=True)

st.markdown(f"""
<div class="card-peticion">
    <b>Justificación Técnica del Plan de Datos:</b> Dada la naturaleza de las 90 operaciones rurales mensuales, la validación inmediata 
    de referencias vía WhatsApp es un paso crítico. El subsidio del 100% ($10) garantiza que el flujo de trabajo sea continuo, 
    permitiendo una respuesta inmediata a los asesores y clientes.
</div>
""", unsafe_allow_html=True)
