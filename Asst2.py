import pandas as pd
import numpy as np
import plotly
import plotly.express as px
import streamlit as st
import plotly.graph_objects as go


url = "https://raw.githubusercontent.com/HusseinDakroub/Asst2_MSBA325/main/global_pop.csv"
df= pd.read_csv(url)

st.title("Global Population")
st.subheader("Hello")
if( st.checkbox("Checking the factors of our dataset")):
    st.subheader("Factors: ")
    st.write(df.columns)


st.subheader("Click on the checkbox if you want to see the Data")
if( st.checkbox("Show raw Data")):
    st.subheader("Raw data")
    st.write(df)


df1 = df.query("Year == 2021")

#Figure 1
st.subheader("urban population")
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


#Figure 2
st.subheader("Map")
fig = px.choropleth(df, locations = "Country", locationmode="country names", color = "Death Rate", hover_name = "Country", animation_frame = "Year", color_continuous_scale = px.colors.sequential.Plasma, projection = "natural earth")
st.plotly_chart(fig)


#Figure 3
st.subheader("Getting the values of the birth rate over years")
fig2 = px.box(df, x = "Birth Rate", y = "Year", orientation = "h")
st.plotly_chart(fig2)

#Figure 4
fig3 = go.Figure()



st.subheader("Checking the Birth and Death rates in Rural/Urban Population")

# Add a slider to switch between factors
factor = st.slider("Select 0 for Urban and 1 for Rural:", min_value=0, max_value=1, step=1)

# Modify the plot based on the selected factor
if factor == 0:
    # Plot Birth Rate and Death Rate for Urban Population
    fig3.add_trace(go.Bar(x=df["Year"], y=df["Birth Rate"], name="Urban Birth Rate"))
    fig3.add_trace(go.Bar(x=df["Year"], y=df["Death Rate"], name="Urban Death Rate"))
    fig3.update_layout(title="Birth Rate and Death Rate for Urban Population Over the Years")
else:
    # Plot Birth Rate and Death Rate for Rural Population
    fig3.add_trace(go.Bar(x=df["Year"], y=df["Birth Rate"], name="Rural Birth Rate"))
    fig3.add_trace(go.Bar(x=df["Year"], y=df["Death Rate"], name="Rural Death Rate"))
    fig3.update_layout(title="Birth Rate and Death Rate for Rural Population Over the Years")

# Update layout for a grouped bar chart
fig3.update_layout(barmode='group')

# Re-display the modified plot
st.plotly_chart(fig3)
