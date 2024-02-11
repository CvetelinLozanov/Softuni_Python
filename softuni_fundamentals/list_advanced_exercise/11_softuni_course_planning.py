from typing import List


def check_if_lesson_is_already_in_schedule(schedule: List[str], lesson: str):
    return lesson in schedule


def course_planning():
    schedule = input().split(', ')

    while True:
        command_args = input().split(':')

        if command_args[0] == 'course start':
            break

        lesson_title = command_args[1]

        if command_args[0] == 'Add':
            if not check_if_lesson_is_already_in_schedule(schedule, lesson_title):
                schedule.append(lesson_title)

        elif command_args[0] == 'Insert':
            index = int(command_args[2])
            if not check_if_lesson_is_already_in_schedule(schedule, lesson_title):
                schedule.insert(index, lesson_title)

        elif command_args[0] == 'Remove':
            if check_if_lesson_is_already_in_schedule(schedule, lesson_title):
                schedule.remove(lesson_title)
                lesson_title_exercise = f'{lesson_title}-Exercise'
                if check_if_lesson_is_already_in_schedule(schedule, lesson_title_exercise):
                    schedule.remove(lesson_title_exercise)

        elif command_args[0] == 'Swap':
            second_lesson_title = command_args[2]
            if check_if_lesson_is_already_in_schedule(schedule, lesson_title) and \
                    check_if_lesson_is_already_in_schedule(schedule, second_lesson_title):
                first_lesson_index = schedule.index(lesson_title)
                second_lesson_index = schedule.index(second_lesson_title)
                schedule[first_lesson_index], schedule[second_lesson_index] = (schedule[second_lesson_index],
                                                                               schedule[first_lesson_index])
                lesson_title_exercise = f'{lesson_title}-Exercise'
                second_lesson_title_exercise = f'{second_lesson_title}-Exercise'
                if check_if_lesson_is_already_in_schedule(schedule, lesson_title_exercise):
                    first_exercise_index = schedule.index(lesson_title_exercise)
                    exercise = schedule.pop(first_exercise_index)
                    schedule.insert(second_lesson_index + 1, exercise)
                if check_if_lesson_is_already_in_schedule(schedule, second_lesson_title_exercise):
                    second_exercise_index = schedule.index(second_lesson_title_exercise)
                    exercise = schedule.pop(second_exercise_index)
                    schedule.insert(first_lesson_index + 1, exercise)

        elif command_args[0] == 'Exercise':
            exercise_title = f'{lesson_title}-Exercise'
            if check_if_lesson_is_already_in_schedule(schedule, lesson_title):
                if not check_if_lesson_is_already_in_schedule(schedule, exercise_title):
                    lesson_index = schedule.index(lesson_title)
                    schedule.insert(lesson_index + 1, exercise_title)
            else:
                schedule.append(lesson_title)
                schedule.append(exercise_title)

    [print(f'{i}.{course}') for i, course in enumerate(schedule, start=1)]


course_planning()

