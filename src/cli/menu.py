from rich.console import Console  # Console allows printing styled text to the terminal
from rich.table import Table  # Table renders data as a formatted grid in the terminal
from rich.panel import Panel  # Panel wraps content inside a bordered box

console = Console()  # Create a single shared console instance used by both functions below


def display_welcome():  # Function that prints the welcome banner when the src starts
    console.print(Panel.fit(  # Print a panel that automatically sizes itself to fit its content
        "[bold cyan]Welcome to SkillForge AI[/bold cyan]\n"  # Bold cyan title displayed inside the panel
        "[dim]Your personalized CLI learning assistant[/dim]",  # Dimmed subtitle shown below the title
        border_style="cyan"  # Set the color of the panel's border to cyan
    ))


def display_commands():  # Function that prints a table listing all available CLI commands
    table = Table(title="Available Commands", border_style="cyan")  # Create a table with a title and cyan borders

    table.add_column("Command", style="bold green")  # First column shows command names in bold green
    table.add_column("Description", style="white")  # Second column shows descriptions in plain white

    table.add_row("create-plan", "Generate a new personalized learning plan")  # Row for create-plan command
    table.add_row("progress",    "View your current learning progress")  # Row for progress command
    table.add_row("complete",    "Mark a task as completed (e.g. complete 3)")  # Row for complete command
    table.add_row("ask",         "Ask the AI mentor a question")  # Row for ask command

    console.print(table)  # Render and display the completed table in the terminal
