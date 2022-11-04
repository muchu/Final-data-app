from xml.dom import minidom
import pandas as pd
import json
import plotly.graph_objects as go
import streamlit as st
import datetime

st.set_page_config(
    page_title="Anchor Page",
    page_icon="🏦",
)

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

st.header("🏦 Deposit and Borrow of Anchor Protocol")
option_ratio = st.sidebar.radio('what you want: ', ('Max', 'Min'))

date_input = st.date_input(
    "Show data before: ",
    datetime.date(2022, 7, 15))
input_stampe = pd.to_datetime(date_input)

# filter
depo = depo[depo['timestamp'] <= input_stampe.timestamp()]
borw = borw[borw['timestamp'] <= input_stampe.timestamp()]

print(len(depo))
# plot
fig = go.Figure()
fig.add_trace(go.Line(x=depo['time'], y=depo['deposit'], name='Deposit',marker=dict(color = "#466b82")))
fig.add_trace(go.Line(x=borw['time'], y=borw['total_borrowed'], name='Borrow',marker=dict(color = "#ecc043")))
fig.update_layout(
    autosize=False,
    width=800,
    height=600,
    paper_bgcolor="#f4f3f4",
    plot_bgcolor="#efedee"
)
st.plotly_chart(fig)

st.write('The main way banks get their benefits is through interest on loans and reinvested of stored funds,and the same is trus for Anchor Protocol')
st.write('But as seen from the deposit-to-loan ratio,deposits are much larger than loans,which makes it difficult to afford the high interest rates of  Anchor Protocol (20%,much more higher than other banks).')
st.write('Eventually, on May 9 of this year, a run on the "bank" led by the capital giants took place.A large number of deposits were withdrawn, causing deposits to fall off a cliff.')


diff = depo['deposit']-borw['total_borrowed']

max_diff = diff.idxmax()
min_diff = diff.idxmin()

option_dict = {'Max': max_diff, "Min": min_diff}
labels = ['Deposit', 'Borrow']
values = [depo.iloc[option_dict[option_ratio]]['deposit'],
          borw.iloc[option_dict[option_ratio]]['total_borrowed']]
fig_pie = go.Figure(data=[go.Pie(labels=labels, values=values,marker=dict(colors=["#466b82","#ecc043"], line=dict(color='#000000', width=2)))])

print(values)
st.plotly_chart(fig_pie)

st.write('This pie chart shows the maximum and minimum proportions of borrowings and deposits over different time periods.')
st.write('Please use the left interactive button and the top date interactive button to operate.')