def numerical_letter_grade(grades):
    grade_map = {
        4.0: "A+",
        3.7: "A",
        3.3: "A-",
        3.0: "B+",
        2.7: "B",
        2.3: "B-",
        2.0: "C+",
        1.7: "C",
        1.3: "C-",
        1.0: "D+",
        0.7: "D",
        0.0: "D-"
    }
    letter_grades = []
    for gpa in grades:
        if gpa < 0 or gpa > 4.0:
            letter_grades.append("Error: GPA out of range")
        else:
            for key in sorted(grade_map.keys(), reverse=True):
                if gpa >= key:
                    letter_grades.append(grade_map[key])
                    break
    return letter_grades
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]), ['A+', 'B', 'C-', 'C', 'A-'])

if __name__ == '__main__':
    unittest.main()