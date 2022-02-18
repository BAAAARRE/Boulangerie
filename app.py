import numpy as np
import streamlit as st

from utils.tools import LoadData


con_database = LoadData.init_connection()


def main():
    # Set configs
    st.set_page_config(
        layout="centered",  # Can be "centered" or "wide". In the future also "dashboard", etc.
        initial_sidebar_state="expanded",  # Can be "auto", "expanded", "collapsed"
        page_title='Bakery Sagna',  # String or None. Strings get appended with "• Streamlit".
        page_icon=None,  # String, anything supported by st.image, or None.
    )

    st.title("Bakery Sagna")
    st.image("https://resize-elle.ladmedia.fr/rcrop/638,,forcex/img/var/plain_site/storage/images/people/la-vie-des-people/news/bresil-2014-les-10-coupes-de-cheveux-les-plus-intrigantes/bacary-sagna-france/48094150-1-fre-FR/Bacary-Sagna-France.jpg", width=150)


    st.header("Choisir une recette")
    list_recette = LoadData.list_recette(con_database)
    recette = st.selectbox("Recette", list_recette)
    qte = st.number_input(f"Nombre de {recette}", min_value=1)
    minutes = int(LoadData.get_time(con_database, recette))
    if minutes == 0:
        minutes = 2
    if minutes > 60:
        hour = round(np.floor(minutes / 60))
        minutes = minutes % 60
        st.write(f"Temps : {hour} h {minutes} min")
    else:
        st.write(f"Temps : {minutes} min")
    #st.write(f"Temps : {hour}:{minutes} min")
    st.image(LoadData.get_image(con_database, recette))

    col1, col2 = st.columns(2)
    with col1:
        st.header("Liste des ingrédients")
        dict_ingredients = LoadData.get_ingredients(con_database, recette)
        for ingredient in dict_ingredients:
            if ingredient['mesure'] == 'pcs':
                st.write(f""" - {ingredient['quantite'] * qte} {ingredient['libelle']}""")
            else:
                if ingredient['libelle'].lower()[0] in ['a', 'e', 'i', 'o', 'u', 'y']:
                    st.write(f""" - {ingredient['quantite'] * qte} {ingredient['mesure']} d'{ingredient['libelle']}""")
                else:
                    st.write(f""" - {ingredient['quantite'] * qte} {ingredient['mesure']} de {ingredient['libelle']}""")

    dict_etapes = LoadData.get_etapes(con_database, recette)

    with col2:
        st.header("Liste des appareils et ustensiles")
        list_app_ust = []
        for etape in dict_etapes:
            if etape['libelle']:
                if etape['libelle'] not in list_app_ust:
                    list_app_ust.append(etape['libelle'])
            if etape['type']:
                if etape['type'] not in list_app_ust:
                    list_app_ust.append(etape['type'])

        for app_ust in list_app_ust:
            st.write(f""" - {app_ust}""")

    st.header("Liste des étapes")
    dict_etapes = LoadData.get_etapes(con_database, recette)

    for idx, etape in enumerate(dict_etapes):
        st.subheader(f" ETAPE {idx + 1}")
        if etape['libelle']:
            st.write(f"Appareil : {etape['libelle']}")
        if etape['type']:
            st.write(f"Ustensile : {etape['type']}")
        st.write(f"Description : {etape['description']}")

    # Bottom page
    st.write("\n")
    st.write("\n")
    st.info("""By the crack : [Highlights](https://www.youtube.com/watch?v=eU0t_JcRBqs)""")


if __name__ == "__main__":
    main()
