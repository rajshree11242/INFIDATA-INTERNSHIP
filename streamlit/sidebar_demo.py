import streamlit as st
add_selection=st.sidebar_selection("how would you like to be contacted")
("email","home phone","mobile phone")
with st.sidebar:
    add_radio=st.radio("choice a shipping method",(" standard(5-15days"),("express(2-5 days")))

name=st.text_input("enter customer name")