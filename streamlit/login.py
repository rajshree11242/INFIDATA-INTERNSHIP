import hasher as hasher
import streamlit as st
import yaml
from yaml.loader import SafeLoader
with open('config.yaml')as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator=(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['expiry_days'],
    config['preauthorized']

)

name, authentication_status, username = authenticator.login(fields='slider')

if authentication_status:
    authenticator.logout('logout','slider')
    st.write(f'welcome *(name)*')
    st.title('an in home page')
elif authentication_status==False:
    st.error('username/password is incorrect')
elif authentication_status==None:
    st.warning('please enter your username and password')

