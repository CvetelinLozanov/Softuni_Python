from project.student import Student
import unittest


class StudentTest(unittest.TestCase):
    def setUp(self):
        courses = {"Fundamentals": ['test', "test_1"], "Advanced": ["test_advanced"]}
        self.student = Student("Pesho", courses)

    def test_initializer_with_empty_courses(self):
        student = Student("Pesho")
        self.assertDictEqual({}, student.courses)

    def test_initializer_with_courses(self):
        courses = {"Fundamentals": ['test', "test_1"], "Advanced": ["test_advanced"]}
        self.assertDictEqual(courses, self.student.courses)

    def test_enroll_method_with_new_course_without_add_course_notes(self):
        result = self.student.enroll("SQL", ["test_SQL"])
        courses = {"Fundamentals": ['test', "test_1"], "Advanced": ["test_advanced"], "SQL": ["test_SQL"]}
        self.assertDictEqual(courses, self.student.courses)
        self.assertEqual(3, len(self.student.courses))
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_method_with_new_course_with_add_course_notes(self):
        result = self.student.enroll("Django", ["test_django"], "Y")
        courses = {"Fundamentals": ['test', "test_1"], "Advanced": ["test_advanced"], "Django": ["test_django"]}
        self.assertDictEqual(courses, self.student.courses)
        self.assertEqual(3, len(self.student.courses))
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_method_with_existing_course(self):
        result = self.student.enroll("Fundamentals", ["test_fund", "test_fund1"])
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual(4, len(self.student.courses["Fundamentals"]))
        self.assertIn('test_fund', self.student.courses["Fundamentals"])
        self.assertIn('test_fund1', self.student.courses["Fundamentals"])

    def test_enroll_method_with_no_as_add_course_notes(self):
        result = self.student.enroll("SQL", ["SQL_test"], "N")
        self.assertEqual("Course has been added.", result)
        self.assertIn("SQL", self.student.courses)
        self.assertEqual(3, len(self.student.courses))
        self.assertListEqual([], self.student.courses["SQL"])
        self.assertEqual(0, len(self.student.courses["SQL"]))

    def test_add_notes_method_with_existing_course(self):
        result = self.student.add_notes("Fundamentals", "fund_test")
        self.assertEqual("Notes have been updated", result)
        self.assertIn("fund_test", self.student.courses["Fundamentals"])
        self.assertEqual(3, len(self.student.courses["Fundamentals"]))

    def test_add_notes_method_with_non_existing_course(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("SQL", "SQL_test")

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))
        self.assertEqual(2, len(self.student.courses))

    def test_leave_course_method_with_existing_course(self):
        result = self.student.leave_course("Fundamentals")
        self.assertEqual("Course has been removed", result)
        self.assertEqual(1, len(self.student.courses))
        self.assertNotIn("Fundamentals", self.student.courses)

    def test_leave_course_method_with_non_existing_course(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("SQL")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))
        self.assertEqual(2, len(self.student.courses))

if __name__ == '__main__':
    unittest.main()