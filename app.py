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


    st.subheader("Choisir une recette")
    list_recette = LoadData.list_recette(con_database)
    recette = st.selectbox("Recette", list_recette)
    st.number_input(f"Nombre de {recette}", min_value=1)
    st.write(f"Temps : {int(LoadData.get_time(con_database, recette))} min")
    st.write(LoadData.get_image(con_database, recette))

    st.subheader("Liste des ingrédients")
    list_ingredient = ["1 Oeuf", "100g de farine"]
    for ingredient in list_ingredient:
        st.write(f"- {ingredient}")

    st.subheader("Etapes")
    list_etapes = ["Etape 1 : Mélanger", "Etape 2 : Cuire"]
    for etape in list_etapes:
        st.write(f"- {etape}")


    # Bottom page
    st.write("\n")
    st.write("\n")
    st.info("""By : [Linkedin](https://www.linkedin.com/in/florent-barre-a25921194/))""")


if __name__ == "__main__":
    main()
