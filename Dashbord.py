import os
import streamlit as st
import requests
from django.core.wsgi import get_wsgi_application
import pandas as pd
from pymongo import MongoClient


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qca_strategy_engine.settings')

application = get_wsgi_application()
from django.contrib.auth import authenticate

col1, col2, col3 = st.columns([1,1,1])
with col2:
    st.sidebar.title("QCA STRATEGY ENGINE")
    st.sidebar.header("Strategy")
    st.sidebar.header("strategy Settings")

def check_password():



    def password_entered():


        """Checks whether a password entered by the user is correct."""
        user = authenticate(
            username=st.session_state['username'],
            password=st.session_state['password']
        )


        if (user is not None):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store username + password
            del st.session_state["username"]

        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show inputs for username + password.
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False

    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 User not known or password incorrect")
        return False
    else:
        # Password correct.
        return True


if check_password():

    col3, col4, col5,col6 = st.columns([1, 1, 50,20])
    col1, col2 = st.columns([1,50])



    with st.sidebar:

        stetus = st.selectbox("Settings",["Add Strategy","Add Parameter","Add Symbol","Add Instance","Instance status"])
        if (stetus == 'Instance status'):
            with col2:
                st.dataframe(requests.get('http://127.0.0.1:8000/Instance_status/').json())



        if (stetus == 'Add Strategy'):

            with col2:
                st.header("Strategies")


                client = MongoClient("mongodb://localhost:27017")
                db = client.qca
                collection = db.strategy_settings_strategy_details
                data = pd.DataFrame(collection.find(),index= None)
                data = data.drop(['_id','id'],axis=1)
                st.write(data)

                with col6:
                    formbtn = st.button("Add strategy")


                with col5:


                    if "formbtn_state" not in st.session_state:
                        st.session_state.formbtn_state = False

                    if formbtn or st.session_state.formbtn_state:
                        st.session_state.formbtn_state = True

                        st.subheader("Add Strategy")

                        with st.form(key='user_info', clear_on_submit=True):
                            st.write('Strategy')
                            Name = st.text_input("Name")
                            Code = st.text_input("Code")
                            Time_Frame = st.selectbox("Time Frame", ["Intraday", "Positional"])
                            Type = st.selectbox("Type",
                                                ["Short Volatility", "Short Directional", "Long Directional", "Pattern System",
                                                 "Calendar Spread", "Expiry"])
                            Initialize_Time = st.time_input("Initialize_Time")
                            Script = st.text_input("Script")
                            submission = st.form_submit_button(label="Submit")

                            if submission == True:
                                st.write(requests.post("http://127.0.0.1:8000/add_strategy/",
                                                       {"Name": Name, "Code": Code, "Time_Frame": Time_Frame, "Type": Type,
                                                        "Initialize_Time": Initialize_Time, "Script": Script}).json())
                                st.success("Successfully submited")


                                if st.form_submit_button('cancel'):
                                    st.warning('cancelled')

                                st.info("Kindly reload your browser to start again!!!!")








        if (stetus == 'Add Parameter'):
            client = MongoClient("mongodb://localhost:27017")
            db = client.qca
            collection = db.strategy_settings_strategy_details
            data = pd.DataFrame(collection.find())
            data = data['id','Name']
            data = dict(data)
            name = data
            with col2:
                def form():
                    st.write("Add New Parameter")
                    with st.form(key="Strategy Details"):
                        Strategy = st.selectbox('Strategy', {i for j in name})
                        Name = st.text_input("Name")
                        Descrption = st.text_input("Descrption")
                        Variable_Name = st.text_input("Variable Name")
                        Parameter_Type = st.selectbox("Parameter Type",["Number","Time"])
                        Parameter_Value = st.text_input("Parameter Value")
                        submission = st.form_submit_button(label="Submit")

                        if submission == True:
                            st.write(requests.post("http://127.0.0.1:8000/add_Parameters/",
                                                   {"Strategy": Strategy, "Name": Name, "Descrption": Descrption, "Variable_Name": Variable_Name,
                                                    "Parameter_Type": Parameter_Type, "Parameter_Value": Parameter_Value}).json())

                            st.success("Successfully submited")


                form()

        if (stetus == 'Add Symbol'):
            client = MongoClient("mongodb://localhost:27017")
            db = client.qca
            collection = db.strategy_settings_strategy_details
            data = pd.DataFrame(collection.find())
            data = data['Name']
            name = data
            with col2:
                def form():
                    st.write("Add New Symbol")
                    with st.form(key="Strategy Details"):
                        strategy = st.selectbox('Strategy',[i for i in name])
                        Exchange = st.selectbox("Exchange",["NSE","BSE"])
                        Symbol = st.selectbox("Symbol",["A","B","C"])
                        is_Monday = st.checkbox("Monday")
                        is_Tuesday = st.checkbox("Tuesday")
                        is_Wednesday = st.checkbox("Wednesday")
                        is_Thursday = st.checkbox("Thursday")
                        is_Friday = st.checkbox("Friday")
                        submission = st.form_submit_button(label="Submit")
                        if submission == True:
                            st.write(requests.post("http://127.0.0.1:8000/add_Symbol/",
                                                   {"strategy": strategy, "Exchange": Exchange, "Symbol": Symbol, "is_Monday": is_Monday,
                                                    "is_Tuesday": is_Tuesday, "is_Wednesday ": is_Wednesday,"is_Thursday":is_Thursday,"is_Friday":is_Friday}).json())

                            st.success("Successfully submited")


                form()

        if (stetus == 'Add Instance'):
            client = MongoClient("mongodb://localhost:27017")
            db = client.qca
            collection = db.strategy_settings_strategy_details
            data = pd.DataFrame(collection.find())
            data = data['Name']
            name = data
            with col2:
                def form():
                    st.write("Add New Instance")
                    with st.form(key="Strategy Details"):
                        Strategy = st.selectbox('Strategy',[i for i in name])
                        Exchange = st.selectbox("Exchange",["NSE","BSE"])
                        Symbol = st.selectbox("Symbol",["A","B","C"])
                        is_Monday = st.checkbox("Monday")
                        is_Tuesday = st.checkbox("Tuesday")
                        is_Wednesday = st.checkbox("Wednesday")
                        is_Thursday = st.checkbox("Thursday")
                        is_Friday = st.checkbox("Friday")
                        Initialize_Time = st.time_input("Initialize_Time")
                        Terminate_Time = st.time_input("Terminate_Time")
                        submission = st.form_submit_button(label="Submit")

                        if submission == True:
                            st.write(requests.post("http://127.0.0.1:8000/add_Instance/",
                                                   {"Strategy": Strategy, "Exchange": Exchange, "Symbol": Symbol, "is_Monday": is_Monday,
                                                    "is_Tuesday": is_Tuesday, "is_Wednesday": is_Wednesday,"is_Thursday":is_Thursday,"is_Friday":is_Friday,"Initialize_Time":Initialize_Time,"Terminate_Time":Terminate_Time}).json())

                            st.success("Successfully submited")


                form()