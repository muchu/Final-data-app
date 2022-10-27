import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn')

df1 = pd.read_csv('D:/resource/MISY225/my-streamlit/Final-data-app/archive/Terra.csv')
fig,ax = plt.subplots()
df1.Volume.plot(label = 'Volumn',linestyle='solid',color='blue')
ax.set_ylabel('Daily volumn')
ax.legend()
ax.set_title('daily volumn of crypto luna',fontsize=15,color='r')
st.pyplot(fig)