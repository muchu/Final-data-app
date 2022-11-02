import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(
    page_title="Luna & UST Page",
    page_icon="🪙",
)


df1 = pd.read_csv(open('./archive/Terra.csv'))
df2 = pd.read_csv(open('./archive/terrausd.csv'))
df3 = pd.read_csv(open('./archive/terra-luna.csv'))
df4 = pd.read_csv(open('./archive/bitcoin.csv'))
df5 = pd.read_csv(open('./archive/ethereum.csv'))


plt.style.use('seaborn')

# 1:全部的luna币价格波动


st.header(
    '🪙 The daily closing price of a luna coin from the date of issue to the crash')
fig, ax = plt.subplots()
df1.Close.plot(label='close price', linestyle='solid', color='blue')
ax.set_ylabel('Daily closing price($)')
ax.legend()
ax.set_title('Daily closing price($) of crypto luna',
             fontsize=15, color='#595959')
ax.set_xlabel('Cumulative days of issue')
st.pyplot(fig)


# 2：5月份两张图
st.header('The daily price of luna and UST during the crash')

fig, ax = plt.subplots(2, 1, figsize=[10, 15])
price_2 = df2.iloc[2:len(df3):10, 2:]
price_3 = df3.iloc[2:len(df3):10, 2:]

price_2.plot(ax=ax[0], label='ust', linestyle='dashed',  color='blue')

price_3.plot(ax=ax[1], label='luna', linestyle='dashed',  color='blue')

ax[0].set_ylabel('Daily price($)')
ax[1].set_ylabel('Daily price($)')


ax[0].legend()
ax[1].legend()

ax[0].set_title(' Ave daily price($) of UST', fontsize=15, color='#595959')
ax[1].set_title(' Ave daily price($) of luna', fontsize=15, color='#595959')
st.pyplot(fig)

# 3：不同币的价格对比（在第三步里）


st.subheader('Please click the left buttons for interaction')
level = st.sidebar.radio(
    "Select the type of currency",
    ('ETH', 'BTC'))


fig, ax = plt.subplots(figsize=[15, 10])
labels = ['05-06', '05-07', '05-08']
x = np.arange(len(labels))
BTC = [df4.price[1], df4.price[60], df4.price[160]]
ETH = [df5.price[1], df5.price[60], df5.price[160]]
luna = [df3.price[1], df3.price[60], df3.price[160]]

if level == 'BTC':

    width = 0.08  # 柱子的宽度
    ax.bar(x - width, luna, width, label='luna', color="#ab594b")
    ax.bar(x, ETH, width, label='ETH', color="#86a9c1")
    ax.bar(x + width, BTC, width, label='BTC', color="#cfb37e")

    ax.set_ylabel('price($)')
    ax.set_title('luna & BTC')
    plt.xticks(x, labels=labels)
    ax.legend()
    st.pyplot(fig)

else:
    width = 0.08

    ax.bar(x - width/2, luna, width, label='luna', color="#2a5e82")
    ax.bar(x + width/2, ETH, width, label='ETH', color="#86a9c1")
    ax.set_ylabel('price($)')
    ax.set_title('luna & BTC')
    plt.xticks(x, labels=labels)
    ax.legend()
    st.pyplot(fig)
