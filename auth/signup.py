import streamlit as st
from auth.auth_utils import register_user


def signup_page():

    st.subheader("Create New Account")

    name = st.text_input("Full Name")

    email = st.text_input("Email Address")

    phone = st.text_input("Phone Number")

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    confirm_password = st.text_input(
        "Confirm Password",
        type="password"
    )

    if st.button("Create Account"):

        if (
            not name
            or not email
            or not phone
            or not username
            or not password
        ):

            st.warning("Please fill all fields")
            return

        if password != confirm_password:

            st.error("Passwords do not match")
            return

        if len(password) < 6:

            st.error(
                "Password must be at least 6 characters"
            )

            return

        success, message = register_user(
            name,
            email,
            phone,
            username,
            password
        )

        if success:

            st.success(message)

            # REDIRECT TO LOGIN
            st.session_state.page = "Login"

            st.rerun()

        else:

            st.error(message)