#---------------------------- LIBRERÍAS ----------------------------#
import joblib   # añadir a requirements
import streamlit as st


# Carga el modelo desde el archivo .pkl
modelo = joblib.load("modelos\Extra_Trees_Regressor.pkl")


# Título predictor
st.title('Ticket price predictor')

# Widgets para la entrada de datos
event_category = st.selectbox('Event Category', options=['THEATER', 'TASTING', 'IGHTLIF', 'CONCERT', 'WELLNESS', 'MIX'])
country = st.selectbox('Country', options=['GB', 'US', 'CA'])

# Botón para realizar la predicción
if st.button('Predecir'):
    # Realiza la predicción utilizando el modelo cargado
    precio_predicho = modelo.predict([[event_category, country]])[0]
    st.write(f'El precio predicho es: {precio_predicho}')


