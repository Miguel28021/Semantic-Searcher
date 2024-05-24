import streamlit as st


def show_contact():
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.write("If you have any questions or feedback feel free to contact me at:")
        st.write("")
        st.write("Email: malomaosorio@gmail.com")
