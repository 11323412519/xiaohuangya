import streamlit as st
import time
from PIL import Image
import  pandas as pd
import  numpy as np
import pyecharts
import base64
from pyecharts.charts import Bar
from pyecharts import options as opts
import streamlit_echarts
from pyecharts.charts import  Line
from pyecharts.globals import ThemeType
from  Gonggao import  add_gonggao
def add_score():
    st.markdown("成绩录入须知：")
    code = '''
            1.选择对应名字进行成绩录入
2.输入提交前请认真检查内容是否正确
3.不能提交别人的成绩
4.只能录入一次成绩，不能多次提交
            '''
    information_list = []
    st.code(code, language='python')
    use = st.selectbox(
        '',
        ('朱奕', '何向东'))

    st.markdown(" "), st.markdown(" ")
    col1, col2, col3 = st.columns(3)
    with col1:
        title_1 = st.text_input('语文', '')
    with col2:
        title_2 = st.text_input('数学', '')
    with col3:
        title_3 = st.text_input('外语', '')
    col1, col2, col3 = st.columns(3)
    with col1:
        title_4 = st.text_input('物理/政治', '')
    with col2:
        title_5 = st.text_input('化学/历史', '')
    with col3:
        title_6 = st.text_input('生物/地理', '')
    col1, col2,col3 = st.columns(3)
    with col1:
        title_7 = st.text_input('班级排名', '')

    with col2:
        title_8 = st.text_input('总分', '')
    with col3:
        title_9 = st.text_input('考试月份', '')
    title_10 = st.text_area('下一个月目标', "")
    st.write("请认真核对填入信息再进行输入密码!!!")
    password = st.text_input('密码', '')
    if st.button("提交"):
        for i in [title_1, title_2, title_3, title_4, title_5, title_6, title_7, title_8,title_9,title_10]:
            information_list.append(i)
        if "" in information_list:
            e = RuntimeError('不合法输入')
            st.exception(e)
            st.stop()
        if len(information_list[9]) < 2:
            e = RuntimeError('下个月目标必须输入50字以上')
            st.exception(e)
            st.stop()
        st.success('✅' + "输入合法")
        if use == "何向东":
            if password == "000000":
                path = 'txt/hxd.txt'
                with open(path,encoding='utf8') as f1:
                    cNames = f1.readlines()
                cNames.append(str(information_list) + "\n")
                with open(path, 'w', encoding='utf8') as f2:
                    f2.writelines(cNames)
                st.success('✅' + "提交时间：" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
                text=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))+" 何向东"+"成功的提交了成绩"+"\n"
                add_gonggao(text)
            else:
                e = RuntimeError('密码错误')
                st.exception(e)
        elif use == "朱奕":
            if password == "000000":
                path = 'txt/zy.txt'
                with open(path,encoding='utf8') as f1:
                    cNames = f1.readlines()
                cNames.append(str(information_list) + "\n")
                with open(path, 'w',encoding='utf8') as f2:
                    f2.writelines(cNames)
                st.success('✅' + "提交时间：" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
                text = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + " 朱奕" + "成功的提交了成绩"+"\n"
                add_gonggao(text)


            else:
                e = RuntimeError('密码错误')
                st.exception(e)
    else:
        e = RuntimeError('未保持提交')
        st.exception(e)