from collections import deque

tools = deque([int(el) for el in input().split()])
substances = deque([int(el) for el in input().split()])
challenges = [int(el) for el in input().split()]


while True:
    if challenges and (not substances or not tools):
        print(f'Harry is lost in the temple. Oblivion awaits him.')
        break

    if not challenges:
        print('Harry found an ostracon, which is dated to the 6th century BCE.')
        break

    result = tools[0] * substances[-1]
    if result in challenges:
        challenges.remove(result)
        tools.popleft()
        substances.pop()
        continue

    tools[0] += 1
    tools.rotate(-1)
    substances[-1] -= 1
    if substances[-1] == 0:
        substances.pop()


if tools:
    print(f"Tools: {', '.join([str(tool) for tool in tools])}")
if substances:
    print(f"Substances: {', '.join([str(substance) for substance in substances])}")
if challenges:
    print(f"Challenges: {', '.join([str(challenge) for challenge in challenges])}")
