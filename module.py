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

def College_Entrance_Examination_Results():
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


def Question_bank():
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

def hxd1():
    path = 'txt/hxd.txt'
    with open(path,encoding='utf8') as f1:
        cNames = f1.readlines()
    cNames1=eval(cNames[-1])
    # 0-5 科目  6 排名 7总分 8月份 9计划
    Class_ranking=cNames1[6]
    total_score=cNames1[7]
    Plan_for_next_month=cNames1[9]

    col1, col2, col3 = st.columns(3)
    with col1:
        pass

    with col2:
        st.subheader('何向东')

    with col3:
        pass

    col1, col2, col3 = st.columns(3)
    with col1:
        title = st.text_input('QQ', '')

    with col2:
        title = st.text_input('手机号', '')

    with col3:
        title = st.text_input('年级', '高二')

    col1, col2, col3 = st.columns(3)
    with col1:
        title = st.text_input('学习之星', '1颗')

    with col2:
        title = st.text_input('热力值', '98')

    with col3:
        title = st.text_input('学习状态', '正常')

    col1, col2, col3 = st.columns(3)
    with col1:
        title = st.text_input('班级排名', Class_ranking)

    with col2:
        title = st.text_input('总分', total_score)

    with col3:
        title = st.text_input('目标学校', '')
    txt = st.text_area('下一个月目标',Plan_for_next_month)


    total_score_list=[]   #总分
    km1_list = []
    km2_list = []
    km3_list = []
    km4_list = []
    km5_list = []
    km6_list = []
    test_list=[]          #月考列表
    for i in cNames:
        new_list=eval(i)
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
        file_ = open("./gif/Pets25.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        st.markdown(
            f'<img  src="data:image/gif;base64,{data_url}" alt="cat gif" style="height:290px; width:290px" >',
            unsafe_allow_html=True,
        )

    option = st.selectbox('', ('语文', '数学', '外语', "政治", "地理", "历史"))

    if option=="语文":
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

    if option=="数学":
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

    if option=="外语":
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

    if option=="政治":
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
    if option=="历史":
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
    if option=="地理":
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



def zy1():

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
        title = st.text_input('QQ', '')

    with col2:
        title = st.text_input('手机号', '')

    with col3:
        title = st.text_input('年级', '高一')

    col1, col2, col3 = st.columns(3)
    with col1:
        title = st.text_input('学习之星', '1颗')

    with col2:
        title = st.text_input('热力值', '98')

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

def add_Score():
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


            else:
                e = RuntimeError('密码错误')
                st.exception(e)
    else:
        e = RuntimeError('未保持提交')
        st.exception(e)


def load_gif(path):
    file_ = open(path, "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    st.markdown(
        f'<img  src="data:image/gif;base64,{data_url}" alt="cat gif" style="height:215px; width:215px" >',
        unsafe_allow_html=True,
    )


def Pets():
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