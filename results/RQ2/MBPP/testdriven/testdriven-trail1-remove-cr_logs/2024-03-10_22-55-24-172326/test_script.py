def check_K(test_tup, K):
    elements_dict = {}
    for element in test_tup:
        if element in elements_dict:
            elements_dict[element] += 1
        else:
            elements_dict[element] = 1
    
    return K in elements_dict
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_K((10, 4, 5, 6, 8), 6), True)

if __name__ == '__main__':
    unittest.main()