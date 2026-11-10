import streamlit as st
import pandas as pd

st.title("Mi Primera App")
st.write("Bienvenido a mi primera aplicación con python")
st.markdown("### Aprendiendo streamlit en visual ###")
st.write("Esta aplicacion muestra informacion de pagina web")

promedio = 4.2
st.write("el promedio es:", promedio)

datos = pd.DataFrame({
    "Estudiante" : ["Juan", "Maria"],
    "Notas" : [4.6,2.1]
})

st.dataframe(datos)

st.table(datos)

if st.button("Mostrar mensaje"):
    st.write("Boton oprimido")

notas = st.slider("Seleccione una nota",
                  min_value=0.0,
                  max_value=5.0,
                  value=3.0,
                  step=0.1)
st.write("La nota seleccionada:", notas)

carrera = st.selectbox("Seleccione una sola carrera",
                       ["ciencia de datos", "sistemas","civil","arquitectura"])
st.write("carrera seleccionada:", carrera)

carrera = st.multiselect("Seleccione una sola carrera",
                       ["ciencia de datos", "sistemas","civil","arquitectura"])
st.write("carrera seleccionada:", carrera)

nombre = st.text_input("escribe tu nombre")
if nombre: 
    st.write("Hola", nombre)



archivo = st.file_uploader(
    "carga un archivo CSV",
    type=["csv"]
)

if archivo:
    datos = pd.read_csv(archivo)
    st.dataframe(datos)