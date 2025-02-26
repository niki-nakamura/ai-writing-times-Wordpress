import streamlit as st
import openai
import os

# シークレットや環境変数からAPIキーを読み込む
openai.api_key = os.environ.get("DEEPSEEK_API_KEY")
openai.api_base = "https://api.deepseek.com/v1"  # DeepSeek APIエンドポイント

def generate_reader_needs(keyword):
    """
    入力されたKWに対して、読者ニーズのみをまとめてLLMから生成する。
    """
    # ChatGPT互換のChatCompletion APIを例とした場合
    prompt = f"""
    以下のキーワード「{keyword}」に興味を持つ読者が求めている具体的なニーズを、箇条書きで簡潔にまとめてください。
    回答は読者ニーズのみにフォーカスし、理由付けや詳細説明は不要です。
    必ず日本語で出力してください。
    """

    # 新しいライブラリの呼び出し方: openai.chat.completions.create
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",  # DeepSeek環境で利用できるモデルへ適宜置き換え
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=300,
        temperature=0.7,
    )

    # 応答テキストを抽出
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
