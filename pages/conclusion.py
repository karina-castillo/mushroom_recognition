"""
Created on Mar 03, 2021.

@author: Cyril Vandenberghe & Karina Castillo
"""
import streamlit as st


def write():
    st.title("Conclusion")
    st.subheader("Les données:")
    st.write("1. **Matrice de confusion**: confusion des labels peut être dû \
             au fait que la classification taxonomique est erronée (très \
             similaire morphologiquement, l’identification des taxon se fait \
             par vote de la communauté du site).")
    st.write("2. **EfficientNetB1 sur 12 genus**: augmentation de l’`accuracy`\
             en retirant 3 des 6 classes confondues. La performance du modèle \
             est probablement liée à la qualité des données.")
    st.write("3. Dans l'affichage des prédictions, nous avons remarqué que \
             dans plusieurs cas, une mauvaise classification était liée à une \
             image de mauvaise qualité.")
    st.subheader("Les modèles:")
    st.write("1. Compte tenu de la qualité des images, les résultats de \
             *VGG16* et *EfficientNetB1* (accuracy **0,7545** et **0.7939** \
             respectivement), peuvent être considérés comme performants.")
    st.write("2. L'approche par *Transfer Learning* avec le modèle \
             *EfficientNetB1*, serait le plus adapté à notre problème de \
             classification des images de champignon.")
    st.subheader("Hypothèse")
    st.write("*La performance de notre modèle est principalement liée à la \
             qualité des données plutôt qu'à son architecture*")

    st.title("Pistes d'amélioration")
    st.write("* Entraîner le modèle avec un dataset adéquat, c'est-à-dire, \
             avec des images de meilleure qualité et une classification plus \
             soignée.")
    st.write("* Augmenter le nombre d'images par label (de 1000 à 2000 par \
             exemple), afin de réduire l'erreur liée à la subjectivité de la \
             classification morphologique.")
    st.write("* Combiner la partie d’extraction des features de notre modèle \
             et en la combinant avec un modèle de classification classique, \
             comme *Random Forest* ou *SVM* par exemple, afin d’obtenir de \
             meilleurs résultats.")
