def bell_Number(n): 
    bell_numbers = [1, 1]
    for i in range(2, n+1):
        bell_num = 0
        for j in range(i):
            bell_num += bell_numbers[j-1] * (i-j)
        bell_numbers.append(bell_num)
    return bell_numbers[n-1]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(bell_Number(2), 2)

if __name__ == '__main__':
    unittest.main()