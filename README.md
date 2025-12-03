## PROYECTO FINAL. BASE DE DATOS NoSQL ELASSANDRA
## Social media usage and emotional well-being dataset

#### Equipo 08:
### ROJAS MENESES EMILY VICTORIA
### UNZUETA AMADOR ZYANYA VALERIA
### SANSORES BALAM CARLOS DANIEL

**Materia: Modelado de datos.**  

**Profesor: Luis Basto Ramírez**


  
  

  








## 1. DATASET
Fue seleccionado el dataset de Social Media Usage and Emotional Well-Being con el siguiente link de kaggle: https://www.kaggle.com/datasets/emirhanai/social-media-usage-and-emotional-well-being/data  

Este dataset tiene información sobre el tiempo de uso de redes sociales, actividades diarias de los usuarios en estas, tales como, posts, likes, comentarios, plataforma utilizada e incluso la emoción predominante durante su estadía. Por lo tanto, este dataset permite modelar y analizar los patrones relacionados con las emociones y el comportamiento digital.  
Contiene registros de usuarios y su comportamiento diario en las redes sociales, cada fila representa a un usuario y sus métrics sociales más relevantes del dia
Este conjunto de datos fue creado para estudiar cómo los hábitos de uso de las redes sociales se relacionan con el bienestar emocional diario de los usuarios. El dataset recopila información detallada del comportamiento de los usuarios en distintas plataformas, así como su emoción predominante durante el día, lo que lo convierte en un recurso ideal para análisis de predicción, clasificación y patrones de comportamiento digital. 

Predice el bienestar emocional usando modelos de machine learning, se puede estimar la emoción dominante del usuario según su actividad en redes. 

Descubre patrones de uso por ejemplo: 
Usuarios que pasan más tiempo en Instagram tienden a mostrar X emoción, quienes publican más pueden recibir más interacción, diferencias de hábitos según edad o género.  

Analiza el impacto de cada plataforma permitiendo identificar si ciertas redes están asociadas a emociones más positivas o negativas. 

Se pueden crear clusters: 
Usuarios intensivos, usuarios pasivos, usuarios con alta interacción social y usuarios con emociones negativas persistentes 

## 3. DICCIONARIO DE DATOS

<img width="595" height="265" alt="imagen" src="https://github.com/user-attachments/assets/47fc94e4-a531-441e-9825-2f8a95baeea1" />

## 4. MODELADO DEL DATASET EN ELASSANDRA
El modelado se realizó utilizando el enfoque de datos tipo Wide-Column Store como en la parte de Cassandra, esto debido a la facilidad de almacenar los id's y de la habilidad adquirida durante el curso sobre sentencias del tipo SQL, para agilizar la creación de la tabla. Primero utilizamos la parte del user_id como partición para la agrupación de actividades por usuario, posteriormente, a platform como clave de clustering, además, se permitiría la consulta por usuario y plataforma específica. Este modelado nos ayudó a mantener una optimización para lecturas rápidas y construir un modelo eficiente y escalable para cargas mayores
Código para la creación del keyspace:
CREATE KEYSPACE IF NOT EXISTS socialks
WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};
Código para la creación de la tabla:
CREATE TABLE IF NOT EXISTS social_media_usage (
    user_id text,
    platform text,
    age int,
    gender text,
    daily_usage_time_minutes int,
    posts_per_day int,
    likes_received_per_day int,
    comments_received_per_day int,
    messages_sent_per_day int,
    dominant_emotion text,
    PRIMARY KEY (user_id, platform)
);

## 4. HERRAMIENTAS UTILIZADAS
1. Docker: Contenedor para elassandra
2. Elassandra: Motor NoSQL para compatibilidad de cassandra y elasticsearch
3. CQLSH: Ejecución de sentencias CQL
4. Phyton 3 con Cassandra driver: script para la importación del datasert
5. GitHub: documentación y control de versiones.

## 5. IMPORTACIÓN DE DATOS
Movimos el train.csv al contenedor y revisamos que haya quedado correctamente
![Sin título](https://github.com/user-attachments/assets/28752dfb-bfb3-4539-8563-e2d9e065a81c)

Creamos una red interna en docker, conectamos elassandra a esta red y creamos un contenedor python moderno con pip
![Sin título-1](https://github.com/user-attachments/assets/67c10b09-ee39-4096-a252-ce4afeccdf19)

Instalamos el driver de Cassandra
![Sin título](https://github.com/user-attachments/assets/fce37eb4-12fb-4665-817e-8fd735e72904)

Copiamos el csv al contenedor cliente
![Sin título-1](https://github.com/user-attachments/assets/21c786e7-1e34-49ef-820c-b315e4834cbe)

Realizamos el script de Python para cargar los datos a la base
![Sin título](https://github.com/user-attachments/assets/61eac621-2bcf-4c1a-bd25-ee5638b79562)

Realizamos la importación con el script
![Sin título-1](https://github.com/user-attachments/assets/10c9c60b-357a-415c-8390-64de3d6d7ff4)

Se revisó que se haya realizado correctamente la importación
![Sin título](https://github.com/user-attachments/assets/62f3e345-f7ec-480c-b2b2-ab64abeeabb2)









