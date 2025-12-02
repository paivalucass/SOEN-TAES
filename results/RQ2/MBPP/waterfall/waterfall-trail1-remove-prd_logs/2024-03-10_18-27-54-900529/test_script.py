def index_minimum(test_list):
    if not test_list:
        raise ValueError("Error handling - Empty input list")

    min_second_value = min(test_list, key=lambda x: x[1])[1]

    min_tuples = [t for t in test_list if t[1] == min_second_value]

    return min(min_tuples, key=lambda x: x[0])[0]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]), 'Varsha')

if __name__ == '__main__':
    unittest.main()