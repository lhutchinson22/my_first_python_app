import argparse
import os

def create_parser():
    # Create an argument parser for the command-line interface
    parser = argparse.ArgumentParser(description="Command-line Todo List App")
    parser.add_argument("-a", "--add", metavar="", help="Add a new task")
    parser.add_argument("-l", "--list", action="store_true", help="List all tasks")
    parser.add_argument("-r", "--remove", metavar="", help="Remove a task by index")
    return parser

def add_task(task):
    # Add a new task to the tasks.txt file
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")

def list_tasks():
    # List all tasks from the tasks.txt file
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task.strip()}")
    else:
        print("No tasks found.")

def remove_task(index):
    # Remove a task by index from the tasks.txt file
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        with open("tasks.txt", "w") as file:
            for i, task in enumerate(tasks, start=1):
                if i != index:
                    file.write(task)