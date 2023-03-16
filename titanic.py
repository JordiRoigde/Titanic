#--------------------LIBRERÍAS----------------------------#
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly_express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st 
import plotly.offline as pyo

#--------------------CONFIGURACIÓN DE LA PÁGINA----------------------------#
#layout="centered" or "wide"
st.set_page_config(page_title="TITANIC", layout="wide", page_icon="🚢")
st.set_option('deprecation.showPyplotGlobalUse', False)

#--------------------LEEMOS LOS DATAFRAMES----------------------------#
df = pd.read_csv(r"data/titanic.csv")
if "Unnamed: 0" in df:
    df = df.drop(columns = ['Unnamed: 0']) 
else:
    pass
df_limpio = pd.read_csv(r"data/titanic_limpio.csv")
if "Unnamed: 0" in df_limpio:
    df_limpio = df_limpio.drop(columns = ['Unnamed: 0'])
else:
    pass 
#--------------------LOGO+CREACIÓN DE COLUMNA----------------------------#
st.image("img/baner.jpg",  use_column_width=True)
col1,col2,col3 = st.columns(3)
with col1:
    st.title("")
with col2:
    st.title("")
with col3:
    st.title("")
#--------------------TITLE + PRESENTACIÓN----------------------------#
col1,col2,col3 = st.columns(3)
st.title("DATASET DE TITANIC")


#--------------------COSAS QUE VAMOS A USAR EN TODA LA APP----------------------------#
def extraer_titulo(name): 
    buca_titulo = re.search(' ([A-Za-z]+)\.', name)
    if buca_titulo:
        return buca_titulo.group(1)
    return 

#--------------------SIDEBAR----------------------------#
st.sidebar.image("img/titanic.png", width=150)
st.sidebar.title("MENÚ")
st.sidebar.subheader("Naveguemos juntos por aquí")
st.sidebar.write("----")
output = st.empty()

if st.sidebar.button("Dataset Original"):
    
    st.markdown(""" <div style='color:white; font-size: 30px; text-align: justify;'> Con el objetivo de asegurar la fiabilidad de los resultados, inicialmente se ha realizado una limpieza y preparación de los datos que se nos han facilitado.<br>
                Una vez completada esta primera fase de la investigación, procedimos a analizar los datos en detalle. A través de diferentes cálculos matemáticos y técnicas estadísticas, hemos obtenido una visión más profunda de los patrones y tendencias presentes en el dataset. <br>
                Por último, hemos creado varios gráficos de visualización de datos a través de los cuales podemos observar los resultados de una manera clara, útil y visualmente más atractiva. Estas representaciones nos ayudan a observar relaciones entre las variables y patrones que no eran evidentes a simple vista y proporcionan una mayor comprensión del dataset.<br><br>                              
                </div> """, unsafe_allow_html=True)
    st.subheader("Éste es el Dataset que nos han facilitado:")   
    st.dataframe(df)
 #--------------------SIDEBAR2----------------------------#   

if st.sidebar.button("Dataset Limpio"):
    st.header("Este es el dataset una vez pasada la limpieza y preparación:")
    st.dataframe(df_limpio)
    
#--------------------SIDEBAR3----------------------------#

if st.sidebar.button("Curiosidades"):
    st.text("Muestro un pequeño resumen, para dar inciso a algunos datos que vemos a primera vista:")
    code="df_limpio.describe()"
    st.code(code,language="python")
    st.write(df_limpio.describe())
    
    sex_counts = df_limpio["Sexo"].value_counts()
    sexoplot = px.pie(
        values=sex_counts.values, 
        names=sex_counts.index, 
        title="Distribución de Hombres y Mujeres en el Titanic"
    )
    st.plotly_chart(sexoplot, use_container_width=True)
    
    sex_counts = df_limpio["Sobrevivio"].value_counts()
    vivioplot = px.pie(
        values=sex_counts.values, 
        names=sex_counts.index, 
        title="Supervivencia"
    )
    st.plotly_chart(vivioplot, use_container_width=True)
    
    
    sex_counts = df_limpio["Titulo"].value_counts()
    tituplot = px.pie(
        values=sex_counts.values, 
        names=sex_counts.index, 
        title="Distribuciín de Titulos en el Titanic"
    )
    st.plotly_chart(tituplot, use_container_width=True)
    
    st.text("Los títulos antiguos eran:")
    st.text("'Master' ,'Ms' ,'Mlle' ,'Miss' , 'Mme' ,'Mrs' , 'Don' ,'Dona' ,'Lady' ,'Sir' ,'Countess' ,'Jonkheer' , 'Major' ,'Col' ,'Capt' ,'Rev' , 'Dr' ,'Mr'.")
    st.text( "Los hemos agrupado y cambiado por:" )
    st.text("'Senor', 'Señora', 'Señorita', 'Joven', 'Realeza', 'Sacerdote','Doctor', 'Militar")
                
    
    sex_counts = df_limpio["Embarcacion"].value_counts()
    embaplot = px.pie(
        values=sex_counts.values, 
        names=sex_counts.index, 
        title="Donde embarcaron"
    )
    st.plotly_chart(embaplot, use_container_width=True)
    
    no_es_str = df['Embarked'].apply(lambda x: not isinstance(x, str))
    noes = df.loc[no_es_str]
    st.text("Me parecía curioso que solo faltaran dos datos de Embarque, así que les presté especial atención:")
    code="df['Embarcacion'].apply(lambda x: not isinstance(x, str))"
    st.code(code,language="python")
    st.write(noes)
    
    
    


#--------------------GRAFICOS----------------------------#
if st.sidebar.button("Gráficos"):
    color_dict = {"Primera": '#ced9e0', "Segunda": '#3b6a84', "Tercera": '#083751'}
    fig6 = px.histogram(df_limpio, y="Sexo", color="Clase", barmode="group", text_auto=True, 
                    title="Cantidad de personas por Clase y Sexo",
                    labels={"Sexo": "", "Clase": "Clase"}, orientation="h",
                    color_discrete_map=color_dict)
    fig6.update_traces(textposition="outside", cliponaxis=False)
    st.plotly_chart(fig6, use_container_width=True)
    
    
    
    

    color_dict = {"Primera": '#ced9e0', "Segunda": '#3b6a84', "Tercera": '#083751'}

    fig = make_subplots(rows=3, cols=1, shared_xaxes=True, vertical_spacing=0.05)

    for i, clase in enumerate(["Primera", "Segunda", "Tercera"]):
        df_clase = df_limpio[df_limpio["Clase"] == clase]
    
        fig_clase = px.histogram(df_clase, x="Titulo", color="Clase", barmode="group", text_auto=True,
                                labels={"Cantidad": "Cantidad de personas", "Clase": "Clase", "Titulo": "Título"},
                                color_discrete_map=color_dict,
                                category_orders={"Clase": ["Primera", "Segunda", "Tercera"], 
                                                "Titulos de los pasajeros": sorted(df_limpio['Titulo'].unique())})
    
    
        fig.add_trace(fig_clase["data"][0], row=i+1, col=1)
    
        fig.update_yaxes(title_text="Cantidad de personas", row=i+1, col=1)
        fig.update_xaxes(title_text=" ", row=i+1, col=1)
        fig.update_xaxes(showticklabels=True, row=i+1, col=1)
        fig.update_layout(title=f"Diferenciando Clases por sus títulos", 
                      legend_title="", 
                      margin=dict(t=50, l=0, r=0, b=0))
    # Modificar tamaño del gráfico
    fig.update_layout(width=1600, height=1000)
    # Mostrar gráfico en Streamlit
    st.plotly_chart(fig, use_container_width=True)
    
    
    color_dict = {"Primera": '#ced9e0', "Segunda": '#3b6a84', "Tercera": '#083751'}
    fig2 = px.scatter(df_limpio, x="Titulo", y="Precio", color="Clase", color_discrete_map=color_dict,
                     title="Precio pagado por pasajero según título y clase",
                    labels={"Precio": "Precio pagado", "Titulo": "Título", "Clase": "Clase"})
         
    st.plotly_chart(fig2, use_container_width=True)


    color_dict = {"Primera": '#ced9e0', "Segunda": '#3b6a84', "Tercera": '#083751'}
    fig3 = px.scatter(df_limpio, x="Edad", y="Precio", color="Clase",
                    labels={"Edad": "Edad (años)", "Precio": "Precio del billete"},
                    title="Relación entre edad, precio del billete y supervivencia",
                    color_discrete_map=color_dict)

    st.plotly_chart(fig3, use_container_width=True)
    
    
    fig4 = px.scatter(df_limpio, x='Titulo', y='Edad', color='Titulo')

    fig.update_layout(
        font=dict(size=16),
        width=1200,
        height=600)
    # Mostrar el gráfico
    st.plotly_chart(fig4, use_container_width=True)
    
    
    # Crear el diccionario de mapeo de colores
    color_map = {"Si": "#6c8fa3", "No": "#660b45"}
    data = df_limpio.groupby(["Titulo", "Sobrevivio"]).size().reset_index(name="count")
    # Crear el gráfico de barras apiladas
    fig5 = px.bar(data, x="count", y="Titulo", color="Sobrevivio", barmode="stack",
                 orientation="h",
                 labels={"Titulo": "Título", "count": "Cantidad de pasajeros", "Sobrevivio": "Supervivencia"},
                 title="Supervivientes por título",
                color_discrete_map=color_map)

    fig5.update_layout(
        font=dict(size=16),
        width=1200,
        height=600)
    # Mostrar el gráfico interactivo
    st.plotly_chart(fig5, use_container_width=True)
    
    
    color_map = {"Si": "#6c8fa3", "No": "#660b45"}

    fig7 = px.box(df_limpio, x="Sobrevivio", y="Edad", color="Sobrevivio",
             title="Distribución sobre Edades/Sobrevivir",
             color_discrete_map=color_map,
             labels={"Sexo": "Género", "Edad": "Edad (años)"},
             hover_data=["Nombre"],
             height=600)

    fig7.update_layout(
    font=dict(size=16),
    width=600,
    height=600
    )

    st.plotly_chart(fig7, use_container_width=True)
    
#--------------------CONCLUSIONES----------------------------#
if st.sidebar.button("Conclusiones"):
    st.title("Con los datos obtenidos, podemos llegar a las siguientes conclusiones:")
    col1,col2,col3 = st.columns(3)
    with col1:
        st.subheader("El 55% de los pasajeros eran de la tercera clase.")
        st.subheader("72% de pasajeros ha embarcado a Southampton y el 93% de los embarcados en Queenstown eran tercera clase.")
        st.subheader("El 72% de mujeres Sobrevivieron y solo el 32% de los sobrevivientes fueron hombres")
        st.subheader("el 64% del total de precio fue pagado por la primera clase.")
        st.subheader("Las personas mayores tienen menos probabilidades de sobrevivir, aunque el mayor de 80 años sobrevivió.")
        st.subheader("Las personas de una clase más baja tienen menos probabilidades de sobrevivir.")
    with col2:
        st.title("")
    with col3:
        st.title("")
