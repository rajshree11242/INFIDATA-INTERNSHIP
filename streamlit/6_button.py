import streamlit as st

animal_shelter= ['cat','dog','lion','rabbit']

animal= st.text_input('type an animal')
if st.button('check availability'):
    have_it=animal_lover()in animal_shelter
    if(have_it):
        st.info("we have this animal")
    else:
        st.info("we dont have this animal")
