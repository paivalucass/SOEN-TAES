def count_first_elements(test_tup):
    count = 0
    for elem in test_tup:
        if isinstance(elem, tuple):
            count += count_first_elements(elem)
        else:
            if elem == 4:
                break
            count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_first_elements((1, 5, 7, (4, 6), 10)), 3)

if __name__ == '__main__':
    unittest.main()