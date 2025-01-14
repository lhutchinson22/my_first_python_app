import argparse
import os

def create_parser():
    # Create an argument parser for the command-line interface
    parser = argparse.ArgumentParser(description="Command-line Todo List App")
    parser.add_argument("-a", "--add", metavar="", help="Add a new task")
    parser.add_argument("-l", "--list", action="store_true", help="List all tasks")
    parser.add_argument("-r", "--remove", metavar="", help="Remove a task by index")
    return parser

def add_task(task, tasks):
    # Add a new task to the tasks list
    tasks.append(task)
    save_tasks(tasks)

def list_tasks(tasks):
    # List all tasks from the tasks list
    if tasks:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("No tasks found.")

def remove_task(index, tasks):
    # Remove a task by index from the tasks list
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
    else:
        print("Invalid task index.")

def load_tasks():
    # Load tasks from the tasks.txt file
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            tasks = file.read().splitlines()
    else:
        tasks = []
    return tasks

def save_tasks(tasks):
    # Save tasks to the tasks.txt file
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def main():
    parser = create_parser()
    args = parser.parse_args()
    tasks = load_tasks()

    if args.add:
        add_task(args.add, tasks)
    elif args.list:
        list_tasks(tasks)
    elif args.remove:
        try:
            index = int(args.remove) - 1
            remove_task(index, tasks)
        except ValueError:
            print("Please provide a valid task index.")

if __name__ == '__main__':
    main()