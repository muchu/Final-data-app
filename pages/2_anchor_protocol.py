from xml.dom import minidom
import pandas as pd
import json
import plotly.graph_objects as go
import streamlit as st
import datetime
from utils import read_all_data



data_depo, data_borrow = read_all_data.read_data_second()

# handle data type
timestamp_depo = [item['timestamp']/1000 for item in data_depo['total_ust_deposits']]
deposit_depo= [eval(item['deposit'])/100000 for item in data_depo['total_ust_deposits']]

timestamp_borrow = [item['timestamp']/1000 for item in data_borrow]
totoal_borrow= [eval(item['total_borrowed'])/100000 for item in data_borrow]

#read to dataFrame
depo = pd.DataFrame()
borw = pd.DataFrame()

depo['deposit'] = list(reversed(deposit_depo))
depo['time'] = pd.to_datetime(list(reversed(timestamp_depo)),unit='s')
depo['timestamp'] = list(reversed(timestamp_depo))

borw['total_borrowed'] = list(reversed(totoal_borrow))
borw['time'] = pd.to_datetime(list(reversed(timestamp_borrow)),unit='s')
borw['timestamp'] = list(reversed(timestamp_borrow))

st.header("Deposit and Borrow of Anchor Protocol") 
option_ratio = st.sidebar.radio('what you want: ',('Max','Min'))

date_input = st.date_input(
    "Show data before: ",
    datetime.date(2022,7, 15))
input_stampe = pd.to_datetime(date_input)

#filter
depo = depo[depo['timestamp'] <= input_stampe.timestamp()]
borw = borw[borw['timestamp'] <= input_stampe.timestamp()]

print(len(depo))
#plot
fig = go.Figure()
fig.add_trace(go.Line(x = depo['time'], y = depo['deposit'],name='Deposit'))
fig.add_trace(go.Line(x = borw['time'],y = borw['total_borrowed'],name='Borrow'))
fig.update_layout(
    autosize=False,
    width=800,
    height=600,
)

st.plotly_chart(fig)

diff = depo['deposit']-borw['total_borrowed']

max_diff = diff.idxmax()
min_diff = diff.idxmin()

option_dict = {'Max':max_diff,"Min": min_diff}
labels = ['Deposit','Borrow']
values = [depo.iloc[option_dict[option_ratio]]['deposit'], borw.iloc[option_dict[option_ratio]]['total_borrowed']]
fig_pie = go.Figure(data=[go.Pie(labels=labels, values=values)])
print(values)
st.plotly_chart(fig_pie)
