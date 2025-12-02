def round_and_sum(list1):
    if all(isinstance(num, (int, float)) for num in list1):
        total_sum = sum(round(num) for num in list1)
        return total_sum * len(list1)
    else:
        raise ValueError("List should contain only numeric values")
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50]), 243)

if __name__ == '__main__':
    unittest.main()