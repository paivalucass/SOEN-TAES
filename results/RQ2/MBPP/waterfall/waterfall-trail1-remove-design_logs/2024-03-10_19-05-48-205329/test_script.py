def index_minimum(test_list):
    if not test_list:
        return None
    min_second_value = min(test_list, key=lambda x: x[1])[1]
    result = [item[0] for item in test_list if item[1] == min_second_value][0]
    return result
import unittest

class Test(unittest.TestCase):
    def test_index_minimum(self):
        self.assertEqual(index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]), 'Varsha')

if __name__ == '__main__':
    unittest.main()