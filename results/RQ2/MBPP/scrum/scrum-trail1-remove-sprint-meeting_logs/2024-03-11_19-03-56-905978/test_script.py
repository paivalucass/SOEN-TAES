class Student:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight


def filter_data(students, h, w):
    result = {}
    for name, (height, weight) in students.items():
        if height >= h and weight >= w:
            result[name] = (height, weight)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(filter_data({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)},6.0,70), {'Cierra Vega': (6.2, 70)})

if __name__ == '__main__':
    unittest.main()