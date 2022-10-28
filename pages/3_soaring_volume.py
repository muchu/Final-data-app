import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from utils import read_all_data

plt.style.use('seaborn')

df1 = read_all_data.read_data_thrid()
fig,ax = plt.subplots()
df1.Volume.plot(label = 'Volumn',linestyle='solid',color='blue')
ax.set_ylabel('Daily volumn')
ax.legend()
ax.set_title('daily volumn of crypto luna',fontsize=15,color='r')
st.pyplot(fig)