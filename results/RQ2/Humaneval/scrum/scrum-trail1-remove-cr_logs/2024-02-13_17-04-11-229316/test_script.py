def add(lst):
    if not lst:
        raise ValueError("Input list cannot be empty")

    if not all(isinstance(x, int) for x in lst):
        raise ValueError("Input list must contain only integers")

    sum_even_odd_indices = 0
    for i in range(1, len(lst), 2):
        if lst[i] % 2 == 0:
            sum_even_odd_indices += lst[i]

    return sum_even_odd_indices
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(add([4, 2, 6, 7]), 2)

if __name__ == '__main__':
    unittest.main()