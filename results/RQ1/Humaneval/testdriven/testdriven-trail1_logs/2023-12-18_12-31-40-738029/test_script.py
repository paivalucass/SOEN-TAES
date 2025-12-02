def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    if not lst or len(lst) < 2:
        raise ValueError("Input list should not be empty or should contain at least two elements")

    even_elements_at_odd_indices = [num for index, num in enumerate(lst) if index % 2 != 0 and num % 2 == 0]
    return sum(even_elements_at_odd_indices)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(add([4, 2, 6, 7]), 2)

if __name__ == '__main__':
    unittest.main()