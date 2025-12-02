def get_ludic(n):
    ludic_numbers = [1]
    num = 2
    while len(ludic_numbers) < n:
        if all(num % i != 0 for i in ludic_numbers):
            ludic_numbers.append(num)
        num += 1
    return ludic_numbers
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_ludic(10), [1, 2, 3, 5, 7])

if __name__ == '__main__':
    unittest.main()