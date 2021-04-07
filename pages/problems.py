"""
Created on Mar 03, 2021.

@author: Cyril Vandenberghe & Karina Castillo
"""
from PIL import Image
import streamlit as st


def write():
    st.title("Difficultés rencontrées")
    st.write("* Images manquantes.")
    image = Image.open('images/missing.png')
    st.image(image, caption='', use_column_width=False)
    st.write("* Qualité de certaines images.")
    image = Image.open('images/qualite.png')
    st.image(image, caption='', use_column_width=False)
    st.write("Certaines images contiennent des éléments qui peuvent empêcher \
             le modèle à bien identifier le champignon, comme par exemple des \
             images avec beaucoup de bruit autour du champignon à classifier \
             (image **1**, **2**). Des images sans champignon à classifier \
             (image **3**). Des images avec plus d’un champignon \
             (image **4**)")
