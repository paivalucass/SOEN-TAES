def max_run_uppercase(test_str):
    if not isinstance(test_str, str):
        raise TypeError("Input must be a string")

    if len(test_str) == 0:
        return 0

    max_run = 0
    current_run = 0

    for char in test_str:
        if char.isupper():
            current_run += 1
            max_run = max(max_run, current_run)
        else:
            current_run = 0

    return max_run
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_run_uppercase('GeMKSForGERksISBESt'), 5)

if __name__ == '__main__':
    unittest.main()