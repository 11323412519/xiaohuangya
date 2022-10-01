import streamlit as st
from PIL import Image
import datetime
import  numpy as np
import streamlit_echarts
import base64
from  shouye import shouye_model
from  zhuyi import zy
from  hexiangdong import hxd
from  add_Score import  add_score
from  Question_bank import  question_bank
from  gaokao import  college_Entrance_Examination_Results
from  Pets import  pets
from  Gonggao import  gonggao
from  exchange import exchange_v1
with st.sidebar:
    file_ = open("./gif/112545-wumpus-hi.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    st.markdown(
        f'<img  src="data:image/gif;base64,{data_url}" alt="cat gif" style="height:215px; width:215px" >',
        unsafe_allow_html=True,
    )
    st.markdown('')
    add_selectbox = st.sidebar.selectbox(
    "导航栏/菜单栏",
    ("首页","朱奕成绩管理系统", "何向东成绩管理系统","月考成绩录入","宠物系统","处罚、通知、警告系统",
     "家长评价系统","学习之星兑换系统","历年高考成绩查询","题库"))

if add_selectbox=="首页":
    #st.balloons()
    shouye_model()
if add_selectbox=="历年高考成绩查询":
    college_Entrance_Examination_Results()
if add_selectbox=="题库":
    question_bank()
if add_selectbox=="何向东成绩管理系统":
    hxd()
if add_selectbox=="朱奕成绩管理系统":
    zy()
if add_selectbox=="月考成绩录入":
    add_score()
if add_selectbox=="宠物系统":
    pets()
if add_selectbox=="处罚、通知、警告系统":
    gonggao()
if add_selectbox=="学习之星兑换系统":
    exchange_v1()





