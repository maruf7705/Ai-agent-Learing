from openai improt openai
import os
from dotenv import load_dotenv

load_dotenv()
# Set the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")
# Function to get a response from OpenAI's GPT-3.5 Turbo model
def get_gpt_response(prompt):

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-1106-preview",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Hello, who are you?"}
            ],
            temperature=0.7,
            max_tokens=150
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        print(f"Error: {e}")
        return None

response = openai.chat.completions.create(
    model="gpt-4-1106-preview",  # Use the correct model name for GPT-4.1
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, who are you?"}
    ]
)

print(response.choices[0].message.content)
