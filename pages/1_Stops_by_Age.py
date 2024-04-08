import streamlit as st 
import pandas as pd 
import altair as alt
import seaborn as sns
import matplotlib.pyplot as plt 

st.header("CMPD Traffic Stops")
@st.cache_data
def load_data(csv): 
    df = pd.read_csv(csv)
    return df

stops = load_data("data/Officer_Traffic_Stops.csv")

age_bar = alt.Chart(stops).mark_bar().encode(
    alt.X("Driver_Age", bin=alt.Bin(maxbins=50)),
    y="count()", 
    tooltip = alt.Tooltip(["Driver_Age", "count()"])
)
st.altair_chart(age_bar)

fig = plt.figure(figsize=(10, 4))
sns.histplot(x = "Driver_Age", data = stops, bins=100)
st.pyplot(fig)


