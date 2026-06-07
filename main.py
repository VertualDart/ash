import requests
url = "http://localhost:11434/api/chat"

messages = []

while True:
    user_input = input("You: ")

    if user_input.lower() in ["quit", "exit"]:
        break

    messages.append({
        "role": "user",
        "content": user_input
    })

    payload = {
        "model": "qwen3.5:4b",
        "messages": messages,
        "stream": False
    }

    response = requests.post(url, json=payload)
    assistant_reply = response.json()["message"]["content"]

    print("Qwen", assistant_reply)

    messages.append({
        "role": "assistant",
        "content": assistant_reply
    })