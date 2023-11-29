serial = input()
seasons = int(input())
episodes = int(input())
episode_time = float(input())

advertisement = episode_time * 0.20
bonus_time = seasons * 10
episode_time = episode_time + advertisement
total_episodes = seasons * episodes
total_time = total_episodes * episode_time + bonus_time

print(f'Total time needed to watch the {serial} series is {int(total_time)} minutes.')
