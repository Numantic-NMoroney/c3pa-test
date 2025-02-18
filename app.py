# [2502] n8
#

import streamlit as st
import psycopg2
from dotenv import load_dotenv
import os


st.subheader("Test App")
st.text('GCP + Postgres + Cloud Run + Streamlit.')

load_dotenv()
conn_str = ( "host="      + os.getenv('PG_HOST') + " " +
             "port="      + os.getenv('PG_PORT') + " " +
             "dbname="    + os.getenv('PG_DB')   + " " +
             "user="      + os.getenv('PG_USER') + " " +
             "password="  + os.getenv('PG_PWD') )

conn = psycopg2.connect(conn_str)
cur = conn.cursor()

query = "SELECT * FROM c3pa_app_usage;"
cur.execute(query)

results = cur.fetchall()

for result in results:
    print(result)


