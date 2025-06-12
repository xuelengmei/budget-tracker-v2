import streamlit as st

st.set_page_config(page_title="小小记账本", page_icon="📔")

# 初始化 session
if "users" not in st.session_state:
    st.session_state.users = {}
if "logged_in_user" not in st.session_state:
    st.session_state.logged_in_user = None

def logout():
    st.session_state.logged_in_user = None

# 登录后显示欢迎内容
if st.session_state.logged_in_user:
    st.success(f"欢迎回来，{st.session_state.logged_in_user}！")
    st.button("🚪 退出登录", on_click=logout)
    st.info("请在左侧选择页面进行记账或查看统计~")
else:
    tab1, tab2 = st.tabs(["🔐 登录", "🆕 注册"])
    with tab1:
        username = st.text_input("用户名")
        password = st.text_input("密码", type="password")
        if st.button("登录"):
            if username in st.session_state.users and st.session_state.users[username] == password:
                st.session_state.logged_in_user = username
                st.success("登录成功！")
            else:
                st.error("用户名或密码错误")

    with tab2:
        new_username = st.text_input("注册用户名")
        new_password = st.text_input("注册密码", type="password")
        if st.button("注册"):
            if new_username in st.session_state.users:
                st.warning("该用户名已被注册")
            else:
                st.session_state.users[new_username] = new_password
                st.success("注册成功，请返回登录")

