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

def zy():
    path = 'txt/zy.txt'
    with open(path,encoding='utf8') as f1:
        cNames = f1.readlines()
    print("ssss")
    cNames1 = eval(cNames[-1])
    Class_ranking = cNames1[6]
    total_score = cNames1[7]
    Plan_for_next_month = cNames1[8]
    col1, col2, col3 = st.columns(3)
    with col1:
        pass
    with col2:
        st.subheader('朱奕')
    with col3:
        pass

    col1, col2, col3 = st.columns(3)
    with col1:
        title = st.text_input('QQ', '2384592258')

    with col2:
        title = st.text_input('手机号', '15680335885')

    with col3:
        title = st.text_input('年级', '高一')

    col1, col2, col3 = st.columns(3)
    with col1:
        title = st.text_input('学习之星', '1颗')

    with col2:
        title = st.text_input('热力值', '60')

    with col3:
        title = st.text_input('学习状态', '正常')

    col1, col2, col3 = st.columns(3)
    with col1:
        title = st.text_input('班级排名', Class_ranking)

    with col2:
        title = st.text_input('总分', total_score)

    with col3:
        title = st.text_input('目标学校', '')

    txt = st.text_area('下一个月目标', Plan_for_next_month)

    total_score_list = []  # 总分
    km1_list = []
    km2_list = []
    km3_list = []
    km4_list = []
    km5_list = []
    km6_list = []
    test_list = []  # 月考列表
    print(cNames)
    for i in cNames:
        new_list = eval(i)
        km1_list.append(new_list[0])
        km2_list.append(new_list[1])
        km3_list.append(new_list[2])
        km4_list.append(new_list[3])
        km5_list.append(new_list[4])
        km6_list.append(new_list[5])
        total_score_list.append(new_list[7])
        test_list.append(new_list[8])

    col1, col2 = st.columns(2)
    with col1:
        bar = (
            Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))  # opts.InitOpts（theme标图主题=ThemeType.LIGHT）
            .add_xaxis(test_list)
            .add_yaxis("总分", total_score_list)
            # 全局配置项可通过 set_global_opts 方法设置
            .set_global_opts(title_opts=opts.TitleOpts(title="总分", subtitle=""))  # subtitle副标题文本，支持使用 \n 换行
        )
        streamlit_echarts.st_pyecharts(bar)
    with col2:
        file_ = open("./gif/Pets26.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        st.markdown(
            f'<img  src="data:image/gif;base64,{data_url}" alt="cat gif" style="height:290px; width:290px" >',
            unsafe_allow_html=True,
        )

    option = st.selectbox('科目成绩查询', ('语文', '数学', '外语', "物理", "化学", "生物"))
    st.markdown("")
    st.markdown("")
    if option == "语文":
        x = test_list
        y1 = km1_list
        line = (
            Line()
            .add_xaxis(xaxis_data=x)
            .add_yaxis(
                option,
                y1,
                symbol="triangle",
                symbol_size=30,
                linestyle_opts=opts.LineStyleOpts(color="red", width=4, type_="dashed"),
                itemstyle_opts=opts.ItemStyleOpts(
                    border_width=3, border_color="yellow", color="blue"
                ),
            )
            .set_global_opts(title_opts=opts.TitleOpts(title="Line-ItemStyle"))
        )
        streamlit_echarts.st_pyecharts(line)

    if option == "数学":
        x = test_list
        y1 = km2_list
        line = (
            Line()
            .add_xaxis(xaxis_data=x)
            .add_yaxis(
                option,
                y1,
                symbol="triangle",
                symbol_size=30,
                linestyle_opts=opts.LineStyleOpts(color="red", width=4, type_="dashed"),
                itemstyle_opts=opts.ItemStyleOpts(
                    border_width=3, border_color="yellow", color="blue"
                ),
            )
            .set_global_opts(title_opts=opts.TitleOpts(title="Line-ItemStyle"))
        )
        streamlit_echarts.st_pyecharts(line)

    if option == "外语":
        x = test_list
        y1 = km3_list
        line = (
            Line()
            .add_xaxis(xaxis_data=x)
            .add_yaxis(
                option,
                y1,
                symbol="triangle",
                symbol_size=30,
                linestyle_opts=opts.LineStyleOpts(color="red", width=4, type_="dashed"),
                itemstyle_opts=opts.ItemStyleOpts(
                    border_width=3, border_color="yellow", color="blue"
                ),
            )
            .set_global_opts(title_opts=opts.TitleOpts(title="Line-ItemStyle"))
        )
        streamlit_echarts.st_pyecharts(line)

    if option == "物理":
        x = test_list
        y1 = km4_list
        line = (
            Line()
            .add_xaxis(xaxis_data=x)
            .add_yaxis(
                option,
                y1,
                symbol="triangle",
                symbol_size=30,
                linestyle_opts=opts.LineStyleOpts(color="red", width=4, type_="dashed"),
                itemstyle_opts=opts.ItemStyleOpts(
                    border_width=3, border_color="yellow", color="blue"
                ),
            )
            .set_global_opts(title_opts=opts.TitleOpts(title="Line-ItemStyle"))
        )
        streamlit_echarts.st_pyecharts(line)
    if option == "化学":
        x = test_list
        y1 = km5_list
        line = (
            Line()
            .add_xaxis(xaxis_data=x)
            .add_yaxis(
                option,
                y1,
                symbol="triangle",
                symbol_size=30,
                linestyle_opts=opts.LineStyleOpts(color="red", width=4, type_="dashed"),
                itemstyle_opts=opts.ItemStyleOpts(
                    border_width=3, border_color="yellow", color="blue"
                ),
            )
            .set_global_opts(title_opts=opts.TitleOpts(title="Line-ItemStyle"))
        )
        streamlit_echarts.st_pyecharts(line)
    if option == "生物":
        x = test_list
        y1 = km6_list
        line = (
            Line()
            .add_xaxis(xaxis_data=x)
            .add_yaxis(
                option,
                y1,
                symbol="triangle",
                symbol_size=30,
                linestyle_opts=opts.LineStyleOpts(color="red", width=4, type_="dashed"),
                itemstyle_opts=opts.ItemStyleOpts(
                    border_width=3, border_color="yellow", color="blue"
                ),
            )
            .set_global_opts(title_opts=opts.TitleOpts(title="Line-ItemStyle"))
        )
        streamlit_echarts.st_pyecharts(line)