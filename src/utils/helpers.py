from rich.console import Console  # Console lets us print styled, colorful text to the terminal
from rich.table import Table  # Table renders structured data as a formatted grid in the terminal

console = Console()  # Create a shared console instance used by all functions in this file


def print_task_table(tasks) -> None:
    """Render tasks as a Rich table in the terminal."""
    table = Table(title="Learning Tasks", border_style="cyan")  # Create a table with a title and cyan borders

    table.add_column("ID",     style="dim",          width=5)   # ID column: dimmed text, fixed 5-char width
    table.add_column("Week",   style="bold magenta",  width=6)  # Week column: bold magenta, fixed 6-char width
    table.add_column("Title",  style="white")                   # Title column: white text, auto width
    table.add_column("Status", style="bold",          width=10) # Status column: bold text, fixed 10-char width

    for task in tasks:  # Loop through each task object to add it as a row in the table
        status = "[green]✅ Done[/green]" if task.completed else "[red]❌ Todo[/red]"  # Green if done, red if not
        table.add_row(str(task.id), str(task.week), task.title, status)  # Add one row with all task fields

    console.print(table)  # Render and display the completed table in the terminal


def validate_positive_int(value: int, field_name: str) -> int:
    """Raise ValueError if value is not a positive integer."""
    if value <= 0:  # Zero or negative numbers are invalid for things like hours or months
        raise ValueError(f"{field_name} must be a positive integer, got {value}.")  # Raise a clear error message
    return value  # If the value is valid, return it unchanged so the caller can use it


def truncate(text: str, max_length: int = 80) -> str:
    """Truncate a string to max_length, appending '…' if needed."""
    return text if len(text) <= max_length else text[:max_length - 1] + "…"  # Cut the text and add ellipsis if too long
