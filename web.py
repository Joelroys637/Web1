import streamlit as st
from streamlit_option_menu import option_menu
import sample as sa
import page1 as pg
with st.sidebar:
    selected = option_menu(
        menu_title="main menu",
        options=["home","ok","project","contact","tuch"],
    )
if selected == "home":
    st.title(f"you have in {selected}")
        
if selected =="ok":
    sa.fun()
if selected == "project":
    st.button("hi")
    if st.button:
        st.title("welcome")
if selected == "contact":
    st.title("hi I AM leo")
if selected == "tuch":
    pg.fun1()
