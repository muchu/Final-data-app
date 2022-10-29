import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



df1 = pd.read_csv('../Final-data-app/archive/Terra.csv')
df2 = pd.read_csv('../Final-data-app/archive/terrausd.csv')
df3 = pd.read_csv('../Final-data-app/archive/terra-luna.csv')
df4 = pd.read_csv('../Final-data-app/archive/bitcoin.csv')
df5 = pd.read_csv('../Final-data-app/archive/ethereum.csv')


plt.style.use('seaborn')

#1:全部的luna币价格波动
from matplotlib.lines import lineStyles
from matplotlib.pyplot import title


st.subheader('The daily closing price of a luna coin from the date of issue to the crash')
fig,ax = plt.subplots()
df1.Close.plot(label = 'close price',linestyle='solid',color='blue')
ax.set_ylabel('Daily closing price($)')
ax.legend()
ax.set_title('daily closing price($) of crypto luna',fontsize=15,color='r')
ax.set_xlabel('Cumulative days of issue')
st.pyplot(fig)


#2：5月份两张图
st.subheader('The daily price of luna and USD during the crash')

fig,ax = plt.subplots(2,1,figsize=[10,15])
price_2 = df2.iloc[2:len(df3):10,2: ]
price_3 = df3.iloc[2:len(df3):10,2: ]

price_2.plot(ax = ax[0],label='usd', linestyle = 'dashed',  color = 'blue')

price_3.plot(ax = ax[1],label='luna', linestyle = 'dashed',  color = 'blue')

ax[0].set_ylabel('Daily price($)')
ax[1].set_ylabel('Daily price($)')


ax[0].legend()
ax[1].legend()

ax[0].set_title(' ave daily price($) of USD',fontsize=15,color='r')
ax[1].set_title(' ave daily price($) of luna',fontsize=15,color='r')
st.pyplot(fig)

#3：不同币的价格对比（在第三步里）


st.subheader('Please click the left buttons for interaction')
level = st.sidebar.radio(
    "Select the type of currency",
    ('ETH', 'BTC'))


fig,ax = plt.subplots(figsize=[15,10])
labels = ['05-06','05-07','05-08']
x = np.arange(len(labels)) 
BTC = [df4.price[1],df4.price[60],df4.price[160]]
ETH = [df5.price[1],df5.price[60],df5.price[160]]
luna =[df3.price[1],df3.price[60],df3.price[160]]

if level == 'BTC':  
   
   width = 0.08 # 柱子的宽度
   ax.bar(x - width,luna, width, label='luna')
   ax.bar(x , ETH, width, label='ETH')
   ax.bar(x + width, BTC, width, label='BTC')

   ax.set_ylabel('price($)')
   ax.set_title('luna & BTC')
   plt.xticks(x, labels=labels)
   ax.legend()
   st.pyplot(fig)
  
else:
   width = 0.08

   ax.bar(x - width/2, luna, width, label='luna')
   ax.bar(x + width/2, ETH, width, label='ETH')
   ax.set_ylabel('price($)')
   ax.set_title('luna & BTC')
   plt.xticks(x, labels=labels)
   ax.legend()
   st.pyplot(fig)





