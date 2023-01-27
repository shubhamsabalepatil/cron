import streamlit as st
import requests


def form():
    st.write("Add New Sample")
    with st.form(key="Sample Details"):
        name = st.text_input("Name")

        submission = st.form_submit_button(label= "Submit")
        r=name
        if submission == True:
            myobj = {"r": "r"}
            st.write(requests.post('http://127.0.0.1:8000/add_strategy/','myobj').json())

            st.success("Successfully submited")
form()

placeholder = st.empty()

actual_username = "username"
actual_password = "password"

# Insert a form in the container
with placeholder.form("login"):
    st.markdown("#### Enter your credentials")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submit = st.form_submit_button("Login")

if submit and username == actual_username and password == actual_password:
    # If the form is submitted and the email and password are correct,
    # clear the form/container and display a success message
    placeholder.empty()
    st.success("Login successful")
elif submit and username != actual_username and password != actual_password:
    st.error("Login failed")
else:
    pass
placeholder = st.empty()

actual_username = "username"
actual_password = "password"

# Insert a form in the container
with placeholder.form("login"):
    st.markdown("#### Enter your credentials")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submit = st.form_submit_button("Login")

if submit and username == actual_username and password == actual_password:
    # If the form is submitted and the email and password are correct,
    # clear the form/container and display a success message
    placeholder.empty()
    st.success("Login successful")
elif submit and username != actual_username and password != actual_password:
    st.error("Login failed")
else:
    pass
placeholder = st.empty()

actual_username = "username"
actual_password = "password"

# Insert a form in the container
with placeholder.form("login"):
    st.markdown("#### Enter your credentials")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submit = st.form_submit_button("Login")

if submit and username == actual_username and password == actual_password:
    # If the form is submitted and the email and password are correct,
    # clear the form/container and display a success message
    placeholder.empty()
    st.success("Login successful")
elif submit and username != actual_username and password != actual_password:
    st.error("Login failed")
else:
    pass
