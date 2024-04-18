import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title("stroke prediction dashboard")
st.markdown("the dashboard will help a reseacher to get to know\ more anout the given datasets and it's output")

st.sidebar.title("select visual charts")
st.sidebar.markdown("select the charts/plots accordingly")

data=pd.read_csv("demo_data_set.csv")

chart_visual = st.sidebar.selectbox('select charts/plot type',('Livechart','Barchart','Bubblechart'))

st.sidebar.checkbox("show analysis by smoking status",True , key=1)
selected_status = st.sidebar.selection('select smoking status',options=('Formly_Smoked','Smoked','Never_Smoked','unkknown'))


fig = go.figure()
if chart_visual == 'Livechart':
    if selected_status == 'Formly_Smoked':
        fig.add_trace(go.Scatter(x=data.Country, y=data.formerly_smoked,
                                 mode='lines',
                                 name = 'Formly_Smoked'))
    elif selected_status == 'Smoked':
        fig.add_trace(go.Scatter(x=data.Country, y=data.Smokes,
                                 mode='lines',
                                 name = 'Smoked'))
    elif selected_status == 'Never_Smoked':
        fig.add_trace(go.Scatter(x=data.Country, y=data.Never_Smoked,
                                 mode='lines',
                                 name = 'Never_Smoked'))
    elif selected_status == 'Unknown':
        fig.add_trace(go.Scatter(x=data.Country, y=data.Unknown,
                                 mode='lines',
                                 name = 'Unknown'))
elif chart_visual == 'Barchart':
    if selected_status == 'Formly_Smoked':
        fig.add_trace(go.Bar(x=data.Country, y=data.formerly_smoked,
                                 name = 'Formly_Smoked'))
    if selected_status == 'Smoked':
        fig.add_trace(go.Bar(x=data.Country, y=data.Smokes,
                                 name = 'Smoked'))
    if selected_status == 'Never_Smoked':
        fig.add_trace(go.Bar(x=data.Country, y=data.Never_Smoked,
                                 name = 'Never_Smoked'))
    if selected_status == 'Unknown':
        fig.add_trace(go.Bar(x=data.Country, y=data.Unknown,
                                 name='Unknown'))
elif chart_visual == 'Bubblechart':
    if selected_status == 'Formly_Smoked':
        fig.add_trace(go.Scatter(x=data.Country, y=data.formerly_smoked,
                                 mode='markers',
                                 marker_size=[10,60,100],
                                 name = 'Formly_Smoked'))
    if selected_status == 'Smoked':
        fig.add_trace(go.Scatter(x=data.Country, y=data.Smokes,
                                 mode='markers',
                                 marker_size=[10,60,100],
                                 name = 'Smoked'))
    if selected_status == 'Never_Smoked':
        fig.add_trace(go.Scatter(x=data.Country, y=data.Never_Smoked,
                                 mode='markers',
                                 marker_size=[10, 60, 100],
                                 name = 'Never_Smoked'))
    if selected_status == 'Unknown':
        fig.add_trace(go.Scatter(x=data.Country, y=data.Unknown,
                                 mode='markers',
                                 marker_size=[10,60,100],
                                 name='Unknown'))
st.plotly_chart(fig,use_container_width=True)