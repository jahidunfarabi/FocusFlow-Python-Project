import sys
from rich.console import Console
from rich.table import Table
from storage import Storage
from manager import TaskManager

# Initialize components
console = Console()
storage = Storage("tasks.json")
# Load existing data into the manager [cite: 9]
manager = TaskManager(storage.load_tasks())

def display_menu():
    """Prints a professional menu using the rich library[cite: 44, 46]."""
    console.print("\n[bold cyan]🎯 Focus-Flow: Priority Task Manager[/bold cyan]")
    console.print("1. [green]Add New Task[/green]")
    console.print("2. [blue]View Sorted Tasks[/blue]")
    console.print("3. [yellow]Search Tasks[/yellow]")
    console.print("4. [red]Delete Task[/red]")
    console.print("5. [magenta]View Summary Report[/magenta]")
    console.print("6. [white]Exit & Save[/white]")

def main():
    """Main loop for the menu-driven interface[cite: 46]."""
    while True:
        display_menu()
        choice = input("\nSelect an option (1-6): ")

        if choice == '1':
            title = input("Enter Task Title: ")
            try:
                # Validation: Handle invalid numbers gracefully [cite: 12]
                urg = int(input("Enter Urgency (1-5): "))
                imp = int(input("Enter Importance (1-5): "))
                if 1 <= urg <= 5 and 1 <= imp <= 5:
                    manager.add_task(title, urg, imp)
                    console.print("[bold green]✔ Task added successfully![/bold green]")
                else:
                    console.print("[bold red]Error: Ratings must be between 1 and 5.[/bold red]")
            except ValueError:
                console.print("[bold red]Invalid input! Please enter numbers only.[/bold red]")

        elif choice == '2':
            tasks = manager.get_sorted_tasks()
            if not tasks:
                console.print("[yellow]No tasks found.[/yellow]")
                continue

            table = Table(title="Priority Task List")
            table.add_column("ID", justify="center", style="cyan")
            table.add_column("Task Name", style="white")
            table.add_column("Score", justify="right", style="bold green")
            
            for t in tasks:
                table.add_row(str(t.task_id), t.title, str(t.priority_score))
            console.print(table)

        elif choice == '3':
            query = input("Search for: ")
            results = manager.search_tasks(query)
            if not results:
                console.print("[yellow]No matching tasks found.[/yellow]") # [cite: 12]
            else:
                for r in results:
                    console.print(f"- [cyan][ID: {r.task_id}][/cyan] {r.title}")

        elif choice == '4':
            try:
                tid = int(input("Enter Task ID to delete: "))
                if manager.delete_task(tid):
                    console.print("[bold green]Task deleted.[/bold green]")
                else:
                    console.print("[bold red]ID not found.[/bold red]")
            except ValueError:
                console.print("[bold red]Invalid ID format.[/bold red]")

        elif choice == '5':
            # Fixing the unpacking error from image_76a5cc.png
            report = manager.get_summary_report()
            console.print("\n[bold magenta]📊 Productivity Summary[/bold magenta]")
            console.print(f"Total Tasks: {report['total']}")
            console.print(f"High Priority Tasks: {report['high_priority']}")
            console.print(f"Avg Priority Score: {report['average_score']}")

        elif choice == '6':
            # Save data before exiting [cite: 9, 60]
            storage.save_tasks(manager.tasks)
            console.print("[bold green]Data saved. Have a productive day![/bold green]")
            sys.exit()
        else:
            console.print("[red]Invalid choice, please try again.[/red]")

if __name__ == "__main__":
    main()