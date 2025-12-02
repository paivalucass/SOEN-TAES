def odd_Equivalent(s, n):
    try:
        if s == "":
            return 0
        elif n <= 0:
            raise ValueError("Number of rotations should be a positive integer")
        else:
            s = s * (n % len(s))
            count = s.count("1")
            return count
    except ValueError as ve:
        return str(ve)
    except Exception as e:
        return str(e)
import unittest

class Test(unittest.TestCase):
    def test_odd_Equivalent(self):
        self.assertEqual(odd_Equivalent("011001", 6), 3)

if __name__ == '__main__':
    unittest.main()