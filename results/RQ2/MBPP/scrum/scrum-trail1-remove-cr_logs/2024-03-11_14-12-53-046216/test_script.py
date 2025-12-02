def get_ludic(n):
    ludic_numbers = []
    number = 1
    while len(ludic_numbers) < n:
        if all(number % i != 0 for i in range(2, int(number ** 0.5) + 1)):
            ludic_numbers.append(number)
        number += 1
    return [x for x in ludic_numbers if x <= n]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_ludic(10), [1, 2, 3, 5, 7])

if __name__ == '__main__':
    unittest.main()