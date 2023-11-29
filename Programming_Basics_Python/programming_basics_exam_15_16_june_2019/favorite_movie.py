command = input()
best_movie = ''
highest_rank = 0
counter = 0
sum_of_letters = 0

while command != 'STOP':
    movie = command
    counter += 1
    for letter in movie:
        sum_of_letters += ord(letter)
        if 65 <= ord(letter) <= 90:
            sum_of_letters -= len(movie)

        elif 97 <= ord(letter) <= 122:
            sum_of_letters -= 2 * len(movie)

    if sum_of_letters > highest_rank:
        highest_rank = sum_of_letters
        best_movie = movie

    sum_of_letters = 0

    if counter == 7:
        print('The limit is reached.')
        break

    command = input()

print(f'The best movie for you is {best_movie} with {highest_rank} ASCII sum.')

