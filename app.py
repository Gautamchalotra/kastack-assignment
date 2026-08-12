import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="KaStack AI/ML Assignment",
    layout="wide"
)

st.title("AI/ML Message Processing System")

# Load outputs
classification_df = pd.read_csv(
    "outputs/classification_results.csv"
)

tasks_df = pd.read_csv(
    "outputs/tasks_events.csv"
)

sensitive_df = pd.read_csv(
    "outputs/sensitive_results.csv"
)

# Metrics
st.header("Summary")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Messages",
    len(classification_df)
)

col2.metric(
    "Tasks/Events",
    len(tasks_df)
)

col3.metric(
    "Sensitive Findings",
    len(sensitive_df)
)

# Classification
st.header("Message Classification")

st.dataframe(
    classification_df,
    use_container_width=True
)

# Tasks
st.header("Task & Event Extraction")

st.dataframe(
    tasks_df,
    use_container_width=True
)

# Sensitive
st.header("Sensitive Information Detection")

st.dataframe(
    sensitive_df,
    use_container_width=True
)
