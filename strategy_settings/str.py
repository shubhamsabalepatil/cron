import streamlit as st
import requests

def form():
    st.write("Add New Strategy")
    with st.form(key="Strategy Details"):
        Name = st.text_input("Name")
        Code = st.text_input("Code")
        Time_Frame = st.selectbox("Time Frame",["Intraday","Positional"])
        Type = st.selectbox("Type",["Short Volatility","Short Directional","Long Directional","Pattern System","Calendar Spread","Expiry"])
        Initialize_Time = st.time_input("Initialize_Time")
        Script = st.text_input("Script")
        submission = st.form_submit_button(label= "Submit")

        if submission == True:
            st.write(requests.post("http://127.0.0.1:8000/add_strategy/",{"Name":Name, "Code":Code,"Time_Frame":Time_Frame, "Type":Type, "Initialize_Time":Initialize_Time,"Script":Script }).json())

            st.success("Successfully submited")

form()

