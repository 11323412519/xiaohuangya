import streamlit as st
from PIL import Image

def question_bank():
    st.write("题库地址：")
    code = '''
    https://www.gaokao.com/
    '''
    st.code(code, language='python')

    st.write("做题步骤：")
    st.write("第一步：复制题库链接，把在浏览器中输入链接打开")
    image = Image.open('image/步骤一.png')
    st.image(image)

    st.write("第二步：点击选择试题库")
    image = Image.open('image/步骤二.png')
    st.image(image)

    st.write("第三步：根据自己的情况选择对应题库")
    image = Image.open('image/步骤三.png')
    st.image(image)