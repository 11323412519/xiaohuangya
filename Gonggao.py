import  streamlit as st
def gonggao():
    path = 'txt/gonggao.txt'
    with open(path,encoding='utf8') as f1:
        text_list = f1.readlines()
    st.write("公告栏：")
    code=""
    for text in text_list:
        code+=text
    st.code(code, language='python')

def add_gonggao(text):
    path = 'txt/gonggao.txt'
    with open(path, encoding='utf8') as f1:
        lists = f1.readlines()
    lists.insert(0,text)
    with open(path, 'w', encoding='utf8') as f2:
        f2.writelines(lists)