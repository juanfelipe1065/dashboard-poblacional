import streamlit as st
import pandas as pd

st.title("sistema de calificaciones")
st.write("consulte y registre sus materias con sus respectivas notas")

st.markdown("### mis materias")

datos = {
    "Materia":["logica","calculo","introduccion","filosofia","algebra"],
    "calificacion":[2.0,2.1,4.5,4.5,3.0]
}

tabla = pd.DataFrame(datos)
st.dataframe(tabla)

promedio = tabla["calificacion"].mean()

st.write("promedio actual: ", round(promedio,2))

st.markdown("### cree una nueva materia")
nueva_materia = st.text_input("ingrese la nueva materia")

nueva_calificacion = st.slider(
    "seleccione la calificacion de la nueva materia",
    min_value=0.0,
    max_value=5.0,
    value=3.0,
    step=0.1
)

if st.button("agregar materia"):

    if nueva_materia != "":
        materia = {
            "Materia": nueva_materia,
            "calificacion": nueva_calificacion
        }

    nueva_fila = pd.DataFrame([materia])

    nueva_tabla = pd.concat([tabla, nueva_fila], ignore_index=True)

    st.success("materia agregada correctamente")

    st.dataframe(nueva_tabla)

    promedio = nueva_tabla["calificacion"].mean()

else:
    st.warning("debes escribir el nombre de la materia")

