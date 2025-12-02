def check_integer(text: str) -> bool:
    if text.isnumeric():
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_integer('python'), False)

if __name__ == '__main__':
    unittest.main()