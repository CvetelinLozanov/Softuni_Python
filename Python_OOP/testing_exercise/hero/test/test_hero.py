from testing_exercise.hero.project.hero import Hero
import unittest


class HeroTest(unittest.TestCase):

    def setUp(self):
        self.hero = Hero("Robocop", 10, 100, 10)

    def test_initializing(self):
        self.assertEqual("Robocop", self.hero.username)
        self.assertEqual(10, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(5, self.hero.damage)

    def test_battle_method_with_same_hero_name(self):
        hero = Hero("Robocop", 100, 100, 50)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_method_with_health_equal_zero(self):
        hero = Hero("Robocop", 100, 0, 50)
        hero_1 = Hero("Ivan", 100, 100, 50)
        with self.assertRaises(ValueError) as ex:
            hero.battle(hero_1)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_method_with_health_lower_than_zero(self):
        hero = Hero("Robocop", 100, -1, 50)
        hero_1 = Hero("Ivan", 100, 100, 50)
        with self.assertRaises(ValueError) as ex:
            hero.battle(hero_1)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_method_with_enemy_hero_health_less_than_zero(self):
        hero = Hero("Robocop", 100, 100, 50)
        enemy_hero = Hero("Ivan", 100, -1, 50)
        with self.assertRaises(ValueError) as ex:
            hero.battle(enemy_hero)

        self.assertEqual(f"You cannot fight {enemy_hero.username}. He needs to rest", str(ex.exception))

    def test_battle_method_with_enemy_hero_health_equal_zero(self):
        hero = Hero("Robocop", 100, 100, 50)
        enemy_hero = Hero("Ivan", 100, 0, 50)
        with self.assertRaises(ValueError) as ex:
            hero.battle(enemy_hero)

        self.assertEqual(f"You cannot fight {enemy_hero.username}. He needs to rest", str(ex.exception))

    def test_battle_method_when_draw_with_zero_health(self):
        enemy_hero = Hero("Ivan", 10, 100, 10)
        result = self.hero.battle(enemy_hero)
        self.assertEqual(0, self.hero.health)
        self.assertEqual(0, enemy_hero.health)
        self.assertEqual("Draw", result)

    def test_battle_method_when_draw_with_negative_health(self):
        enemy_hero = Hero("Ivan", 10, 100, 11)
        hero = Hero("Robocop", 10, 100, 11)
        result = hero.battle(enemy_hero)
        self.assertEqual(-10, self.hero.health)
        self.assertEqual(-10, enemy_hero.health)
        self.assertEqual("Draw", result)

    def test_battle_method_when_enemy_hero_health_become_zero(self):
        enemy_hero = Hero("Ivan", 5, 100, 10)
        result = self.hero.battle(enemy_hero)
        self.assertEqual(0, enemy_hero.health)
        self.assertEqual(11, self.hero.level)
        self.assertEqual(55, self.hero.health)
        self.assertEqual(15, self.hero.damage)
        self.assertEqual("You win", result)

    def test_battle_method_when_enemy_hero_health_become_less_than_zero(self):
        enemy_hero = Hero("Ivan", 5, 50, 10)
        result = self.hero.battle(enemy_hero)
        self.assertEqual(-50, enemy_hero.health)
        self.assertEqual(11, self.hero.level)
        self.assertEqual(55, self.hero.health)
        self.assertEqual(15, self.hero.damage)
        self.assertEqual("You win", result)

    def test_battle_method_when_enemy_hero_win_the_battle_with_zero_health(self):
        enemy_hero = Hero("Ivan", 10, 110, 10)
        result = self.hero.battle(enemy_hero)
        self.assertEqual(11, enemy_hero.level)
        self.assertEqual(15, enemy_hero.health)
        self.assertEqual(15, enemy_hero.damage)
        self.assertEqual(0, self.hero.health)
        self.assertEqual("You lose", result)

    def test_battle_method_when_enemy_hero_win_the_battle_with_negative_health(self):
        enemy_hero = Hero("Ivan", 11, 110, 10)
        result = self.hero.battle(enemy_hero)
        self.assertEqual(12, enemy_hero.level)
        self.assertEqual(15, enemy_hero.health)
        self.assertEqual(15, enemy_hero.damage)
        self.assertEqual(-10, self.hero.health)
        self.assertEqual("You lose", result)

    def test_str_representing_method(self):
        result = str(self.hero)
        self.assertEqual(f"Hero Robocop: 10 lvl\nHealth: 100\nDamage: 10\n", result)

    def test_str_representing_method_after_battle(self):
        enemy_hero = enemy_hero = Hero("Ivan", 5, 100, 10)
        self.hero.battle(enemy_hero)
        result = str(self.hero)
        self.assertEqual(f"Hero Robocop: 11 lvl\nHealth: 55\nDamage: 15\n", result)



if __name__ == '__main__':
    unittest.main()