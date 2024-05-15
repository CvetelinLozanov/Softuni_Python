def students_credits(*args):
    courses = {}
    total_credits = 0
    for arg in args:
        info = arg.split('-')
        course_name = info[0]
        credits = int(info[1])
        max_test_points = int(info[2])
        diyan_points = int(info[3])
        credits = (diyan_points / max_test_points) * credits
        total_credits += credits
        courses[course_name] = credits

    sorted_courses = sorted(courses.items(), key=lambda x: -x[1])
    result = []

    if total_credits >= 240:
        result.append(f"Diyan gets a diploma with {total_credits:.1f} credits.")
    else:
        result.append(f"Diyan needs {240 - total_credits:.1f} credits more for a diploma.")

    for course, credits in sorted_courses:
        result.append(f"{course} - {credits:.1f}")

    return '\n'.join(result)


print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)