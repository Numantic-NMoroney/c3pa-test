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

st.subheader("Press the Button?")
st.text('Please consider pressing the button.')

lines = read_lines(file_path)

if st.button("Button", type="primary"):
    with open(file_path, "w") as file:
        file.write(lines[0] + "\n")
        n1 = int(lines[1]) + 1
        file.write(str(n1) + "\n")

lines = read_lines(file_path)

st.text("The button has been pressed " + 
        str(lines[1]) + 
        " times.")

st.text("Thank you.")

