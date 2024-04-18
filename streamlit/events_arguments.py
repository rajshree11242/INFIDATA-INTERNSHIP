import streamlit as st

if 'stage' not in st.session_state:
    st.session_state.stage=0

def set_state(i):
    st.session_state.stage=i

if st.session_state.stage==0:
    st.button('Begin', on_click=set_state,args=[1])

if st.session_state.stage>=1:
    name=st.text_input('name',on_change=set_stat,args[2])

if st.session_state.stage>=2:
    st.write("Hello",name)
    colour=st.selectbox('pick a colour',[none,red,blue,voilet,pink],on_change=set_state,args=[3])

if colour is none:
    set_state(2)

if st.session_state.stage>=2
    st.write(f':{colour}{thankyou!}')
    st.button('start over',on_click=set_state,args=[0])

