number_of_movies = int(input())

highest_raiting = 0
lowest_raiting = 999
movie_with_highest_raiting = ''
movie_with_lowest_raiting = ''
total_raiting = 0

for _ in range(number_of_movies):
    movie_name = input()
    movie_raiting = float(input())
    total_raiting += movie_raiting

    if movie_raiting > highest_raiting:
        movie_with_highest_raiting = movie_name
        highest_raiting = movie_raiting

    elif movie_raiting < lowest_raiting:
        movie_with_lowest_raiting = movie_name
        lowest_raiting = movie_raiting


average_raiting = total_raiting / number_of_movies
print(f'{movie_with_highest_raiting} is with highest rating: {highest_raiting:.1f}')
print(f'{movie_with_lowest_raiting} is with lowest rating: {lowest_raiting:.1f}')
print(f'Average rating: {average_raiting:.1f}')