def string_to_tuple(input_string: str) -> tuple:
    try:
        if not isinstance(input_string, str):
            raise TypeError("Input is not a string")
        
        return tuple(input_string)
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(string_to_tuple('python 3.0'), ('p', 'y', 't', 'h', 'o', 'n', ' ', '3', '.', '0'))

if __name__ == '__main__':
    unittest.main()