curl https://api.scaleway.ai/af81c82e-508d-4d91-ba6b-5d4a9e1bb8d5/v1/chat/completions \
     -H "Authorization: Bearer c3f74df4-9888-42e7-bf1f-ac2bae2b941e" \
     -H "Content-Type: application/json" \
     -d '{
       "model": "deepseek-r1",
       "messages": [
         {"role": "system", "content": "システムメッセージ"},
         {"role": "user", "content": "ユーザーメッセージ"}
       ],
       "max_tokens": 100
     }'
