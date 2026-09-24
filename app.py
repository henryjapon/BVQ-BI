import streamlit as st
st.title("Bolsa de valores Quito BI")
st.sidebar.title("Parametros")
st.write("Elaborado por: Henry Japon")

archivo = st.file_uploader("Cargue su archivo")

if archivo is not None:
  tabla = pd.read_csv(archivo)
  st.write(tabla)
