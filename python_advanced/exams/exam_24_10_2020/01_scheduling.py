from collections import deque


def is_valid_index(index, array_length):
    return 0 <= index < len(array_length)


jobs = [int(num) for num in input().split(', ')]
job_index = int(input())
searched_job = 0
cycles = 0
left_part = jobs[:job_index]

if is_valid_index(job_index, jobs):
    searched_job = jobs[job_index]

if searched_job in left_part:
    count = left_part.count(searched_job)
    cycles += searched_job * count

sorted_jobs = deque(sorted(jobs))

while sorted_jobs:
    current_job = sorted_jobs.popleft()
    cycles += current_job
    if current_job == searched_job:
        break

print(cycles)

# jobs = [int(i) for i in input().split(", ")]
# index = int(input())
# print(sum([i for i in jobs if i <= jobs[index]]))

# jobs = [int(job) for job in input().split(', ')]
# target_index = int(input())
#
# target_job = jobs[target_index]
# cycles = 0
#
# for i in range(len(jobs)):
#     current_job = jobs[i]
#     if current_job < target_job or current_job == target_job and target_index >= i:
#         cycles += current_job
#
# print(cycles)