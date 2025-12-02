def filter_data(students, h, w):
    if not isinstance(students, dict):
        raise TypeError("Input 'students' must be a dictionary")
    if not all(isinstance(val, (int, float)) for val in [h, w]):
        raise TypeError("Input 'h' and 'w' must be numeric values")

    filtered_students = {}
    for student, (height, weight) in students.items():
        if height >= h and weight >= w:
            filtered_students[student] = (height, weight)

    return filtered_students
import unittest

class Test(unittest.TestCase):
    def test_filter_data(self):
        self.assertEqual(filter_data({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}, 6.0, 70), {'Cierra Vega': (6.2, 70)})

if __name__ == '__main__':
    unittest.main()