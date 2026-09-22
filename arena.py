import requests


API_KEY = "f30b6d08710e99d314580a0a14d200ce"


URL = "https://api.kie.ai/codex/v1/responses"


# Store conversation history
conversation = []


print("🤖 GPT-6 Astra Chatbot")
print("Type 'exit' to quit\n")




def ask_gpt(message):


    # Add user message to conversation
    conversation.append({
        "role": "user",
        "content": [
            {
                "type": "input_text",
                "text": message
            }
        ]
    })


    payload = {
        "model": "gpt-6-astra",


        "input": conversation,


        "stream": False,


        "reasoning": {
            "effort": "medium"
        }
    }


    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }


    try:


        response = requests.post(
            URL,
            headers=headers,
            json=payload
        )


        response.raise_for_status()


        data = response.json()


        # Find assistant response
        assistant_message = ""


        for item in data.get("output", []):


            if item.get("type") == "message":


                for content in item.get("content", []):


                    if content.get("type") == "output_text":


                        assistant_message += content.get(
                            "text",
                            ""
                        )


        # Save assistant response to memory
        conversation.append({
            "role": "assistant",
            "content": [
                {
                    "type": "output_text",
                    "text": assistant_message
                }
            ]
        })


        return assistant_message


    except Exception as e:
        return f"Error: {e}"




# Chat loop
while True:


    user_message = input("You: ")


    if user_message.lower() in ["exit", "quit", "bye"]:
        print("Bot: Goodbye! 👋")
        break


    print("\nBot is thinking...\n")


    answer = ask_gpt(user_message)


    print("GPT-6 Astra:", answer)
    print()
