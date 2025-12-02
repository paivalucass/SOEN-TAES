def max_val(input_list):
    if not isinstance(input_list, list) or not input_list:
        return None
    max_value = None
    for value in input_list:
        if isinstance(value, (int, float)):
            if max_value is None or value > max_value:
                max_value = value
    return max_value
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_val(['Python', 3, 2, 4, 5, 'version']), 5)

if __name__ == '__main__':
    unittest.main()