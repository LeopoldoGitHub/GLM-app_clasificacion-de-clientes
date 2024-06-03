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

ETL= '''
Se realizó la carga de varios dataset desde Kaggle , para una empresa brasilera de E-commerce. Estos archivos estan en formato csv 
por lo que la carga no ha tenido mayor inconveniente. Se realizó la importación directamente con Pandas para el inicio del tratamiento
de los datos.
'''



EDA= '''
Se realizó una exploración de los datos para ver la interacción entre las variables.
Luego se realizó una ingeniería de características para ajustar las variables necesarias
que se utilizarán en nuestro modelo de aprendizaje.
'''

VIZ= '''
Realizamos una exploración visual exhaustivo utilizando Power BI para extraer
insights del conjunto de datos de la empresa brasileña de comercio electrónico, OLIST.
Mediante el uso de gráficos interactivos, 
somos capaces de realizar consultas detalladas y observar la descripción de los datos desde múltiples perspectivas.
Te invito a ver la próxima sección para ver el dashboard.'''


ML= '''
Presentamos un modelo de segmentación de machine learning diseñado específicamente
para los consumidores de “Olist”, una prominente empresa brasileña de comercio electrónico.
Este modelo es el resultado de un riguroso análisis de datos y una cuidadosa ingeniería de características,
y tiene como objetivo agrupar a los clientes en segmentos distintos basados en sus comportamientos y patrones de compra.
Puedes ver la sección del "Modelo de segmentación" para ver con mayor claridad el proceso que se desarrollo para llegar a nuestro modelo final..'''

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

st.header('ETL')
st.write(ETL, unsafe_allow_html=True)
img=st.image('./img/dataset_Olist_Original.png', width=500)

st.header('EDA')
st.write(EDA, unsafe_allow_html=True)

img=st.image('./img/univariado.png', width=500)
img=st.image('./img/bivariado.png', width=500)

st.header('Visualización')
st.write(VIZ, unsafe_allow_html=True)

img=st.image('./img/viz.png', width=500)

st.header('ML')
st.write(ML, unsafe_allow_html=True)
img=st.image('./img/ML_seg.jpeg', width=500)

st.write(repositorio, unsafe_allow_html=True)

