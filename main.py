#Import Packages
import streamlit as st 
import pandas as pd 

st.header("CMPD Traffic Stops")

stops = pd.read_csv("data/Officer_Traffic_Stops.csv")

st.dataframe(stops)