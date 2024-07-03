import streamlit as st
from text_generate import page_text_generation


# Configuration du menu
menu = ["Génération de Texte", "Entité Nommée", "Audio en Texte"]
choice = st.sidebar.selectbox("Menu", menu)

# Affichage de la page sélectionnée
if choice == "Génération de Texte":
    page_text_generation()
elif choice == "Entité Nommée":
    