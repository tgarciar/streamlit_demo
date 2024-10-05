import streamlit as st
import os

st.markdown("""# This is Page 1: LW Images!
""")


st.markdown("""
---
""")

from PIL import Image

image = Image.open(os.path.join(os.getcwd(), 'raw_data/lw2.png'))
st.image(image, use_column_width=False)

st.markdown("""## All the LOGO pls!
""")

if st.button('Logo 2 :)'):
    from PIL import Image
    image = Image.open(os.path.join(os.getcwd(), 'raw_data/lw1.png'))
    st.image(image, caption='Le Wagon!', use_column_width=False)
