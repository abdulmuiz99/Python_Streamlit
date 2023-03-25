import streamlit as st
import time
import pandas as pd
import numpy as np

st.subheader("DataFrames")
st.caption("We are going to display the data elements")

df = pd.read_csv("tips.csv")
st.dataframe(data=df, width=1000, height=500)

st.markdown("---")
st.subheader("Tables")
st.caption("We are going to display the Tables list")

st.table(data=df.head(5))

st.markdown("---")
st.subheader("Json")
st.caption("We are going to display the object or string JSON string")

json_values = df.head(3).to_dict()
st.json(json_values)

st.markdown("---")
st.subheader("Progress Bar")
st.caption("Here we are going to display the progress bar")

def progress_bar():
    for pct_complete in range(1,121,20):
        time.sleep(0.5)
        pct_complete = min(pct_complete, 100)
        my_bar.progress(pct_complete)

with st.spinner("Something is processsing ..."):
    my_bar = st.progress(0)
    progress_bar()

st.markdown("---")
st.subheader("info")
st.info("This is Information Message")

st.subheader("Success")
st.success("This is Success Message")

st.subheader("Warning")
st.warning("This is Warning Message")

st.subheader("Error")
st.error("This is an Error")

time.sleep(2)
st.balloons()