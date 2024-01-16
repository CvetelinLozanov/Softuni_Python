from typing import List
from project.animal import Animal
from project.worker import Worker


class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price: int):

        if self.__budget - price < 0:
            return 'Not enough budget'

        if self.__animal_capacity == 0:
            return 'Not enough space for animal'

        self.animals.append(animal)
        self.__budget -= price
        self.__animal_capacity -= 1
        return f'{animal.name} the {animal.__class__.__name__} added to the zoo'

    def hire_worker(self, worker: Worker):

        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f'{worker.name} the {worker.__class__.__name__} hired successfully'

        return 'Not enough space for worker'

    def fire_worker(self, worker_name: str):

        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f'{worker_name} fired successfully'

        return f'There is no {worker_name} in the zoo'

    def pay_workers(self):
        total_salary = sum([worker.salary for worker in self.workers])

        if self.__budget >= total_salary:
            self.__budget -= total_salary
            return f'You payed your workers. They are happy. Budget left: {self.__budget}'

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        needed_budget = sum([animal.money_for_care for animal in self.animals])

        if self.__budget >= needed_budget:
            self.__budget -= needed_budget
            return f'You tended all the animals. They are happy. Budget left: {self.__budget}'

        return 'You have no budget to tend the animals. They are unhappy.'

    def profit(self, amount: int):
        self.__budget += amount

    def animals_status(self):
        result = []
        lions = [animal for animal in self.animals if animal.__class__.__name__ == 'Lion']
        tigers = [animal for animal in self.animals if animal.__class__.__name__ == 'Tiger']
        cheetahs = [animal for animal in self.animals if animal.__class__.__name__ == 'Cheetah']
        result.append(f"You have {len(self.animals)} animals")
        result.append(f"----- {len(lions)} Lions:")
        result.append('\n'.join([str(lion) for lion in lions]))
        result.append(f"----- {len(tigers)} Tigers:")
        result.append('\n'.join([str(tiger) for tiger in tigers]))
        result.append(f"----- {len(cheetahs)} Cheetahs:")
        result.append('\n'.join([str(cheetah) for cheetah in cheetahs]))
        return '\n'.join(result)

    def workers_status(self):
        result = []
        keepers = [worker for worker in self.workers if worker.__class__.__name__ == 'Keeper']
        caretakers = [worker for worker in self.workers if worker.__class__.__name__ == 'Caretaker']
        vets = [worker for worker in self.workers if worker.__class__.__name__ == 'Vet']
        result.append(f"You have {len(self.workers)} workers")
        result.append(f"----- {len(keepers)} Keepers:")
        result.append('\n'.join([str(keeper) for keeper in keepers]))
        result.append(f"----- {len(caretakers)} Caretakers:")
        result.append('\n'.join([str(caretaker) for caretaker in caretakers]))
        result.append(f"----- {len(vets)} Vets:")
        result.append('\n'.join([str(vet) for vet in vets]))

        return '\n'.join(result)

