def count_first_elements(test_tup):
    count = 0
    stack = [test_tup]

    while stack:
        current = stack.pop()
        for item in current:
            if isinstance(item, tuple):
                stack.extend(item)
            else:
                count += 1

    return count

assert count_first_elements((1, 5, 7, (4, 6), 10)) == 3
import unittest

class Test(unittest.TestCase):
    def test_count_first_elements(self):
        self.assertEqual(count_first_elements((1, 5, 7, (4, 6), 10)), 3)

if __name__ == '__main__':
    unittest.main()