import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import datetime as dt
import date_process.calc_date as dc
from dateutil.relativedelta import relativedelta

st.cache()
def read_master():
    data = pd.read_csv('master.csv')
    return data

data = read_master()


st.title('お産予測アプリ')

# 牛の名前をリストで取得する
cow_name = list(data['名前'].unique())

select_name = st.selectbox('牛の名前を選択してください。',cow_name)

# 種付日を検索する
tane_date = data.loc[data['名前']==select_name,'種付日1']
tane_date = tane_date.values[0].split('/')
tane_date = dt.datetime(int(tane_date[0]),int(tane_date[1]), int(tane_date[2])) 
st.write('種付日')
st.write(tane_date)
st.write('お産予定日')
pred_birth = tane_date+relativedelta(months=+9,days=+10)
st.write(pred_birth)
st.write('15日前の日付')
st.write(pred_birth-dt.timedelta(days=15))
st.write('45日前の日付')
st.write(pred_birth-dt.timedelta(days=45))