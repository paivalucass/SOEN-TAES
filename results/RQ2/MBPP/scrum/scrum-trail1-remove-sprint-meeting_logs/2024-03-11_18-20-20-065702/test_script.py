def count(lst):
    if not lst:
        return "Input list is empty. Please provide a non-empty list."

    count = 0
    for item in lst:
        if isinstance(item, bool) and item:
            count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count([True, False, True]), 2)

if __name__ == '__main__':
    unittest.main()