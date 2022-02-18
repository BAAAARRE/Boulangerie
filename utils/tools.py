import pandas as pd
import streamlit as st
import mysql.connector

from utils.queries import LoadDataQueries

dict_queries = LoadDataQueries.dict_queries


class LoadData:
    @staticmethod
    def init_connection():
        return mysql.connector.connect(**st.secrets["mysql"])
