class Party:
    def __init__(self):
        self.people = []


party = Party()
while True:
    person = input()

    if person == 'End':
        break

    party.people.append(person)

print(f'Going: {", ".join(party.people)}')
print(f'Total: {len(party.people)}')
