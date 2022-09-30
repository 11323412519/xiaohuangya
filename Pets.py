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

def pets():
    col1, col2, col3 = st.columns(3)
    with col1:
        file_ = open("./gif/Pets1.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        st.markdown(
            f'<img  src="data:image/gif;base64,{data_url}" alt="cat gif" style="height:220px; width:220px" >',
            unsafe_allow_html=True, )
    with col2:
        file_ = open("./gif/Pets2.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        st.markdown(
            f'<img  src="data:image/gif;base64,{data_url}" alt="cat gif" style="height:220px; width:220px" >',
            unsafe_allow_html=True, )
    with col3:
        file_ = open("./gif/Pets3.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        st.markdown(
            f'<img  src="data:image/gif;base64,{data_url}" alt="cat gif" style="height:220px; width:220px" >',
            unsafe_allow_html=True, )

    col1, col2, col3 = st.columns(3)
    with col1:
        file_ = open("./gif/Pets4.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        st.markdown(
            f'<img  src="data:image/gif;base64,{data_url}" alt="cat gif" style="height:220px; width:220px" >',
            unsafe_allow_html=True, )
    with col2:
        file_ = open("./gif/Pets5.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        st.markdown(
            f'<img  src="data:image/gif;base64,{data_url}" alt="cat gif" style="height:220px; width:220px" >',
            unsafe_allow_html=True, )
    with col3:
        file_ = open("./gif/Pets6.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        st.markdown(
            f'<img  src="data:image/gif;base64,{data_url}" alt="cat gif" style="height:220px; width:220px" >',
            unsafe_allow_html=True, )

    col1, col2, col3 = st.columns(3)
    with col1:
        file_ = open("./gif/Pets7.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        st.markdown(
            f'<img  src="data:image/gif;base64,{data_url}" alt="cat gif" style="height:220px; width:220px" >',
            unsafe_allow_html=True, )
    with col2:
        file_ = open("./gif/Pets8.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        st.markdown(
            f'<img  src="data:image/gif;base64,{data_url}" alt="cat gif" style="height:220px; width:220px" >',
            unsafe_allow_html=True, )
    with col3:
        file_ = open("./gif/Pets9.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        st.markdown(
            f'<img  src="data:image/gif;base64,{data_url}" alt="cat gif" style="height:220px; width:220px" >',
            unsafe_allow_html=True, )

    col1, col2, col3 = st.columns(3)
    with col1:
        file_ = open("./gif/Pets10.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        st.markdown(
            f'<img  src="data:image/gif;base64,{data_url}" alt="cat gif" style="height:220px; width:220px" >',
            unsafe_allow_html=True, )
    with col2:
        file_ = open("./gif/Pets11.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        st.markdown(
            f'<img  src="data:image/gif;base64,{data_url}" alt="cat gif" style="height:220px; width:220px" >',
            unsafe_allow_html=True, )
    with col3:
        file_ = open("./gif/Pets12.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        st.markdown(
            f'<img  src="data:image/gif;base64,{data_url}" alt="cat gif" style="height:220px; width:220px" >',
            unsafe_allow_html=True, )

    col1, col2, col3 = st.columns(3)
    with col1:
        file_ = open("./gif/Pets13.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        st.markdown(
            f'<img  src="data:image/gif;base64,{data_url}" alt="cat gif" style="height:220px; width:220px" >',
            unsafe_allow_html=True, )
    with col2:
        file_ = open("./gif/Pets14.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        st.markdown(
            f'<img  src="data:image/gif;base64,{data_url}" alt="cat gif" style="height:220px; width:220px" >',
            unsafe_allow_html=True, )
    with col3:
        file_ = open("./gif/Pets15.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        st.markdown(
            f'<img  src="data:image/gif;base64,{data_url}" alt="cat gif" style="height:220px; width:220px" >',
            unsafe_allow_html=True, )
    col1, col2, col3 = st.columns(3)
    with col1:
        file_ = open("./gif/Pets16.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        st.markdown(
            f'<img  src="data:image/gif;base64,{data_url}" alt="cat gif" style="height:220px; width:220px" >',
            unsafe_allow_html=True, )
    with col2:
        file_ = open("./gif/Pets17.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        st.markdown(
            f'<img  src="data:image/gif;base64,{data_url}" alt="cat gif" style="height:220px; width:220px" >',
            unsafe_allow_html=True, )
    with col3:
        file_ = open("./gif/Pets18.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        st.markdown(
            f'<img  src="data:image/gif;base64,{data_url}" alt="cat gif" style="height:220px; width:220px" >',
            unsafe_allow_html=True, )

    col1, col2, col3 = st.columns(3)
    with col1:
        file_ = open("./gif/Pets19.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        st.markdown(
            f'<img  src="data:image/gif;base64,{data_url}" alt="cat gif" style="height:220px; width:220px" >',
            unsafe_allow_html=True, )
    with col2:
        file_ = open("./gif/Pets20.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        st.markdown(
            f'<img  src="data:image/gif;base64,{data_url}" alt="cat gif" style="height:220px; width:220px" >',
            unsafe_allow_html=True, )
    with col3:
        file_ = open("./gif/Pets21.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        st.markdown(
            f'<img  src="data:image/gif;base64,{data_url}" alt="cat gif" style="height:220px; width:220px" >',
            unsafe_allow_html=True, )

    col1, col2, col3 = st.columns(3)
    with col1:
        file_ = open("./gif/Pets22.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        st.markdown(
            f'<img  src="data:image/gif;base64,{data_url}" alt="cat gif" style="height:220px; width:220px" >',
            unsafe_allow_html=True, )
    with col2:
        file_ = open("./gif/Pets23.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        st.markdown(
            f'<img  src="data:image/gif;base64,{data_url}" alt="cat gif" style="height:220px; width:220px" >',
            unsafe_allow_html=True, )
    with col3:
        file_ = open("./gif/Pets24.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        st.markdown(
            f'<img  src="data:image/gif;base64,{data_url}" alt="cat gif" style="height:220px; width:220px" >',
            unsafe_allow_html=True, )