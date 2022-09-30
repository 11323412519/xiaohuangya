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
def college_Entrance_Examination_Results():
    image = Image.open('image/高考.jpg')
    st.image(image)
    data_22_21, data_20_19, data_18_17 = st.tabs(["2022-2021", "2020-2019", "2018-2017"])

    with data_22_21:
        col1, col2 = st.columns(2)
        with col1:
            df = pd.DataFrame({
                "年份": [2022, 2022, 2022, 2022],
                "地区": ["四川", "四川", "四川", "四川"],
                "批次": ["理科第一批(一本)", "理科第二批(二本)", "文科第一批(一本)", "文科第二批(二本)"],
                "分数线": [515, 426, 538, 466]
            })
            st.dataframe(df)

        with col2:
            df = pd.DataFrame({
                "年份": [2021, 2021, 2021, 2021],
                "地区": ["四川", "四川", "四川", "四川"],
                "批次": ["理科第一批(一本)", "理科第二批(二本)", "文科第一批(一本)", "文科第二批(二本)"],
                "分数线": [521, 430, 541, 474]
            })
            st.dataframe(df)
    with data_20_19:
        col1, col2 = st.columns(2)
        with col1:
            df = pd.DataFrame({
                "年份": [2020, 2020, 2020, 2020],
                "地区": ["四川", "四川", "四川", "四川"],
                "批次": ["理科第一批(一本)", "理科第二批(二本)", "文科第一批(一本)", "文科第二批(二本)"],
                "分数线": [529, 443, 527, 459]
            })
            st.dataframe(df)

        with col2:
            df = pd.DataFrame({
                "年份": [2019, 2019, 2019, 2019],
                "地区": ["四川", "四川", "四川", "四川"],
                "批次": ["理科第一批(一本)", "理科第二批(二本)", "文科第一批(一本)", "文科第二批(二本)"],
                "分数线": [547, 459, 540, 472]
            })
            st.dataframe(df)

    with data_18_17:
        col1, col2 = st.columns(2)
        with col1:
            df = pd.DataFrame({
                "年份": [2018, 2018, 2018, 2018],
                "地区": ["四川", "四川", "四川", "四川"],
                "批次": ["理科第一批(一本)", "理科第二批(二本)", "文科第一批(一本)", "文科第二批(二本)"],
                "分数线": [546, 458, 553, 492]
            })
            st.dataframe(df)

        with col2:
            df = pd.DataFrame({
                "年份": [2017, 2017, 2017, 2017],
                "地区": ["四川", "四川", "四川", "四川"],
                "批次": ["理科第一批(一本)", "理科第二批(二本)", "文科第一批(一本)", "文科第二批(二本)"],
                "分数线": [511, 436, 537, 470]
            })
            st.dataframe(df)

    st.markdown("2022年四川省各学校最低录取分数线  (这才是录取的标准)：")
    col1, col2 = st.columns(2)
    with col1:
        image = Image.open('image/学校录取图1.png')

        st.image(image, caption='理科')

    with col2:
        image = Image.open('image/学校录取图2.png')

        st.image(image, caption='文科')