import streamlit as st

st.title("arithmetic operation")
st.sidebar.markdown("please give the input")
st.sidebar.title("select the option")
st.sidebar.markdown("select the option accordingly")

choice=st.sidebar.selectbox('select',('ADD','MUL'))
selected_status=st.sidebar.selection('select number', option=['2N','3N'])
if choice=='ADD':
    if selected_status=='2N':
        n1=st.number_input('enter value of n1')
        n2=st.number_input('enter value of n2')
        sum=n1+n2
        st.success(sum)
    elif selected_status=='3N':
        n1 = st.number_input('enter value of n1')
        n2 = st.number_input('enter value of n2')
        n3 = st.number_input('enter value of n3')
        sum=n1+n2+n3
        st.success(sum)
elif choice=='MUL' :
    if selected_status=='2N':
        n1=st.number_input('enter value of n1')
        n2=st.number_input('enter value of n2')
        mul=n1*n2
        st.success(mul)
    elif selected_status=='3N':
        n1 = st.number_input('enter value of n1')
        n2 = st.number_input('enter value of n2')
        n3 = st.number_input('enter value of n3')
        mul = n1 * n2 * n3
        st.success(mul)
        
        
        
        
        
        