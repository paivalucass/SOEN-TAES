def list_to_float(test_list):
    try:
        result = [tuple(map(float, sublist)) for sublist in test_list]
    except (ValueError, TypeError) as e:
        print(f"Error: Non-convertible elements present in the input list")
        result = []
    
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(list_to_float([(3.0, 4.0), (1.0, 26.45), (7.32, 8.0), (4.0, 8.0)]), [(3.0, 4.0), (1.0, 26.45), (7.32, 8.0), (4.0, 8.0)])

if __name__ == '__main__':
    unittest.main()