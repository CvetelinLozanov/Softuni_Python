from typing import Dict


def add_user(messanger_: Dict, username_: str, sent_messages_: int, received_messages_: int):
    if username_ not in messanger_:
        messanger_[username_] = {}
        messanger_[username_]['sent'] = sent_messages_
        messanger_[username_]['received'] = received_messages_

    return messanger_


def process_messages(messanger_: Dict, sender_: str, receiver_: str, capacity_: int):
    if sender_ in messanger_ and receiver_ in messanger_:
        messanger_[sender_]['sent'] += 1
        messanger_[receiver_]['received'] += 1

        sender_sum = messanger_[sender_]['sent'] + messanger_[sender_]['received']
        receiver_sum = messanger_[receiver_]['sent'] + messanger_[receiver_]['received']
        if sender_sum >= capacity_:
            print(f'{sender_} reached the capacity!')
            del messanger_[sender_]

        if receiver_sum >= capacity_:
            print(f'{receiver_} reached the capacity!')
            del messanger_[receiver_]

    return messanger_


def print_users(messanger_: Dict):
    print(f'Users count: {len(messanger_)}')

    for user, user_info in messanger_.items():
        sum_of_messages = user_info['received'] + user_info['sent']
        print(f'{user} - {sum_of_messages}')


capacity = int(input())
messanger = {}

while True:

    text = input()

    if text == 'Statistics':
        break

    command_args = text.split('=')

    if command_args[0] == 'Add':
        username = command_args[1]
        sent_messages = int(command_args[2])
        received_messages = int(command_args[3])
        messanger = add_user(messanger, username, sent_messages, received_messages)

    elif command_args[0] == 'Message':
        sender = command_args[1]
        receiver = command_args[2]
        messanger = process_messages(messanger, sender, receiver, capacity)

    elif command_args[0] == 'Empty':
        username = command_args[1]

        if username == 'All':
            messanger = {}
        else:
            if username in messanger:
                del messanger[username]


print_users(messanger)