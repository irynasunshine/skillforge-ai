from typing import List, Dict  # Type hints that make function signatures easier to read and understand


def distribute_tasks_by_week(tasks: List[Dict], total_weeks: int) -> List[Dict]:
    """Distribute tasks evenly across the total number of weeks."""
    if not tasks:  # If the task list is empty there is nothing to distribute
        return []  # Return an empty list immediately to avoid further processing

    tasks_per_week = max(1, len(tasks) // total_weeks)  # Calculate tasks per week; at least 1 to avoid zero

    for i, task in enumerate(tasks):  # Loop through tasks along with their index position (0, 1, 2, ...)
        task["week"] = (i // tasks_per_week) + 1  # Assign a week number; +1 because weeks start at 1 not 0

    return tasks  # Return the updated task list with "week" keys filled in


def get_current_week_tasks(tasks, current_week: int) -> List:
    """Return only tasks belonging to the given week."""
    return [t for t in tasks if t.week == current_week]  # Keep only tasks whose week number matches the target week


def calculate_completion_percentage(tasks) -> float:
    """Return the percentage of completed tasks."""
    if not tasks:  # Guard against an empty list to prevent dividing by zero
        return 0.0  # Return 0% when there are no tasks at all
    completed = sum(1 for t in tasks if t.completed)  # Count tasks where the completed flag is True
    return round((completed / len(tasks)) * 100, 2)  # Divide completed by total, scale to percent, round to 2 decimals
