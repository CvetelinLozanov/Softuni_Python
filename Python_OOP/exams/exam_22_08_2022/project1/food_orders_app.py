from typing import List

from project.client import Client
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.meal import Meal
from project.meals.starter import Starter
from copy import deepcopy


class FoodOrdersApp:
    receipt_id = 0
    ALLOWED_MEALS = ["Starter", "MainDish", "Dessert"]

    def __init__(self):
        self.menu: List[Meal] = []
        self.clients_list: List[Client] = []

    def register_client(self, client_phone_number: str):
        client = self._get_client(client_phone_number)
        if client:
            raise Exception("The client has already been registered!")

        self.clients_list.append(Client(client_phone_number))
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if meal.__class__.__name__ in self.ALLOWED_MEALS:
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        result = ''
        for meal in self.menu:
            result += meal.details() + '\n'

        return result.strip()

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):

        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        client = self._get_client(client_phone_number)
        if not client:
            self.register_client(client_phone_number)

        client = self._get_client(client_phone_number)
        current_client_bill = client.bill
        current_client_meals = deepcopy(client.shopping_cart)
        current_menu = deepcopy(self.menu)

        for meal_name, quantity in meal_names_and_quantities.items():
            meal = self._get_meal(meal_name)

            if meal is None:
                client.bill = current_client_bill
                client.shopping_cart = current_client_meals
                self.menu = current_menu
                raise Exception(f"{meal_name} is not on the menu!")

            if quantity > meal.quantity:
                client.bill = current_client_bill
                client.shopping_cart = current_client_meals
                self.menu = current_menu
                raise Exception(f"Not enough quantity of {meal.__class__.__name__}: {meal_name}!")

            if meal_name not in client.ordered_meals:
                client.ordered_meals[meal_name] = 0

            client.ordered_meals[meal_name] += quantity
            client.shopping_cart.append(meal)
            client.bill += meal.price * quantity
            meal.quantity -= quantity

        return (f"Client {client_phone_number} successfully ordered "
                f"{', '.join([meal.name for meal in client.shopping_cart])} for {client.bill:.2f}lv.")

    def cancel_order(self, client_phone_number: str):
        client = self._get_client(client_phone_number)

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        for meal, quantity in client.ordered_meals.items():
            for menu_meal in self.menu:
                if menu_meal.name == meal:
                    menu_meal.quantity += quantity

        client.shopping_cart = []
        client.ordered_meals = {}
        client.bill = 0
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = self._get_client(client_phone_number)

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        self.receipt_id += 1
        client_total_bill = client.bill
        client.bill = 0
        client.shopping_cart = []
        client.ordered_meals = {}
        return (f"Receipt #{self.receipt_id} with total amount of {client_total_bill:.2f} was successfully"
                f" paid for {client_phone_number}.")

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."

    def _get_meal(self, meal_name: str):
        meal = [meal for meal in self.menu if meal.name == meal_name]
        return meal[0] if meal else None

    def _get_client(self, phone_number):
        client = [client for client in self.clients_list if client.phone_number == phone_number]
        return client[0] if client else None