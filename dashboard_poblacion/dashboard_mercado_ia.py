
import pandas as pd
import numpy as np
import streamlit as st

st.title("Mercado laboral en Inteligencia Artificial")
st.write("Análisis de ofertas laborales, salarios y habilidades.")
st.divider()



def promedio(columna):
    """Calcula el promedio de una columna."""
    return np.mean(columna)


def filtrar(tabla, columna, opcion):
    """Filtra los datos según la opción seleccionada."""
    if opcion != "Todos":
        tabla = tabla[tabla[columna] == opcion]
    return tabla



archivo = st.file_uploader("Sube el archivo CSV", type="csv")

if archivo is not None:
    datos = pd.read_csv(archivo)
    st.success("Archivo cargado correctamente")

   
    st.sidebar.header("Filtros de búsqueda")

    niveles = ["Todos", "Entry", "Mid", "Senior"]
    paises = ["Todos"]

    for pais in datos["country"].unique():
        paises.append(pais)

    nivel = st.sidebar.selectbox("Experiencia", niveles)
    pais = st.sidebar.selectbox("País", paises)

    datos = filtrar(datos, "experience_level", nivel)
    datos = filtrar(datos, "country", pais)

    if len(datos) > 0:

        
        st.header("Resumen general")

        salario = datos["salary"]
        experiencia = datos["years_experience"]

        c1, c2, c3 = st.columns(3)

        c1.metric("Ofertas laborales", len(datos))
        c2.metric("Salario promedio", round(promedio(salario), 2))
        c3.metric("Años de experiencia", round(promedio(experiencia), 1))

        
        st.subheader("Estadísticas salariales")

        estadisticas = {
            "Media": round(np.mean(salario), 2),
            "Mediana": round(np.median(salario), 2),
            "Mínimo": np.min(salario),
            "Máximo": np.max(salario),
            "Desviación estándar": round(np.std(salario), 2)
        }

        for nombre in estadisticas:
            st.write(nombre, ":", estadisticas[nombre])

        st.caption("Salarios en las unidades monetarias del dataset.")
        st.divider()

        
        st.header("Análisis del mercado laboral")
        st.subheader("Salario promedio por experiencia")

        niveles = ["Entry", "Mid", "Senior"]
        salarios = {}

        for nivel in niveles:
            grupo = datos[datos["experience_level"] == nivel]

            if len(grupo) > 0:
                salarios[nivel] = promedio(grupo["salary"])

        st.bar_chart(pd.Series(salarios))

       
        años = sorted(datos["job_posting_year"].unique())
        ofertas_anuales = {}
        salarios_anuales = {}

        for año in años:
            grupo = datos[datos["job_posting_year"] == año]

            ofertas_anuales[año] = len(grupo)
            salarios_anuales[año] = promedio(grupo["salary"])

        st.subheader("Ofertas laborales por año")
        st.line_chart(pd.Series(ofertas_anuales))

        st.subheader("Evolución del salario promedio")
        st.area_chart(pd.Series(salarios_anuales))

        st.divider()

        
        st.header("Oportunidades profesionales")
        st.subheader("Cargos más frecuentes")

        cargos = datos["job_title"].value_counts()
        st.dataframe(cargos.head(6))

        st.divider()

       
        st.header("Explorador de ofertas laborales")
        st.subheader("Búsqueda por salario")

        minimo = st.slider("Salario mínimo", 0, 210000, 50000, 10000)
        ofertas = datos[datos["salary"] >= minimo]

        columnas = ["job_title", "country", "salary"]

        st.write("Ofertas encontradas:", len(ofertas))
        st.dataframe(ofertas[columnas].head(10))

       
        st.subheader("Oportunidades con Python")

        mostrar = st.checkbox("Mostrar ofertas que requieren Python")

        if mostrar:
            python = datos[datos["skills_python"] == 1]

            st.write("Ofertas con Python:", len(python))
            st.dataframe(python[columnas].head(10))

        st.divider()

        
        st.header("Exploración del dataset")
        st.write("Primeros diez registros.")
        st.dataframe(datos.head(10))

        st.divider()
        st.caption("Proyecto Integrador | Ingeniería en Datos e IA")
        st.caption("Universidad Santo Tomás | Primer semestre")

    else:
        st.warning("No hay ofertas con los filtros seleccionados.")

else:
    st.info("Sube el archivo CSV para comenzar.")
