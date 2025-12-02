def my_dict(input_dict: dict) -> bool:
    if bool(input_dict):
        return False
    else:
        return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(my_dict({}), True)

if __name__ == '__main__':
    unittest.main()