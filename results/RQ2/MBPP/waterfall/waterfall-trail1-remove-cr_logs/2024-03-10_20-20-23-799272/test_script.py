def max_run_uppercase(test_str):
    max_run = 0
    current_run = 0
    
    if test_str is None or len(test_str) == 0:
        return 0
    
    for char in test_str:
        if char.isupper():
            current_run += 1
        else:
            max_run = max(max_run, current_run)
            current_run = 0
    
    max_run = max(max_run, current_run)
    
    return max_run
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_run_uppercase('GeMKSForGERksISBESt'), 5)

if __name__ == '__main__':
    unittest.main()