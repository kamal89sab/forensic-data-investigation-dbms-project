import streamlit as st
from database import add_data
def create_1():
    col1, col2 = st.columns(2)
    with col1:
        hair_colour = st.text_input("hair_colour")
        complexion = st.text_input("complexion")
        blood_group=st.text_input("blood_group")
    with col2:
        eye_colour = st.text_input("eye_colour")
        DNA = st.text_input("DNA")
    if st.button("Add Details"):
        add_data(hair_colour, complexion, blood_group, eye_colour, DNA)
        st.success("Successfully added :")