import json
import pandas as pd
import matplotlib
import streamlit as st
from utils import read_all_data

st.set_page_config(
    page_title="Hello Page",
    page_icon="👋",
)

str_description1,str_description2,str_description3,df3,df5,data_depo = read_all_data.read_data_home()

st.header("Data we used: ")
tab1, tab2, tab3 = st.tabs(["Data used 1", "Data used 2", "Data used 3"])

with tab1:
   st.markdown(str_description1)
   col1, col2 = st.columns(2)

with col1:
   st.write("terra-luna.csv")
   st.dataframe(df3)
with col2:
   st.write("ethereum.csv")
   st.dataframe(df5)


with tab2:
   st.markdown(str_description2)
   st.json(data_depo)

with tab3:
   st.markdown(str_description3)

