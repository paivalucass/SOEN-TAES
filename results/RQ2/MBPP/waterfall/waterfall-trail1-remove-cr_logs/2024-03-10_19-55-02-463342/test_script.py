def extract_singly(test_list):
    result_set = set()

    def flatten_list(input_list):
        for i in input_list:
            if isinstance(i, list):
                flatten_list(i)
            else:
                if isinstance(i, int):
                    result_set.add(i)
                else:
                    raise ValueError("Error: Non-numeric value found in the input list")
    flatten_list(test_list)
    return result_set
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_singly([(3, 4, 5), (4, 5, 7), (1, 4)]), {1, 3, 4, 5, 7})

if __name__ == '__main__':
    unittest.main()