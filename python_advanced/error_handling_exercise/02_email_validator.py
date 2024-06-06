class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


VALID_DOMAINS = ['bg', 'com', 'net', 'org']


while True:
    command = input()

    if command == 'End':
        break

    if '@' not in command:
        raise MustContainAtSymbolError("Email must contain @")

    name = command.split('@')[0]
    domain = command.split('@')[1].split('.')[-1]

    if len(name) < 4:
        raise NameTooShortError("Name must be more than 4 characters")

    if domain not in VALID_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
