import streamlit as st
import pandas as pd
st.title("Student Management System")
st.subheader("Enter Studeent Details")
name=st.text_input("Enter Name:")
age=st.number_input("Enter Age:")
st.button("Submit")
stu_list={"Name":name,"Age",age}
st.dataframe(stu_list)