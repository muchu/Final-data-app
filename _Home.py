import json
import pandas as pd
import matplotlib
import streamlit as st


st.set_page_config(
    page_title="Hello Page",
    page_icon="👋",
)

str_description1 = '''
##### 1 Data from https://www.kaggle.com/datasets/avanawallet/crypto-price-data-during-terra-luna-crash provide by AvanaWallet
>The collapse of Terra Luna and Terra USD (UST) shocked the broader cryptocurrency and financial markets. The aggregate market capitalization of large-cap cryptocurrencies dropped several hundreds of billions dollars in a matter of a week. Avana Wallet has aggregated 15-minute interval price data for stablecoins (US dollar pegs) and large-cap cryptocurrencies for you to analyze. The data span between 5/6/2022 and 5/17/2022, which captures the entire episode.
>
>Several pricing discrepancies occurred during the volatility. You can analyze the data to find the discrepancies that occurred when the market panicked.
>
>**Data associated with Terra**:  
>Anchor Protocol ANC (anchor-protocol.csv)
>Terra Luna LUNA (terra-luna.csv)
>Terra USD UST (terrausd.csv)
>
>**Large-cap cryptocurrencies**:
>Avalanche AVAX (avalanche.csv)
>Bitcoin BTC (bitcoin.csv)
>Binance BNB (bnb.csv)
>Cardano ADA (cardano.csv)
>Dogecoin DOGE (dogecoin.csv)
>Ethereum ETH (ethereum.csv)
>Polygon MATIC (polygon.csv)
>Solana SOL (solana.csv)
>XRP (xrp.csv)
>
>**Stablecoins**:
>Binance USD BUSD (binance-usd.csv)
>DAI (dai.csv)
>Tether USDT (tether.csv)
>USD Coin UDSC (usd-coin.csv)'''
str_description2 = '##### 2 The data crawled from here https://app.anchorprotocol.com/'
str_description3 = '''
##### 1 Data from https://www.kaggle.com/datasets/programmerrdai/terra-came-back-to-the-ground provide by hrterhrter
>I have used alot of Kaggle Datasets and I want to help the community also. So I hope this helps at least one person.  
>:)  
>This is data from the oldest terra price. :)  
>The data has been taken from https://finance.yahoo.com/  
>I will update as frequently as possible.  '''
   
df3 = pd.read_csv(open("../Final-data-app/archive/terra-luna.csv"))
df5 = pd.read_csv(open("../Final-data-app/archive/ethereum.csv"))
data_depo = json.load(open("../Final-data-app/archive/deposit.json"))


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


