#############
## Imports ##
#############

import streamlit as st
import pandas as pd
import numpy as np
import time
import os
import joblib


#########################
## Important Variables ##
#########################

modelo = '''
La elección del modelo de aprendizaje automático es vital para la segmentación de clientes en
una empresa de comercio electrónico. Este paso determina la precisión de las predicciones
y se basa en evaluar varios algoritmos para encontrar el que mejor se adapte a los datos y al problema.
Una selección adecuada mejora la precisión, reduce el sobreajuste y aumenta la interpretabilidad 
convirtiéndola en una parte esencial del flujo de trabajo de aprendizaje automático.
'''

rfm= '''
Recencia(R): Se refiere a cuándo fue la última vez que un cliente realizó una compra.
Cuanto más reciente sea la compra, mayor será la probabilidad de que el cliente vuelva a comprar.

Frecuencia (F): Indica con qué frecuencia un cliente ha realizado compras en el pasado. 
Un cliente que compra con frecuencia es más probable que vuelva a comprar en comparación con uno que raramente lo hace.

Valor Monetario (M): Representa el monto total que un cliente ha gastado en tus productos o servicios. 
Los clientes que han gastado más en el pasado son más propensos a realizar compras de alto valor en el futuro.

Visualizar estas variables permite a las empresas segmentar a sus clientes en grupos distintos
basados en sus comportamientos de compra.
Esto puede ayudar a las empresas a entender mejor a sus clientes
y a personalizar sus estrategias de marketing para cada segmento
'''

customer = '''
La segmentación de clientes ayuda a las empresas a personalizar sus estrategias de marketing
y optimizar su enfoque hacia cada segmento de clientes.
Por ejemplo, podrían enviar ofertas especiales a clientes que compran con frecuencia,
o podrían intentar reenganchar a clientes que no han comprado recientemente.

En resumen, la segmentación de clientes con machine learning permite a las empresas
de e-commerce entender mejor a sus clientes, personalizar sus interacciones y mejorar sus resultados.
Mostramos la categorización de los clientes de nuestro modelo final
'''

customer_new=''' Se ingresan los datos de nuevo cliente y se piden su identificación de usuario y datos de compra'''

clustering=''' El modelo se ejecuta generando una segmentación de acuerdo al comportamiento de compra del usuario'''

marketing=''' Se analizan las métricas de los segmentos y se diseña una campaña de marketing personalizada la cual será recomendada de acuerdo al comportamiento de compra del cliente'''

recomendacion=''' Se muestra la informacion general del cluster y se muestra la recomendación diseñada para cada caso'''

st.title('Modelo de Segmentación')
st.write(modelo, unsafe_allow_html=True)

img=st.image('./img/ML_seg.jpeg', width=500)

st.title('Creando caracteristicas RFM')
img=st.image('./img/rfm.png', width=500)

st.title('Visualizando variables RFM')
st.write(rfm, unsafe_allow_html=True)

img=st.image('./img/RFM_by_cluster.png', width=500)



st.title('Categorizando clientes')
st.write(customer, unsafe_allow_html=True)

img=st.image('./img/cluster_6_2d.png', width=500)
img=st.image('./img/cluster_6_3d.png', width=500)


st.title('Clientes por cluster')
img=st.image('./img/clientes_por_cluster.png', width=500)

st.title('Categorizando Cliente Nuevo-Ingreso de Datos')
st.write(customer_new, unsafe_allow_html=True)

img=st.image('./img/ingresar_cliente.png', width=500)

st.title('Ejecución del modelo-Kmeans')
st.write(clustering, unsafe_allow_html=True)

img=st.image('./img/clustering.png', width=500)

st.title('Campaña de Marketing')
st.write(marketing, unsafe_allow_html=True)

img=st.image('./img/marketing.png', width=500)

st.title('Cliente Nuevo-Recomendación')
st.write(recomendacion, unsafe_allow_html=True)

img=st.image('./img/recomendacion.png', width=700)
