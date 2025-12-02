def number_of_substrings(input_string):
    if not isinstance(input_string, str):
        raise TypeError("Input should be a string")
    
    if len(input_string) == 0:
        return 0

    count = 0
    for i in range(len(input_string)):
        for j in range(i+1, len(input_string)+1):
            if input_string[i:j]:
                count += 1
    
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(number_of_substrings('abc'), 6)

if __name__ == '__main__':
    unittest.main()