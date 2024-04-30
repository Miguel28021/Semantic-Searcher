import streamlit as st


def wide_space_default():
    st.set_page_config(initial_sidebar_state="collapsed",layout="wide")

wide_space_default()
st.empty()

import os
from streamlit_navigation_bar import st_navbar
import st_pages as pg


parent_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(parent_dir, "logo.svg")
styles = {
    "nav": {
        "background-color": "royalblue",
        "justify-content": "left",
    }, "img": {
        "padding-right": "14px",
        "justify-content": "left",
        
    },
    "div": {
        "max-width": "32rem",
    },
    
    "span": {
        "color": "white",
        "padding": "14px",
    },
    "active": {
        "color": "var(--text-color)",
        "background-color": "white",
        "font-weight": "normal",
        "padding": "44px",
    },
    "hover": {
        "background-color": "rgba(255, 255, 255, 0.35)",
    },
}
options = {
    "show_menu": True,
    "show_sidebar": False,
}
page = st_navbar(["Acerca de", "Contacto"],logo_path=logo_path,options=options,styles=styles)

functions = {
    "Home": pg.show_home,
    "Acerca de": pg.show_about,
    "Contacto": pg.show_contact,
}
go_to = functions.get(page)
if go_to:
    go_to()
