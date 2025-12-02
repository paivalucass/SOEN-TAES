def freq_count(list1):
    frequency_count = {}
    for element in list1:
        if not isinstance(element, (int, float)):
            return "Error: Non-numeric elements found in the input list"
        if element in frequency_count:
            frequency_count[element] += 1
        else:
            frequency_count[element] = 1
    return frequency_count
import unittest

class Test(unittest.TestCase):
    def test_freq_count(self):
        self.assertEqual(freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30]), {10: 4, 20: 4, 40: 2, 50: 2, 30: 1})

if __name__ == '__main__':
    unittest.main()