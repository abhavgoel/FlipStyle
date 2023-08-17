import streamlit as st
from openaiApi import *


st.set_page_config(
    page_title="FlipStyle",
    page_icon="🧊",
)
st.title("FlipStyle")
# st.sidebar.success("Select a page above")

if("my_input" not in st.session_state):
    st.session_state["my_input"] = ""

my_input = st.text_input("Describe an outfit you want to generate", st.session_state["my_input"])
submit = st.button("Submit")
if(submit):
    st.session_state["my_input"] = my_input
    reply = outfit_generator(my_input)
    st.write(reply)
    