import streamlit as st
import pandas as pd

if "logged_in_user" not in st.session_state or not st.session_state.logged_in_user:
    st.warning("请先登录后再使用本页面~")
    st.stop()

user = st.session_state.logged_in_user
if "records" not in st.session_state:
    st.session_state.records = {}
if user not in st.session_state.records:
    st.session_state.records[user] = []

st.title("✨ 小小记账本 ✨")

date = st.date_input("📅 请输入日期")
record_type = st.radio("记录类型", ["支出", "收入"], horizontal=True)

category = st.selectbox(
    "📂 分类",
    ["饮食", "交通", "购物", "娱乐", "其他"] if record_type == "支出" else ["工资", "兼职", "理财", "红包", "其他"]
)

amount = st.text_input("💰 请输入金额", placeholder="例如：58.00")
note = st.text_input("📝 备注")

if st.button("📥 添加记录"):
    try:
        amount_value = float(amount)
        st.session_state.records[user].append({
            "日期": str(date),
            "类型": record_type,
            "分类": category,
            "金额": amount_value,
            "备注": note
        })
        st.success("记录添加成功!")
    except:
        st.warning("金额格式不对，请重新输入数字~~")

if st.button("🧹 清空全部"):
    st.session_state.records[user] = []

st.markdown("---")
st.subheader("🧾 当前记录：")
user_records = st.session_state.records[user]

if user_records:
    df = pd.DataFrame(user_records)
    for i, row in df.iterrows():
        col1, col2, col3, col4, col5 = st.columns([2, 2, 2, 2, 1])
        col1.write(row["日期"])
        col2.write(f"{row['类型']} - {row['分类']}")
        col3.write(f"¥{row['金额']:.2f}")
        col4.write(row["备注"])
        if col5.button("🗑️", key=f"del_{i}"):
            st.session_state.records[user].pop(i)
            st.rerun()
else:
    st.info("目前还没有记录哦~")

