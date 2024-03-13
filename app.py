import streamlit as st
from dbhelper import DB
import plotly.graph_objects as go
import plotly.express as px

db = DB()

st.sidebar.title('Select Analytics Option')

user_option = st.sidebar.selectbox('Menu',['Select One','Analytics'])


if user_option == 'Analytics':
    airline, frequency = db.fetch_airline_frequency()
    fig = go.Figure(
        go.Pie(
            labels=airline,
            values=frequency,
            hoverinfo="label+percent",
            textinfo="value"
        ))

    st.header("No. of flights Per Airline")
    st.plotly_chart(fig)

    city, frequency1 = db.busy_airport()
    fig = px.bar(
        x=city,
        y=frequency1,
        labels=dict(x="City", y="Total No of Flights"))

    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

    date, frequency2 = db.daily_frequency()

    print(len(date))
    print(len(frequency2))
    fig = px.line(
        x=date,
        y=frequency2,
        labels=dict(x="Date", y="Frequency of Flights")
    )

    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

else:
    st.title('To Get Flights Analytics Information Select Left Panel')