import pandas as pd
import streamlit as st
from database import view_all_data, view_only_DNA, delete_DNA


def delete():
    result = view_all_data()
    df = pd.DataFrame(result, columns=['hair_colour', 'complexion', 'blood_group', 'eye_colour', 'DNA'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_DNA = [i[0] for i in view_only_DNA()]
    selected_DNA = st.selectbox("DNA to Delete", list_of_DNA)
    st.warning("Do you want to delete ::{}".format(selected_DNA))
    if st.button("Delete info"):
        delete_DNA(selected_DNA)
        st.success("DNA has been deleted successfully")
    new_result = view_all_data()
    df2 = pd.DataFrame(new_result, columns=['hair_colour', 'complexion', 'blood_group', 'eye_colour', 'DNA'])
    with st.expander("Updated data"):
        st.dataframe(df2)