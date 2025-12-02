def round_and_sum(list1):
    if not list1:
        return "Error: Empty input list"

    for num in list1:
        if not isinstance(num, (int, float)):
            return "Error: Non-numeric values in the list"

    rounded_sum = sum(round(num) for num in list1)

    return rounded_sum * len(list1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50]), 243)

if __name__ == '__main__':
    unittest.main()