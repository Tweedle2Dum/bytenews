import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
def generate_summary(text):
    #openai.api_key = os.getenv("OPENAI_API_KEY")
    
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=f"Summarize this in less than 70 words:\n\n{text}",
      temperature=0.7,
      max_tokens=64,
      top_p=1.0,
      frequency_penalty=0.0,
      presence_penalty=0.0
    )
    return response.choices[0].text
r=generate_summary('''
BLOOM is an open-access multilingual language model that contains 176 billion parameters and was trained for 3.5 months on 384 A100–80GB GPUs. A BLOOM checkpoint takes 330 GB of disk space, so it seems unfeasible to run this model on a desktop computer. However, you just need enough disk space, at least 16GB of RAM, and some patience (you don't even need a GPU), to run this model on your computer.
''')
print(r)