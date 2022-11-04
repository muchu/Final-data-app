import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json


st.set_page_config(
    page_title="Analyse Page",
    page_icon="📉",
)

df1 = pd.read_csv(open('./archive/Terra.csv'))
df2 = pd.read_csv(open('./archive/terrausd.csv'))
df3 = pd.read_csv(open('./archive/terra-luna.csv'))
df4 = pd.read_csv(open('./archive/bitcoin.csv'))
df5 = pd.read_csv(open('./archive/ethereum.csv'))
data_depo = json.load(open("./archive/deposit.json"))
data_borrow = json.load(open("./archive/borrow.json"))


# handle data type
timestamp_depo = [item['timestamp'] /
                  1000 for item in data_depo['total_ust_deposits']]
deposit_depo = [eval(item['deposit']) /
                100000 for item in data_depo['total_ust_deposits']]

timestamp_borrow = [item['timestamp']/1000 for item in data_borrow]
totoal_borrow = [eval(item['total_borrowed'])/100000 for item in data_borrow]

# read to dataFrame
depo = pd.DataFrame()
borw = pd.DataFrame()

depo['deposit'] = list(reversed(deposit_depo))
depo['time'] = pd.to_datetime(list(reversed(timestamp_depo)), unit='s')
depo['timestamp'] = list(reversed(timestamp_depo))

borw['total_borrowed'] = list(reversed(totoal_borrow))
borw['time'] = pd.to_datetime(list(reversed(timestamp_borrow)), unit='s')
borw['timestamp'] = list(reversed(timestamp_borrow))

tab1, tab2 = st.tabs(['🔍Volume',"🔍Correlation"])
with tab1:
    plt.style.use('seaborn')

    st.header('📉 The volume of luna from the date of issue to the crash')
    fig, ax = plt.subplots()

    df1.Volume.plot(label='Volumn', linestyle='solid', color='blue')
    ax.set_ylabel('Daily volumn')
    ax.legend()
    ax.set_title('Daily volumn of crypto luna', fontsize=15, color='#595959')
    st.pyplot(fig)
    st.write('A large number of depositors took out USTs from the "bank", causing the number of USTs to surge and the price to crash, and they all wanted to exchange their USTs for Luna to hedge their risks. ')
    st.write('Luna went down the same path as USTs, soaring in volume, plummeting in price, and the death spiral began.')
with tab2:
    correlation_price = pd.DataFrame(
    data={
        "borrow":borw["total_borrowed"],
        "deposit":depo["deposit"],
        "BTC":df4["price"],
        "ETH":df5["price"],
        "Terra":df1["Close"],
        "terrausd":df2["price"],
        "terra-luna":df3["price"],
        }
    )
    corr = correlation_price.corr()
    st.header('📉 Correlation overviews')

    st.dataframe(corr)