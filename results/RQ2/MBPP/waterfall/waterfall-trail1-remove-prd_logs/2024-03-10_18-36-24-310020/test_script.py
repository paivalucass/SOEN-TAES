def extract_freq(test_list):
    # Input validation
    if not all(isinstance(t, tuple) for t in test_list):
        raise ValueError("Input list should only contain tuples")
    if len(test_list) == 0:
        raise ValueError("Input list should not be empty")
    
    # Extract unique tuples
    unique_tuples = set(test_list)
    
    # Return the count
    return len(unique_tuples)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_freq([(3, 4), (1, 2), (4, 3), (5, 6)]), 3)

if __name__ == '__main__':
    unittest.main()