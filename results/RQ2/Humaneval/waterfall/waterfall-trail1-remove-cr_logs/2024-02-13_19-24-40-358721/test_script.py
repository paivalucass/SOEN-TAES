def make_a_pile(n):
    result = [n]
    current_stones = n
    for i in range(1, n):
        if current_stones % 2 == 0:
            current_stones += 1
        else:
            current_stones += 2
        result.append(current_stones)
    return result
import unittest

class Test(unittest.TestCase):
    def test_make_a_pile(self):
        self.assertEqual(make_a_pile(3), [3, 5, 7])
        self.assertEqual(make_a_pile(4), [4, 6, 8, 10])
        self.assertEqual(make_a_pile(5), [5, 7, 9, 11, 13])

if __name__ == '__main__':
    unittest.main()