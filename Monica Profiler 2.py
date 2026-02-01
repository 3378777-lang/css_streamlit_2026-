# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 01:19:57 2026

@author: moghenekome
"""
import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title("Researcher Profile Page with STEM Data")

# Collect basic information
name = "Dr. Monica Oghenekome"
field = "Geology / Sedimentology"
institution = "University of the Western Cape"

# Display basic profile information
st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")

st.image(
    "https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg",
    caption="Nature (Pixabay)"
)

# -------------------------------
# Publications Section (Embedded)
# -------------------------------
st.header("Publications")

publications = pd.DataFrame([
    {
        "Title": "Impacts of diagenetic alterations on siliciclastic sediments of the Pletmos Basin: Implications for reservoir",
        "Journal": "Journal of Petroleum Exploration and Production Technology",
        "Year": 2025,
        "Volume": "",
        "Pages": "",
        "DOI_or_URL": ""
    },
    {
        "Title": "Petrographic Evaluation from the Southern Pletmos Basin: Insight into its Reservoir quality, provenance, weather condition and tectonic setting",
        "Journal": "Journal of African Earth Sciences",
        "Year": 2025,
        "Volume": "",
        "Pages": "",
        "DOI_or_URL": ""
    },
    {
        "Title": "Petrographic Evaluation from the Southern Pletmos Basin: Insight into its Reservoir quality, provenance, weather condition and tectonic setting",
        "Journal": "Sedimentary Geology",
        "Year": 2025,
        "Volume": "",
        "Pages": "",
        "DOI_or_URL": ""
    },
    {
        "Title": "Geochemistry and Weathering History of the Balfour Sandstone Formation, Karoo Basin, South Africa: Insight to Provenance and Tectonic Setting",
        "Journal": "Journal of African Earth Sciences",
        "Year": 2018,
        "Volume": "147",
        "Pages": "623–632",
        "DOI_or_URL": "http://dx.doi.org/10.1016/j.jafrearsci.2018.07.014"
    },
    {
        "Title": "Provenance study from petrography of the Late Permian–Early Triassic sandstones of the Balfour Formation, Karoo Supergroup, South Africa",
        "Journal": "Journal of African Earth Sciences",
        "Year": 2016,
        "Volume": "114",
        "Pages": "1–8",
        "DOI_or_URL": "http://dx.doi.org/10.1016/j.jafrearsci.2015.11.002"
    }
])

st.dataframe(publications)

# Keyword filter
keyword = st.text_input("Filter publications by keyword", "")
if keyword:
    filtered_pubs = publications[
        publications.apply(
            lambda row: keyword.lower() in row.astype(str).str.lower().values,
            axis=1
        )
    ]
    st.write(f"Filtered Results for '{keyword}':")
    st.dataframe(filtered_pubs)

# Publication trend visualization
st.subheader("Publication Trends")
year_counts = publications["Year"].value_counts().sort_index()
st.bar_chart(year_counts)

# -------------------------------
# STEM Data Section
# -------------------------------
st.header("Explore STEM Data")

physics_data = pd.DataFrame({
    "Experiment": ["Alpha Decay", "Beta Decay", "Gamma Ray Analysis", "Quark Study", "Higgs Boson"],
    "Energy (MeV)": [4.2, 1.5, 2.9, 3.4, 7.1],
    "Date": pd.date_range(start="2024-01-01", periods=5),
})

astronomy_data = pd.DataFrame({
    "Celestial Object": ["Mars", "Venus", "Jupiter", "Saturn", "Moon"],
    "Brightness (Magnitude)": [-2.0, -4.6, -1.8, 0.2, -12.7],
    "Observation Date": pd.date_range(start="2024-01-01", periods=5),
})

weather_data = pd.DataFrame({
    "City": ["Cape Town", "London", "New York", "Tokyo", "Sydney"],
    "Temperature (°C)": [25, 10, -3, 15, 30],
    "Humidity (%)": [65, 70, 55, 80, 50],
    "Recorded Date": pd.date_range(start="2024-01-01", periods=5),
})

st.subheader("STEM Data Viewer")
data_option = st.selectbox(
    "Choose a dataset to explore",
    ["Physics Experiments", "Astronomy Observations", "Weather Data"]
)

if data_option == "Physics Experiments":
    st.dataframe(physics_data)
    energy_filter = st.slider("Filter by Energy (MeV)", 0.0, 10.0, (0.0, 10.0))
    st.dataframe(
        physics_data[physics_data["Energy (MeV)"].between(*energy_filter)]
    )

elif data_option == "Astronomy Observations":
    st.dataframe(astronomy_data)
    brightness_filter = st.slider("Filter by Brightness (Magnitude)", -15.0, 5.0, (-15.0, 5.0))
    st.dataframe(
        astronomy_data[astronomy_data["Brightness (Magnitude)"].between(*brightness_filter)]
    )

elif data_option == "Weather Data":
    st.dataframe(weather_data)
    temp_filter = st.slider("Filter by Temperature (°C)", -10.0, 40.0, (-10.0, 40.0))
    humidity_filter = st.slider("Filter by Humidity (%)", 0, 100, (0, 100))
    st.dataframe(
        weather_data[
            weather_data["Temperature (°C)"].between(*temp_filter) &
            weather_data["Humidity (%)"].between(*humidity_filter)
        ]
    )

# Contact section
st.header("Contact Information")
email = "monica.oghenekome@uwc.ac.za"
