def filter_data(students, min_height, min_weight):
    if not isinstance(students, dict) or not all(isinstance(val, (int, float)) for sublist in students.values() for val in sublist):
        return "Invalid input"

    filtered_students = {}
    for student, data in students.items():
        if data[0] >= min_height and data[1] >= min_weight:
            filtered_students[student] = data
    return filtered_students
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(filter_data({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)},6.0,70), {'Cierra Vega': (6.2, 70)})

if __name__ == '__main__':
    unittest.main()