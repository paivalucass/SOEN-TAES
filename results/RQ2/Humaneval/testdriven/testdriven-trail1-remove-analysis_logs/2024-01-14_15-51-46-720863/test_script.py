def numerical_letter_grade(grades):
    grade_boundaries = {
        4.0: 'A+',
        3.7: 'A',
        3.3: 'A-',
        3.0: 'B+',
        2.7: 'B',
        2.3: 'B-',
        2.0: 'C+',
        1.7: 'C',
        1.3: 'C-',
        1.0: 'D+',
        0.7: 'D',
        0.0: 'D-',
        -1: 'E'
    }
    letter_grades = []
    for g in grades:
        for boundary, letter in sorted(grade_boundaries.items(), reverse=True):
            if g >= boundary:
                letter_grades.append(letter)
                break
    return letter_grades
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]), ['A+', 'B', 'C-', 'C', 'A-'])

if __name__ == '__main__':
    unittest.main()