def count_charac(str1):
    if not isinstance(str1, str) or any(not char.isalpha() and char != ' ' for char in str1):
        raise ValueError("Invalid input string. Input should only contain alphabets and spaces.")

    count = len(str1)

    return count

# Test the function with an example
assert count_charac("python programming")==18
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_charac('python programming'), 18)

if __name__ == '__main__':
    unittest.main()