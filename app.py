import streamlit as st
import openai
import os

# openai.api_key の行は削除し、api_base だけ設定
openai.api_base = "https://api.deepseek.com/v1"

def generate_reader_needs(keyword):
    """
    入力されたKWに対して、読者ニーズのみをまとめてLLMから生成する。
    """
    prompt = f"以下のキーワード「{keyword}」に興味を持つ読者が..."
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300,
        temperature=0.7,
    )
    return response.choices[0].message["content"]

def main():
    st.title("KW向け読者ニーズ自動生成ツール")
    keyword = st.text_input("キーワードを入力してください")

    if st.button("読者ニーズを生成"):
        if not keyword:
            st.warning("キーワードを入力してください")
        else:
            with st.spinner("読者ニーズを生成中..."):
                needs = generate_reader_needs(keyword)
            st.write("### 読者ニーズ")
            st.write(needs)

if __name__ == "__main__":
    main()
