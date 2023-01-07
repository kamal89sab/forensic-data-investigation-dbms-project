import streamlit as st 
import pandas as pd
from database import c
from database import delete_DNA
def sql_executor(raw_code):
	print(raw_code)
	c.execute(raw_code)
	data = c.fetchall()
	return data 

emp= ['first_name', 'last_name', 'age', 'sex', 'emp_ID']
proof=['hair_colour', 'complexion', 'blood_group', 'eye_colour', 'DNA']
identify=['victim_ID', 'DNA']
person=['first_name', 'last_name', 'age', 'sex', 'weapon_used', 'victim_ID']
cop=['first_name', 'last_name', 'age', 'sex', 'police_ID', 'address']
relation=['victim_ID', 'suspect_ID']
sus=['first_name', 'last_name', 'age', 'sex', 'victim_ID', 'police_ID', 'suspect_ID']
vic=['first_name', 'last_name', 'age', 'sex', 'detail_of_death', 'date_of_death', 'emp_ID', 'victim_ID']


def execution():
	col1,col2 = st.columns(2)

	with col1:
		with st.form(key='query_form'):
			raw_code = st.text_area("SQL Code Here")
			submit_code = st.form_submit_button("Execute")


		with st.expander("Table Info"):
			table_info = {'employees':emp,'Evidences':proof,'identified_by':identify,'murderer':person,'police':cop, 'related_to':relation, 'suspects':sus,'victims':vic}
			st.json(table_info)

	with col2:
		if submit_code:
			st.info("Query Submitted")
			st.code(raw_code)

			query_results = sql_executor(raw_code)
			with st.expander("Results"):
				st.write(query_results)

			with st.expander("Table View"):
				query_df = pd.DataFrame(query_results)
				st.dataframe(query_df)