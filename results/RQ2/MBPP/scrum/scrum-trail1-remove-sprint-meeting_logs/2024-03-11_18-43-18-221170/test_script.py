def find_Average_Of_Cube(n):
    total = 0
    for i in range(1, n+1):
        total += i**3
    return total / n
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Average_Of_Cube(2), 4.5)

if __name__ == '__main__':
    unittest.main()