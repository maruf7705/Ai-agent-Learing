from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Create an OpenAI client instance with the API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_text_basic(prompt: str, model="gpt-4o-mini", system_prompt="You are a helpful AI assistant"):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {str(e)}"
