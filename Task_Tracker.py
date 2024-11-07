# Task Tracker Building
from dateutil.parser import parse
from datetime import datetime
from dateutil.relativedelta import relativedelta
import json

task = [

    ]
with open("tasks.json", 'w') as file:
    json.dump(task, file, indent=4)


# Now I will create the functions

def add_task():
    description = input("What will be the description of your task? ")
    custom_date = input("Enter due date (e.g., 'tomorrow', 'next Monday', 'in 3 days',\nor leave blank for today): ")
    if custom_date:
        # This handle input like "tomorrow" or "next tomorrow"
        if 'tomorrow' in custom_date.lower():
            due_date = (datetime.today() + relativedelta(days =+1)).strftime('%Y-%m-%d')
        elif "next tomorrow" in custom_date.lower():
            due_date = (datetime.today() + relativedelta(days =+2)).strftime("%Y-%m-%d")
        elif "next monday" in custom_date.lower():
            # Finding the next monday
            today = datetime.today()
            days_ahead = 0 - today.weekday() + 7 #The number of days until next monday
            due_date = (today + relativedelta(days= days_ahead)).strftime("%Y-%m-%d")

        elif "in" in custom_date and 'days' in custom_date.lower():
            # This helps handle inputs like 'in 3 days'
            days = int(custom_date.split()[1])
            due_date = datetime.today().strftime("%Y-%m-%d")


        else:
            # This helps fallback to parse (for other date expressions like "next tuesday"
            due_date = datetime.today().strftime('%Y-%m-%d')
    else:
        due_date = datetime.today().strftime('%Y-%m-%d')

    status = "Pending"
    new_task = {"description": description, "due_date": due_date, "status": status}

    with open("tasks.json", 'r') as file:
        tasks = json.load(file)

    # Now i will add the function to the task file
    tasks.append(new_task)

    with open("tasks.json", 'w') as file:
        json.dump(tasks, file, indent=4)


# Time to list the tasks

def list_task():
    with open("tasks.json", 'r') as file:
        tasks = json.load(file)

    for index, task in enumerate(tasks):# enumerate is used to add a counter
        print(f"Task {index + 1}: ")
        print(f"    Description: {task['description']}")#Choosing an index in a file uses single coumn
        print(f"    Due Date: {task['due_date']}")
        print(f"    Status {task['status']}\n") # The space is to ensure structure


# This next function allows it to mark a task complete once its done
def mark_complete():
    with open("tasks.json", 'r') as file:
        data = json.load(file)

# Loading the list_task function so the user can select which task they want completed or mark
    list_task()

    task_number = int(input("Enter the task number to mark as completed: ")) -1 # This deducts one from the task_number
#chosen to match the indexing for 'data'

    if 0 <= task_number < len(data): # This checks when the number chosen is less than t
        data[task_number]['status'] = 'complete'
        #data[if task_number = 3, therefore, task_number - 1 = 2 (To match the indexing number for data)['status'] and change to 'complete'
        # We save the changes to the file
        with open("tasks.json", 'w') as file:
            json.dump(data, file, indent=4)

        print("Task marked as complete!")
    else:
        print("Invalid task number") # Error handling incase input is invalid


# Combining all the functions together

def main():
    while True:
        print("\n Task Tracker by Gaji")
        print("Task Tracker will help you keep track of your activities :) ")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Complete")
        print("4. Exit")

        choice = input("Choose an option (1/2/3/4) : ")

        if choice == '1':
            add_task()
            print("Task added sucessfully :)")
            q1 = input("Would you like to choose another option? (yes/no) ").lower()
            if q1 in ["yes", "sure", "okay"]:
                continue #Not putting 'main' to avoid stack overflow
            elif q1 in ["No", "no", "nope"]:
                print("File all saved :)")
            else:
                print("Invalid choice, please try again: ")
                continue


        elif choice == "2":
            list_task()
            q1 = input("Would you like to choose another option? (yes/no) ").lower()
            if q1 in ["yes", "sure", "okay"]:
                continue
            elif q1 in ["No", "no", "nope"]:
                print("All tasks sucessfully viewed :) ")
            else:
                print("Invalid choice, please try again: ")
                continue


        elif choice == "3":
            mark_complete()
            q1 = input("Would you like to choose another option? (yes/no) ").lower()
            if q1 in ["yes", "sure", "okay"]:
                continue
            elif q1 in ["No", "no", "nope"]:
                print("File marked complete sucessfully :)")
            else:
                print("Invalid choice, please try again: ")
                continue




        elif choice == "4":
            break
        else:
            print("Invalid choice, please try again: ")


# This ensures the program isn't in existence as main
if __name__ == "__main__":

    # Ensuring tasks.json exists
    try:
        with open("tasks.json", 'x') as file: # This creates the file only when tasks doesn't exist
            json.dump([], file) # This is to load the file as a list

    except FileExistsError: # Error handling
        print("This file eists already")
        pass

    main()







