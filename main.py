import os
from groq import Groq

client = Groq(api_key="")

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "",
        }
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)