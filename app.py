import streamlit as st

from utils.tools import LoadData


con_database = LoadData.init_connection()


def main():
    # Set configs
    st.set_page_config(
        layout="centered",  # Can be "centered" or "wide". In the future also "dashboard", etc.
        initial_sidebar_state="expanded",  # Can be "auto", "expanded", "collapsed"
        page_title='Twitter',  # String or None. Strings get appended with "• Streamlit".
        page_icon=None,  # String, anything supported by st.image, or None.
    )

    st.title("Bakery Sagna")


    st.header("Choisir une recette")
    list_recette = LoadData.list_recette(con_database)
    recette = st.selectbox("Recette", list_recette)
    qte = st.number_input(f"Nombre de {recette}", min_value=1)
    st.write(f"Temps : {int(LoadData.get_time(con_database, recette))} min")
    st.image(LoadData.get_image(con_database, recette))

    st.header("Liste des ingrédients")
    dict_ingredients = LoadData.get_ingredients(con_database, recette)
    for ingredient in dict_ingredients:
        st.write(f""" - {ingredient['quantite'] * qte} {ingredient['mesure']} de {ingredient['libelle']}""")

    st.header("Liste des étapes")
    dict_etapes = LoadData.get_etapes(con_database, recette)
    # st.write(dict_etapes)

    for idx, etape in enumerate(dict_etapes):
        st.subheader(f" ETAPE {idx + 1}")
        st.write(etape['libelle'])

    # Bottom page
    st.write("\n")
    st.write("\n")
    st.info("""By : [Linkedin](https://www.linkedin.com/in/florent-barre-a25921194/))""")


if __name__ == "__main__":
    main()
