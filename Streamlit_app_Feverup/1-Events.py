#---------------------------- LIBRERÍAS ----------------------------#
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly_express as px
import streamlit.components.v1 as components
import base64
from wordcloud import WordCloud




#---------------------------- CONFIGURACIÓN DE LA PÁGINA ----------------------------#


st.set_page_config(
    page_title= "Feverup - Events & Price tickets",
    layout="wide"                                        
)

logo = "Streamlit_app_Feverup/img/logo.png"
eventos_feverup = "Streamlit_app_Feverup/img/events.png" 


#---------------------------- DATOS DE LA PÁGINA ----------------------------#
link_data = "https://docs.google.com/spreadsheets/d/1cTW5rp8av-12UuJ4zDkrqTRUDR4hokKSvWPqKl_WO3g/export?format=csv"                         # 'export?format=csv' -> añadir para que exporte correctamente desde google sheets
events = pd.read_csv(link_data)






#---------------------------- HEADER ----------------------------#
st.image(logo, width=200)    
st.title("")
st.markdown("<h1 style='color: #38b6ff; font-size: 52px;'>New entertainment with a multitude of possibilities!</h1>", unsafe_allow_html=True)
st.title("")
st.title("")
st.write("<h5>This analysis shows trending events, ticket prices and gross revenue visualizations. Finally, it introduces machine learning models for ticket price prediction.</h5>", unsafe_allow_html=True)
st.title("")
st.title("")
st.image(eventos_feverup, width=800) 
st.write("Image: https://feverup.com")
st.title("")
st.title("")
st.title("")
st.title("")
st.markdown("<h1 style='color: #38b6ff;'>Let's go with trending events!</h1>", unsafe_allow_html=True)
st.title("")
st.write("<h5>The original data contains 233725 rows and 13 columns with 3085 unique events. Data contain events from the USA, Canada, the United Kingdom and Ireland. The events start on September 18, 2023 and continue until August 4, 2027. There are a total of 209255 events from the beginning until April 1st.</h5>", unsafe_allow_html=True)
st.title("")




#---------------------------- SIDEBAR ----------------------------# Todo lo que se haga en la pantalla principal, se puede hacer también en el sidebar
st.sidebar.title("")
st.sidebar.title("")
st.sidebar.title("")
st.sidebar.title("")
st.sidebar.title("")
st.sidebar.title("")
st.sidebar.title("")
st.sidebar.title("")
st.sidebar.title("")
st.sidebar.title("")
st.sidebar.title("")
st.sidebar.title("")
st.sidebar.title("")
st.sidebar.title("")
st.sidebar.title("")
st.sidebar.markdown("**Marta Hinojosa Jiménez**")
st.sidebar.write("")
st.sidebar.write("Linkedin: https://www.linkedin.com/in/marta-hinojosa-jimenez/")
st.sidebar.write("")
st.sidebar.write("Github: https://github.com/martahinojosa1")
st.sidebar.title("")
st.sidebar.title("")
st.sidebar.image(logo, width=100)





#---------------------------- BODY ----------------------------#
st.title("")
st.subheader("How many event categories are there?")
col1, col2 = st.columns(2)

with col1:                                                                                                  # GRÁFICO PASTEL
    st.subheader("")
    fig = px.bar(events, 
             x=events['event_category'].value_counts().index, 
             y=events['event_category'].value_counts().values,
             color=events['event_category'].value_counts().index)

    fig.update_traces(marker_color='#38b6ff')                                                               # Establecer el color de las barras
    
    fig.update_layout(width=1200, height=600,                                                               # Ajustar el tamaño de la figura
                    title_text='<b>Event categories</b>', title_x=0.5,                                      # Centrar el título y ponerlo en negrita
                    xaxis_title='', yaxis_title='',                                                         # Ocultar los nombres de los ejes
                    showlegend=False) 
    st.plotly_chart(fig, use_container_width=True)                                                          # Asegurar que Streamlit use el ancho completo de la columna para el gráfico
    

with col2:                                                                                                  # GRÁFICA BARRAS VERTICALES
    st.title("")
    fig = px.pie(events, names='country', color_discrete_sequence=px.colors.sequential.Blues_r)
    fig.update_layout(width=600, height=500,
                    title_text='<b>Events by country in data (%)</b>', title_x=0.37)
    st.plotly_chart(fig, use_container_width=True)
    
st.title("")
st.title("")


col1, col2 = st.columns(2)
with col1:
    if st.checkbox('Trending category "MIX". What does it contain?'):                                       # GRÁFICA WORDCLOUD MIX                          
        st.title("")
        mix_events = events[events['event_category']=='MIX']                                                # Filtrar eventos categoría 'MIX'
        titles = ' '.join(mix_events['title'])                                                              # Concatenar todos los títulos en una sola cadena
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(titles)             # Crear un objeto WordCloud
        plt.figure(figsize=(12, 8))                                                                         # Mostrar el gráfico de palabras
        plt.imshow(wordcloud, interpolation='bicubic')                                                      # imshow() muestra el gráfico de palabras generado por WordCloud. Opciones de interpolación: 'bilinear', 'nearest', 'bicubic', 'hamming'
        plt.axis('off') 
        st.image(wordcloud.to_array())
with col2:
    if st.checkbox('Trending category "IGHTLIF"'): 
        st.title("")
        mix_events = events[events['event_category']=='IGHTLIF']                                            # Filtrar eventos categoría 'IGHTLIF'
        titles = ' '.join(mix_events['title'])                                                              # Concatenar todos los títulos en una sola cadena
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(titles)             # Crear un objeto WordCloud
        plt.figure(figsize=(10, 6))
        plt.imshow(wordcloud, interpolation='bicubic')                                                      # imshow() muestra el gráfico de palabras generado por WordCloud
        plt.axis('off')
        st.image(wordcloud.to_array())





st.title("")
st.title("")
st.title("")
st.title("")


st.subheader("TOP 5 - MIX category")
st.title("")

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    event1 = "Streamlit_app_Feverup/img/event1.png"
    st.image(event1)
    st.write("Baltimore Indoor Skydiving Experience with 2 Flights & Certificate")
    st.write("Total of events: 3808")
with col2:
    event2 = "Streamlit_app_Feverup/img/event2.png"
    st.image(event2)
    st.write("StreetHunt Games: Outdoor Adventure Game")
    st.write("Total of events: 3604")
with col3:
    event3 = "Streamlit_app_Feverup/img/event3.png"
    st.image(event3)
    st.write("British Music Experience")
    st.write("Total of events: 3343")
    
with col4:
    event4 = "Streamlit_app_Feverup/img/event4.png"
    st.image(event4)
    st.write("Las Vegas Escape Game Private Adventure")
    st.write("Total of events: 3149")
with col5:
    event5 = "Streamlit_app_Feverup/img/event5.png"
    st.image(event5)
    st.write("Gourmaze: A Dessert Treasure Hunt")
    st.write("Total of events: 2882")
st.write("Images: https://feverup.com")
st.title("")
st.write("To review each one in depth:")
st.write("Baltimore Indoor Skydiving Experience with 2 Flights & Certificate: https://feverup.com/m/120622")
st.write("StreetHunt Games: Outdoor Adventure Game: https://feverup.com/m/124046")
st.write("British Music Experience: https://feverup.com/m/98210") 
st.write("Las Vegas Escape Game Private Adventure: https://feverup.com/m/113713")  
st.write("Las Vegas Escape Game Private Adventure: https://feverup.com/m/127411")


st.title("")
st.title("")
st.title("")

st.subheader("How many events have there been in the last few months? Which is the trend day and time?")

col1, col2 = st.columns(2)
with col1:
    events['datetime_local'] = pd.to_datetime(events['datetime_local'])
    events_sorted = events.sort_values(by='datetime_local')                                                 # GRÁFICA LINEAL EVENTOS HASTA ABRIL 2024. Ordenar datos según 'datetime_local' 
    events_sorted.set_index('datetime_local', inplace=True)                                                 # Restablecer índice
    events_filtered = events_sorted[events_sorted.index <= '2024-04-01 00:00:00']                           # Filtrar los datos hasta abril de 2024
    events_by_month = events_filtered.resample('M').size()                                                  # Resample -> re-muestrea los datos en intervalos de meses y calcula el tamaño de cada intervalo
    fig = px.line(events_by_month, 
                x=events_by_month.index, 
                y=events_by_month.values,
                labels={'x': 'Date', 'y': 'Events count'},
                markers=True, 
                line_shape='linear')
    fig.update_layout(width=1200, height=500,                                                               # Ajustar el tamaño de la figura
                        xaxis_title='', yaxis_title='',                                                     # Ocultar los nombres de los ejes
                        title_text='<b>Total of events last months</b>', title_x=0.4)                                      # Centrar el título y ponerlo en negrita
    fig.update_yaxes(range=[0, 80000])
    st.plotly_chart(fig)

with col2:                                                                                                  # GRÁFICA BARRAS DISTRIBUCIÓN EVENTOS EN LOS DÍAS DE LA SEMANA
    events['day_of_week'] = events['datetime_local'].dt.day_name()                                          # Obtener el nombre del día de la semana para cada fecha
    events_per_day = events['day_of_week'].value_counts().reset_index()                                     # Contar la frecuencia de eventos por día de la semana y restablecer índice para tener df con 2 columnas
    events_per_day.columns = ['Day of week', 'Event count']                 
    # Crear el gráfico de barras
    fig = px.bar(events_per_day, 
                x='Day of week', 
                y='Event count', 
                labels={'Event Count': 'Number of Events'})          

    fig.update_layout(width=1200, height=500,                                                               # Ajustar el tamaño de la figura
                        xaxis_title='', yaxis_title='',                                                     # Ocultar los nombres de los ejes
                        title_text='<b>Total events by day</b>', title_x=0.38)                              # Centrar el título y ponerlo en negrita
    fig.update_yaxes(range=[0, 80000])                                                                      # Establecer el rango del eje y para que sea igual que en la gráfica lineal
    st.plotly_chart(fig)


col1, col2 = st.columns(2)
with col1:                                                                                                  
    events['hour'] = events['datetime_local'].dt.hour
    events_schedule = events[['hour', 'event_category']]                                                    # Crear un DataFrame con la hora y la categoría
    event_counts = events_schedule.groupby(['hour', 'event_category']).size().reset_index(name='count')     # Contar el número de eventos por hora y categoría
    fig = px.bar(event_counts,                                                                              # Crear el gráfico de barras agrupado por hora y categoría 
                x='hour', 
                y='count', 
                color='event_category',
                labels={'hour': 'Time (hour)', 'count': 'Events count'})
    fig.update_layout(xaxis=dict(type='category'),                                                          # Tipo 'category' para mostrar todas las horas
                        width=1200, height=800,                                                             # Ajustar el tamaño de la figura
                        xaxis_title='', yaxis_title='',
                        title_text='<b>Event distribution by time and category</b>', title_x=0.4)
    fig.update_traces(textfont_size=16)
    st.plotly_chart(fig)
        
with col2:                                                                                                  # GRÁFICO PASTEL PORCENTAJE EVENTOS EN CADA FRANJA HORARIA             
    def get_time_slot(hour):                                                                                # Función para crear nueva columna con franja horaria de los eventos (morning, afternoon, night)
        if hour < 12:
            return 'morning'
        elif hour < 18:
            return 'afternoon'
        else:
            return 'night'

    events['time_slot'] = events['datetime_local'].apply(lambda x: get_time_slot(x.hour))                   # Aplicar la función a la columna 'datetime_local' para obtener la franja horaria                                                                                                 
    time_slot_counts = events['time_slot'].value_counts()                                                   # Calcular el total de eventos en cada franja horaria
    fig = px.pie(time_slot_counts, 
                values=time_slot_counts.values, 
                names=time_slot_counts.index, 
                color_discrete_sequence=px.colors.diverging.Portland)
    fig.update_layout(width=1200, height=500,                                                               # Ajustar el tamaño de la figura
                        title_text='<b>% of events by time</b>', title_x=0.38,                              # Centrar el título y ponerlo en negrita
                        xaxis_title='', yaxis_title='')                                                     # Ocultar los nombres de los ejes
    fig.update_traces(textinfo='percent+label', textfont_size=16)  
    st.plotly_chart(fig)
