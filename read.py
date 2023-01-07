import pandas as pd
import streamlit as st
from database import view_all_data
def read():
    result = view_all_data()
    df = pd.DataFrame(result, columns=['hair_colour', 'complexion', 'blood_group', 'eye_colour', 'DNA']) 
    with st.expander("View All evidences"):
        st.dataframe(df)
 