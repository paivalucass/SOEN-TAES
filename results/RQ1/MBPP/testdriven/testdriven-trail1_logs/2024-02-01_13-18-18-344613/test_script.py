def left_insertion(a, x):
    '''
    Write a function to locate the left insertion point for a specified value in sorted order.
    https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-data-structure-exercise-24.php
    assert left_insertion([1,2,4,5],6)==4
    '''

    # Input validation
    if not a or not isinstance(a, list):
        return "Invalid input for 'a'"
    if not isinstance(x, (int, float)):
        return "Invalid input for 'x'"

    # Logic to find insertion point
    index = 0
    for i in range(len(a)):
        if a[i] < x:
            index = i + 1
        else:
            break
    return index
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(left_insertion([1,2,4,5], 6), 4)

if __name__ == '__main__':
    unittest.main()