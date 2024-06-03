#############
## Imports ##
#############

import streamlit as st

#########################
## Important Variables ##
#########################
img=st.image('./img/etapas.png', width=500)
desarrollo = '''

En esta sección se muestra las diferentes etapas por las cuales desarrolaremos la aplicación de segmentación. Se tomó en cuenta la carga de la información, la exploración de la data para luego crear visualizaciones y encontrar insights valiosos. 
Luego desarrollaremos un modelo de Machine Learning que nos permitirá catalogar los clientes segun su comportamiento de consumo'''

EDA= '''
Se realizó una exploración de los datos para ver la interacción entre las variables.
Luego se realizó una ingeniería de características para ajustar las variables necesarias
que se utilizarán en nuestro modelo de aprendizaje.
'''

repositorio = '''
<center style=''>
<a href='https://github.com/LeopoldoGitHub/s15-32-m-data-bi.git' style='margin-left: 5%;'>Github</a>
</center>
'''

#################
## Application ##
#################

st.title('Desarrollo del Proyecto')
st.write(desarrollo, unsafe_allow_html=True)

st.header('EDA')
st.write(EDA, unsafe_allow_html=True)

st.write(repositorio, unsafe_allow_html=True)

