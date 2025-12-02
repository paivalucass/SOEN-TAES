def empty_dit(input_list):
    if not isinstance(input_list, list):
        return "Invalid Input"
    return all(not d for d in input_list) if input_list else True
import unittest

class Test(unittest.TestCase):
    def test_empty_dit(self):
        self.assertEqual(empty_dit([{}, {}, {}]), True)

if __name__ == '__main__':
    unittest.main()