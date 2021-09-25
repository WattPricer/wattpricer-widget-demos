## import Streamlit Library
import altair as alt
import numpy as np
import pandas as pd
import pydeck as pdk
import streamlit as st


st.set_option("deprecation.showPyplotGlobalUse", False)


## Title
st.title("WattPricer Demo Widget #1")


## Header
st.header("ERCOT Over Time")

## Subheader
st.subheader("What is this?")

## Text
st.text(
    "The following graph shows the results of ERCOT's Real-time Energy Prices over time."
)
st.text(
    "This is a period that includes ERCOT's response to the blizzards of early 2021."
)

## Subheader
st.subheader("What does the data look like?")

## Text
st.text("The following is a plot generated from the ERCOT data.")

st.markdown('[February 13–17, 2021 North American winter storm - Wikipedia](https://en.wikipedia.org/wiki/February_13%E2%80%9317,_2021_North_American_winter_storm)')


st.subheader("Real-time Prices Plot")

## Load data
df_rt = pd.read_csv(
    "files/ERCOT-HourlyRealTime-20210207000000-20210222230000.csv"
)

c = (
    alt.Chart(df_rt)
    .mark_line()
    .encode(
        x="Date and Time:T",
        y="Real-Time Pricee in US Dollars:Q",
        color="Geo",
        tooltip=["Date and Time", "Real-Time Pricee in US Dollars", "Geo"],
    )
)

st.altair_chart(c, use_container_width=True)

st.subheader("Day-ahead Prices Plot")

df_dt = pd.read_csv(
    "files/ERCOT-HourlyDayAhead-20210207000000-20210222230000.csv"
)

c = (
    alt.Chart(df_dt)
    .mark_line()
    .encode(
        x="Date and Time:T",
        y="Day-Ahead Price in US Dollars:Q",
        color="Geo",
        tooltip=["Date and Time", "Day-Ahead Price in US Dollars", "Geo"],
    )
)

st.altair_chart(c, use_container_width=True)

st.text('This visualization was created with data obtained from the following API call:')

st.image('files/ERCOT Demo Script.png')

st.set_option("deprecation.showPyplotGlobalUse", False)

## Title
st.title("WattPricer Demo Widget #2")


## Header
st.header("CAISO Nodes across California")

## Subheader
st.subheader("What is this?")

## Text
st.text(
    "The following heatmap shows variation in real-time energy prices acros all of CAISO over the course of a week."
)
st.text(
    "This is the kind of data that can be collected with WattPricer's real-time endpoint."
)

## Subheader
st.subheader("What does the data look like?")

## Text
st.text(
    "The following is a plot generated from the CAISO data (rendered using matplotlib and geopandas)."
)

## Load data
df_rt = pd.read_csv("files/CAISO-HourlyDayAhead-20210922230000.csv")

st.subheader("Real-time LMP data (09/22/2021 23:00:00)")

## Plotting
st.pydeck_chart(
    pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v9",
        initial_view_state=pdk.ViewState(
            latitude=36.76,
            longitude=-120.4,
            zoom=5,
            pitch=0,
        ),
        layers=[
            pdk.Layer(
                "ScatterplotLayer",
                data=df_rt,
                pickable=True,
                get_position="[longitude, latitude]",
                get_color="[colormap_r, colormap_g, colormap_b, colormap_a]",
                get_radius=5000,
            ),
        ],
        tooltip={"text": "Name: {name}\nType: {type}\nUSD/kWh:{realtime}"},
    )
)

st.text('This visualization was created with data obtained from the following API call:')

st.image('files/CAISO_Demo_Script.png')


## Title
st.title("WattPricer Demo Widget #3")


## Header
st.header("ISONE rates, compared to your latest monthly energy rate")

## Subheader
st.subheader("What is this?")

## Text
st.text(
    "The following graph shows the results of ISONE's Real-time Energy Prices one month."
)
st.text(
    "This also features the option of comparing your latest electricity rate to these real-time prices."
)
st.text(
    "See whether you're overpaying compared the rest of New England, or how much your current rate is shielding you from price volatility."
)

## Subheader
st.subheader("What does the data look like?")

## Text
st.text("The following is a plot generated from the ERCOT data.")


st.subheader("Real-time Prices Plot (Interactive)")

## Load data
df_rt = pd.read_csv(
    "files/ISONE-HourlyRealTime-20210822000000-20210922230000.csv"
)

# YOUR_DATA_RATE = 34.56

YOUR_DATA_RATE = st.slider(
    "What is your average monthly energy rate?", 1.00, 130.00, 0.50
)

new_df = df_rt.copy()

new_df["Real-Time Price in US Dollars"] = np.array(
    [YOUR_DATA_RATE] * len(new_df)
)
new_df["Geo"] = np.array(["YOUR_DATA_RATE"] * len(new_df))
new_df = new_df.drop_duplicates()
df_rt = pd.concat([df_rt, new_df])

c = (
    alt.Chart(df_rt)
    .mark_line()
    .encode(
        x="Date and Time:T",
        y="Real-Time Price in US Dollars:Q",
        color="Geo",
        tooltip=["Date and Time", "Real-Time Price in US Dollars", "Geo"],
    )
)

st.altair_chart(c, use_container_width=True)

st.text('This visualization was created with data obtained from the following API call:')

st.image('files/ISONE Demo Script.png')
