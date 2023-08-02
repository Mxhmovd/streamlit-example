from st_aggrid import AgGrid
import pandas as pd
import streamlit as st

df = pd.read_csv('Deleted Domains.csv')
st.dataframe(data=df)
