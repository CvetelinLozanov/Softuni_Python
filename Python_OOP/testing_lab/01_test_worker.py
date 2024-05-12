class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


import unittest


class WorkerTests(unittest.TestCase):
    def setUp(self):
        self.worker = Worker("Ivan", 1000, 100)

    def test_worker_initializing(self):
        self.assertEqual("Ivan", self.worker.name)
        self.assertEqual(1000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_worker_work_with_positive_energy(self):
        self.assertEqual(1000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

        self.worker.work()

        self.assertEqual(1000, self.worker.money)
        self.assertEqual(99, self.worker.energy)

        self.worker.work()

        self.assertEqual(2000, self.worker.money)
        self.assertEqual(98, self.worker.energy)

    def test_worker_with_energy_equal_to_zero(self):
        worker = Worker("Pesho", 1000, 0)

        with self.assertRaises(Exception) as ex:
            worker.work()

        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_worker_with_energy_less_then_zero(self):
        worker = Worker("Azis", 50000, -100)

        with self.assertRaises(Exception) as ex:
            worker.work()

        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_rest_method(self):
        self.assertEqual(100, self.worker.energy)
        self.worker.rest()
        self.assertEqual(101, self.worker.energy)
        self.worker.rest()
        self.assertEqual(102, self.worker.energy)

    def test_get_info_method(self):

        expected_result = "Ivan has saved 0 money."
        self.assertEqual(expected_result, self.worker.get_info())
        self.worker.work()
        expected_result = "Ivan has saved 1000 money."
        self.assertEqual(expected_result, self.worker.get_info())


if __name__ == '__main__':
    unittest.main()