def index_minimum(test_list):
    if len(test_list) == 0:
        return None
    if not all(isinstance(item[1], int) and item[1] > 0 for item in test_list):
        return "Invalid input data"
    min_tuple = min(test_list, key=lambda x: x[1])
    return min_tuple[0] if all(item[1] > 0 for item in test_list) else "Unexpected output"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]), 'Varsha')

if __name__ == '__main__':
    unittest.main()