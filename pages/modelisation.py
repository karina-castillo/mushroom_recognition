"""
Created on Mar 03, 2021.

@author: Cyril Vandenberghe & Karina Castillo
"""
from PIL import Image
import streamlit as st


def write():
    st.title("Modélisation")
    st.header("1. Classification du problème")
    st.write("Rappelons-nous que l'objectif de ce projet est l'identification \
             des images des champignons à l’aide d'algorithmes de computer \
             vision.")
    st.write("Il s'agit d'un problème de **classification d'images** qui \
             peut être abordé par des méthodes de **deep learning**.")
    image = Image.open('images/Deeplearning.jpg')
    st.image(image, caption='', use_column_width=True)
    st.write("Pour atteindre notre objectif, nous avons testé 3 modèles.")
    st.write("La métrique utilisée pour comparer les performances de ces \
             modèles était la `accuracy`.")
    st.write("Nous avons aussi calculé le `top-k accuracy` (du package \
             `sklearn.metrics`) avec k = 2 et 3 pour évaluer la fréquence à \
             laquelle la catégorie réelle se situe entre les deux ou trois \
             catégories les plus probables.")

    st.header("2. Test des différents modèles")
    st.subheader("LeNet")
    image = Image.open('images/LeNet.png')
    st.image(image, caption='', use_column_width=True)
    st.write("**loss**: 0.9852 - **accuracy**: 0.7146 - **val_loss**: 11.3361 \
             - **val_accuracy**: 0.0983")
    st.write("* Le modèle de base ne semble pas être adapté à nos données.")
    st.write("* Il a été décidé qu'il était préférable d'essayer d'autres \
             modèles.")

    st.subheader("VGG16")
    image = Image.open('images/VGG16.jpg')
    st.image(image, caption='', use_column_width=True)
    st.write("* **Première itération**: Prédiction sur 3 genus en utilisant \
             *VGG16* en *transfer learning*.")
    st.write("* **Deuxième itération**: Etendre la prédiction aux 15 genus et \
             augmenter la complexité.")
    st.write("Les résultats étaient encourageants mais le modèle souffrait \
             d'*overfitting.*")
    st.write("* **Nouvelle architecture**: Ajout de couche *Dense* et \
             augmentation de la valeur du *Dropout* afin de diminuer \
             l'*overfitting*. Utilisation des callbacks *ReduceLROnPlateau* \
             et *EarlyStopping*.")
    st.write("**Résultat final**:")
    st.write("* **accuracy**: 0.7999 - **val_accuracy**: 0.7545 - \
             **top_2_accuracy**: 0.8626 - **top_3_accuracy**:0.9055")
    st.write("Voici un affichage des prédictions du modèle sur 6 images:")
    image = Image.open('images/vgg_results.png')
    st.image(image, caption='', use_column_width=True)

    st.subheader("EfficientNetB1")
    st.write("* **Première itération**:")
    st.write("Pour l’architecture des couches de classification nous nous \
             sommes inspirés du modèle précédent (VGG16) vu les résultats \
             obtenus.")
    st.write("Le premier test a donné les résultats suivants :")
    st.write("**loss**: 0.1514, **accuracy**: 0.9498, **val_loss**: 0.7976 , \
             **val_accuracy**: 0.7985")
    st.write("On observe un bon score mais on peut noter la présence \
             d’overfitting.")
    st.write("**Test pour améliorer le score du modèle** :")
    st.write("* Les modèles EfficientNet :")
    image = Image.open('images/tableau_efficient.png')
    st.image(image, caption='', use_column_width=True)
    st.write("**EffcientNetB1**: meilleur score avec une architecture moins \
             complexe (par rapport aux autres architectures EfficientNet).")
    st.write("* *Modification des paramètres des couches de classification*:")
    st.write("*Overfitting*: ajout d’une couche `Dense` et une couche \
             `Dropout` (augmentation de la valeur de couche `Dropout`Dropout \
             de 0.2 à 0.6)")
    st.write("* *Les callbacks*:")
    st.write("Pendant l'entraînement du modèle nous utilisons également les \
             callbacks `EarlyStopping` et `ReduceLROnPlateau` (VGG16).")
    st.write("* **Nouvelle architecture**:")
    image = Image.open('images/EfficientNetB1.jpg')
    st.image(image, caption='', use_column_width=True)
    st.write("Pour cette nouvelle architecture (schéma), les valeurs de \
             classifications sont les suivantes:")
    st.write("**Résultat final**:")
    image = Image.open('images/score_efficient.png')
    st.image(image, caption='', use_column_width=True)
    st.write("Voici un affichage des prédictions du modèle sur 6 images:")
    image = Image.open('images/pred_efficient15.png')
    st.image(image, caption='', use_column_width=True)

    st.subheader("Analyse des classes confondues")
    st.write("La **matrice de confusion** montre que 6 classes sont \
             confondues lors de la classification (8 et 13, 0 et 7, 3 et 4)")
    image = Image.open('images/Matrice_confusion.jpg')
    st.image(image, caption='Matrice de confusion EfficientNetB1',
             use_column_width=True)
    st.write("La littérature montre que ces couples de champignons confondus \
             sont **très similaires morphologiquement** et appartiennent à la \
             **même famille taxonomique**.")
    image = Image.open('images/Classes_confondus_table.png')
    st.image(image, caption='', use_column_width=True)
    st.write("Les images suivantes montrent ces similitudes morphologiques \
             (*source: Wikipedia*)")
    image = Image.open('images/champignon.jpg')
    st.image(image, caption='', use_column_width=True)
    st.write("En considérant les résultats de la matrice de confusion \
             présentée ci-dessus, nous avons voulu évaluer notre modèle en \
             l’entraînant sur 12 genus en supprimant trois des classes \
             confondues.")

    st.subheader("EfficientNetB1: Evaluation sans classes confondus")
    st.write("L'architecture est la même mais avec 12 genres (3 éliminés).")
    image = Image.open('images/Genres_eliminés_table.png')
    st.image(image, caption='', use_column_width=True)
    st.write("Les valeurs des scores des classifications sont les suivantes:")
    image = Image.open('images/score_effi12genus.png')
    st.image(image, caption='', use_column_width=True)
    st.write("* Le score de l’accuracy est meilleur que celui présenté \
             précédemment avec les 15 genus (`val_accuracy`: **0.7939**).")
    st.write("* Les scores de `top_k_accuracy` sont supérieurs à **0.90**.")
    st.write("Cela montre que ce modèle est robuste et suggère que avec un \
             dataset mieux classé, nous aurions probablement obtenu un modèle \
             encore plus performant.")

    st.header("3. Synthèse des résultats")
    image = Image.open('images/tableau_synthese_resultats.png')
    st.image(image, caption='', use_column_width=True)
    st.markdown("**EfficientNet** serait l'approche la plus adaptée à notre \
                problème de classification des images de champignons.")
