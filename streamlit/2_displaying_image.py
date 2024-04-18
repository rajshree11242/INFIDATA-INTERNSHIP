import streamlit as st
from PIL import image
img=Image.open('_.jpg')
st.title('DISPLAYING IMAGE')
st.image(img)
