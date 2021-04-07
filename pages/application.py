"""
Created on Mar 02, 2021.

@author: Cyril Vandenberghe & Karina Castillo
"""
from PIL import Image
import streamlit as st


def write():
    st.title("Possible application")
    st.markdown("https://mushroomobserver.org")
    image = Image.open('images/Mushroom_observer_web.png')
    st.image(image, caption='', use_column_width=True)
    st.write("L'identification des champignons se fait par le vote de la \
             communauté du site. Cette identification est assez subjective et \
             peut induire en erreur lorsque les espèces sont très \
             ressemblantes")
    st.write("Notre modèle pourrait contribuer à donner une vision plus \
             objective de cette classification, en fonctionnant comme un \
             *widget* sur cette page où les utilisateurs soumettent leur \
             image et le modèle prédit son identification.")
    st.write("Le modèle actuel peut assurer une identification réelle à \
             ~90% (`top_k_accuracy` avec k=2).")
