from openai import OpenAI
client = OpenAI(api_key="sk-proj-WxS17ehGk2PnwmzCHcDwT3BlbkFJFMj6bYTk9jG1bqZaFTcj",)

ompletion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are TITAN assistant."},
        {
            "role": "user",
            "content": "What is coding"
        }
    ]
)

print(completion.choices[0].message)