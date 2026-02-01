# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 00:54:53 2026

@author: moghenekome
"""
import pandas as pd
import streamlit as st

df = pd.read_csv("publications.csv")
st.dataframe(df)

    Title,Journal,Year,Volume,Pages,DOI_or_URL
    "Impacts of diagenetic alterations on siliciclastic sediments of the Pletmos Basin: Implications for reservoir","Journal of Petroleum Exploration and Production Technology",2025,,,
    "Petrographic Evaluation from the Southern Pletmos Basin: Insight into its Reservoir quality, provenance, weather condition and tectonic setting","Journal of African Earth Sciences",2025,,,
    "Petrographic Evaluation from the Southern Pletmos Basin: Insight into its Reservoir quality, provenance, weather condition and tectonic setting","Sedimentary Geology",2025,,,
    "Geochemistry and Weathering History of the Balfour Sandstone Formation, Karoo Basin, South Africa: Insight to Provenance and Tectonic Setting","Journal of African Earth Sciences",2018,147,"623-632","http://dx.doi.org/10.1016/j.jafrearsci.2018.07.014"
    "Provenance study from petrography of the Late Permian–Early Triassic sandstones of the Balfour Formation, Karoo Supergroup, South Africa","Journal of African Earth Sciences",2016,114,"1-8","http://dx.doi.org/10.1016/j.jafrearsci.2015.11.002"
