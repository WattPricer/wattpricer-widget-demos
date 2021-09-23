import numpy as np
import streamlit as st
import altair as alt

st.set_option('deprecation.showPyplotGlobalUse', False)


## Title
st.title('WattPricer Demo Widget #3')


## Header
st.header('ISONE rates, compared to your latest monthly energy rate')

## Subheader
st.subheader('What is this?')

## Text
st.text("The following graph shows the results of ISONE's Real-time Energy Prices one month.")
st.text("This also features the option of comparing your latest electricity rate to these real-time prices.")
st.text("See whether you're overpaying compared the rest of New England, or how much your current rate is shielding you from price volatility.")

## Subheader
st.subheader('What does the data look like?')

## Text
st.text("The following is a plot generated from the ERCOT data.")

## Load data
import pandas as pd

st.subheader("Real-time Prices Plot (Interactive)")

df_rt = pd.read_csv('files/ISONE-HourlyRealTime-20210822000000-20210922230000.csv')
#df_rt.to_csv('files/ISONE-HourlyRealTime-20210822000000-20210922230000.csv', index=False)

#YOUR_DATA_RATE = 34.56

YOUR_DATA_RATE = st.slider('What is your average monthly energy rate?', 1.00, 130.00, 0.50)

new_df = df_rt.copy()

new_df['Real-Time Price in US Dollars'] = np.array([YOUR_DATA_RATE] * len(new_df))
new_df['Geo'] = np.array(['YOUR_DATA_RATE'] * len(new_df))
new_df = new_df.drop_duplicates()
df_rt = pd.concat([df_rt, new_df])

c = alt.Chart(df_rt).mark_line().encode(
    x='Date and Time:T',
    y='Real-Time Price in US Dollars:Q',
    color='Geo',
    tooltip=['Date and Time', 'Real-Time Price in US Dollars', 'Geo']
    )

st.altair_chart(c, use_container_width=True)