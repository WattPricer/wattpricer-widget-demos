## import Streamlit Library
import streamlit as st
import altair as alt

st.set_option('deprecation.showPyplotGlobalUse', False)


## Title
st.title('WattPricer Demo Widget #1')


## Header
st.header('ERCOT Over Time')

## Subheader
st.subheader('What is this?')

## Text
st.text("The following graph shows the results of ERCOT's Real-time Energy Prices over time.")
st.text("This is a period that includes ERCOT's response to the blizzards of early 2021.")

## Subheader
st.subheader('What does the data look like?')

## Text
st.text("The following is a plot generated from the ERCOT data.")

#February 13–17, 2021 North American winter storm
#https://en.wikipedia.org/wiki/February_13%E2%80%9317,_2021_North_American_winter_storm

## Load data
import pandas as pd

st.subheader("Real-time Prices Plot")

df_rt = pd.read_csv('files/ERCOT-HourlyRealTime-20210207000000-20210222230000.csv')

c = alt.Chart(df_rt).mark_line().encode(
    x='Date and Time:T',
    y='Real-Time Pricee in US Dollars:Q',
    color='Geo',
    tooltip=['Date and Time', 'Real-Time Pricee in US Dollars', 'Geo']
    )

st.altair_chart(c, use_container_width=True)

st.subheader("Day-ahead Prices Plot")

df_da = pd.read_csv('files/ERCOT-HourlyDayAhead-20210207000000-20210222230000.csv')

c = alt.Chart(df_da).mark_line().encode(
    x='Date and Time:T',
    y='Day-Ahead Price in US Dollars:Q',
    color='Geo',
    tooltip=['Date and Time', 'Day-Ahead Price in US Dollars', 'Geo']
    )

st.altair_chart(c, use_container_width=True)
