#############
## Imports ##
#############

import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

st.title("Visualización/ Análisis de datos")
img=st.image('./img/LogoGLM.png', width=500)

st.write("A través de Power BI realizamos un análisis de los datos del comportamiento de compras de los clientes de Olist, que se pueden consultar de manera interactiva en el siguiente dashboard:")

with st.expander('Dashboard'):
    # img = Image.open("./img/LogoGLM.png")
    # imagen = img.resize((800, 400))
    # st.image(imagen)    

    st.write("<iframe width='1000' height='600' src='https://app.powerbi.com/view?r=eyJrIjoiZjdiNmFjOWUtNzNlMy00MmRhLWJkNDgtZWEwYTBlMmFkNTEwIiwidCI6ImI1ZDc4OTI3LTI1ZDAtNDRhOS04MzcwLWQ4NmU1N2M3YmE5NiIsImMiOjR9' style='display:block;margin:auto;'></iframe>", unsafe_allow_html=True)
