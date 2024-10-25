import sys
from usage import usage_information, welcome_text


def display_tasks():
    '''
    Lists all tasks and adds numbering before each task.
    ------
    If file does not exists then it creates tasks.txt file.
    ------
    Parameters: None
    ------
    Returs: None

    '''
    try:
        tasks_file = "tasks.txt"
        with open(tasks_file, "r") as file:
            tasks = file.readlines()

        if not tasks:
            print("No todos for today! :)")
        else:
            print("--- To-Do-List ---")
            i = 1
            for task in tasks:
                print(i, end="")
                print(". " + task.strip())
                i += 1
    except FileNotFoundError:
        open('tasks.txt', "x")
        print("No todos for today! :)")


def add_task(new_task):
    '''
    Add a new task to the tasks.txt file.
    ------
    If file does not exists then it creates tasks.txt file.
    ------
    Parameters: new_task(str) - The task to be added.
    ------
    Returns: None

    '''
    tasks_file = "tasks.txt"
    with open(tasks_file, "a") as file:

        if len(sys.argv) > 2:
            file.write("[ ] " + str(new_task) + "\n")
            print("Task added successfully.")

        else:
            print("Unable to add: No task provided!!")


def remove_task(line_number):
    '''
    Removes the task from the tasks.txt file.
    ------
    If file does not exists then it creates tasks.txt file.
    ------
    Parameters: line_number(int) - The index of the task to be removed.
    ------
    Returns: None

    '''
    tasks_file = "tasks.txt"
    with open(tasks_file) as file:
        lines = file.readlines()

        if (line_number <= len(lines)):

            del lines[line_number - 1]

            with open(tasks_file, "w") as file:
                for line in lines:
                    file.write(line)
            print("Task removed successfully")

        else:
            print("!! Unable to remove: index is out of bound !!")


def complete_task(task_index):
    '''
    Mark a task as completed by adding a checkmark box [X] in front.
    ------
    If file does not exists then it creates tasks.txt file.
    ------
    Parameters: task_index(int) - The index of the task to be completed.
    ------
    Returns: None
    '''

    tasks_file = "tasks.txt"
    with open(tasks_file) as file:
        lines = file.readlines()

    if (task_index <= len(lines)):
        if lines[task_index - 1][:3] == "[X]":
            print("Task is already completed")
        else:
            lines[task_index - 1] = "[X]" + lines[task_index - 1][3:]

            with open(tasks_file, "w") as file:
                file.writelines(lines)
                print("Task is marked as completed")
    else:
        print("!! Unable to complete: index is out of bound !!")


def undo_complete_task(task_index):
    '''
    Unmarks the task by removing checkmark box [X].
    ------
    If file does not exists then it creates tasks.txt file.
    ------
    Parameters: task_index(int) - The index of the task to be unmarked.
    ------
    Returns: None
    '''
    tasks_file = "tasks.txt"
    with open(tasks_file) as file:
        lines = file.readlines()

    if (task_index <= len(lines)):
        if lines[task_index - 1][:3] == "[ ]":
            print("Task was never completed/marked!!")
        else:
            lines[task_index - 1] = "[ ]" + lines[task_index - 1][3:]

            with open(tasks_file, "w") as file:
                file.writelines(lines)
            print("Task is unmarked")
    else:
        print("!! Unable to uncheck: index is out of bound !!")


def main():
    '''
    This is the main function that handles different command line arguements
    and performs corresponding actions.
    ------
    If no argument is provided then it creates tasks file if it does not exist.
    If '-a' argument is provided then it adds provided task to tasks.txt file.
    If '-l' argument is provided then it lists all the tasks.
    If '-r' argument is provided then it removes the specified task.
    If '-c' argument is provided then it completes the specified task.
    If '-z' argument is provided then it unchecks the specified task.
    If Invalid arguement is provided then it prints the usage information
    ------
    It also does most of the error handling incase of unnecessary arguments.
    '''
    if len(sys.argv) == 1:
        try:
            open('tasks.txt', "x")
            print(welcome_text)
        except FileExistsError:
            print(welcome_text)

    elif sys.argv[1] == "-a":
        new_task = " ".join(sys.argv[2:])
        add_task(new_task)

    elif sys.argv[1] == "-l":
        if len(sys.argv) > 2:
            print("Unable to list: Unwanted extension provided!!")
        else:
            display_tasks()

    elif sys.argv[1] == "-r":
        try:
            if len(sys.argv) <= 3:
                if len(sys.argv) > 2:
                    line_number = int(sys.argv[2])
                    if line_number > 0:
                        remove_task(line_number)
                    else:
                        print("Unable to remove: Zero/Negative index provided")
                else:
                    print("Unable to remove: No index provided!!")
            else:
                print("Unable to remove: Unwanted extension provided!!")

        except ValueError:
            print("Unable to remove: Index is not a number!!")

    elif sys.argv[1] == "-c":
        try:
            if len(sys.argv) <= 3:
                if len(sys.argv) > 2:
                    task_index = int(sys.argv[2])
                    if task_index > 0:
                        complete_task(task_index)
                    else:
                        print("Unable to complete: Zero/Negative index provided")
                else:
                    print("Unable to complete: No index provided!!")
            else:
                print("Unable to complete: Unwanted extension provided!!")

        except ValueError:
            print("Unable to complete: Index is not a number!!")

    elif sys.argv[1] == "-z":
        try:
            if len(sys.argv) <= 3:
                if len(sys.argv) > 2:
                    task_index = int(sys.argv[2])
                    if task_index > 0:
                        undo_complete_task(task_index)
                    else:
                        print("Unable to uncheck: Zero/Negative index provided")
                else:
                    print("Unable to uncheck: No index provided!!")
            else:
                print("Unable to uncheck: Unwanted extension provided!!")
        except ValueError:
            print("Unable to uncheck: Index is not a number!!")

    else:
        print(usage_information)


if __name__ == "__main__":
    main()
