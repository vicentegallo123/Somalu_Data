import streamlit as st

def draw_metric(
    title,
    value,
    delta=None
):
    st.metric(
        label=title,
        value=value,
        delta=delta
    )