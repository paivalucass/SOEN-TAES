from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    try:
        if not isinstance(values, list):
            raise ValueError("Input value must be a list")
        else:
            integer_list = [value for value in values if isinstance(value, int)]
            return integer_list
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Test cases
print(filter_integers(['a', 3.14, 5]))  # Output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(filter_integers(['a', 3.14, 5]), [5])
    
    def test2(self):
        self.assertEqual(filter_integers([1, 2, 3, 'abc', {}, []]), [1, 2, 3])

if __name__ == '__main__':
    unittest.main()