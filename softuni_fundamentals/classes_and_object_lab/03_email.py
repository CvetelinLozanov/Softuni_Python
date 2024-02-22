class Email:
    def __init__(self, sender_: str, receiver_: str, content_: str):
        self.sender = sender_
        self.receiver = receiver_
        self.content = content_
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}'


email = Email
emails = []

while True:
    command = input()

    if command == 'Stop':
        break

    sender, receiver, content = command.split()
    emails.append(email(sender, receiver, content))

indices = [int(i) for i in input().split(', ')]
for index in indices:
    emails[index].send()

for email in emails:
    print(email.get_info())