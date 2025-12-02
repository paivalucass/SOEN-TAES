from collections import Counter

def freq_count(input_list):
    if not isinstance(input_list, list):
        raise ValueError("Input must be a list")
    
    frequencies = dict(Counter(input_list))
    return frequencies
import unittest

class Test(unittest.TestCase):
    def test_freq_count(self):
        self.assertEqual(freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30]), {10: 4, 20: 4, 40: 2, 50: 2, 30: 1})

if __name__ == '__main__':
    unittest.main()