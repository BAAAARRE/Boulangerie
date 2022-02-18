import pandas as pd
import streamlit as st
import mysql.connector

from utils.queries import LoadDataQueries

dict_queries = LoadDataQueries.dict_queries


class LoadData:
    @staticmethod
    def init_connection():
        return mysql.connector.connect(**st.secrets["mysql"])

    @staticmethod
    def list_recette(con):
        return pd.read_sql(sql=dict_queries["all_recettes"], con=con)

    @staticmethod
    def get_image(con, recette):
        return pd.read_sql(sql=f"SELECT url_image FROM Recette WHERE Libelle = '{recette}'", con=con).iloc[0, 0]

    @staticmethod
    def get_time(con, recette):
        return pd.read_sql(sql=f"""
        Select sum(temps)
        FROM Etape
        LEFT JOIN Recette ON (Etape.ID_Etape = Recette.Id_Recette)
        WHERE Recette.Libelle = '{recette}';
        """, con=con).iloc[0, 0]

    @staticmethod
    def get_ingredients(con, recette):
        return pd.read_sql(sql=f"""
        Select Ingredients.*
        FROM Ingredients
        LEFT JOIN Recette ON (Ingredients.ID_Recette = Recette.Id_Recette)
        WHERE Recette.libelle = '{recette}';
        """, con=con).to_dict(orient='records')
