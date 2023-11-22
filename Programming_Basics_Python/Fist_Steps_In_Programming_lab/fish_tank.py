length = int(input())
width = int(input())
height = int(input())
percentage = float(input())
aquarium_volume = length * width * height
volume_in_liters = aquarium_volume / 1000
percentage /= 100
occupied_space = 1 - percentage
total_liters_of_water = volume_in_liters * occupied_space
print(total_liters_of_water)

