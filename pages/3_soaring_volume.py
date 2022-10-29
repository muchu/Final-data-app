import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



@st.cache
def read_data_thrid():
    df1 = pd.read_csv('../Final-data-app/archive/Terra.csv')
    return df1

plt.style.use('seaborn')

df1 = read_data_thrid()
fig,ax = plt.subplots()
df1.Volume.plot(label = 'Volumn',linestyle='solid',color='blue')
ax.set_ylabel('Daily volumn')
ax.legend()
ax.set_title('daily volumn of crypto luna',fontsize=15,color='r')
st.pyplot(fig)