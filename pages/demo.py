"""
Created on Mar 03, 2021.

@author: Cyril Vandenberghe & Karina Castillo
"""
from PIL import Image
import streamlit as st
import tensorflow as tf


@st.cache(allow_output_mutation=True)
def load_model(name):
    model = tf.keras.models.load_model('models/'+name)
    return model


def write():
    st.title("Prédiction (Démo)")
    labels = {
        0: "Agrocybe",
        1: "Cantharellus",
        2: "Cladonia",
        3: "Coprinellus",
        4: "Coprinopsis",
        5: "Galerina",
        6: "Helvella",
        7: "Hypholoma",
        8: "Leccinum",
        9: "Lepiota",
        10: "Lycoperdon",
        11: "Morchella",
        12: "Trametes",
        13: "Tylopilus",
        14: "Xylaria"
    }
    file = st.file_uploader(label="", type=['jpg'])
    if file is not None:
        st.header("Choix du modèle")
        options = ["EfficientNetB1", "VGG16"]
        selectbox = st.selectbox("", options)
        if selectbox == "VGG16":
            model = load_model('VGG16.h5')
            size = (224, 224)
        else:
            model = load_model('EfficientNetB1.h5')
            size = (256, 256)
        X_test = []
        im = tf.io.read_file("images/test/"+file.name)
        im = tf.image.decode_jpeg(im, channels=3)
        im = tf.image.resize(im, size=size)
        X_test.append([im])
        X_test = tf.concat(X_test, axis=0)
        prediction = model.predict(X_test)
        st.write(prediction)
        prediction = tf.argmax(prediction, axis=-1).numpy()
        check = st.checkbox(label="Afficher les labels", value=False)
        if check:
            st.json(labels)
        image = Image.open(file)
        st.image(image)
        st.write("Le vrai label est: "+file.name.capitalize().split('.')[0])
        st.write("La prédiction est: "+labels[prediction[0]])
