def max_run_uppercase(test_str):
    if test_str is None or len(test_str) == 0:
        return 0
    
    max_run_count = 0
    current_run_count = 0
    
    for char in test_str:
        if char.isupper():
            current_run_count += 1
            max_run_count = max(max_run_count, current_run_count)
        else:
            current_run_count = 0
    
    return max_run_count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_run_uppercase('GeMKSForGERksISBESt'), 5)

if __name__ == '__main__':
    unittest.main()