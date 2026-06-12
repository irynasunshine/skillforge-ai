LEARNING_PLAN_PROMPT = """
You are an expert learning coach.

Create a personalized learning roadmap.

Skill: {skill}
Current Level: {level}
Weekly Hours: {hours}
Duration: {months} months

Return a weekly learning plan.

Format:
Week 1:
- topic
- task
- resource
"""
# ^ Multi-line string used as the AI prompt template for generating learning plans.
# The {skill}, {level}, {hours}, and {months} placeholders are filled in at runtime
# using Python's .format() method before the prompt is sent to the AI.
# The "Week N:" and "- item" format tells the AI how to structure its response
# so that planner.py can parse the output line by line.


MENTOR_PROMPT = """
You are a helpful AI mentor.

Answer clearly and simply.

Question:
{question}
"""
# ^ Multi-line string used as the AI prompt template for answering user questions.
# The {question} placeholder is replaced with the user's actual question at runtime.
# The instructions ("Answer clearly and simply") guide the AI's tone and style.
