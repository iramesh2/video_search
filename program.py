from openai import OpenAI
import os
from dotenv import load_dotenv


load_dotenv()
key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=key)

# Make sure to replace 'your_api_key_here' with your actual OpenAI API key

def chat_with_assistant(question):
    response = client.chat.completions.create(model="gpt-3.5-turbo-1106",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2021?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2021."},
        {"role": "user", "content": question}
    ])
    return response.choices[0].message.content

# Prompt the user to input a question
user_question = input("Please enter your question: ")
# Use the question in the chat_with_assistant function
answer = chat_with_assistant(user_question)
print(f"Answer: {answer}")