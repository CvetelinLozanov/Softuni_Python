import unittest
from project.climbing_robot import ClimbingRobot


class ClimbingRobotTest(unittest.TestCase):
    def setUp(self):
        self.climbing_robot = ClimbingRobot("Mountain", "some_part_type", 10, 1000)

    def test_initializer_with_correct_data(self):
        self.assertEqual("Mountain", self.climbing_robot.category)
        self.assertEqual("some_part_type", self.climbing_robot.part_type)
        self.assertEqual(10, self.climbing_robot.capacity)
        self.assertEqual(1000, self.climbing_robot.memory)
        self.assertEqual([], self.climbing_robot.installed_software)

    def test_initializer_with_wrong_category(self):
        with self.assertRaises(ValueError) as ex:
            self.climbing_robot.category = 'some_cat'
        self.assertEqual("Category should be one of ['Mountain', 'Alpine', 'Indoor', 'Bouldering']", str(ex.exception))

    def test_get_used_capacity_method(self):
        self.climbing_robot.installed_software = [{'capacity_consumption': 10}, {'capacity_consumption': 100}]
        result = self.climbing_robot.get_used_capacity()
        self.assertEqual(110, result)

    def test_get_used_capacity_method_with_empty_list(self):
        result = self.climbing_robot.get_used_capacity()
        self.assertEqual(0, result)

    def test_get_available_capacity_method(self):
        self.climbing_robot.installed_software = [{'capacity_consumption': 10}]
        result = self.climbing_robot.get_available_capacity()
        self.assertEqual(0, result)

    def test_get_used_memory_method(self):
        self.climbing_robot.installed_software = [{'memory_consumption': 100}, {'memory_consumption': 400}]
        result = self.climbing_robot.get_used_memory()
        self.assertEqual(500, result)

    def test_get_used_memory_method_with_empty_list(self):
        result = self.climbing_robot.get_used_memory()
        self.assertEqual(0, result)

    def test_get_available_memory_method(self):
        self.climbing_robot.installed_software = [{'memory_consumption': 100}, {'memory_consumption': 400}]
        result = self.climbing_robot.get_available_memory()
        self.assertEqual(500, result)

    def test_install_software_with_valid_data(self):
        result = self.climbing_robot.install_software({"name": "avast", "memory_consumption": 100,
                                                       "capacity_consumption": 1})
        self.assertEqual("Software 'avast' successfully installed on Mountain part.", result)
        self.assertIn({"name": "avast",
                       "memory_consumption": 100, "capacity_consumption": 1}, self.climbing_robot.installed_software)

    def test_install_software_method_with_invalid_capacity(self):
        self.climbing_robot.capacity = 0
        result = self.climbing_robot.install_software({"name": "avast", "memory_consumption": 100,
                                                       "capacity_consumption": 1})
        self.assertEqual("Software 'avast' cannot be installed on Mountain part.", result)
        self.assertNotIn({"name": "avast",
                          "memory_consumption": 100, "capacity_consumption": 1}, self.climbing_robot.installed_software)

    def test_install_software_method_with_invalid_memory(self):
        self.climbing_robot.memory = 10
        result = self.climbing_robot.install_software({"name": "avast", "memory_consumption": 100,
                                                       "capacity_consumption": 1})
        self.assertEqual("Software 'avast' cannot be installed on Mountain part.", result)
        self.assertNotIn({"name": "avast",
                          "memory_consumption": 100, "capacity_consumption": 1}, self.climbing_robot.installed_software)

    def test_install_software_method_with_equal_memory_and_capacity(self):
        self.climbing_robot.memory = 100
        self.climbing_robot.capacity = 1
        result = self.climbing_robot.install_software({"name": "avast", "memory_consumption": 100,
                                                       "capacity_consumption": 1})
        self.assertEqual("Software 'avast' successfully installed on Mountain part.", result)
        self.assertIn({"name": "avast",
                       "memory_consumption": 100, "capacity_consumption": 1}, self.climbing_robot.installed_software)


if __name__ == '__main__':
    unittest.main()
