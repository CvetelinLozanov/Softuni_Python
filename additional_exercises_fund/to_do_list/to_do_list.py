from typing import List


# Check if task is already in to do list if it exists it prompts user to edit the task.
# if task is not already in list adding the task to list with tasks
def add_task(tasks: List):
    task_description = input('Please enter your task description:')
    task = {'task': task_description, 'completed': False}
    task_exists = False
    for index, existing_task in enumerate(tasks):
        if task_description in existing_task.values():
            task_exists = True
            print('Task is already in your list. If you want to edit it Y/N:')
            user_choice = input()
            if user_choice.lower() == 'y':
                edit_task(index, tasks)
            break

    if not task_exists:
        tasks.append(task)


# shows the edit menu options on console
def display_edit_menu_options():
    print(f'===== Edit Task Menu =====')
    print('1. Change task description')
    print('2. Change task status')
    print('3. Change both task status and description')


# provide option to edit already existing task based on user choice.
# possible options 1 - edit only description, 2 - status change, 3 - both status and description change
def edit_task(index: int, tasks: List):
    display_edit_menu_options()
    while True:
        edit_choice = input('Please select edit option:')

        if edit_choice == '1':
            new_description = input('Please enter new task description:')
            tasks[index]['task'] = new_description
            print('Your task has been updated with new description')
            break
        elif edit_choice == '2':
            current_status = tasks[index]['completed']
            tasks[index]['completed'] = not current_status
            print('Your task status has been changed')
            break
        elif edit_choice == '3':
            new_description = input('Please enter new task description:')
            current_status = tasks[index]['completed']
            tasks[index]['task'] = new_description
            tasks[index]['completed'] = not current_status
            print('Your task has been updated with new description and status has been changed.')
            break
        else:
            print('Invalid option. Please select a option between 1 and 3')


# print all tasks on console with their information: task information and task status: [X] completed [ ] not completed
def view_all_tasks(tasks: List):
    print('===== Tasks =====')
    for index, task in enumerate(tasks):
        status = '[X]' if task['completed'] else '[ ]'
        task_desc = task['task']
        print(f'{index}. {status} {task_desc}')


# mark selected task as completed
def mark_task_as_completed(tasks: List):
    view_all_tasks(tasks)
    task_index = get_task_index(tasks)
    tasks[task_index]['completed'] = True


# validate and returns the index if it is in valid range
def get_task_index(tasks: List):
    while True:
        try:
            index = int(input('Please enter index of the task you want to edit:'))
            task = tasks[index]
            return index
        except IndexError:
            print(f'Please enter a valid index in range 0-{len(tasks) - 1}')
        except ValueError:
            print(f'Please enter a number in range 0-{len(tasks) - 1}')


# prints the to do list options
def display_menu():
    print(f'===== To-Do List Menu =====')
    print('1. Add a new task')
    print('2. Mark a task as completed')
    print('3. View all tasks')
    print('4. Edit task')
    print('5. Quit')


# execute the program
def executor():
    display_menu()
    tasks = []
    while True:
        choice = input('Enter your choice (1-5):')

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            mark_task_as_completed(tasks)
        elif choice == '3':
            view_all_tasks(tasks)
        elif choice == '4':
            if not tasks:
                print('There are no tasks in the list. Please first add tasks!')
                continue
            view_all_tasks(tasks)
            index = get_task_index(tasks)
            edit_task(index, tasks)
        elif choice == '5':
            print('Exiting the program. Goodbye!')
            break
        else:
            print('Invalid choice. Please enter option between 1-4')

        display_menu()


executor()
