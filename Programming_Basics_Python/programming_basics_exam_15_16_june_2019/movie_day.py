time_for_film = int(input())
number_of_scenes = int(input())
time_for_scene = int(input())

field_preparation = time_for_film * 0.15

time_for_scenes = time_for_scene * number_of_scenes

total_time_for_film = time_for_scenes + field_preparation

if time_for_film >= total_time_for_film:
    print(f'You managed to finish the movie on time! You have {round(time_for_film - total_time_for_film)} minutes left!')

else:
    print(f'Time is up! To complete the movie you need {round(total_time_for_film - time_for_film)} minutes.')