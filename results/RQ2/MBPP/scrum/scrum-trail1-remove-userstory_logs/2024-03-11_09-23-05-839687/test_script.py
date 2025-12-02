def filter_data(students, min_height, min_weight):
    filtered_students = {name: (height, weight) for name, (height, weight) in students.items() if height >= min_height and weight >= min_weight}
    return filtered_students
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(filter_data({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}, 6.0, 70), {'Cierra Vega': (6.2, 70)})

if __name__ == '__main__':
    unittest.main()