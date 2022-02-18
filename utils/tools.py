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
        LEFT JOIN Recette ON (Etape.ID_Recette = Recette.Id_Recette)
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

    @staticmethod
    def get_etapes(con, recette):
        return pd.read_sql(
            sql=f"""
            Select
            Etape.description,
            U.type,
            A.libelle
            FROM Etape
            LEFT JOIN Recette ON (Etape.ID_Recette = Recette.Id_Recette)
            LEFT JOIN Ustensile2Etape U2E on Etape.ID_Etape = U2E.ID_Etape
            LEFT JOIN Ustensile U on U.ID_Ustensile = U2E.ID_Ustensile
            LEFT JOIN Appareils2Etape A2E on Etape.ID_Etape = A2E.ID_Etape
            LEFT JOIN Appareils A on A.ID_Appareils = A2E.ID_Appareils
            WHERE Recette.libelle = "{recette}";
            """, con=con
        ).to_dict(orient='records')
