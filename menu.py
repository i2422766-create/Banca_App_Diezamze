import streamlit as st
from views import home, simulador

def mostrar_menu():
    opciones = {
        "Inicio": home.mostrar,
        "Simulador de créditos": simulador.mostrar
    }

    seleccion = st.sidebar.selectbox("Navegación", list(opciones.keys()))
    opciones[seleccion]()
