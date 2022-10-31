import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import datetime as dt
import date_process.calc_date as dc

st.title('お産予測アプリ')

date_injection = st.date_input('注射日を選択してください。')

if date_injection:

    st.write('15日前の日付')
    st.write(date_injection-dt.timedelta(days=15))
    st.write('45日前の日付')
    st.write(date_injection-dt.timedelta(days=45))