from typing import List


def add_task(tasks: List):
    task_description = input('Please enter your task description:')
    task = {'task': task_description, 'completed': False}
    tasks.append(task)
    # for task in tasks:
    #     if task_description in task.values():
    #         task_desc = task.values()[0]
    #         task_status = task.values()[1]
    #         if task_status:
    #             print('Task is already added in your list.')
    #         print('Task is already added in your list.')
    #         user_choice = input('Do you want to edit it: Y/N:')
    #         if user_choice.lower() == 'y':


def edit_task(task):
    pass


def view_all_tasks(tasks):
    print('===== Tasks =====')
    for index, task in enumerate(tasks):
        status = '[X]' if task['completed'] else '[ ]'
        task_desc = task['task']
        print(f'{index}. {status} {task_desc}')


def mark_task_as_completed(tasks):
    view_all_tasks(tasks)
    task_index = int(input('Enter the index of the task to mark as completed:'))
    tasks[task_index]['completed'] = True


def display_menu():
    print(f'===== To-Do List Menu =====')
    print('1. Add a new task')
    print('2. Mark a task as completed')
    print('3. View all tasks')
    print('4. Quit')


def executor():
    display_menu()
    tasks = []
    while True:
        choice = input('Enter your choice (1-4):')

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            mark_task_as_completed(tasks)
        elif choice == '3':
            view_all_tasks(tasks)
        elif choice == '4':
            print('Exiting the program. Goodbye!')
            break
        else:
            print('Invalid choice. Please enter option between 1-4')

        display_menu()


executor()
