# To-Do List Command Line Application
A simple command-line Python application to manage to-do tasks. This program allows users to add, list, complete, unmark, and remove tasks stored in a tasks.txt file.

# Features
- Add Tasks: Add new tasks to tasks.txt.
- List Tasks: View all tasks with each task numbered.
- Complete Tasks: Mark specific tasks as completed.
- Remove Tasks: Delete specific tasks from the list.
- Unmark Tasks: Revert completed tasks to incomplete status.

# Usage
Run the program with one of the following arguments:

- No Argument: Creates **tasks.txt** if it doesn’t exist, displays a welcome message.
- **-a "task"**: Adds a new task to the list.
- **-l**: Lists all tasks with their statuses.
- **-r index**: Removes the task at the specified index.
- **-c index**: Marks the task at the specified index as completed.
- **-z index**: Unmarks the completed task at the specified index.

# Error Handling
- Handles file creation if tasks.txt is missing.
- Checks for invalid inputs (e.g., out-of-bounds indices, non-integer values).

# File Structure
- tasks.txt: Stores tasks with [ ] for incomplete and [X] for complete status.
- Main Script: The primary program logic is in main() to handle command-line arguments.

Task Status Indicators
- [ ]: Indicates a task is incomplete.
- [X]: Indicates a task is completed.

# Example Commands

```python
python todo.py -a "Finish homework"  # Adds a new task
python todo.py -l                    # Lists all tasks with statuses
python todo.py -c 2                  # Marks the second task as completed
python todo.py -r 3                  # Removes the third task
python todo.py -z 1                  # Unmarks the first task

```

# Getting Started

1 - Clone this repository.

2 - Navigate to the directory containing todo.py.

3 - Run commands as shown in the usage examples above to interact with your to-do list!
