from typing import List


# Function to check if the index is in valid range 0 - list length - 1
def is_index_valid(neighborhood_: List[int], index: int):
    return 0 <= index < len(neighborhood_)


# Function to check if house is celebrating(house value must be equal to zero)
def check_if_house_celebrate(neighborhood_: List[int], index: int):
    return neighborhood_[index] == 0


# Function to print the final cupid's position and did he make happy the whole neighborhood
def print_result(neighborhood_: List[int], last_position: int):
    sum_of_neighborhoods = sum(neighborhood_)
    print(f"Cupid's last position was {last_position}.")

    if sum_of_neighborhoods == 0:
        print('Mission was successful.')
    else:
        count_of_houses = len([n for n in neighborhood_ if n > 0])
        print(f'Cupid has failed {count_of_houses} places.')


# Function to check if house in neighborhood already celebrate and if not to decrease the value with
# 2 for house at cupid's index
def process_main_logic(neighborhood_: List[int], index: int):

    if check_if_house_celebrate(neighborhood_, index):
        print(f"Place {index} already had Valentine's day.")
        return

    neighborhood_[index] -= 2
    if check_if_house_celebrate(neighborhood_, index):
        print(f"Place {index} has Valentine's day.")


# Function to execute the main logic and returns the final neighborhood state with last cupid's position
def heart_delivery_main_logic():
    neighborhood_ = list(map(int, input().split('@')))
    cupid_position = 0
    while True:
        command = input()
        if command == 'Love!':
            break
        index = int(command.split()[1])
        cupid_position += index
        if is_index_valid(neighborhood_, cupid_position):
            process_main_logic(neighborhood_, cupid_position)
        else:
            cupid_position = 0
            process_main_logic(neighborhood_, cupid_position)

    return neighborhood_, cupid_position


neighborhood, position = heart_delivery_main_logic()
print_result(neighborhood, position)