import transformers
from time import time 


# model_id = "maum-ai/Llama-3-MAAL-8B-Instruct-v0.1"
model_id = "mistralai/Mistral-7B-v0.1"
model = transformers.AutoModelForCausalLM.from_pretrained(model_id).to("cuda")
tokenizer = transformers.AutoTokenizer.from_pretrained(model_id)
streamer = transformers.TextStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)

# we recommend using the fixed prompt for the model unless you fine-tune it
prompt = "너는 마음에이아이의 챗봇 MAAL이다. 고객의 질문에 친절하게 답하여라."
instruction = "사과 한 박스에는 사과가 30개 들어있는데, 처음에는 사과 3박스가 있었고, 내가 사과 5개를 먹었어. 남은 사과는 총 몇개야?"

messages = [
    {"role": "system", "content": f"{prompt}"},
    {"role": "user", "content": f"{instruction}"}
    ]

inputs = tokenizer.apply_chat_template(
    messages,
    tokenize=True,
    return_tensors='pt').to("cuda")

t1 = time()
outputs = model.generate(inputs, streamer=streamer, max_new_tokens=1024, pad_token_id=tokenizer.eos_token_id)
t2 = time()

num_tokens = len(outputs[0])
print(f"tokens per second = {num_tokens / (t2-t1)}")
