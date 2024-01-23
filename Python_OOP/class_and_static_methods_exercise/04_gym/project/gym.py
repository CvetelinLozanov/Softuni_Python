from typing import List
from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers: List[Customer] = []
        self.trainers: List[Trainer] = []
        self.equipment: List[Equipment] = []
        self.plans: List[ExercisePlan] = []
        self.subscriptions: List[Subscription] = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        result = []
        subscription = [sub for sub in self.subscriptions if sub.id == subscription_id][0]
        customer_id = subscription.customer_id
        trainer_id = subscription.trainer_id
        customer = [customer for customer in self.customers if customer.id == customer_id][0]
        trainer = [trainer for trainer in self.trainers if trainer_id == trainer.id][0]
        exercise_plan = [plan for plan in self.plans if plan.trainer_id == trainer_id][0]
        equipment_id = exercise_plan.equipment_id
        equipment = [equipment for equipment in self.equipment if equipment.id == equipment_id][0]
        result.append(repr(subscription))
        result.append(repr(customer))
        result.append(repr(trainer))
        result.append(repr(equipment))
        result.append(repr(exercise_plan))
        return '\n'.join(result)



