from typing import List


class Hero:
    def __init__(self,name: str,  hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp

    def cast_spell(self, mp_needed: int, spell_name: str):
        if self.mp >= mp_needed:
            self.mp -= mp_needed
            print(f'{self.name} has successfully cast {spell_name} and now has {self.mp} MP!')
        else:
            print(f'{self.name} does not have enough MP to cast {spell_name}!')

    def take_damage(self, damage: int, attacker: str):
        self.hp -= damage
        if self.hp > 0:
            print(f'{self.name} was hit for {damage} HP by {attacker} and now has {self.hp} HP left!')

    def recharge(self, amount: int):
        self.mp += amount
        recovered_amount = amount
        if self.mp > 200:
            recovered_amount = amount - (self.mp - 200)
            self.mp = 200

        print(f'{self.name} recharged for {recovered_amount} MP!')

    def heal(self, amount: int):
        self.hp += amount
        recovered_amount = amount
        if self.hp > 100:
            recovered_amount = amount - (self.hp - 100)
            self.hp = 100

        print(f'{self.name} healed for {recovered_amount} HP!')

    def print_information(self):
        print(f'{self.name}\n  HP: {self.hp}\n  MP: {self.mp}')


def fill_heroes(heroes: List[Hero], num_of_lines: int):
    for _ in range(num_of_lines):
        hero_name, hp, mp = input().split()
        hero = Hero(hero_name, int(hp), int(mp))
        heroes.append(hero)

    return heroes


def process_commands(heroes_: List[Hero]):
    while True:
        text = input()

        if text == 'End':
            break

        command_args = text.split(' - ')
        hero_name = command_args[1]
        hero = [h for h in heroes if h.name == hero_name][0]

        if command_args[0] == 'CastSpell':
            mp_needed = int(command_args[2])
            spell_name = command_args[3]
            hero.cast_spell(mp_needed, spell_name)

        elif command_args[0] == 'TakeDamage':
            damage = int(command_args[2])
            attacker = command_args[3]
            hero.take_damage(damage, attacker)
            if hero.hp <= 0:
                heroes_.remove(hero)
                print(f'{hero_name} has been killed by {attacker}!')

        elif command_args[0] == 'Recharge':
            amount = int(command_args[2])
            hero.recharge(amount)

        elif command_args[0] == 'Heal':
            amount = int(command_args[2])
            hero.heal(amount)

    return heroes_


heroes = []
n = int(input())

heroes = fill_heroes(heroes, n)
heroes = process_commands(heroes)
[h.print_information() for h in heroes]