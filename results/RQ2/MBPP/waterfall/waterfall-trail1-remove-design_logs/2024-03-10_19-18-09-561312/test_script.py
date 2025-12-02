def find_remainder(arr, n):
    result = 1
    for num in arr:
        result = (result * num) % n
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_remainder([100, 10, 5, 25, 35, 14], 11), 9)

if __name__ == '__main__':
    unittest.main()