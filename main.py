#Import Packages
import streamlit as st 
import pandas as pd 

st.write('Jackson Stevens was here!')

st.header("CMPD Traffic Stops")

stops = pd.read_csv("data/Officer_Traffic_Stops.csv")

st.dataframe(stops)