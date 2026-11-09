import os
from openai import OpenAI

def summarize_log(log_text):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "Summarize build logs. Identify the error, cause and solution in simple language."
            },
            {
                "role": "user",
                "content": log_text
            }
        ]
    )

    return response.choices[0].message.content


with open("sample_build.log", "r") as file:
    log = file.read()

print(summarize_log(log))
