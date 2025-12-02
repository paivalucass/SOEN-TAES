def ascii_value(k):
    '''
    Write a function to find the ascii value of a character.
    Input: k (string) - a single character
    Output: ascii_val (integer) - the ASCII value of the input character
    Raises: ValueError - if the input is not a single character or not a string
    '''
    try:
        if len(k) != 1 or not isinstance(k, str):
            raise ValueError("Input must be a single character")

        ascii_val = ord(k)
        return ascii_val

    except ValueError as ve:
        print("Input validation error:", ve)
        return None
    except Exception as e:
        print("Error occurred:", e)
        return None
import unittest

class TestAsciiValue(unittest.TestCase):
    def test_ascii_value(self):
        self.assertEqual(ascii_value('A'), 65)

if __name__ == '__main__':
    unittest.main()