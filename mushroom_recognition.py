"""
Created on Mar 01, 2021.

@author: Cyril Vandenberghe & Karina Castillo
"""
import streamlit as st
from pages import project, eda, modelisation, problems, demo, application, \
    conclusion

PAGES = {
        "Le projet Mushroom Recognition": project,
        "Analyse exploratoire": eda,
        "Modélisation": modelisation,
        "Prédiction (Démo)": demo,
        "Difficultés rencontrées lors du projet": problems,
        "Conclusion": conclusion,
        "Possible application": application
    }


def main():
    st.sidebar.title("Mushroom Recognition")
    st.sidebar.subheader("Menu")
    selection = st.sidebar.radio("", tuple(PAGES.keys()))
    page = PAGES[selection]
    with st.spinner(f"Loading {selection} ..."):
        page.write()
    st.sidebar.info(
        "**Projet Final**\n\n"
        "Parcours Bootcamp - Data Scientist Mars 2021\n\n"
        "*Auteurs*:\n\n"
        "Karina Castillo Pérez\n\n"
        "Cyril Vandenberghe\n\n"
        "*Mentor*: Adrien Ruimy"
    )


if __name__ == '__main__':
    main()
