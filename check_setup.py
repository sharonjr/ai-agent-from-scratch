from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-5.4-mini",
    messages=[{"role": "user", "content": "Say hello in Malayalam, in five words or fewer."}],
)
print(response.choices[0].message.content)
print(response.usage)
