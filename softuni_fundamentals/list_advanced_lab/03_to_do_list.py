def process_to_do_notes():

    to_do_notes = []

    while True:
        note = input()

        if note == 'End':
            break

        to_do_notes.append(note)

    sorted_to_do_list = sorted(to_do_notes, key=lambda n: int(n.split('-')[0]))
    final_notes = [note.split('-')[1] for note in sorted_to_do_list]
    print(final_notes)


process_to_do_notes()