"""
Created on Mar 03, 2021.

@author: Cyril Vandenberghe & Karina Castillo
"""
from PIL import Image
import streamlit as st


def write():
    st.title("Le projet Mushroom Recognition")
    st.header("Objectif du projet:")
    st.write("Faire de la **reconnaissance d'images de champignon** à \
                l’aide d'algorithmes de **computer vision**.")
    image = Image.open('images/computer_vision.jpg')
    st.image(image, caption='', use_column_width=True)
