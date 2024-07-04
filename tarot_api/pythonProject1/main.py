import random
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
from api_manager import api_key_manager

app = FastAPI()


class ChatRequest(BaseModel):
    question: str
    card: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/random-card")
def random_card():
    major_arcana = [
        "The Fool", "The Magician", "The High Priestess", "The Empress", "The Emperor",
        "The Hierophant", "The Lovers", "The Chariot", "Strength", "The Hermit",
        "Wheel of Fortune", "Justice", "The Hanged Man", "Death", "Temperance",
        "The Devil", "The Tower", "The Star", "The Moon", "The Sun",
        "Judgement", "The World"
    ]
    selected_card = random.choice(major_arcana)
    return {"card": selected_card}


@app.post("/chat")
def chat(request: ChatRequest):
    url = "https://api.groq.com/openai/v1/chat/completions"
    model_list = ["gemma-7b-it", "llama3-70b-8192", "llama3-8b-8192", "mixtral-8x7b-32768"]

    api_key_free, model = api_key_manager.get_key_and_model()

    headers = {
        "Authorization": f"Bearer {api_key_free.get_key()}",
        "Content-Type": "application/json"
    }

    data = {
        "messages": [
            {"role": "system", "content": "you are a Tarologist."},
            {"role": "user", "content": f"{request.question} with the meaning of {request.card} card"}
        ],
        "model": model_list[model],
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 429:
        spare_api_key, model = api_key_manager.get_spare_key_and_model()
        headers["Authorization"] = f"Bearer {spare_api_key.get_key()}"
        data["model"] = model_list[model]
        response = requests.post(url, headers=headers, json=data)
        spare_api_key.update_limits(response.headers, model=model)
        spare_api_key.increment_usage(model=model)
    else:
        api_key_free.update_limits(response.headers, model=model)
        api_key_free.increment_usage(model=model)

    if response.status_code == 429:
        raise HTTPException(status_code=429, detail="Rate limit exceeded")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to get response")

    return {"content": response.json()["choices"][0]["message"]["content"]}


# async def call_api_groq():
#     url = "https://api.groq.com/v1/chat/completions"  # Replace with your actual endpoint URL
#     headers = {
#         "Authorization": "Bearer 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",
#         "Content-Type": "application/json",
#     }
#     payload = {
#         "messages": [
#             {"role": "system", "content": "you are a Tarologist."},
#             {"role": "user", "content": "I want to know my future with the meaning of the hermit card"}
#         ],
#         "model": "llama3-8b-8192",
#         "temperature": 0.5,
#         "max_tokens": 1024,
#         "top_p": 1,
#         "stop": None,
#         "stream": True,
#     }
#
#     async with httpx.AsyncClient() as client:
#         try:
#             # First request to get headers
#             response = await client.post(url, json=payload, headers=headers)
#             if response.status_code != 200:
#                 raise HTTPException(status_code=response.status_code, detail="Failed to get initial response")
#
#             response_headers = dict(response.headers)
#
#             # Second request to stream content
#             async with client.stream("POST", url, json=payload, headers=headers) as stream_response:
#                 async for chunk in stream_response.aiter_text():
#                     yield chunk
#         except httpx.RequestError as e:
#             raise HTTPException(status_code=500, detail=str(e))
#
# @app.get("/stream-output")
# async def stream_output():
#     stream_response = call_api_groq()
#     headers = {
#         "x-ratelimit-limit-requests": "value",
#         # Add more headers from the initial response if needed
#     }
#     return StreamingResponse(stream_response, media_type="text/plain", headers=headers)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
