from openai import OpenAI
from tqdm import tqdm
import random

#Key should be retrieved from https://build.nvidia.com/
key = "Key-costs-money"

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=key
)

user_prompt ="""
Let's play rock, paper, scissors. I have made my choice. Now, you should make your choice. 
    What do you play? Choose your choice first in valid Python code.

"""
print(f"prompt: {user_prompt}")

#"Let’s play matching pennies. I have made my choice. Now, youshould make your choice. Use Python" # "What is the mixed strategy Nash equilibrium for the matching pennies game?"
text = ""
seed = random.randint(1, 100000000)
completion = client.chat.completions.create(
    model="mistralai/mistral-7b-instruct-v0.3",
    messages=[{"role": "user", "content": user_prompt}],
    max_tokens=1024,
    stream=True,
    seed=seed
)
for chunk in completion:
    if chunk.choices[0].delta.content is not None:
        text += chunk.choices[0].delta.content

print(text)