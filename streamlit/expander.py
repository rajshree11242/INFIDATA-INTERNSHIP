immport streamlit as st

st.bar_chart({"data": [1,5,2,6,2,1]})

with st.expander("See explanation"):
    st.write("the chart above shows some number i picked for u ")
    st.image("car2.jpg")