import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Solar Data Dashboard", layout="centered")

st.title("🌞 Solar Data Dashboard")
st.write("Compare GHI, DNI, and DHI across Benin, Togo, and Sierra Leone")

# Country selector
country = st.selectbox("Select a country", ["Benin", "Togo", "Sierra Leone"])

# Load corresponding cleaned data
file_map = {
    "Benin": "data/benin-malanville.csv",
    "Togo": "data/sierraleone-bumbuna.csv",
    "Sierra Leone": "data/togo-dapaong_qc.csv"
}

@st.cache_data
def load_data(path):
    return pd.read_csv(path)

df = load_data(file_map[country])

# Metric selector
metric = st.selectbox("Select a metric", ["GHI", "DNI", "DHI"])

# Boxplot
st.subheader(f"{metric} Distribution in {country}")
fig, ax = plt.subplots()
sns.boxplot(y=df[metric], ax=ax)
st.pyplot(fig)

# Summary
st.subheader("Summary Statistics")
st.write(df[[metric]].describe())
