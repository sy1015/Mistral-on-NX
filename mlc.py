from mlc_chat import ChatModule, ConvConfig, ChatConfig
from mlc_chat.callback import StreamToStdout
import transformers

conv_config = ConvConfig(
    name='MAAL',
    system='<|start_header_id|>system<|end_header_id|>\n\n너는 마음에이아이의 챗봇 MAAL이다. 고객의 질문에 친절하게 답하여라.<|eot_id|>',
    roles=['<|start_header_id|>system<|end_header_id|>', '<|start_header_id|>user<|end_header_id|>', '<|start_header_id|>assistant<|end_header_id|>'],
    messages= [],
    offset = 0,
    separator_style=0,
    seps=['<|eot_id|>', '<|eot_id|>'],
    role_msg_sep='\n\n',
    role_empty_sep='\n\n',
    stop_tokens=[128001, 128009], # <|end_of_text|>, <|eot_id|>
    stop_str='<|eot_id|>',
    add_bos=True
)
chat_config = ChatConfig(
    conv_config=conv_config
)

# Create a ChatModule instance
cm = ChatModule(
    model="dist/Llama-3-MAAL-8B-Instruct-v0.1-q4f32-MLC",
    model_lib_path="dist/libs/Llama-3-MAAL-8B-Instruct-v0.1-q4f32-cuda.so",
    chat_config=chat_config,
)

tokenizer = transformers.AutoTokenizer.from_pretrained('./Llama-3-MAAL-8B-Instruct-v0.1')
# we recommend using the fixed prompt for the model unless you fine-tune it
prompt = "너는 마음에이아이의 챗봇 MAAL이다. 고객의 질문에 친절하게 답하여라."
instruction = "사과 한 박스에는 사과가 30개 들어있는데, 처음에는 사과 3박스가 있었고, 내가 사과 5개를 먹었어. 남은 사과는 총 몇개야?"
messages = [
    {"role": "system", "content": f"{prompt}"},
    {"role": "user", "content": f"{instruction}"}
    ]

inputs = tokenizer.apply_chat_template(messages, tokenize=False)

# Generate a response for a given prompt
output = cm.generate(
    prompt=inputs,
    progress_callback=StreamToStdout(callback_interval=2),
)

# Print prefill and decode performance statistics
print(f"Statistics: {cm.stats()}\n")

# Reset the chat module by
# cm.reset_chat()
