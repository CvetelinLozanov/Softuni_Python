def gather_credits(credits: int, *args):
    enrolled_courses = []
    total_credits_collected = 0
    for arg in args:
        course = arg[0]
        course_credits = int(arg[1])

        if course in enrolled_courses:
            continue

        if total_credits_collected < credits:
            total_credits_collected += course_credits
            enrolled_courses.append(course)
        else:
            break

    if total_credits_collected >= credits:
        return f"Enrollment finished! Maximum credits: {total_credits_collected}.\nCourses: {', '.join(sorted(enrolled_courses))}"
    else:
        return f"You need to enroll in more courses! You have to gather {credits - total_credits_collected} credits more."


print(gather_credits(
    60,
    ("Basics", 30),
    ("Fundamentals", 30),
    ("Advanced", 30),
    ("Web", 30)
))