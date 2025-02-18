# app.py

import streamlit as st
import openai

# ▼ OpenAI APIキーを安全に管理するため、Streamlitの「Secrets」などを利用してください。
# openai.api_key = st.secrets["OPENAI_API_KEY"]  # 例: secrets.toml

st.title("AI記事作成ツール")
st.write("キーワードを入力すると、AIが記事の骨格や文章のサンプルを生成します。")

# ユーザーからのキーワード入力
keyword = st.text_input("キーワードまたはテーマを入力してください:")

# 「記事を生成」ボタン
if st.button("記事を生成"):
    if not keyword.strip():
        st.warning("キーワードを入力してください。")
    else:
        with st.spinner("AIが記事を作成中..."):
            try:
                # ChatGPT (gpt-3.5-turbo) へのリクエスト例
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "あなたは優秀なブログ記事ライターです。"
                                "指定されたキーワードに関するブログ記事のアウトラインと簡易本文を、"
                                "ユーザーに提案してください。"
                            )
                        },
                        {
                            "role": "user",
                            "content": f"キーワード: {keyword} について、ブログ記事を書いてください。"
                        },
                    ],
                    temperature=0.7,
                    max_tokens=800,
                )
                article_text = response["choices"][0]["message"]["content"]
                st.subheader("記事サンプル")
                st.write(article_text)

            except Exception as e:
                st.error(f"エラーが発生しました: {e}")
