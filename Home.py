#############
## Imports ##
#############

import streamlit as st
import pandas as pd
import numpy as np
from streamlit.components.v1 import html


# def add_logo():
#     st.sidebar.image('./img/LogoGLM.png', width=300)
#     st.sidebar.markdown("GML'S Analytics App")

# # Llama a la función add_logo en cada página de tu aplicación
# add_logo()

#########################
## Important Variables ##
#########################
img=st.image('./img/LogoGLM.png', width=500)

intro = '''
Bienvenido a la aplicación de segmentación de clientes, 
la herramienta perfecta para cualquier gerente de Marketing que busque evaluar
el compotamiento de compras un usuario de E-commerce.
Con esta aplicación, puedes identificar rapidamente si un cliente es un buen comprador o es propenso a no comprar en la tienda. 
Ya del equipo de Marketing de la empresa o parte del equipo que analiza estos comportamientos ,  esta
aplicación está diseñada para proporcionarte valiosos insghts y hacer que tus decisiones o recomendaciones al negocio
sean más eficientes. '''

#################
## Application ##
#################

st.title("GML'S Analytics App")
st.write(intro, unsafe_allow_html=True)