import pandas as pd
import streamlit as st
import plotly.express as px


df = pd.read_csv("censo_1872.csv")
df = df.drop_duplicates()


st.set_page_config(page_title="Censo 1872", layout="wide")

st.title("Painel Streamlit do Censo de 1872")
st.header("Gráficos de  Homens livres")
