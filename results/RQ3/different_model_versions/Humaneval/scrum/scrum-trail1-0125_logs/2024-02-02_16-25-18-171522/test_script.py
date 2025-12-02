def add_elements(arr, k):
    sum_elements = 0

    for num in arr[:k]:
        if len(str(num)) <= 2:
            sum_elements += num

    return sum_elements
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4), 24)

if __name__ == '__main__':
    unittest.main()