import streamlit as st
import requests

# ▼ Scaleway (deepseek-r1) 用の設定
SCW_API_KEY = st.secrets["DEEPSEEK_API_KEY"]  # 例: secrets.toml で {"DEEPSEEK_API_KEY": "XXXXXXX"}

# Scaleway LLM APIエンドポイント
SCW_BASE_URL = "https://api.scaleway.ai/af81c82e-508d-4d91-ba6b-5d4a9e1bb8d5/v1"
SCW_MODEL_NAME = "deepseek-r1"

def call_deepseek_llm(system_msg: str, user_msg: str, max_tokens: int = 800) -> str:
    """Scalewayのdeepseek-r1モデルを呼び出し、LLM応答を返す"""
    url = f"{SCW_BASE_URL}/chat/completions"
    payload = {
        "model": SCW_MODEL_NAME,
        "messages": [
            {"role": "system", "content": system_msg},
            {"role": "user", "content": user_msg},
        ],
        "max_tokens": max_tokens,
        "temperature": 0.7,
        "top_p": 0.95,
        "presence_penalty": 0,
        "stream": False,
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {SCW_API_KEY}",
    }

    resp = requests.post(url, headers=headers, json=payload)
    if resp.status_code != 200:
        return f"APIエラー: {resp.status_code} {resp.text}"

    data = resp.json()
    if not data.get("choices"):
        return f"(LLM応答なし)\n{data}"

    return data["choices"][0]["message"]["content"]


# ----------------------------
# Streamlitアプリ本体
# ----------------------------

st.title("AI記事作成ツール")
st.write("キーワードを入力すると、LLM（大規模言語モデル）が記事の骨格やサンプル文章を生成します。")

# ユーザー入力欄
keyword = st.text_input("キーワードまたはテーマを入力してください:")

if st.button("記事を生成"):
    if not keyword.strip():
        st.warning("キーワードを入力してください。")
    else:
        with st.spinner("記事を生成中 (deepseek-r1)..."):
            try:
                # systemメッセージ（方針設定）
                system_msg = (
                    "あなたは優秀なブログ記事ライターです。"
                    "ユーザーが入力したキーワードをもとに、"
                    "日本語で記事のアウトラインや簡易本文を提案してください。"
                )
                # userメッセージ（実際のリクエスト内容）
                user_msg = f"キーワード: {keyword}\n\n" \
                           "上記テーマでブログ記事を書いてください。日本語で。"

                # deepseek-r1で生成
                result_text = call_deepseek_llm(system_msg, user_msg, max_tokens=800)

                st.subheader("記事サンプル")
                st.write(result_text)

            except Exception as e:
                st.error(f"エラーが発生しました: {e}")
