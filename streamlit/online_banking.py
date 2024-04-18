import streamlit as st

st.title("welcome to online banking")

st.sidebar.title("create your account")
name=st.text_input("enter your name")
id=st.number_input("enter your id")
branch=st.text_input("enter the branch")

st.sidebar.title("select operation")

balance=0
choice=st.sidebar.selectbox ('select',('DEPOSIT','WITHDRAW','DISPLAY'))
if choice=='DEPOSIT':
    amount=st.number_input("enter the amount u want to deposit")
    balance=balance+amount
    st.success(balance)


elif choice=='WITHDRAW':
    amount=st.number_input("enter the amount u want to deposit")
    if balance>=amount:
    balance=balance-amount
    st.write(balance)
    else:
    st,write(insufficent balance)

elif choice=='DISPLAY':
st.write(name)
st.write(branch)
st.write(id)
st.write(balance)





