from src.database.repository import get_tasks  # Import function to fetch all tasks from the database
from src.core.scheduler import calculate_completion_percentage  # Import helper to compute the completion percentage


def get_progress_summary() -> dict:
    """Return a summary dict of the user's overall learning progress."""
    tasks = get_tasks()  # Load all tasks stored in the database

    total = len(tasks)  # Count the total number of tasks
    completed = sum(1 for t in tasks if t.completed)  # Count tasks where completed is True
    percentage = calculate_completion_percentage(tasks)  # Compute the overall completion percentage

    weeks = sorted(set(t.week for t in tasks))  # Build a sorted list of unique week numbers from all tasks
    week_summaries = []  # Empty list that will hold one summary dictionary per week

    for week in weeks:  # Loop through each unique week number
        week_tasks = [t for t in tasks if t.week == week]  # Filter tasks that belong to this week
        week_done = sum(1 for t in week_tasks if t.completed)  # Count completed tasks in this week
        week_summaries.append({  # Build a summary dictionary for this week and add it to the list
            "week": week,  # The week number (e.g. 1, 2, 3)
            "total": len(week_tasks),  # Total number of tasks in this week
            "completed": week_done,  # How many tasks in this week are completed
        })

    return {  # Return the full progress summary as a single dictionary
        "total": total,  # Total tasks across all weeks
        "completed": completed,  # Total completed tasks across all weeks
        "percentage": percentage,  # Overall completion percentage (0.0 – 100.0)
        "weeks": week_summaries,  # List of per-week breakdown dictionaries
    }
