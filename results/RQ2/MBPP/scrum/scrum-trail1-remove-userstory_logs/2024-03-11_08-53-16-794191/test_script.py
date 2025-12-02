def index_minimum(test_list):
    if not test_list or not all(isinstance(item, tuple) for item in test_list):
        raise ValueError("Input list is empty or contains non-tuple elements")

    min_second_value = float('inf')
    result_tuple = None
    for item in test_list:
        if len(item) != 2:
            raise ValueError("Tuple does not have exactly two elements")
        if item[1] < min_second_value:
            min_second_value = item[1]
            result_tuple = item

    if result_tuple is None:
        raise ValueError("No valid tuple found in the input list")

    return result_tuple[0] # returning the first value of the tuple with the smallest second value
import unittest

class Test(unittest.TestCase):
    def test_index_minimum(self):
        self.assertEqual(index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]), 'Varsha')

if __name__ == '__main__':
    unittest.main()