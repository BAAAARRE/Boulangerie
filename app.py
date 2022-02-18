import streamlit as st

from utils.tools import LoadData


LoadData.init_connection()


def main():
    # Set configs
    st.set_page_config(
        layout="centered",  # Can be "centered" or "wide". In the future also "dashboard", etc.
        initial_sidebar_state="expanded",  # Can be "auto", "expanded", "collapsed"
        page_title='Twitter',  # String or None. Strings get appended with "• Streamlit".
        page_icon=None,  # String, anything supported by st.image, or None.
    )

    LoadData.init_connection()

    # Bottom page
    st.write("\n")
    st.write("\n")
    st.info("""By : [Linkedin](https://www.linkedin.com/in/florent-barre-a25921194/) / 
            Ligue des Datas [Instagram](https://www.instagram.com/ligueddatas/)  |
            Data source : [Twitter](https://twitter.com/home)""")


if __name__ == "__main__":
    main()
