import pandas as pd
import streamlit as st
from database import view_all_data, view_only_DNA, get_DNA, edit_DNA
def update():
    result = view_all_data()
    df = pd.DataFrame(result, columns=['hair_colour', 'complexion', 'blood_group', 'eye_colour', 'DNA'])
    with st.expander("Current Values"):
        st.dataframe(df)
    list_of_DNA = [i[0] for i in view_only_DNA()]
    selected_DNA = st.selectbox("DNA", list_of_DNA)
    selected_result = get_DNA(selected_DNA)
    if selected_result:
        hair_colour = selected_result[0][0]
        complexion = selected_result[0][1]
        blood_group = selected_result[0][2]
        eye_colour = selected_result[0][3]
        DNA = selected_result[0][4]
        col1, col2 = st.columns(2)
        with col1:
            new_hair_colour = st.text_input("Hair Colour", hair_colour)
            new_complexion = st.text_input("Complexion", complexion)
            
        with col2:
            new_blood_group = st.text_input("Blood group",blood_group)
            new_eye_colour = st.text_input("Eye Colour", eye_colour)
            new_DNA = st.text_input("DNA", DNA)

        if st.button("Update"):
            edit_DNA(new_hair_colour, new_complexion, new_blood_group, new_eye_colour, new_DNA, hair_colour, complexion, blood_group, eye_colour, DNA)
            st.success("Successfully updated:: {} to ::{}".format(DNA, new_DNA))
        result2 = view_all_data()
    df2 = pd.DataFrame(result2, columns=['new_hair_colour', 'new_complexion', 'new_blood_group', 'new_eye_colour', 'DNA'])
    with st.expander("Updated data"):
        st.dataframe(df2)
