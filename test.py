import joblib   # añadir a requirements
import pandas as pd
#import streamlit as st
print("Hola")

# Carga el modelo desde el archivo .pkl
modelo = joblib.load("modelos\Extra_Trees_Regressor.pkl")
input_data = {
    'city':['New York'],            # Example city
    'country': ['US'],               # Example country
    'event_category': ['IGHTLIF'],   # Example event category
    # Add more features as needed
}
precio_predicho = modelo.predict(input_data)
print(precio_predicho)
    