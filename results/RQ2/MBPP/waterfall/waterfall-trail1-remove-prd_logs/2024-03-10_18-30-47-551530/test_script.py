def frequency(a, x):
    if not isinstance(a, list) or not all(isinstance(i, (int, float)) for i in a) or not (isinstance(x, (int, float)) or isinstance(x, list)):
        return "Invalid input. Please provide a list of numbers for 'a' and a number or list of numbers for 'x'."

    if len(a) == 0:
        return [0] if isinstance(x, list) else 0

    if isinstance(x, list):
        return [sum(1 for num in a if num == i) for i in x]
    
    count = 0
    for num in a:
        if num == x:
            count += 1
    
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(frequency([1,2,3], 4), 0)

if __name__ == '__main__':
    unittest.main()