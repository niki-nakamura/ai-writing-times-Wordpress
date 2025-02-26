import streamlit as st
import openai
import os

# いったん削除・またはコメントアウト:
# openai.api_key = os.environ.get("DEEPSEEK_API_KEY")
openai.api_base = "https://api.deepseek.com/v1"

def generate_reader_needs(keyword):
    ...
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300,
        temperature=0.7,
    )
    return response.choices[0].message["content"]
