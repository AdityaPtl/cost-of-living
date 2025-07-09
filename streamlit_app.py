import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set custom favicon and tab title using HTML
st.set_page_config(
    page_title="Cost of Living Explorer",
    page_icon="🏙️",  # You can use an emoji or a URL to an image
)

# Load data
df = pd.read_csv("data/cost_of_living_template.csv")
df['Monthly Cost (AUD)'] = pd.to_numeric(df['Monthly Cost (AUD)'], errors='coerce')
df.dropna(subset=['Monthly Cost (AUD)'], inplace=True)

st.title("🏙️ Cost of Living Explorer – Australia")
st.markdown("Compare monthly living costs across Melbourne, Sydney, Adelaide, and Hobart.")

cities = df['City'].unique()
selected_city = st.selectbox("Select a city to explore:", ["All"] + list(cities))

if selected_city != "All":
    city_df = df[df["City"] == selected_city]
else:
    city_df = df

# Plot
st.subheader("💸 Monthly Cost Breakdown")
fig, ax = plt.subplots(figsize=(8, 4))
bars = city_df.groupby(["City", "Category"])["Monthly Cost (AUD)"].sum().unstack().plot(kind="bar", ax=ax)
plt.ylabel("Monthly Cost (AUD)")
plt.xticks(rotation=0)
st.pyplot(fig)

# Totals
st.subheader("📊 Total Monthly Cost per City")
total_df = df.groupby("City")["Monthly Cost (AUD)"].sum().sort_values()
st.bar_chart(total_df)
