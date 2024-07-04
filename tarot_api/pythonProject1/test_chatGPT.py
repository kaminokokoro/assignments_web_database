import asyncio
import os

from groq import Groq

# client = Groq(
#     # This is the default and can be omitted
#     # api_key=os.environ.get("GROQ_API_KEY"),
#     api_key="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",
# )
#
# chat_completion = client.chat.completions.create(
#     messages=[
#         {
#             "role": "system",
#             "content": "you are a Tarologist."
#         },
#         {
#             "role": "user",
#             "content": "i want to know my future with the meaning of the hermit card",
#         }
#     ],
#     model="gemma-7b-it",
# )
#
# # print(chat_completion.id)
# print(chat_completion.choices[0].message.content)

import requests
import json

headers = {
    "Authorization": "Bearer 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",
    "Content-Type": "application/json"
}

data = {
    "messages": [
        {
            "role": "system",
            "content": "you are a Tarologist."
        },
        {
            "role": "user",
            "content": "i want to know my future with the meaning of the hermit card"
        }
    ],
    "model": "llama3-8b-8192",
    "stream": True
}

url = "https://api.groq.com/openai/v1/chat/completions"

# Sử dụng stream=True để cho phép streaming dữ liệu từ phản hồi
for i in range(100):
    response = requests.post(url, headers=headers, json=data, stream=True)

    # Xử lý dữ liệu nhận được từ phản hồi
    # print("Streaming Output - Content:")
    # for chunk in response.iter_content(chunk_size=1024):
    #     if chunk:
    #         # Giải mã chunk nhận được từ phản hồi
    #         decoded_chunk = chunk
    #         print(decoded_chunk)



    # In ra tất cả headers của phản hồi
    print("Response Headers:")
    for header, value in response.headers.items():
        print(f"{header}: {value}")

# Nếu không cần giải mã và in ra, bạn có thể xử lý chunk nhận được dưới dạng raw data
# for chunk in response.iter_content(chunk_size=1024):
#     if chunk:
#         process_chunk(chunk)







