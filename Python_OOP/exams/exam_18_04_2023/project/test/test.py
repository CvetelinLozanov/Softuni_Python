from project.robot import Robot
from unittest import main, TestCase


class TestRobot(TestCase):
    def setUp(self):
        self.robot = Robot("123", "Military", 50, 1000)

    def test_initializer_with_valid_data(self):
        self.assertEqual("123", self.robot.robot_id)
        self.assertEqual("Military", self.robot.category)
        self.assertEqual(50, self.robot.available_capacity)
        self.assertEqual(1000, self.robot.price)
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual([], self.robot.software_updates)

    def test_initializer_with_invalid_category(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = 'dsadada'

        self.assertEqual("Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'", str(ve.exception))

    def test_initializer_with_negative_price(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.price = -100

        self.assertEqual("Price cannot be negative!", str(ve.exception))

    def test_upgrade_method_with_existing_component(self):
        self.robot.hardware_upgrades.append("RAM")
        result = self.robot.upgrade("RAM", 100)

        self.assertEqual("Robot 123 was not upgraded.", result)

    def test_upgrade_method_with_valid_component(self):
        result = self.robot.upgrade("RAM", 1000)
        self.assertIn("RAM", self.robot.hardware_upgrades)
        self.assertEqual(2500, self.robot.price)
        self.assertEqual("Robot 123 was upgraded with RAM.", result)

    def test_update_method_with_invalid_version(self):
        self.robot.software_updates.append(1)
        result = self.robot.update(1, 10)
        self.assertEqual("Robot 123 was not updated.", result)

    def test_update_method_with_invalid_capacity(self):
        result = self.robot.update(1, 100)
        self.assertEqual("Robot 123 was not updated.", result)
        self.assertEqual(0, len(self.robot.software_updates))
        self.assertEqual(50, self.robot.available_capacity)

    def test_update_method_with_valid_parameters(self):
        result = self.robot.update(1, 40)
        self.assertIn(1, self.robot.software_updates)
        self.assertEqual("Robot 123 was updated to version 1.", result)
        self.assertEqual(1, len(self.robot.software_updates))
        self.assertEqual(10, self.robot.available_capacity)

    def test_gt_method_with_cheaper_robot(self):
        test_robo = Robot("12", "Education", 10, 500)
        self.assertEqual(f'Robot with ID 123 is more expensive than Robot with ID 12.', self.robot > test_robo)

    def test_gt_method_with_equal_robots(self):
        test_robo = Robot("12", "Military", 100, 1000)
        self.assertEqual('Robot with ID 123 costs equal to Robot with ID 12.', self.robot > test_robo)

    def test_gt_method_with_expensive(self):
        test_robo = Robot("12", "Education", 100, 4000)
        self.assertEqual('Robot with ID 123 is cheaper than Robot with ID 12.', self.robot > test_robo)


if __name__ == '__main__':
    main()