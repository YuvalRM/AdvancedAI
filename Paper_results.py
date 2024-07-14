from openai import OpenAI
from tqdm import tqdm
import random

#Key should be retrieved from https://build.nvidia.com/
key = "Key-costs-money"

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=key
)

part = 1

user_prompt_part_1 = (
    "Respond to the following text with one of the following answers:"
    "‘heads’, ‘tails’. Provide your response in JSON format containing a single"
    "key ‘answer’. Text: Let’s play matching pennies. I have made my choice."
    "Now, you should make your choice. What do you play?"
)

user_prompt_part_2 = (
    "Respond to the following text with one of the following answers: `rock`, `paper`, `scissors`. "
    "Provide your response in JSON format containing a single key `answer`. "
    "**Text**: ```Let's play rock, paper, scissors. I have made my choice. Now, you should make your choice. What do "
    "you play?```"
)

if part == 1:
    user_prompt = user_prompt_part_1
else:
    user_prompt = user_prompt_part_2

with open(f"results_{part}.txt", "w") as file:
    for i in tqdm(range(1000)):
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
        text += "\n"
        file.write(text)




