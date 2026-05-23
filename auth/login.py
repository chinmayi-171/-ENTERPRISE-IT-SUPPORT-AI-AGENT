import streamlit as st
from auth.auth_utils import authenticate_user


def login_page():

    st.subheader("Login to AI Helpdesk")

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        if not username or not password:

            st.warning(
                "Please enter username and password"
            )

            return

        success, response = authenticate_user(
            username,
            password
        )

        if success:

            # LOGIN SESSION
            st.session_state.logged_in = True

            st.session_state.username = username

            st.session_state.name = response["name"]

            st.session_state.email = response["email"]

            st.session_state.phone = response["phone"]

            # REDIRECT TO DASHBOARD
            st.session_state.page = "Dashboard"

            st.success("Login Successful")

            st.rerun()

        else:

            st.error(response)