import streamlit as st
import os

st.markdown("""# This is Page 1: LW Images!
""")


st.markdown("""
---
""")

from PIL import Image
raw_data_path = '/raw_data'
st.write(os.listdir(raw_data_path))  # List files in the directory

 st.write(f"Current working directory: {os.getcwd()}")
image = Image.open('/raw_data/lw2.png')
st.image(image, use_column_width=False)

st.markdown("""## All the LOGO pls!
""")

if st.button('Logo 2 :)'):
    from PIL import Image
    image = Image.open('/raw_data/lw1.png')
    st.image(image, caption='Le Wagon!', use_column_width=False)
