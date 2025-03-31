import streamlit as st
from nicegui import ui

st.set_page_config(
    page_title="Rebeccas CV",
)

st.title("")
st.sidebar.success("Select a page above.")


page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
background-image: url("https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/i/b2ee91ac-78f3-4325-b7f1-0791dd72f0b9/djh4e4o-f8befbb7-c711-4b7e-8628-27284c03cd16.png");
background-size: cover;
}}

[data-testid="stHeader"] {{
    background-color: rgba(0, 0, 0, 0);
}}


[data-testid="stToolbar"] {{
    right: 2rem;
}}

</style>
"""


with st.container():
    st.write("1")

with st.container():
    st.write("2")

with st.container():
    st.write("3")

with st.container():
    st.write("4")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("")
    with right_column:
        st.write("")
with st.container():
    st.write("5")

with st.container():
    st.write("6")




# Apply the background style
st.markdown(page_bg_img, unsafe_allow_html=True)

# Add your title
