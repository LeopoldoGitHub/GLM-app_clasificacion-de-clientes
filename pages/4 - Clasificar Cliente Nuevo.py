#############
## Imports ##
#############

import streamlit as st
import pandas as pd
import streamlit as st
import pickle
import numpy as np
from datetime import datetime
from dateutil import parser
from sklearn.preprocessing import StandardScaler
import os
import joblib
import time

cliente = '''
Sistema de recomendación de Marketing aplicado a comportamiento de compra de clientes
'''


st.title('Marketing para consumidores')
st.write(cliente, unsafe_allow_html=True)

img=st.image('./img/LogoGLM.png', width=350)


# Cargar el modelo KMeans
with open('kmeans_model_glm.pkl', 'rb') as file:
    kmeans_model = pickle.load(file)

# Definiciones de los clusters y campañas de marketing
clusters_info = {
    0: ("Compradores Frecuentes Moderados", "Clientes que compran con una frecuencia moderada y han comprado recientemente. Su gasto es moderadamente alto.",
        "Programa de Fidelización.", "Gracias por ser un cliente leal. Disfruta de un 15% de descuento en tu próxima compra.", "Email marketing y notificaciones push."),
    1: ("Compradores Recientes", "Clientes que han realizado compras recientemente pero con poca frecuencia y bajo gasto.",
        "Ofertas de Bienvenida.", "¡Nos encanta verte nuevamente! Aquí tienes un cupón de 10% de descuento en tu próxima compra.", "Email marketing y pop-ups en la web."),
    2: ("Compradores Inactivos", "Clientes que no han comprado recientemente y tienen baja frecuencia de compra y gasto.",
        "Reactivación.", "¡Hace tiempo que no te vemos! Vuelve y recibe un 20% de descuento en tu próxima compra.", "Email marketing y remarketing en redes sociales."),
    3: ("Compradores de Alto Valor", "Clientes que compran ocasionalmente pero con un gasto muy alto.",
        "Exclusividad.", "Como uno de nuestros mejores clientes, te invitamos a una venta exclusiva con un 25% de descuento en productos seleccionados.", "Email marketing personalizado y eventos exclusivos."),
    4: ("Compradores Únicos Moderados", "Clientes que compran solo una vez con un gasto moderado y no han comprado recientemente.",
        "Incentivos para la Segunda Compra.", "Aprovecha un 15% de descuento en tu segunda compra. ¡Esperamos verte de nuevo!", "Email marketing y retargeting en redes sociales."),
    5: ("Compradores Frecuentes de Alto Valor", "Clientes que compran con alta frecuencia y con un gasto muy alto.",
        "VIP.", "Bienvenido al club VIP. Disfruta de un 30% de descuento y acceso anticipado a nuestras nuevas colecciones.", "Email marketing personalizado y programas de fidelización.")
}

# Función para calcular RFM
def calcular_rfm(df_rfm):
    
    # Calculamos la fecha máxima del dataset, la que consideraremos para contrastarla contra las demas fechas y calcular recencia
    df_rfm["purchase_date"] = pd.to_datetime(df_rfm["purchase_date"])
    max_date = df_rfm["purchase_date"].max()

    # Creamos las variables Recency (R), Frequency (F), Monetary (M)
    df_rfm["dif_days"] = max_date - df_rfm["purchase_date"]
    df_rfm["recency"] = df_rfm["dif_days"].dt.days

    # Hacemos el groupby
    by_rfm = df_rfm.groupby(by="customer_unique_id").agg({"recency": "max",
                                                          "order_id": "count",
                                                          "payment_value": "sum"
                                                          })

    # Renombramos
    by_rfm.columns = ["recency", "frequency", "monetary"]
    
    return by_rfm



# Función para quitar outliers

def clean_out(df,cols):
    df_clean = df.copy()
    for column in cols:
        Q1 = np.quantile(df[column], 0.05)
        Q3 = np.quantile(df[column], 0.95)
        IQR = Q3-Q1
        LOWER = (Q1 - 1.5 * IQR)
        UPPER = (Q3 + 1.5 * IQR)

        df_clean = df_clean[(df_clean[column] >= LOWER) &
                            (df_clean[column] <= UPPER)]
    return df_clean



# Función para normalizar
def normalizar(rfm_clean):
    # Instanciamos el scaler
    scaler = StandardScaler()

    X = pd.DataFrame(scaler.fit_transform(rfm_clean))
    X.columns = rfm_clean.columns
    X.index = rfm_clean.index
    
    return X



# Título de la aplicación
st.title("Clustering para nuevo usuario")

# Entrada de datos del cliente
cliente_id = st.text_input("Ingrese el ID del cliente:", "")
orden_id = st.text_input("Ingrese el ID de la orden:", "")
valor_orden = st.number_input("Ingrese el valor total de la orden con decimales:", min_value=0.0)
fecha_compra = st.text_input('Ingrese la fecha y hora en el formato YYYY-MM-DD HH:MM:SS', '2018-06-18 16:45:05')

# Botón para procesar
if st.button("Clasificar"):
    # Verificación y preprocesamiento de datos

    if cliente_id and orden_id and valor_orden and fecha_compra:
        try:
             # Limpieza y parsing de la fecha
            fecha_compra = datetime.strptime(fecha_compra.strip(), '%Y-%m-%d %H:%M:%S')
            
            # Leer el dataframe base
            df_rfm = pd.read_csv('./model/df_rfm.csv')

            # Crear el DataFrame para los nuevos datos
            data_nueva = pd.DataFrame({
                "customer_unique_id": [cliente_id],
                "order_id": [orden_id],
                "purchase_date": [fecha_compra],
                "payment_value": [valor_orden]
            })

            # Concatenar los datos nuevos con el dataframe base
            df_rfm = pd.concat([df_rfm, data_nueva], ignore_index=True)

            # Procesar el dataframe concatenado


            #crear caracteristicas rfm en un dataframe by_rfm
            by_rfm = calcular_rfm(df_rfm)
            
            #eliminar outliers de by_rfm
            cols_to_clean = ["recency", "monetary"]
            rfm_clean = clean_out(by_rfm, cols_to_clean)


            # Guardar rfm_clean para uso futuro
            rfm_clean.to_csv('./model/rfm_clean.csv', index=False)

            # Normalizar rfm_clean para obtener X
            X = normalizar(rfm_clean)

            # Predecir el cluster
            cluster = kmeans_model.predict(X)


            # Mostrar la clasificación del nuevo cliente
            cluster_info = clusters_info[cluster[0]]
            st.write(f'El usuario se ajusta a la categoría de "{cluster_info[0]}".')
            st.write(cluster_info[1])
            st.write(f"Campaña de Marketing: {cluster_info[2]}")
            st.write(f"Recomendación:")
            st.write(f"Mensaje: \"{cluster_info[3]}\"")
            st.write(f"Canal: {cluster_info[4]}")


        except ValueError as e:
            st.write(f"Formato de fecha incorrecto: {e}. Por favor, ingrese la fecha en el formato '2018-06-18 16:45:05'.")
    else:
        st.write("Por favor, complete todos los campos.")