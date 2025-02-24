# [2502] n8
#

import streamlit as st
import sys, os
import json
from datetime import datetime
import time
import hashlib


def portable_hash(string):
    encoded_string = string.encode('utf-8')
    hash_object = hashlib.sha256(encoded_string)
    return hash_object.hexdigest()

testing_path = os.environ.get('MOUNT_PATH', '/c3pa-app/testing')    # gcs
# testing_path = 'c3pa-app/testing'

name_txt = 'questions-2502-q26.txt'
in_path = os.path.join(testing_path, name_txt)


st.subheader("C3PA Testing")
st.text('Batch mode testing of the California Community Colleges Policy-Assistant.')

st.divider()

questions = []
with open(in_path, "r") as file:
    for line in file:
        questions.append(line.strip())
        # st.text(line)

qn = str(len(questions))
dt = str(datetime.now()).replace(" ", "-")

st.text(dt)

data = []
for i, question in enumerate(questions) :
    st.text(question)
    h1 = portable_hash(question)

    prompt = question
    t1 = str(datetime.now()).replace(" ", "_")

    time.sleep(0.5)
    result = "add bot reply here"

    t2 = str(datetime.now()).replace(" ", "_")

    dict_ = {
        "n" : str(i+1),
        "qn" : qn,
        "question" : question,
        "prompt" : prompt,
        "response" : result,
        "start" : t1,
        "stop" : t2,
        "hash" : h1
    }
    data.append(dict_)

json_str = json.dumps(data)

name_json = "log_testing-ccc-bot-" + dt + ".json"
out_path = os.path.join(testing_path, name_json)
with open(out_path, "w") as f:
    f.write(json_str)

