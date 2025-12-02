def bell_number(n):
    if n < 0:
        return "Invalid Input"
    bell = [0] * (n+1)
    bell[0] = 1
    for i in range(1, n+1):
        prev_bell = bell[i-1]
        for j in range(i+1):
            temp = bell[j]
            bell[j] = prev_bell + (bell[j-1] if j-1 >= 0 else 0)
            prev_bell = temp
    return bell[n]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(bell_number(2), 2)

if __name__ == '__main__':
    unittest.main()