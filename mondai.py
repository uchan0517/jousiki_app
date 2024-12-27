import pandas as pd
import streamlit as st
import random
import time

def question():
    st.session_state.q = q = random.choice(st.session_state.ql)
    st.subheader(q[0])
    with st.form(key='my_from'):
        percent = st.slider("何パーセント", 0, 100, 50,key="inp")
        submit_button = st.form_submit_button(label='決定',on_click=check)

def check():
    q = st.session_state.q
    inp = st.session_state.inp
    ans = q[1]
    
    if ans == inp:
        st.header("ピッタリ 自分の答え" + str(inp) + "%  正解" + str(ans) + "%")
        st.session_state.point += 50
    elif ans + 5 >= inp and ans - 5 <= inp:
        st.header("ニアピン 自分の答え" + str(inp) + "% 正解" + str(ans) +"%")
        st.session_state.point += 20
    elif ans + 20 >= inp and ans - 20 <= inp:
        st.header("普通 自分の答え" + str(inp) + "% 正解" + str(ans) +"%")
        st.session_state.point += 10
    else:
        st.header("あちゃー 自分答え" + str(inp) + "%正解" + str(ans) +"%")
        st.session_state.point += -10
    st.session_state.hp -= abs(inp-ans)
    
    st.subheader(f"現在の得点：{st.session_state.point} / 残りのライフ：{st.session_state.hp}")
    if  st.session_state.hp>=1:
        st.button  ("次の問題", on_click=question)
    else:
        if st.session_state.point>=120:
            st.subheader("すばらしい常識者です")
        elif st.session_state.point>=90:
            st.subheader("常識あり")
        elif st.session_state.point>=60:
            st.subheader("普通普通")
        elif st.session_state.point>=30:
            st.subheader("ちょいずれてます")
        else:
            st.subheader("真の非常識")


        st.subheader("ゲームオーバー")
        st.session_state.hp = 100
        st.session_state.point = 0
        st.button  ("ニューゲーム", on_click=question)


if not "idx"in st.session_state:
    df = pd.read_excel('何パーセント問題リスト.xlsx',index_col="index")
    st.session_state.ql = df.values.tolist()
    st.title('非常識をあぶりだすクイズ')
    st.session_state.idx = 0
    st.session_state.point = 0
    st.session_state.hp = 100
    question()


