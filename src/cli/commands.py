import typer  # Typer makes it easy to build command-line interfaces (CLIs) in Python
from rich.console import Console  # Console lets us print styled, colorful text to the terminal
from src.ai.planner import generate_learning_plan  # Function that calls the AI to create a learning plan
from src.ai.mentor import ask_mentor  # Function that sends a question to the AI mentor
from src.database.repository import save_tasks, get_tasks, complete_task  # Database helpers for task management

app = typer.Typer()  # Create the main CLI application object that manages all commands
console = Console()  # Create a console object for printing styled output to the terminal


@app.command()  # Register the function below as a CLI command; the command name is "create-plan"
def create_plan():  # Called when the user runs: python main.py create-plan
    skill = typer.prompt("What skill do you want to learn?")  # Pause and ask the user to type the skill name
    level = typer.prompt("Current level")  # Ask for the user's current experience level (e.g. "beginner")
    hours = typer.prompt("Hours per week", type=int)  # Ask how many hours per week; type=int ensures it's a number
    months = typer.prompt("Target duration in months", type=int)  # Ask for plan length; must be an integer

    plan = generate_learning_plan(skill, level, hours, months)  # Call the AI to generate a list of weekly tasks

    save_tasks(plan)  # Persist all the generated tasks to the SQLite database

    console.print("\n[green]Learning Plan Generated Successfully![/green]\n")  # Print a green success message

    for task in plan:  # Loop through each task dictionary in the plan
        console.print(f"Week {task['week']}: {task['title']}")  # Print the week number and task title


@app.command()  # Register this function as the "progress" CLI command
def progress():  # Called when the user runs: python main.py progress
    tasks = get_tasks()  # Fetch all tasks stored in the database

    completed = sum(task.completed for task in tasks)  # Count how many tasks have completed == True
    total = len(tasks)  # Total number of tasks in the database

    console.print(f"Completed {completed}/{total} tasks")  # Show completed vs total count

    for task in tasks:  # Loop through every task to show its status
        status = "✅" if task.completed else "❌"  # Pick a checkmark emoji if done, otherwise an X
        console.print(f"{status} {task.id}. {task.title}")  # Print the icon, task ID, and title


@app.command()  # Register this function as the "complete" CLI command
def complete(task_id: int):  # Called as: python main.py complete 3  (the number is the task's ID)
    complete_task(task_id)  # Update the task in the database to mark it as completed
    console.print("[green]Task completed![/green]")  # Confirm success to the user with a green message


@app.command()  # Register this function as the "ask" CLI command
def ask(question: str):  # Called as: python main.py ask "How do I learn recursion?"
    answer = ask_mentor(question)  # Send the question to the AI and wait for the response
    console.print(f"\n[cyan]{answer}[/cyan]\n")  # Print the answer in cyan color with blank lines around it
