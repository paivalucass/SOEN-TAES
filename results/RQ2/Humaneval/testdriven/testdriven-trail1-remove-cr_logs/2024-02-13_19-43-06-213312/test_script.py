from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    unique_elements = []
    seen = set()
    for num in numbers:
        if num not in seen:
            unique_elements.append(num)
            seen.add(num)
    return unique_elements
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 2, 4]), [1, 3, 4])

if __name__ == '__main__':
    unittest.main()