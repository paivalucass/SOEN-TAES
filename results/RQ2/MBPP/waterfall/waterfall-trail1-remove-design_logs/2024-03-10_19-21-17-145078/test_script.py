def get_ludic(n):
    ludic_numbers = []
    for num in range(1, n + 1):
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            ludic_numbers.append(num)
    return ludic_numbers
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_ludic(10), [1, 2, 3, 5, 7])

if __name__ == '__main__':
    unittest.main()