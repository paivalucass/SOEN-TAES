def index_minimum(test_list):
    min_index = test_list.index(min(test_list, key=lambda x: x[1]))
    return test_list[min_index][0]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]), 'Varsha')

if __name__ == '__main__':
    unittest.main()