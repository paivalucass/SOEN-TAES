def freq_count(list1: list) -> dict:
    freq_dict = {}
    if list1 is None or len(list1) == 0:
        return freq_dict
    
    for element in list1:
        if element in freq_dict:
            freq_dict[element] += 1
        else:
            freq_dict[element] = 1
    
    return freq_dict
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30]), {10: 4, 20: 4, 40: 2, 50: 2, 30: 1})

if __name__ == '__main__':
    unittest.main()