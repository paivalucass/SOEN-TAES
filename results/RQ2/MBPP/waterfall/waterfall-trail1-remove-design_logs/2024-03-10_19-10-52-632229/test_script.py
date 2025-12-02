def split_two_parts(list1, L):
    if not list1:
        raise ValueError("List1 is empty")
    if L < 0 or L > len(list1):
        raise ValueError("L is out of bounds")

    try:
        first_part = list1[:L]
        second_part = list1[L:]
        return (first_part, second_part)
    except Exception as e:
        raise ValueError("Invalid input")
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(split_two_parts([1,1,2,3,4,4,5,1], 3), ([1, 1, 2], [3, 4, 4, 5, 1]))

if __name__ == '__main__':
    unittest.main()