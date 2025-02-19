# -*- coding: utf-8 -*-
import streamlit as st
import openai  # 公式 OpenAI or scaleway-labs の openai を想定

st.title("AI記事作成ツール (Scaleway DeepSeek-R1)")

# 1) Secrets から APIキー取得
SCW_API_KEY = st.secrets["DEEPSEEK_API_KEY"]

# 2) OpenAI(client) 形式で初期化
openai.api_base = "https://api.scaleway.ai/af81c82e-508d-4d91-ba6b-5d4a9e1bb8d5/v1"
openai.api_key = SCW_API_KEY   # これで "Authorization: Bearer ..." が自動付与される想定

# 3) ユーザー入力
keyword = st.text_input("キーワードまたはテーマを入力してください:")

if st.button("記事を生成"):
    if not keyword.strip():
        st.warning("キーワードを入力してください。")
    else:
        with st.spinner("LLMを呼び出しています..."):
            try:
                # Playgroundのコード例にほぼ合わせる
                response = openai.ChatCompletion.create(
                    model="deepseek-r1",  # 必要なら "deepseek/deepseek-r1-distill-llama-8b:fp8"
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {
                            "role": "user",
                            "content": f"キーワード: {keyword}\n\n日本語でブログ記事を書いてください。"
                        },
                    ],
                    max_tokens=512,
                    temperature=0.6,
                    top_p=0.95,
                    presence_penalty=0,
                    stream=False,
                )
                # 通常レスポンス(ストリーム=False)なら .choices[0].message.content にテキストが格納
                text = response.choices[0].message.content
                st.write("## 記事サンプル")
                st.write(text)

            except Exception as e:
                st.error(f"エラー: {e}")
