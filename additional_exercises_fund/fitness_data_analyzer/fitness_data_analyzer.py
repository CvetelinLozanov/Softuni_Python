from long_name_exception import LongNameException
from invalid_height_exception import InvalidHeight


# Function returns the Body Mass Index for person
def calculate_bmi(weight, height):
    """Calculate the Body Mass Index (BMI)."""
    return weight / (height ** 2)


# Function returns the calories burned per minute of walking
def calculate_calories_burned(duration):
    """Calculate the estimated number of calories burned during exercise."""
    return 4 * duration


# Function returns all people which are with Body Mass Index greater or equal to 25
def filter_overweight_people(people_data):
    """Filter overweight people based on BMI."""
    _overweight_people = [p for p in people_data if p['bmi'] >= 25]
    return _overweight_people


# Function to check if weight, height and duration are numbers
def validate_weight_height_and_duration():
    while True:
        try:
            weight = float(input("Enter person's weight in kilograms: "))
            height = float(input("Enter person's height in meters(0 - 3): "))
            if height < 0 or height > 3:
                raise InvalidHeight
            duration = float(input("Enter exercise duration in minutes: "))
            return weight, height, duration
        except ValueError:
            print("All information for weight, height and duration must be number")
        except InvalidHeight:
            print('Please enter height in range 0 - 3')


# Function to check if name entered by user is longer than 20 chars
def validate_name_length():
    while True:
        try:
            name = input("Enter person's name: ").strip()
            if len(name) >= 20:
                raise LongNameException
            return name
        except LongNameException:
            print('You entered too long name please enter a name with chars less than 20')


# Function to read the information for each user and keep it in list
def read_people_information():
    """Read fitness users information."""

    people_data = []

    print("Enter fitness data for each person (Enter a blank name to finish):")
    while True:
        name = validate_name_length()
        if not name:
            break
        weight, height, duration = validate_weight_height_and_duration()
        _bmi = calculate_bmi(weight, height)
        _calories_burned = calculate_calories_burned(duration)
        _person = {'name': name, 'weight': weight, 'height': height, 'duration': duration, 'bmi': _bmi,
                   'calories_burned': _calories_burned}
        people_data.append(_person)

    return people_data


# Function that prints the fitness users information
def print_people_information(people_data):
    """Prints users data information"""

    if people_data:
        print("\nFitness Analysis:")
        for person in people_data:
            bmi = person['bmi']
            calories_burned = person['calories_burned']
            name = person['name']
            print(f"{name}: BMI = {bmi:.2f}, Calories burned = {calories_burned}")

        overweight_people = filter_overweight_people(people_data)
        if overweight_people:

            print("\nOverweight People:")
            for person in overweight_people:
                bmi = person['bmi']
                name = person['name']
                print(f"{name}: BMI = {bmi:.2f}")
        else:
            print('\nThere are no overweight people')
    else:
        print('Goodbye! There are no users in our database.')


# main function to execute the program
def main():
    people_information = read_people_information()
    print_people_information(people_information)


if __name__ == '__main__':
    main()



