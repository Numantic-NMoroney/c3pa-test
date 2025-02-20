# [2502] n8
#

import streamlit as st
import os


st.subheader("Test App")
st.text('GCP + Cloud Storage Bucket + Cloud Run + Streamlit.')

bucket_mount_path = os.environ.get('MOUNT_PATH', '/c3pa-app')

name_csv = 'app_counter.csv'
file_path = os.path.join(bucket_mount_path, name_csv)

st.text("bucket mount path : " + bucket_mount_path)

with open(file_path, "r") as file:
    for line in file:
        st.text(line.strip())

