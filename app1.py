# Importing pakages
import streamlit as st
import mysql.connector

import pandas as pd

from create import create_1
from database import create_table
from delete import delete
from read import read
from update1 import update
from query import execution

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
c = mydb.cursor()



def main():
    st.title("Forensic_investigation PES1UG20CS653")
    menu = ["Add", "View", "Edit", "Remove","Custom query"]
    choice = st.sidebar.selectbox("Menu", menu)

    create_table()
    if choice == "Add":
        st.subheader("Enter Evidence Details:")
        create_1()

    elif choice == "View":
        st.subheader("View Evidences")
        read()

    elif choice == "Edit":
        st.subheader("Update Evidences")
        update()

    elif choice == "Remove":
        st.subheader("Delete Evidences")
        delete()

    elif choice=="Custom query":
        st.subheader("Enter query")
        execution()

    else:
        st.subheader("About Evidences")


if __name__ == '__main__':
    main()