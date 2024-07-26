from typing import List, Optional
from project.baked_food.baked_food import BakedFood
from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.drink import Drink
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.table.table import Table


class Bakery:
    VALID_FOOD = {"Bread": Bread, "Cake": Cake}
    VALID_DRINKS = {"Tea": Tea, "Water": Water}
    VALID_TABLES = {"InsideTable": InsideTable, "OutsideTable": OutsideTable}

    def __init__(self, name: str):
        self.name = name
        self.food_menu: List[BakedFood] = []
        self.drinks_menu: List[Drink] = []
        self.tables_repository: List[Table] = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        # food = self.__find_prod_by_name(name, self.food_menu)
        food = self.__find_food_by_name(name)

        if food:
            raise Exception(f"{food_type} {name} is already in the menu!")

        if food_type in self.VALID_FOOD:
            food = self.VALID_FOOD[food_type](name, price)
            self.food_menu.append(food)
            return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        # drink = self.__find_prod_by_name(name, self.drinks_menu)
        drink = self.__find_drink_by_name(name)
        if drink:
            raise Exception(f"{drink_type} {name} is already in the menu!")

        if drink_type in self.VALID_DRINKS:
            drink = self.VALID_DRINKS[drink_type](name, portion, brand)
            self.drinks_menu.append(drink)
            return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        table = self.__find_table_by_number(table_number)
        if table:
            raise Exception(f"Table {table_number} is already in the bakery!")

        if table_type in self.VALID_TABLES:
            table = self.VALID_TABLES[table_type](table_number, capacity)
            self.tables_repository.append(table)
            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        table = self.__find_appropriate_table(number_of_people)

        if not table:
            return f"No available table for {number_of_people} people"

        table.reserve(number_of_people)
        return f"Table {table.table_number} has been reserved for {number_of_people} people"

    def order_food(self, table_number: int, *food_names):
        ordered_food = []
        unordered_food = []
        result = [f"Table {table_number} ordered:"]
        table = self.__find_table_by_number(table_number)
        if not table:
            return f"Could not find table {table_number}"

        # return self.__make_orders(self.food_menu, table, *food_names)
        for food in food_names:
            food_from_menu = self.__find_food_by_name(food)
            if food_from_menu:
                table.food_orders.append(food_from_menu)
                ordered_food.append(food_from_menu)
            else:
                unordered_food.append(food)

        [result.append(repr(f)) for f in ordered_food]
        result.append(f"{self.name} does not have in the menu:")
        [result.append(uf) for uf in unordered_food]
        return '\n'.join(result)

    def order_drink(self, table_number: int, *drink_names):
        ordered_drinks = []
        unordered_drinks = []
        result = [f"Table {table_number} ordered:"]
        table = self.__find_table_by_number(table_number)
        if not table:
            return f"Could not find table {table_number}"

        # return self.__make_orders(self.food_menu, table, *food_names)
        for food in drink_names:
            food_from_menu = self.__find_food_by_name(food)
            if food_from_menu:
                table.food_orders.append(food_from_menu)
                ordered_drinks.append(food_from_menu)
            else:
                unordered_drinks.append(food)

        [result.append(repr(f)) for f in ordered_drinks]
        result.append(f"{self.name} does not have in the menu:")
        [result.append(uf) for uf in unordered_drinks]
        return '\n'.join(result)

    def leave_table(self, table_number: int):
        table = self.__find_table_by_number(table_number)
        bill = table.get_bill()
        self.total_income += bill
        table.clear()
        return f"Table: {table_number}\nBill: {bill:.2f}"

    def get_free_tables_info(self):
        result = [t.free_table_info() for t in self.tables_repository if not t.is_reserved]
        return '\n'.join(result)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"

    # def __make_orders(self, type_of_order, table, *products):
    #     ordered_food = []
    #     unordered_food = []
    #     result = [f"Table {table.table_number} ordered:"]
    #     for prod in products:
    #         prod_from_bakery = self.__find_prod_by_name(prod, type_of_order)
    #         if prod_from_bakery:
    #             if prod_from_bakery.__class__.__bases__[0].__name__ == 'BakedFood':
    #                 table.food_orders.append(prod_from_bakery)
    #                 ordered_food.append(prod_from_bakery)
    #             elif prod_from_bakery.__class__.__bases__[0].__name__ == 'Drink':
    #                 table.drink_orders.append(prod_from_bakery)
    #                 ordered_food.append(prod_from_bakery)
    #         else:
    #             unordered_food.append(prod)
    #
    #     [result.append(repr(f)) for f in ordered_food]
    #     result.append(f"{self.name} does not have in the menu:")
    #     [result.append(uf) for uf in unordered_food]
    #     return '\n'.join(result)

    # @staticmethod
    # def __find_prod_by_name(prod_name: str, type_of_prod):
    #     return next((f for f in type_of_prod if f.name == prod_name), None)

    def __find_food_by_name(self, food_name: str,):
        return next((f for f in self.food_menu if f.name == food_name), None)

    def __find_drink_by_name(self, drink_name: str):
        return next((d for d in self.drinks_menu if d.name == drink_name), None)

    def __find_table_by_number(self, table_number: int):
        return next((t for t in self.tables_repository if t.table_number == table_number), None)

    def __find_appropriate_table(self, number_of_people: int):
        return next((t for t in self.tables_repository if t.capacity >= number_of_people and not t.is_reserved), None)


