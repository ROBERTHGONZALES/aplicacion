import streamlit as st
import pandas as pd
import plotly.express as px

st.title('DataVizBuilder')


uploaded_file = st.file_uploader("Elige un archivo CSV", type="csv")

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)
    
 
    st.write("Datos cargados:")
    st.write(df)
    

    x_axis = st.selectbox("Selecciona la columna para el eje X", options=df.columns)
    y_axis = st.selectbox("Selecciona la columna para el eje Y", options=df.columns)
    

    fig = px.scatter(df, x=x_axis, y=y_axis)

    st.plotly_chart(fig)
