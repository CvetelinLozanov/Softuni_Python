from collections import deque


eggs = deque([int(egg) for egg in input().split(', ')])
papers = deque([int(paper) for paper in input().split(', ')])
boxes = 0

while eggs and papers:
    if eggs[0] <= 0:
        eggs.popleft()
        continue

    if eggs[0] == 13:
        eggs.popleft()
        papers[0], papers[-1] = papers[-1], papers[0]
        continue

    current_egg = eggs.popleft()
    current_paper = papers.pop()
    total_sum = current_egg + current_paper

    if total_sum <= 50:
        boxes += 1


if boxes > 0:
    print(f"Great! You filled {boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join(map(str, eggs))}")
if papers:
    print(f"Pieces of paper left: {', '.join(map(str, papers))}")
