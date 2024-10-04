import streamlit as st

import numpy as np
import pandas as pd

st.set_page_config(
            page_title="Streamlit is cool and easy", # => Quick reference - Streamlit
            page_icon="🐍",
            layout="centered", # wide
            initial_sidebar_state="auto") # collapsed

st.markdown("""# This is a HEADER
## This is a sub header
This is text

## This is a list:
---
- Hello
- This
- Is
- A
- List

---
""")
def get_df():
    return pd.DataFrame({
        'first column': list(range(1, 11)),
        'second column': np.arange(10, 101, 10),
        'third column': np.random.randn(10)
    })

@st.cache
def get_df2():
    return pd.DataFrame({
        'first column': list(range(1, 11)),
        'second column': np.arange(10, 101, 10),
        'third column': np.random.randn(10)
    })


# this slider allows the user to select a number of lines
# to display in the dataframe
# the selected value is returned by st.slider
line_count = st.slider('Select a line count', 1, 10, 3)

st.markdown("""
---
""")
# and used to select the displayed lines


col1, col2= st.columns(2)

col1.write(get_df().head(line_count))

col2.write(get_df2().head(line_count))

st.markdown("""
            ---
            """)
@st.cache
def get_plotly_data():

    z_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')
    z = z_data.values
    sh_0, sh_1 = z.shape
    x, y = np.linspace(0, 1, sh_0), np.linspace(0, 1, sh_1)
    return x, y, z

import plotly.graph_objects as go

x, y, z = get_plotly_data()

fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])
fig.update_layout(title='IRR', autosize=False, width=800, height=800, margin=dict(l=40, r=40, b=40, t=40))
st.plotly_chart(fig)

st.markdown("""
            ---
            """)

direction = st.radio('Select a direction', ('top', 'right', 'bottom', 'left'))

st.write(direction)

if direction == 'top':
    st.write('🔼')
elif direction == 'right':
    st.write('▶️')
elif direction == 'bottom':
    st.write('🔽')
else:
    st.write('◀️')
