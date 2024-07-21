from project1.team import Team
import unittest


class TestTeam(unittest.TestCase):
    def setUp(self):
        self.team = Team("team")

    def test_initializer_with_valid_data(self):
        self.assertEqual('team', self.team.name)
        self.assertEqual({}, self.team.members)

    def test_initializer_with_digits_in_name(self):
        with self.assertRaises(ValueError) as ve:
            self.team.name = '3'

        self.assertEqual("Team Name can contain only letters!", str(ve.exception))

    def test_add_member_method(self):
        result = self.team.add_member(Pesho=14, Ivan=12)
        self.assertEqual(2, len(self.team.members))
        self.assertEqual(2, len(self.team))
        self.assertEqual("Successfully added: Pesho, Ivan", result)
        self.assertEqual({"Pesho": 14, "Ivan": 12}, self.team.members)
        result = self.team.add_member(Gosho=16)
        self.assertEqual(3, len(self.team.members))
        self.assertEqual(3, len(self.team))
        self.assertEqual("Successfully added: Gosho", result)
        self.assertEqual({"Pesho": 14, "Ivan": 12, "Gosho": 16}, self.team.members)
        result = self.team.add_member(Mario=17, Koce=18)
        self.assertEqual(5, len(self.team.members))
        self.assertEqual(5, len(self.team))
        self.assertEqual("Successfully added: Mario, Koce", result)
        self.assertEqual({"Pesho": 14, "Ivan": 12, "Gosho": 16, "Mario": 17, "Koce": 18}, self.team.members)
        result = self.team.add_member(Mario=17, Koce=18)
        self.assertEqual(5, len(self.team.members))
        self.assertEqual(5, len(self.team))
        self.assertEqual("Successfully added: ", result)
        self.assertEqual({"Pesho": 14, "Ivan": 12, "Gosho": 16, "Mario": 17, "Koce": 18}, self.team.members)

    def test_add_member_method_without_member(self):
        result = self.team.add_member()
        self.assertEqual(0, len(self.team.members))
        self.assertEqual(0, len(self.team))
        self.assertEqual("Successfully added: ", result)

    def test_remove_member_method_with_non_existing_member(self):
        self.team.add_member(Pesho=14, Ivan=12)
        result = self.team.remove_member("Gosho")
        self.assertEqual("Member with name Gosho does not exist", result)
        self.assertEqual(2, len(self.team.members))

    def test_remove_member_method_with_valid_member(self):
        self.team.add_member(Pesho=14, Ivan=12)
        result = self.team.remove_member("Pesho")
        self.assertEqual("Member Pesho removed", result)
        self.assertEqual(1, len(self.team.members))
        self.assertEqual(1, len(self.team))
        self.assertNotIn("Pesho", self.team.members)
        self.assertEqual({"Ivan": 12}, self.team.members)
        result = self.team.remove_member("Ivan")
        self.assertEqual("Member Ivan removed", result)
        self.assertEqual(0, len(self.team.members))
        self.assertEqual(0, len(self.team))
        self.assertNotIn("Ivan", self.team.members)
        self.assertEqual({}, self.team.members)

    def test_gt_method(self):
        self.team.add_member(Pesho=14, Ivan=12)
        other_team = Team('teamA')
        other_team.add_member(Gosho=15)
        self.assertTrue(self.team > other_team)
        self.assertFalse(other_team > self.team)

    def test_len_method(self):
        self.team.add_member(Pesho=14, Ivan=12)
        self.assertEqual(2, len(self.team))
        self.team.add_member(Gosho=16)
        self.assertEqual(3, len(self.team))

    def test_add_method(self):
        self.team.add_member(Pesho=14, Ivan=12)
        other_team = Team('teamA')
        other_team.add_member(Gosho=15)
        new_team = self.team + other_team
        self.assertEqual("teamteamA", new_team.name)
        self.assertEqual(3, len(new_team))
        self.assertIn("Pesho", new_team.members)
        self.assertIn("Ivan", new_team.members)
        self.assertIn("Gosho", new_team.members)

    def test_str_method_with_equal_age(self):
        self.team.add_member(Pesho=14, Ivan=12, Atanas=12)
        expected = ("Team name: team\nMember: Pesho - 14-years old\nMember: Atanas - 12-years old"
                    "\nMember: Ivan - 12-years old")
        self.assertEqual(expected, str(self.team))

    def test_str_method(self):
        self.team.add_member(Pesho=14, Ivan=11, Atanas=12)
        expected = ("Team name: team\nMember: Pesho - 14-years old\nMember: Atanas - 12-years old"
                    "\nMember: Ivan - 11-years old")
        self.assertEqual(expected, str(self.team))

    def test_str_method_without_members(self):
        expected = "Team name: team"
        self.assertEqual(expected, str(self.team))


if __name__ == '__main__':
    unittest.main()
