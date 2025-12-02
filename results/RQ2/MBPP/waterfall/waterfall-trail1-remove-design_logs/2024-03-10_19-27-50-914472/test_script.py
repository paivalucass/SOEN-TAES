from typing import Union

def max_run_uppercase(test_str: str) -> Union[int, str]:
    if not test_str:
        return 0

    max_run = 0
    current_run = 0

    for char in test_str:
        if char.isupper():
            current_run += 1
            max_run = max(max_run, current_run)
        else:
            current_run = 0

    return max_run if max_run > 0 else "Invalid input"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_run_uppercase('GeMKSForGERksISBESt'), 5)

if __name__ == '__main__':
    unittest.main()