def max_run_uppercase(test_str):
    max_count = 0
    count = 0
    for char in test_str:
        if char.isupper():
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    return max_count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_run_uppercase('GeMKSForGERksISBESt'), 5)

if __name__ == '__main__':
    unittest.main()