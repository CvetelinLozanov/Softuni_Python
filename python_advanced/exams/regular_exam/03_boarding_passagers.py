def boarding_passengers(ship_capacity, *args):
    ship_passenger = {}
    passengers = []

    for arg in args:
        number_of_passengers = int(arg[0])
        passenger_plan = arg[1]

        if ship_capacity <= 0:
            break

        if number_of_passengers <= ship_capacity:
            if passenger_plan not in ship_passenger:
                ship_passenger[passenger_plan] = 0

            ship_passenger[passenger_plan] += number_of_passengers
            ship_capacity -= number_of_passengers
            passengers.append(arg)

    sorted_passengers = sorted(ship_passenger.items(), key=lambda x: (-x[1], x[0]))

    result = []
    result.append("Boarding details by benefit plan:")
    for passenger_program, number in sorted_passengers:
        result.append(f"## {passenger_program}: {number} guests")

    if len(passengers) == len(args):
        result.append("All passengers are successfully boarded!")
    elif len(passengers) != len(args) and ship_capacity == 0:
        result.append("Boarding unsuccessful. Cruise ship at full capacity.")
    elif len(passengers) != len(args) and ship_capacity > 0:
        result.append(f"Partial boarding completed. Available capacity: {ship_capacity}.")
    return '\n'.join(result)


print(boarding_passengers(150, (150, 'Diamond'), (55, 'Platinum'), (35, 'Gold'), (25, 'First Cruiser')))

# print(boarding_passengers(100, (20, 'Diamond'), (15, 'Platinum'), (25, 'Gold'), (25, 'First Cruiser'), (15, 'Diamond'), (10, 'Gold')))
#
# print(boarding_passengers(120, (30, 'Gold'), (20, 'Platinum'), (30, 'Diamond'), (10, 'First Cruiser'), (31, 'Platinum'), (20, 'Diamond')))


# Practice 3 Test case there is still available capacity and not all passengers have embarked on the vessel
from unittest import TestCase, main


class TestBoardingPassengers(TestCase):
    def test_boarding_passengers(self):
        result = boarding_passengers(120, (30, 'Gold'), (20, 'Platinum'), (30, 'Diamond'), (10, 'First Cruiser'), (31, 'Platinum'), (20, 'Diamond'))
        expected = """Boarding details by benefit plan:
## Diamond: 50 guests
## Gold: 30 guests
## Platinum: 20 guests
## First Cruiser: 10 guests
Partial boarding completed. Available capacity: 10."""
        self.assertEqual(result.strip(), expected)


if __name__ == '__main__':
    main()