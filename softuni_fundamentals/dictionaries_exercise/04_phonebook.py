phonebook = {}


def fill_phonebook(contact_, phone_num_, phonebook_):
    phonebook[contact_] = phone_num_
    return phonebook_


def check_contacts(number, phonebook_):
    for _ in range(number):
        contact_name = input()
        if contact_name in phonebook_:
            print(f"{contact_name} -> {phonebook_[contact_name]}")
        else:
            print(f"Contact {contact_name} does not exist.")


while True:
    contact_info = input().split('-')

    if len(contact_info) < 2:
        check_contacts(int(contact_info[0]), phonebook)
        break

    contact, phone_num = contact_info
    phonebook = fill_phonebook(contact, phone_num, phonebook)