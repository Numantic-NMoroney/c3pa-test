# [2502] n8
#

import streamlit as st
import os


bucket_mount_path = os.environ.get('MOUNT_PATH', '/c3pa-app')
# bucket_mount_path = ''

name_csv = 'app_counter.csv'
file_path = os.path.join(bucket_mount_path, name_csv)
# file_path = name_csv


def read_lines(file_path):
    lines = []
    with open(file_path, "r") as file:
        for line in file:
            lines.append(line.strip())
    return lines


if 'lines' not in st.session_state:
    st.session_state.lines = read_lines(file_path)

st.subheader("Press the Button?")
st.text('Please consider pressing the button.')

if st.button("Button", type="primary"):
    with open(file_path, "w") as file:
        n1 = int(st.session_state.lines[1]) + 1
        st.session_state.lines[1] = str(n1)

        file.write(st.session_state.lines[0] + "\n")
        file.write(str(n1) + "\n")

st.text("The button has been pressed " + 
        str(st.session_state.lines[1]) + 
        " times.")

st.text("Thank you.")

