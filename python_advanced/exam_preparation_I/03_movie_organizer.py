def movie_organizer(*args):
    movies = {}
    for el in args:
        movie = el[0]
        genre = el[1]
        if genre not in movies:
            movies[genre] = []
        movies[genre].append(movie)

    sorted_movies = sorted(movies.items(), key=lambda x: (-len(x[1]), x[0]))
    result_list = []

    for genre, movies in sorted_movies:
        result_list.append(f'{genre} - {len(movies)}')
        for movie in sorted(movies):
            result_list.append(f'* {movie}')

    return '\n'.join(result_list)

    #return '\n'.join(f'{key}: {len(value)}' for key, value in sorted_movies)


print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))
