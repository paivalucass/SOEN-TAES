def get_ludic(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")

    ludic_numbers = [1]
    unpicked_numbers = set(range(2, n+1))

    for num in range(2, n+1):
        if num in unpicked_numbers:
            ludic_numbers.append(num)
            unpicked_numbers -= set(range(num, n+1, num))

    return ludic_numbers
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_ludic(10), [1, 2, 3, 5, 7])

if __name__ == '__main__':
    unittest.main()