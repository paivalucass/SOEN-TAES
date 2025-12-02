def is_sublist(l, s):
    """
    Function to check whether a list contains the given sublist or not.
    :param l: main list
    :param s: sublist
    :return: True if the sublist is found in the main list, otherwise False
    """

    if not isinstance(l, list) or not isinstance(s, list):
        return False  # input validation

    if len(s) == 0:
        return True  # an empty list is always a sublist

    if len(s) > len(l):
        return False  # sublist is longer than main list

    for i in range(len(l) - len(s) + 1):
        if l[i:i + len(s)] == s:
            return True  # found the sublist

    return False  # sublist not found

#Function to check whether a list contains the given sublist or not.
assert is_sublist([2,4,3,5,7],[3,7])==False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_sublist([2,4,3,5,7],[3,7]), False)

if __name__ == '__main__':
    unittest.main()