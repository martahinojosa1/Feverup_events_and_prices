#---------------------------- LIBRERÍAS ----------------------------#
import joblib  
import streamlit as st

# Carga el modelo desde el archivo .pkl
modelo = joblib.load("modelos/Gradient_Boosting_Regressor.pkl")


# Título predictor
st.title('Ticket price predictor')

# Widgets para la entrada de datos
event_category = st.selectbox('Event Category', options=['THEATER', 'TASTING', 'IGHTLIF', 'CONCERT', 'WELLNESS', 'MIX'])
city = st.selectbox('City', options=['London', 'New York', 'Chicago', 'Dallas', 'Birmingham', 'Austin', 'Edmonton'])

# Botón para realizar la predicción
if st.button('Predecir'):
    # Realiza la predicción utilizando el modelo cargado
    data = {
    'city': [city],            
    'event_category': [event_category],   
}
    precio_predicho = round(modelo.predict(data)[0],2)
    print(precio_predicho) 
    st.write(f'El precio predicho es: {precio_predicho}')


