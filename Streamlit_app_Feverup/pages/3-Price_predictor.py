#---------------------------- LIBRERÍAS ----------------------------#
import joblib  
import streamlit as st
import pycaret 

# Carga el modelo desde el archivo .pkl
modelo = joblib.load("modelos/Gradient_Boosting_Regressor.pkl")


# Título predictor
st.title("")
st.markdown("<h1 style='color: #38b6ff; font-size: 52px;'>Ticket price predictor</h1>", unsafe_allow_html=True)
st.title("")
st.title("")
st.title("")
st.write("This analysis trains and explores different kinds of machine learning models for this data. You can see a brief and useful sample here:")
st.title("")
st.title("")
st.title("")

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
    
    


st.title("")
st.title("")
st.title("")
st.subheader("More predictions are coming very soon!")


