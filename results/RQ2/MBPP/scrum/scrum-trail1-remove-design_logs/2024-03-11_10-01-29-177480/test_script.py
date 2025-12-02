def freq_count(list1):
    freq_dict = {}
    
    if isinstance(list1, list):
        for element in list1:
            if element in freq_dict:
                freq_dict[element] += 1
            else:
                freq_dict[element] = 1
        return freq_dict
    else:
        return "Input is not a list"
import unittest

class Test(unittest.TestCase):
    def test_freq_count(self):
        self.assertEqual(freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30]), {10: 4, 20: 4, 40: 2, 50: 2, 30: 1})

if __name__ == '__main__':
    unittest.main()