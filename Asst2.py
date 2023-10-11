# Import necessary libraries
import pandas as pd
import numpy as np
import plotly
import plotly.express as px
import streamlit as st
import plotly.graph_objects as go

# Fetch and load the dataset from the provided URL
url = "https://raw.githubusercontent.com/HusseinDakroub/Asst2_MSBA325/main/global_pop.csv"
df= pd.read_csv(url)

# Set the Streamlit title
st.title("Global Population")

st.markdown("### Dataset Overview")
st.write("Below, you can check the columns (or factors) of the dataset and also view the raw data:")

# Allow users to check the factors/columns of the dataset
if( st.checkbox("Show Columns of the Dataset")):
    st.subheader("Columns: ")
    st.write(df.columns)

# Allow users to view the raw dataset
if( st.checkbox("Show Raw Data")):
    st.subheader("Raw data")
    st.write(df)

df1 = df.query("Year == 2021")

st.markdown("### Urban vs. Rural Population")
st.write("This scatter plot visualizes the urban and rural populations of different countries, animated over the years. The X-axis represents the life expectancy, and the Y-axis shows the population numbers.")
fig0 = px.scatter(df, x = "Life Expectancy", y = "Urban Population", color = "Country", animation_frame = "Year", animation_group = "Country")
fig0.add_trace(go.Scatter(x=df1["Life Expectancy"], y=df1["Rural Population"], mode="markers", name="Rural Population", marker=dict(color="red")))
fig0.update_layout(
    yaxis2=dict(
        title="Rural Population",
        overlaying="y",
        side="right",
        showgrid=False,
    )
)
st.plotly_chart(fig0)

st.write("There's a noticeable concentration of data points (countries) with life expectancies ranging from 60 to 80 years and with urban populations below 5 million. Only a few data points have urban populations that surpass the 10 million mark. This could represent highly urbanized countries or countries with vast metropolitan areas.")

st.markdown("### Global Death Rate Visualization")
st.write("The map below showcases the death rate of various countries, color-coded and animated over the years.")
fig = px.choropleth(df, locations = "Country", locationmode="country names", color = "Death Rate", hover_name = "Country", animation_frame = "Year", color_continuous_scale = px.colors.sequential.Plasma, projection = "natural earth")
st.plotly_chart(fig)

st.markdown("### Birth Rate Over Years")
st.write("This horizontal box plot displays the distribution of birth rates over various years.")
fig2 = px.box(df, x = "Birth Rate", y = "Year", orientation = "h")
st.plotly_chart(fig2)

st.markdown("### Comparing Birth and Death Rates")
st.write("The interactive bar chart below allows you to compare birth and death rates for both urban and rural populations. Use the slider to switch between urban and rural data.")
factor = st.slider("Select 0 for Urban and 1 for Rural:", min_value=0, max_value=1, step=1)
fig3 = go.Figure()
if factor == 0:
    fig3.add_trace(go.Bar(x=df["Year"], y=df["Birth Rate"], name="Urban Birth Rate"))
    fig3.add_trace(go.Bar(x=df["Year"], y=df["Death Rate"], name="Urban Death Rate"))
    fig3.update_layout(title="Birth Rate and Death Rate for Urban Population Over the Years")
else:
    fig3.add_trace(go.Bar(x=df["Year"], y=df["Birth Rate"], name="Rural Birth Rate"))
    fig3.add_trace(go.Bar(x=df["Year"], y=df["Death Rate"], name="Rural Death Rate"))
    fig3.update_layout(title="Birth Rate and Death Rate for Rural Population Over the Years")
fig3.update_layout(barmode='group')
st.plotly_chart(fig3)
st.write("There was a sharp decline in the urban birth rate from 2018 to 2019, bringing it very close to the death rate. 2020 saw a rebound in birth rates, but it again decreased in 2021. The urban death rate generally followed a similar trend as the birth rate, with the exception of 2019, where it increased slightly while the birth rate declined. The reasons for these fluctuations could be multifaceted and would require additional information to decipher accurately. Economic, healthcare, sociopolitical, or even environmental factors could play a role in these shifts. In conclusion, while there are noticeable changes in both the urban birth and death rates across these years, the birth rate has consistently remained higher than the death rate. However, the reasons behind these fluctuations would need more contextual information.")
