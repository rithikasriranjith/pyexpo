import streamlit as st
import pandas as pd
st.title("Student Management System")
st.subheader("Add New Student") 
name = st.text_input("Student Name")
age = st.number_input("Age", min_value=1, max_value=100)    
if st.button("Submit"):
    if name and age :
        new_student = {"Name": name, "Age": age}
        if 'students' not in st.session_state:
            st.session_state['students'] = []
        st.session_state['students'].append(new_student)
        st.success(f"Student {name} added successfully!")
    else:
        st.error("Please fill all the fields.") 
st.subheader("Student List")
if 'students' in st.session_state and st.session_state['students']:
    df = pd.DataFrame(st.session_state['students'])
    st.table(df)
st.subheader("Search Student")
search_name = st.text_input("Enter student name to search") 
if st.button("Search"):
    if 'students' in st.session_state:
        results = [s for s in st.session_state['students'] if search_name.lower() in s['Name'].lower()]
        if results:
            df_results = pd.DataFrame(results)
            st.table(df_results)
        else:
            st.warning("No matching students found.")     
st.subheader("Delete Student")
delete_name = st.text_input("Enter student name to delete")
if st.button("Delete"):
    if 'students' in st.session_state:
        original_count = len(st.session_state['students'])
        st.session_state['students'] = [s for s in st.session_state['students'] if delete_name.lower() != s['Name'].lower()]
        if len(st.session_state['students']) < original_count:
            st.success(f"Student {delete_name} deleted successfully!")
        else:
            st.warning("No matching student found to delete.")