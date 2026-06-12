import os  # os lets us read environment variables (secret keys stored outside the code)
from groq import Groq  # Groq is the AI provider; this imports its Python client library
from dotenv import load_dotenv  # load_dotenv reads a .env file and makes its values available via os.getenv
from src.ai.prompts import MENTOR_PROMPT  # Import the pre-written mentor prompt template

load_dotenv()  # Load variables from the .env file so os.getenv() can find them

client = Groq(api_key=os.getenv("GROQ_API_KEY"))  # Create a Groq AI client using the API key from the environment


def ask_mentor(question):  # Function that sends a question to the AI mentor and returns the answer
    prompt = MENTOR_PROMPT.format(question=question)  # Fill in the {question} placeholder inside the prompt template

    response = client.chat.completions.create(  # Send the prompt to the AI model and wait for a response
        model="llama-3.3-70b-versatile",  # The name of the AI model we want to use
        messages=[  # A list of messages to send (like a conversation history)
            {
                "role": "user",  # "user" means this message comes from the human side
                "content": prompt  # The actual text content of the message
            }
        ]
    )
    answer = response.choices[0].message.content  # Extract the text from the first response choice
    return answer  # Send the answer back to whoever called this function
