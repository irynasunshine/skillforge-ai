import os  # Provides access to environment variables like secret API keys
from groq import Groq  # Groq AI client library for making API calls
from dotenv import load_dotenv  # Reads the .env file to load secret keys into the environment
from src.ai.prompts import LEARNING_PLAN_PROMPT  # Import the prompt template for generating plans

load_dotenv()  # Load secrets (like the API key) from the .env file

client = Groq(api_key=os.getenv("GROQ_API_KEY"))  # Connect to the Groq API using the stored key


def generate_learning_plan(skill, level, hours, months):  # Generates a weekly learning plan using the AI
    prompt = LEARNING_PLAN_PROMPT.format(  # Build the final prompt by inserting user values into the template
        skill=skill,  # The skill the user wants to learn (e.g. "Python")
        level=level,  # The user's current experience level (e.g. "beginner")
        hours=hours,  # How many hours per week the user can study
        months=months  # How many months the learning plan should span
    )

    response = client.chat.completions.create(  # Ask the AI model to generate a response for the prompt
        model="llama-3.3-70b-versatile",  # Name of the AI model to use
        messages=[  # List of messages forming the conversation context
            {
                "role": "user",  # This message is from the user
                "content": prompt  # The actual prompt text we built above
            }
        ]
    )

    content = response.choices[0].message.content  # Get the AI's text response as a plain string

    tasks = []  # Start with an empty list that will hold each parsed learning task

    current_week = 1  # Begin counting from week 1

    for line in content.splitlines():  # Go through each line of the AI response one at a time
        if line.startswith("-"):  # Lines starting with "-" are task items in the AI's formatted output
            tasks.append({  # Add a new task dictionary to the list
                "week": current_week,  # Record which week this task belongs to
                "title": line.replace("-", "").strip()  # Remove the leading dash and trim extra whitespace
            })

        if line.lower().startswith("week"):  # Lines starting with "week" mark the beginning of a new week section
            try:  # Try to parse the week number; may fail if the format is unexpected
                current_week = int(line.split()[1].replace(":", ""))  # Extract the number from e.g. "Week 2:"
            except:  # If parsing fails for any reason, silently continue with the current week number
                pass

    return tasks  # Return the final list of task dictionaries
