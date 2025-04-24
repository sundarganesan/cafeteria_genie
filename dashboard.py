import streamlit as st
import time
from shared_state import get_all_counters

st.set_page_config(page_title="Cafeteria Genie Dashboard", layout="wide")
st.title("\U0001F468‍\U0001F373 Cafeteria Genie - Live Person Stats")

placeholder = st.empty()

while True:
    counter_data = get_all_counters()
    with placeholder.container():
        for counter, data in counter_data.items():
            st.subheader(f"Counter: {counter}")
            col1, col2, col3, col4 = st.columns(4)
            col1.metric(label="Current", value=f"{data['count']} people")
            col2.metric(label="Initial", value=f"{data['initial']} people")
            col3.metric(label="Entered", value=f"{data['entered']}")
            col4.metric(label="Exited", value=f"{data['exited']}")
    time.sleep(1)