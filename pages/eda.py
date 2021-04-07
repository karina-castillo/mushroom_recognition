"""
Created on Mar 03, 2021.

@author: Cyril Vandenberghe & Karina Castillo
"""
from PIL import Image
import streamlit as st


def write():
    st.title("Analyse exploratoire")
    st.header("1. Les données")
    st.markdown("**Site utilisé**: [MushroomObserver](https://mushroomobserver.org/)")
    st.write("* Base de données d'images dédiée à l’identification des champignons.")
    image = Image.open('images/Mushroom_observer_web.png')
    st.image(image, caption='', use_column_width=True)
    st.header("2. Exploration des données")
    st.markdown("**Projet existant**: [mushroomobser-dataset](https://github.com/bechtle/mushroomobser-dataset)")
    st.write("* Cet ancien projet avait déjà exploré ce site et a créé un \
             dataset d'images datant de 2006 à 2016.")
    st.write("* Les images sont dans deux datasets distincts. \
             L’un nommé *complete_dataset* qui contient toutes les images \
             scrapées de 2006 à 2016. L’autre nommé *clean_dataset* contient \
             les images considérées comme valides.")
    st.write("* 12 fichiers json qui contiennent des informations relatives \
             aux images.")
    st.write("**Partie 'Data Engineering'**:")
    st.write("Pour créer notre dataframe et avoir les images utiles à notre \
             modélisation, nous avons créé plusieurs fonctions.")
    st.write("* Une fonction qui crée un dataframe à partir des fichiers \
             json.")
    st.write("* Une fonction qui crée un dataset d’images contenant \
             uniquement les images avec les genres que nous souhaitons \
             prédire.")
    st.write("* Une fonction qui crée un fichier zip contenant le dataset \
             créé avec la fonction précédente. Le but est de pouvoir utiliser \
             ce fichier zip pour se partager facilement les images et de les \
             utiliser par la suite dans l’environnement *Google Colab*")
    st.write("* Une fonction qui va copier notre fichier zip depuis \
             *Google Drive* dans l’environnement de *Google Colab*")
    st.write("Ces fonctions nous ont permis de créer notre dataframe issu des \
             images de notre dataset d'intérêt.")
    st.write("Ces images représentent environ 34% (soit 218 262 images) du \
             nombre d'images disponibles")

    st.header("3. Nettoyage des données")
    st.subheader("Suppresion des données non-informatives")
    st.write("**Suppresion des colonnes non-informatives**: Nous gardons \
             uniquement les variables relatives aux images et à la taxonomie \
             des champignons.")
    st.write("**Suppresion des observations non-informatives**: La colonne \
             `rank` indique quel est le dernier niveau taxonomique atteint \
             dans l'identification des champignons.")
    image = Image.open('images/taxonomy.jpg')
    st.image(image, caption='Rangs taxonomiques', use_column_width=True)
    image = Image.open('images/species.png')
    st.image(image, caption='', use_column_width=True)
    image = Image.open('images/kingdom.png')
    st.image(image, caption='', use_column_width=True)
    st.write("Ainsi, si une entrée a pour valeur `KINGDOM` dans la colonne \
             `rank`, cela signifie que la valeur du label sera la plus \
             générale de l'identification. Les images identifiées peuvent \
             donc appartenir à n'importe quel champignon et être très \
             hétérogènes.")
    image = Image.open('images/tax_final.png')
    st.image(image, caption='Taxons supprimés', use_column_width=True)
    st.write("C'est pourquoi les images ayant `KINGDOM`, `PHYLUM`, `CLASS` et \
             `ORDER` pour valeurs dans la colonne `rank` ne seront pas \
             conservées car elles sont trop générales et non-informatives.")

    st.header("4. Visualisation des données")
    st.write("Nous voulons maintenant connaître la distribution des images \
             dans les taxons `SPECIES`,`GENUS` et `FAMILY`.")
    st.write("**Le fait de disposer d'un bon nombre d'images est essentiel \
             pour le développement de notre projet.**")

    st.subheader("Distributions de nombre des images par taxon")
    st.write("Le graphique ci-dessous, nous permet de visualiser la \
             distribution du nombre d’images de chaque label dans les 3 \
             taxons.")
    st.write("Cette distribution est représentée en 4 intervalles, avec des \
             labels représentés par **1 à 10 images**, de **11 à 100 images**,\
             de **101 à 1000 images** et de **plus de 1000 images**.")
    image = Image.open('images/tax_comparative.png')
    st.image(image, caption='', use_column_width=True)
    st.write("* 75 % des labels des `SPECIES` sont représentés par 1 ou 10 \
             images.")
    st.write("* Nous observons que `GENUS` et `FAMILY` ont environ 40 labels \
             chacun, représentés avec 1000 images ou plus.")
    st.write("* Pour la suite de notre projet, nous considerons que `GENUS` \
             est un bon compromis entre le niveau taxonomique et le nombre \
             d'images disponible.")
    st.subheader("Taxon Genus: Data final")
    st.write("Le graphique ci-dessous montre le nombre d'images pour les 41 \
             genres selectionnés. Pour une question de puissance de calcul et \
             différence des nombre d'images entre eux, nous avons choisi les \
            15 premiers genres comme jeu de données final pour nos analyses.")
    image = Image.open('images/genus_final.png')
    st.image(image, caption='', use_column_width=True)
