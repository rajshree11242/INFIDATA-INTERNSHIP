import streamlit as st
if'clicked1' not in st.session_state:
    st.session_state.clicked1= False
if'clicked2' not in st.session_state:
    st.session_state.clicked2= False
def click_button1():
    st.session_state.clicked1= True
    st.write('Add BUtton clicked1!')
def click_button2():
    st.session_state.clicked2= True
    st.write('add button clicked2!')
st.button('ADD',on_click=click_button1)
st.button('sub',on_click=click_button2)

if(st.session_state.clicked1):
    st.title("Addition program")
    n1=st.number_input("enter n1")
    n2 = st.number_input("enter n2")
    sum=n1+n2
    st.info("addition of 2 int number:")
    st.success(sum)
if(st.session_state.clicked2):
    st.title("subtraction prgm")
    n1=st.number_input("enter n1")
    n2=st.number_input("enter n2")
    sub=n1-n2
    st.info("subtraction of 2 int number:")
    st.success(sub)


