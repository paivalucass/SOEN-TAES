def freq_count(list1):
    from collections import Counter
    return dict(Counter(list1))
import unittest

class Test(unittest.TestCase):
    def test_freq_count(self):
        self.assertEqual(freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30]), {10: 4, 20: 4, 40: 2, 50: 2, 30: 1})

if __name__ == '__main__':
    unittest.main()