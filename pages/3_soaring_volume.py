import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df1 = pd.read_csv(open('./archive/Terra.csv'))

plt.style.use('seaborn')

st.header('The volume of luna from the date of issue to the crash')
fig, ax = plt.subplots()

df1.Volume.plot(label='Volumn', linestyle='solid', color='blue')
ax.set_ylabel('Daily volumn')
ax.legend()
ax.set_title('Daily volumn of crypto luna', fontsize=15, color='#595959')
st.pyplot(fig)
