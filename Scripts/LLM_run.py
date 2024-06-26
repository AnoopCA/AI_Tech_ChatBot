
#LLM-From-Scratch-For-ChatBots-GPT2

import torch
import sys
import tiktoken

sys.path.append(r'D:\ML_Projects\AI_Tech_ChatBot\Scripts')
from LLM_Finetune_Tiktoken import Head, MultiHeadAttention, FeedFoward, Block, GPTLanguageModel

device = 'cuda' if torch.cuda.is_available() else 'cpu'
tokenizer = tiktoken.get_encoding("cl100k_base")

model = torch.load(r'D:\ML_Projects\AI_Tech_ChatBot\Models\model-23_loss-0.181.pth')
#model = torch.load(r'D:\ML_Projects\AI_Tech_ChatBot\Models\model_checkpoints\model_temp_275_loss-1.209.pth')
model.eval()
model.to(device)

while True:
    prompt = input("Prompt (enter 'x' to exit):\n")
    if prompt.lower() == "x":
        break
    #prompt = " [SEP] Question: " + str(prompt) + " [SEP] Answer: "
    #prompt = " [SEP] " + prompt #+ " [SEP] "
    prompt = prompt + " [SEP] "
    context = torch.tensor(tokenizer.encode(prompt), dtype=torch.long, device=device)
    generated_chars = tokenizer.decode(model.generate(context.unsqueeze(0), max_new_tokens=250)[0].tolist())
    print(f'Generated text:\n{generated_chars}')
