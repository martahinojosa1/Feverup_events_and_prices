#---------------------------- LIBRERÍAS ----------------------------#
import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly_express as px
import streamlit.components.v1 as components




#---------------------------- CONFIGURACIÓN DE LA PÁGINA ----------------------------#
st.set_page_config(
    layout="wide"                                        
)

logo = r"C:\Users\Marta\Documents\GitHub\Feverup_events_and_prices\Streamlit_app_Feverup\img\logo.png"




#---------------------------- DATOS DE LA PÁGINA ----------------------------#
tickets = pd.read_csv(r"C:\Users\Marta\Desktop\BOOTCAMP_DATA_ANALYTICS\DATA\TEMARIO\Modulo_3\8-PROYECTO_FINAL\data\tickets_processed.csv")




#---------------------------- HEADER ----------------------------#
st.image(logo, width=200)    
st.title("")
st.markdown("<h1 style='color: #38b6ff; font-size: 52px;'>Ticket price analysis</h1>", unsafe_allow_html=True)
st.title("")
st.title("")
st.write("<h5>The sample dataset contains 2655 rows and 20 columns with 19 unique events. In this case, it includes numeric variables that are interesting for the price analysis. Countries represented are the USA and the United Kingdom. The sample data starts on October 8, 2023 and ends on December 31, 2023 (84 days).</h5>", unsafe_allow_html=True)
st.title("")
st.title("")




#---------------------------- BODY ----------------------------#
col1, col2_3 = st.columns([1, 2])
with col1:                                                                                              # BOX PLOT DISTRIBUCIÓN 'ticket_price'
    fig = px.box(tickets, y='ticket_price')
    fig.update_layout(width=400, height=600,                                                            # Ajustar el tamaño de la figura
                        title_text='<b>Distribution of ticket prices ($)</b>', title_x=0.25,            # Centrar el título y ponerlo en negrita
                        xaxis_title='', yaxis_title='Price ($)')                                        # Ocultar los nombres de los ejes
    st.plotly_chart(fig)

with col2_3:                                                                                            # SCATTER PLOT TICKETS MÁS VENDIDOS
    ticket_counts = tickets['ticket_price'].value_counts().reset_index()                                # Obtener el recuento de tickets vendidos para cada precio
    ticket_counts.columns = ['ticket_price', 'ticket_count']
    fig = px.scatter(ticket_counts, x='ticket_price', y='ticket_count',
                    labels={'ticket_price': 'Ticket Price', 'ticket_count': 'Ticket Count'},
                    size='ticket_count', size_max=20)
    fig.update_layout(width=900, height=600,                                                            # Ajustar el tamaño de la figura
                        title_text='<b>Best selling tickets</b>', title_x=0.45,                         # Centrar el título y ponerlo en negrita
                        xaxis_title='Price ($)', yaxis_title='Tickets count')                           # Ocultar los nombres de los ejes
    st.plotly_chart(fig)


st.title("")
st.title("")
st.title("")


col1, col2_3 = st.columns([1, 2])
with col1:                                                                                              # TREEMAP TOTAL TICKETS VENDIDOS POR CATEGORÍAS
    category_counts = tickets.groupby('event_category')['quantity'].sum().reset_index()                 # Agrupar por categoría y sumar la cantidad de tickets vendidos en cada una
    category_counts.columns = ['event_category', 'revenue']
    fig = px.treemap(category_counts, path=['event_category'], values='revenue')
    fig.update_layout(width=400, height=600,  
                        title_text='<b>Total of tickets sold by category</b>', title_x=0.2)             # Título centrado y en negrita
    st.plotly_chart(fig)

with col2_3:                                                                                            # SCATTER PLOT AVERAGE OF TICKET PRICE BY CATEGORY
    mean_prices = tickets.groupby('event_category')['ticket_price'].mean().reset_index()
    mean_prices = round(mean_prices,2)
    fig = px.scatter(mean_prices, x='event_category', y='ticket_price',
                    color='ticket_price', color_continuous_scale='RdYlGn',                              # Paleta de colores de rojo a verde 
                    size='ticket_price', size_max=20,
                    hover_data={'event_category': False})                                               # Ocultar la información de la categoría de evento al pasar el ratón)
    fig.update_layout(width=1000, height=600,                                                           # Ajustar el tamaño de la figura
                        title_text='<b>Mean of ticket price by category</b>', title_x=0.4,              # Centrar el título y ponerlo en negrita
                        xaxis_title='', yaxis_title='Price ($)')                                        # Ocultar los nombres de los ejes
    st.plotly_chart(fig)

    
st.title("")
st.title("")
st.title("")

st.markdown('<iframe title="Gross_revenue_tickets" width="600" height="373.5" src="https://app.powerbi.com/view?r=eyJrIjoiNGUwODA0MGMtZjgxMy00OTdjLTk0N2MtMWY2MWM5OWRiYTllIiwidCI6IjhhZWJkZGI2LTM0MTgtNDNhMS1hMjU1LWI5NjQxODZlY2M2NCIsImMiOjl9" frameborder="0" allowFullScreen="true"></iframe>', unsafe_allow_html=True)


