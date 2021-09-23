## import Streamlit Library
import streamlit as st
import pydeck as pdk

st.set_option('deprecation.showPyplotGlobalUse', False)


## Title
st.title('WattPricer Demo Widget #2')


## Header
st.header('CAISO Nodes across California')

## Subheader
st.subheader('What is this?')

## Text
st.text("The following heatmap shows variation in real-time energy prices acros all of CAISO over the course of a week.")
st.text("This is the kind of data that can be collected with WattPricer's real-time endpoint.")

## Subheader
st.subheader('What does the data look like?')

## Text
st.text("The following is a plot generated from the CAISO data (rendered using matplotlib and geopandas).")

## Load data
import numpy as np
import pandas as pd


## Plotting

df = pd.read_csv('files/CAISO-HourlyDayAhead-20210922230000.csv')

st.subheader("Real-time LMP data (09/22/2021 23:00:00)")

st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/light-v9',
    initial_view_state=pdk.ViewState(
        latitude=36.76,
        longitude=-120.4,
        zoom=5,
        pitch=0,
        ),
        layers=[
            pdk.Layer(
                'ScatterplotLayer',
                data=df,
                pickable=True,
                get_position='[longitude, latitude]',
                get_color='[colormap_r, colormap_g, colormap_b, colormap_a]',
                get_radius=5000,
        ),
        ],
        tooltip={"text": "Name: {name}\nType: {type}\nUSD/kWh:{realtime}"}
        )
    )