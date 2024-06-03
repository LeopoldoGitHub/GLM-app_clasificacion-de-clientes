# s15-32-m-data-bi
Repositorio del proyecto seleccionado de simulación laboral s15-32-m-data-bi

![LogoGLM](img/LogoGLM.png)

# PROYECTO GLM'S ANALYTICS 
Aplicación que segmenta los clientes segun su comportamiento de compra. El gerente de marketing y todo el departamento , tendrá a su disposición esta aplicación para hacer seguimiento en tiempo real del comportamiento  de compra de los clientes dentro del E commerce. Incluso puede predecir , introduciendo variables que le indicará el sistema , en que segmento estará un cliente nuevo.


<h3 align="center">🛠️ Miembros del Equipo</h3>
****
<br>
<div align="center"> 
 

|Participantes|Roles|Redes|
|:---:|:---:|:---:|
|**Marcelo Peralta**|![](https://img.shields.io/badge/PROJECT%20MANAGER-red?style=for-the-badge) <br> ![](https://img.shields.io/badge/DATA%20SCIENTIST-blue?style=for-the-badge)| <a target="_blank" rel="noopener noreferrer" href="https://www.linkedin.com/in/marcelo-peralta2/">[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/marcelo-peralta2/) </a> |
|**Stiven Lopez**| <br> ![](https://img.shields.io/badge/DATA%20ANALYST-yellow?style=for-the-badge)| <a target="_blank" rel="noopener noreferrer" href="https://www.linkedin.com/in/stivenlm/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" /></a> |
|**Giuseppe Navarro**|![](https://img.shields.io/badge/DATA%20SCIENTIST-blue?style=for-the-badge)| <a target="_blank" rel="noopener noreferrer" href="https://www.linkedin.com/in/gnavarromarin/">[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/gnavarromarin/)</a> |
|**Leopoldo Flores**|![](https://img.shields.io/badge/DATA%20SCIENTIST-blue?style=for-the-badge)| <a target="_blank" rel="noopener noreferrer" href="https://www.linkedin.com/in/leopoldofloresc/">[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/leopoldofloresc/)</a> |


</div>
<br>




<h2>🚧 Stack de Tecnologías </h2>

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Colab](https://img.shields.io/badge/Colab-F9AB00?style=flat&logo=google-colab&logoColor=white)](https://colab.research.google.com/)
[![PowerBI](https://img.shields.io/badge/PowerBI-F2C811?style=flat&logo=power-bi&logoColor=white)](https://powerbi.microsoft.com/)
[![Trello](https://img.shields.io/badge/Trello-0052CC?style=flat&logo=trello&logoColor=white)](https://trello.com/)
[![Discord](https://img.shields.io/badge/Discord-5865F2?style=flat&logo=discord&logoColor=white)](https://discord.com/)

<h2>🚩 User Stories:</h2>

1. El sector financiero y en específico el director financiero necesita que analicemos los datos de ventas y en lo posible los márgenes de beneficio por categoría de producto para optimizar la asignación de recursos y maximizar la rentabilidad de la empresa.
2. El sector de atención y experiencia del cliente necesita evaluar la satisfacción de los clientes con productos, tiempos de demora y estado de los productos a la hora de la entrega para una posible mejora en nuestro servicio al cliente, buscando aumentar la lealtad de los clientes, también se busca analizar los tiempos de demora en el shipping.
3. Desde el área de ventas se busca analizar las zonas de mayor venta para la tienda, y así mismo las de menor, para plantear posibles estrategias que permitan abarcar mayor territorio en ventas y mejorar los ingresos a la empresa
4. Como gerente de ventas de olist, quiero conocer los tipos de productos más vendidos en la plataforma, para ver el rendimiento de nuestros Sellers.
5. Como área de marketing, queremos conocer el perfil de los clientes y como se segmentan para poder proponer campañas de publicidad personalizadas según sus comportamientos de compra (montos, frecuencia y recencia)
6. Como área de logística, nos interesa conocer la distribución territorial de nuestros clientes para poder mejorar nuestras rutas y poder estimar cuales de nuestros centros de distribución tendrán mayor demanda.
7. Como gerente de logística me interesa ver cuantos de nuestros pedidos están llegando a tiempo (Ejm. OTIF)
8. Como Director de Marketing de nuestra tienda de ecommerce, quiero utilizar el análisis RFM para identificar a los clientes que están en riesgo de no volver a comprar, de modo que podamos crear campañas específicas de retención para mantenerlos comprometidos con nuestra marca.
Criterios de Aceptación:

Identificación de Clientes en Riesgo:
Los clientes que tienen una puntuación baja en Recency (R) y frecuencia (F) pero alta en Monetary (M) deben ser identificados como en riesgo.
Obtener una lista de estos clientes con sus detalles de contacto.
Desarrollo de Campañas de Retención:
Crear campañas de marketing específicas (emails, descuentos personalizados) dirigidas a estos clientes en riesgo.
Monitoreo y Evaluación:
Implementar métricas para medir la efectividad de estas campañas, como el incremento en la tasa de retorno de estos clientes y el aumento en sus compras.

9. Como Gerente de Ventas, quiero usar el análisis RFM para identificar a nuestros clientes más leales y de alto valor para ofrecerles productos exclusivos y promociones especiales, con el objetivo de aumentar sus compras y fidelización a largo plazo.

Criterios de Aceptación:

Identificación de Clientes Leales:
Identificar a los clientes que tienen altas puntuaciones en Frecuencia (F) y Monetary (M), independientemente de su Recency (R).
Generar una lista de estos clientes con sus historiales de compra.
Ofrecimiento de Promociones Exclusivas:
Diseñar y lanzar promociones especiales (por ejemplo, acceso anticipado a nuevas colecciones, descuentos exclusivos).
Seguimiento de Resultados:
Medir el impacto de estas promociones en términos de aumento en el valor de las compras y la frecuencia de compra.
Recopilar feedback de los clientes sobre su satisfacción con las promociones.

10.  Como Analista de Datos, quiero implementar el análisis RFM para segmentar a nuestros clientes en diferentes grupos, de manera que podamos personalizar nuestras campañas de marketing y maximizar el retorno de la inversión (ROI).

Criterios de Aceptación:

Segmentación de Clientes:
Segmentar a los clientes en categorías como "Mejores Clientes", "Clientes Leales", "Clientes en Riesgo", y "Clientes Perdidos" usando el modelo RFM.
Crear un dashboard interactivo que visualice estas segmentaciones.
Personalización de Campañas:
Colaborar con el equipo de marketing para diseñar campañas específicas para cada segmento.
Implementar campañas automatizadas basadas en los segmentos definidos.
Análisis y Reportes:
Analizar el rendimiento de cada campaña segmentada en términos de tasas de apertura, clics y conversiones.
Presentar informes mensuales sobre la efectividad de las campañas personalizadas y recomendar ajustes basados en los resultados.

11. Como usuario de la app, quiero recibir notificaciones y alertas relevantes sobre ofertas especiales, actualizaciones de mis pedidos y recordatorios, para estar siempre informado y aprovechar las oportunidades.

Criterios de Aceptación:

Personalización de Notificaciones:
Las notificaciones deben estar personalizadas según mis intereses y hábitos de compra.
Actualizaciones en Tiempo Real:
Recibir alertas en tiempo real sobre el estado de mis pedidos, incluyendo confirmaciones de envío y entrega.
Facilidad de Gestión de Notificaciones:
Puedo gestionar mis preferencias de notificaciones desde la app, eligiendo qué tipo de alertas quiero recibir y cómo.

12. Como analista de datos en una tienda de ecommerce, quiero utilizar técnicas de machine learning para mejorar la segmentación de clientes basada en el análisis RFM, para identificar patrones de comportamiento más complejos y optimizar nuestras estrategias de marketing.

Criterios de Aceptación:

Preparación de los Datos:
Extraer y limpiar los datos de transacciones de clientes, asegurándome de que los datos estén completos y correctamente formateados.
Calcular los valores de Recency, Frequency y Monetary para cada cliente.
Aplicación de Técnicas de Machine Learning:
Utilizar algoritmos de clustering, como K-means o DBSCAN, para identificar segmentos de clientes basados en los valores RFM.
Evaluar diferentes algoritmos y parámetros para encontrar el modelo que mejor agrupe a los clientes según sus comportamientos de compra.
Análisis y Visualización de Resultados:
Crear visualizaciones claras (e.g., gráficos de dispersión, diagramas de calor) para mostrar los segmentos resultantes y los patrones detectados.
Generar informes detallados que describan las características de cada segmento y las recomendaciones de marketing asociadas.
Integración con Estrategias de Marketing:
Colaborar con el equipo de marketing para diseñar campañas específicas basadas en los segmentos identificados, como campañas para "Mejores Clientes", "Clientes en Riesgo", etc.
Monitorear el rendimiento de estas campañas y ajustar los modelos y estrategias según sea necesario para mejorar la efectividad.
Criterios de Aceptación Detallados:

Preparación de los Datos:

Extracción y Limpieza de Datos: Utilizar herramientas de ETL (Extract, Transform, Load) para asegurar la calidad de los datos.
Cálculo de RFM: Implementar scripts en Python o R para calcular Recency, Frequency y Monetary.
Aplicación de Técnicas de Machine Learning:

Selección de Algoritmo: Comparar algoritmos de clustering y elegir el más adecuado según métricas de evaluación como el índice de silueta o la inercia.
Entrenamiento y Evaluación del Modelo: Entrenar el modelo con los datos y evaluar su rendimiento para garantizar una segmentación precisa.
Análisis y Visualización de Resultados:

Visualizaciones: Crear gráficos utilizando librerías como Matplotlib, Seaborn o Plotly para ilustrar los segmentos.
Informes: Generar informes con herramientas como Tableau, Power BI o Jupyter Notebooks que incluyan análisis descriptivo y recomendaciones.
Integración con Estrategias de Marketing:

Diseño de Campañas: Trabajar con el equipo de marketing para desarrollar estrategias específicas para cada segmento identificado.
Monitoreo y Ajustes: Implementar un sistema de monitoreo continuo para evaluar el impacto de las campañas y ajustar el modelo de segmentación basado en los resultados obtenidos.




13. Como cliente(que Busca Sostenibilidad:) consciente del medio ambiente, quiero encontrar productos que sean ecológicos y sostenibles, para poder reducir mi huella de carbono y apoyar a empresas responsables.
Datos Necesarios: Preferencias de productos ecológicos, historial de compras de productos sostenibles, interacciones con campañas de sostenibilidad.


14. Como cliente que valora la personalización, quiero recibir recomendaciones de productos personalizados basados en mis compras anteriores y mis gustos específicos, para sentir que la tienda me entiende y me valora.
Datos Necesarios: Historial de compras, interacciones en el sitio web, encuestas de preferencias.

15. Como cliente que busca experiencias, quiero que me recomienden productos que se complementen entre sí para crear una experiencia completa, como sets de productos o combinaciones sugeridas.
Datos Necesarios: Patrones de compra de productos relacionados, búsquedas y clics en sets o combos, feedback de experiencias pasadas.


16. Como vendedor(que Quiere Optimizar el Inventario), quiero segmentar a mis clientes en función de su propensión a comprar ciertos tipos de productos, para optimizar el inventario y mejorar la disponibilidad de los productos más demandados.
Datos Necesarios: Historial de compras, tendencias de ventas, datos demográficos de clientes.

17. Como vendedor que Desea Mejorar la Retención:, quiero identificar a los clientes que están en riesgo de abandonar la plataforma, para poder ofrecerles incentivos y mejorar mi tasa de retención.
Datos Necesarios: Historial de compras, frecuencia de compras, análisis de comportamiento de navegación.


18. Como responsable de logística que Optimiza las Entregas, quiero segmentar a los clientes en función de sus ubicaciones y preferencias de entrega, para optimizar las rutas y tiempos de entrega, mejorando así la eficiencia operativa.
Datos Necesarios: Direcciones de entrega, preferencias de entrega (horarios, métodos), datos geográficos.
Logística :

19. Como responsable de logística que Minimiza las Devoluciones, quiero identificar los patrones que llevan a devoluciones frecuentes, para implementar estrategias que reduzcan las devoluciones y mejoren la satisfacción del cliente.
Datos Necesarios: Historial de devoluciones, motivos de devolución, productos más devueltos, feedback de clientes sobre entregas.



<h2>🚧 Producto mínimo viable (MVP):</h2>
<br>
El objetivo de este proyecto es que el gerente de marketing y todo el departamento , tendrá a su disposición esta aplicación para hacer seguimiento en tiempo real del comportamiento  de compra de los clientes dentro del E commerce. Incluso puede predecir , introduciendo variables que le indicará el sistema , en que segmento estará un cliente nuevo
<br>
Con acceso a datos que abarcan un período entre  2016 y 2018 de transacciones on line de una tienda de E commerce en Brasil, se podán analizar los datos de compras recopilados en ese periodo y clasificar a los clientes pro su comportamiento de consumo.
<br>
Con este análisis se podrán diseñar campañas de marketing personalizadas y orientadas a los clientes que mas compras realizan, o los que tienen mayor riesgo de abandonar la plataforma.
<br>

<h2>🚧 Etapas del Proyecto</h2>

<img src="xxx/.png" width='100%'>

****
<h1 align='center' >Memoria del Proyecto</h1>
<br>
<h2 align='center' >✅ Sprint 0 ✅ </h2>
<br>


<h3>🚩 Creación del canal de Slack:</h3>

<p>Se ha propuesto utilizar Slack como nuestra plataforma de comunicación principal. Esta decisión se basa en las siguientes ventajas que ofrece Slack:</p>

<li>Compartir pantalla: ideal para colaborar en tareas que requieren visualización y edición conjunta de contenido. </li>
<li>Familiaridad: la mayoría de nosotros ya conoce Slack, lo que facilita la adopción de la plataforma. </li>


<h3>🚩 Definición de horario de reuniones diarias.</h3>
Hemos acordado que la reunión diaria se llevará a cabo todos los días a las 10:00 AM, hora de Argentina.
Durante estas reuniones diarias, cada miembro del equipo tendrá la oportunidad de compartir actualizaciones sobre su progreso, discutir posibles obstáculos y colaborar en soluciones. Se destacó la importancia de que todos participemos activamente y que mantengamos una actitud abierta y receptiva hacia las ideas de los demás. Adicionalmente , debido a las bajas iniciales hemos estado de acuerdo en el compromiso de cada integrante para cumplir con el proyecto de acuerdo a la cantidad de personas que conforma el equipo actualmente.(5)


<h3>🚩 Primeras ideas sobre proyectos.</h3>
En un principio, se consideraron diversas opciones de proyecto basado en que hay mas cantidad de data scientist en el equipo. Prediccones, clasificación, series de tiempo, entre otras. Luego de hacer una tormenta de ideas se decidió buscar data set y traer ideas sobre que tipo de análisis se podría hacer y luego acordar una idea en común.


<h3>🚩 Recolección de diferentes Dataset.</h3>
Se propuso la busqueda de diferentes datasets para cada proyecto propuesto, esto con el fin de evaluar cuanta información se tenia de cada uno de ellos. Estos fueron detallados en un documento de Drive donde cada integrante aportaba a cada uno de los proyectos la información correspondiente y agregando ademas que tipos de analisis podrian realizarse con ellos.
<br>

<h2 align='center' >✅ Sprint 1 ✅ </h2>

<br>
<h3>🚩 Elección del proyecto</h3>
Despues de haber reunido la información sobre los datset y sus viabilidad para los análisis, se sometio la eleccion del mismo a votación quedando el dataset de Kaggle, sobre una empresa brasilera de E-commerce https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce?select=olist_order_items_dataset.csv.
<br>
Después de haber establecido el rubro y el dataset, el equipo se reunió para discutir que orientación se le dará al análisis para definir el proyecto final el cual se trata de segmentación de clientes
<br>
Durante este Sprint la tarea principal a completar es la limpieza del Dataset para poder trabajar con ella en las diferentes areas.
<br>
El equipo se comprometió a mantener una comunicación abierta y constante para garantizar un flujo de trabajo eficiente y colaborativo.
<br>

<h3>🚩 Definir User Stories:</h3>

1. Como área de marketing, queremos conocer el perfil de los clientes y como se segmentan para poder proponer campañas de publicidad personalizadas según sus comportamientos de compra (montos, frecuencia y recencia)

<br>

<br>
<img src="./img/etapas.png" width='100%'>

<h3>🚩 Extracción y limpieza de datos:</h3>


<h4>🚩 Dataset Olist:</h4>

Para comenzar, vamos a examinar un conjunto de datos que pertenece a “Olist”, una empresa brasileña de comercio electrónico. Nuestro objetivo es progresar en el proyecto mediante la identificación de percepciones y datos valiosos que podrían ser incorporados en nuestro estudio.

Estructura que tenia al inicio:

<img src="./img/dataset_Olist_Original.png" width='100%'>

En el archivo [Limpieza de Datos Olist](ruta) se puede ver todo el proceso de extracción y limpieza de este dataset.
O bien en el cuaderno virtual de Google Colab a continuación: [Limpieza de Datos Olist](ruta)


<br>
<h3>🚩 Conexión de la base de datos a Power BI y primeros análisis</h3>

Luego de la limpieza, tanto para la parte de análisis de datos como para el desarrollo del modelo, se comenzó a analizar algunos insights en Power BI. Logrando asi desarrollar las primeras visualizaciones para el dashboard


##Visualizaciones en construcción


<h2 align='center' >✅ Sprint 2 ✅ </h2>
<br>
<h3>🚩 Creación de Streamlit:</h3>

Streamlit es una herramienta de Python que facilita la creación de aplicaciones web para ciencia de datos y aprendizaje automático. Permite a los usuarios interactuar con datos y ver resultados en tiempo real, optimizando así el proceso desde la exploración hasta la implementación de modelos.

Para este proyecto se realizó la implementación en esta plataforma creando la estructura inicial en 4 partes:

1. Home: En esta se encuentra la descripción del proyecto y una vista general de la aplicación.
2. Desarrollo del proyecto: Se muestra cómo se obtuvieron y cargaron los datos, así cómo el proceso de transformación y limpieza para tener las tablas que finalmente se utilizarán en el proyecto.
3. Visualización: En esta sección, nos embarcamos en un viaje de exploración visual exhaustivo utilizando Power BI para desentrañar insights del conjunto de datos de la empresa brasileña de comercio electrónico, OLIST. Mediante el uso de gráficos interactivos, somos capaces de realizar consultas detalladas y observar la descripción de los datos desde múltiples perspectivas.

Estos gráficos interactivos nos permiten manipular y examinar los datos en diversas combinaciones, lo que nos ayuda a entender mejor las tendencias, patrones y relaciones subyacentes. Esto es especialmente útil para identificar insights clave que podrían pasar desapercibidos en un análisis estático.

4. Modelo de segmentación: En una sección clave de nuestro proyecto, presentamos un modelo de segmentación de machine learning diseñado específicamente para los consumidores de “Olist”, una prominente empresa brasileña de comercio electrónico. Este modelo es el resultado de un riguroso análisis de datos y una cuidadosa ingeniería de características, y tiene como objetivo agrupar a los clientes en segmentos distintos basados en sus comportamientos y patrones de compra.

Hemos desarrollado una aplicación intuitiva que permite al gerente de marketing de “Olist” visualizar y entender estos segmentos de clientes de manera efectiva. Esta aplicación no solo muestra la segmentación de los clientes, sino que también proporciona insights valiosos sobre cada segmento, lo que permite al equipo de marketing diseñar estrategias de marketing más personalizadas y efectivas.

En resumen, esta sección del proyecto destaca nuestro compromiso con la aplicación práctica de machine learning y data science para resolver problemas comerciales reales y generar valor para nuestros clientes.

##Esta tarea será actualizada conforme avance el proyecto.

<h3>🚩 Division de Insights para el Dashboard:</h3>

Se analizó el dataset en el que se estaba trabajando para asi dividir y definir cuales serian los parametros y la información que se mostrará en el dashboard.

Se hizo la division en los siguientes campos:

1. ##a.
2. ##b.
3. ##c.
4. ##d
<h3>🚩 Desarrollo de modelos predictivos:</h3>

###En proceso de ejecución
