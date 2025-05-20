import streamlit as st
import pandas as pd
import plotly.express as plt
import seaborn as sns
# URLs de los archivos CSV 
barreras_por_pais_url=https://github.com/JosephRojas-UNA/dashboard-zapateria/tree/main 
demanda_potencial_url=https://github.com/JosephRojas-UNA/dashboard-zapateria/commits?author=JosephRojas-UNA
riesgo_pais_url=https://github.com/JosephRojas-UNA/dashboard-zapateria/tree/main
ventas_url=https://github.com/JosephRojas-UNA/dashboard-zapateria/commits?author=JosephRojas-UNA
barreras_por_pais=pd.read_csv(barreras_por_pais_url) 
demanda_potencial=pd.read_csv(demanda_potencial_url) 
riesgo_pais=pd.read_csv(riesgo_pais_url) 
ventas=pd.read_csv(ventas_url) 
# Título del Dashboard 
st.title("Dashboard Interactivo de riesgo_pais de Chocolates") 
# Filtro de país 
paises = riesgo_pais["País"].unique() 
pais_seleccionado = st.selectbox("Selecciona un país para ver los detalles", paises) 
# Mostrar datos de barreras_por_pais
st.subheader("barreras_por_pais") 
barreras_por_pais_filtrados = barreras_por_pais[barreras_por_pais["País"] == pais_seleccionado] 
st.dataframe(barreras_por_pais_filtrados) 
# Mostrar datos de riesgo_pais
st.subheader("riesgo_pais de Chocolates") 
riesgo_pais_filtradas = riesgo_pais [riesgo_pais["País"] == pais_seleccionado] 
fig, ax = plt.subplots() 
ax.bar(riesgo_pais_filtradas["País"], riesgo_pais_filtradas["riesgo_pais (USD millones)"], color='#2E86C1') 
ax.set_xlabel("País") 
ax.set_ylabel("riesgo_pais (USD millones)") 
ax.set_title(f"riesgo_pais de Chocolates en {pais_seleccionado}") 
plt.xticks(rotation=45) 
st.pyplot(fig) 
# Mostrar datos de demanda_potencial 
st.subheader("Segmentos de Mercado") 
demanda_potencial_filtrados = demanda_potencial[demanda_potencial["País"] == pais_seleccionado] 
st.dataframe(demanda_potencial_filtrados) 
# Mostrar ventas
st.subheader("ventas") 
ventas_filtradas = ventas[ventas["País"] == pais_seleccionado] 
st.dataframe(ventas_filtradas) 
# Análisis Comparativo 
st.subheader("Análisis Comparativo") 
fig2, ax2 = plt.subplots(figsize=(8, 5)) 
ax2.bar(demanda_potencial["País"], demanda_potencial["Tamaño del Mercado (USD millones)"], 
color='#F39C12') 
ax2.set_xlabel("País") 
ax2.set_ylabel("Tamaño del Mercado (USD millones)") 
ax2.set_title("Comparación de Tamaños de Mercado") 
plt.xticks(rotation=45) 
st.pyplot(fig2)
