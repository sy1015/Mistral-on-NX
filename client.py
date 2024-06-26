import requests
import json


prompt = "너는 마음에이아이의 챗봇 MAAL이다. 고객의 질문에 친절하게 답하여라."
instruction = "사과 한 박스에는 사과가 30개 들어있는데, 처음에는 사과 3박스가 있었고, 내가 사과 5개를 먹었어. 남은 사과는 총 몇개야?"
messages = [
    #{"role": "system", "content": f"{prompt}"},
    {"role": "user", "content": f"{instruction}"}
    ]


# Get a response using a prompt without streaming
payload = {
   "model": "dist/Llama-3-MAAL-8B-Instruct-v0.1-q4f32-MLC/",
   "messages": messages,
   "stream": False,
   "stop": ['<|end_of_text|>', '<|eot_id|>'],
}
r = requests.post("http://127.0.0.1:8000/v1/chat/completions", json=payload)
print(f"Without streaming:\n{r.json()['choices'][0]['message']['content']}\n")

# Get the latest runtime stats
r = requests.get("http://127.0.0.1:8000/stats")
print(f"Runtime stats: {r.json()}\n")

# Reset the chat
r = requests.post("http://127.0.0.1:8000/chat/reset", json=payload)
print(f"Reset chat: {str(r)}\n")


# Get a response using a prompt with streaming
payload = {
   "model": "dist/Llama-3-MAAL-8B-Instruct-v0.1-q4f32-MLC/",
   "messages": messages,
   "stream": True,
   "stop": ['<|end_of_text|>', '<|eot_id|>'],
}
with requests.post("http://127.0.0.1:8000/v1/chat/completions", json=payload, stream=True) as r:
   print(f"With streaming:")
   for chunk in r:
      content = json.loads(chunk[6:-2])["choices"][0]["delta"].get("content", "")
      print(f"{content}", end="", flush=True)
   print("\n")

# Get the latest runtime stats
r = requests.get("http://127.0.0.1:8000/stats")
print(f"Runtime stats: {r.json()}\n")
