def monotonic(l: list):
    """Return True if list elements are monotonically increasing or decreasing.
    
    Args:
    l (list): Input list
    
    Returns:
    bool: True if list is monotonically increasing or decreasing, False otherwise
    """
    
    if len(l) <= 1:
        return True
    
    increasing = all(l[i] <= l[i + 1] for i in range(len(l) - 1))
    decreasing = all(l[i] >= l[i + 1] for i in range(len(l) - 1))
    
    return increasing or decreasing
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(monotonic([1, 2, 4, 20]), True)
        self.assertEqual(monotonic([1, 20, 4, 10]), False)
        self.assertEqual(monotonic([4, 1, 0, -10]), True)

if __name__ == '__main__':
    unittest.main()