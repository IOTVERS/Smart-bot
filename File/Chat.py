import openai

openai.api_key = "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" # Enter your API Key here 

message_history = []

def chat(inp, role="user"):

    message_history.append({"role": role, "content": inp})

    completion = openai.ChatCompletion.create(

        model = "gpt-3.5-turbo", # gpt version 

        messages=message_history,

    )

    reply_content = completion.choices[0].message.content # It will simplify the output 

    Print(reply_content)

    message_history.append({"role": "assistant", "content": reply_content})  # For storing your massage history 

    return reply_content

for i in range(2):

    user_input=input(">>> ")

    print("User's input was", user_input)

    print()

    chat(user_input)
