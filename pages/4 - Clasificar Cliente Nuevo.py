#############
## Imports ##
#############

import streamlit as st
import pandas as pd
import numpy as np
import os
import joblib
import time

cliente = '''
Para cargar información de nuevo cliente, por favir siga las instrucciones y verifique que los datos sean correctos. AL terminar de cargar podr´ejecutar la aplicación
y obtener en que segmento estará el nuevo cliente segun su comportamiento de compras y los datos adicionales.:
'''


st.title('Calsificar nuevo Cliente')
st.write(cliente, unsafe_allow_html=True)

img=st.image('./img/MLenconstruccion.png', width=500)
