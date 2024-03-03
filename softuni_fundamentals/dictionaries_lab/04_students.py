from typing import List, Dict


def fill_the_dictionary_with_information(info: List[str], course_list: Dict[str, Dict[str, int]]):
    student_name, student_id, course = info
    if course not in course_list:
        course_list[course] = {}
    if student_id not in course_list[course]:
        course_list[course][student_id] = student_name

    return course_list


def read_input():
    course_info = {}
    while True:
        information = input().split(':')

        if len(information) < 3:
            if '_' in information[0]:
                information[0] = information[0].replace('_', ' ')

            if information[0] in course_info:
                for key in course_info.keys():
                    if key == information[0]:
                        [print(f"{value} - {key}") for key, value in course_info[key].items()]
            break

        course_info = fill_the_dictionary_with_information(information, course_info)


read_input()

