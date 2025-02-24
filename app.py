# [2502] n8
#

import streamlit as st
import os


questions_path = os.environ.get('MOUNT_PATH', '/c3pa-app/testing')
# questions_path = 'c3pa-app/testing'

name_txt = 'questions-2502-q26.txt'
file_path = os.path.join(questions_path, name_txt)


st.subheader("C3PA Testing")
st.text('Batch mode testing of the California Community Colleges Policy-Assistant.')

st.divider()

questions = []
with open(file_path, "r") as file:
    for line in file:
        questions.append(line.strip())
        st.text(line)

