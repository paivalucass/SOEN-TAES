def closest_integer(value):
    try:
        input_number = float(value)
        if input_number % 1 < 0.5:
            return int(input_number)
        else:
            return int(input_number) + 1 if input_number > 0 else int(input_number) - 1
    except ValueError:
        return "Invalid Input"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(closest_integer('10'), 10)
        self.assertEqual(closest_integer('15.3'), 15)
        self.assertEqual(closest_integer('14.5'), 15)
        self.assertEqual(closest_integer('-14.5'), -15)

if __name__ == '__main__':
    unittest.main()