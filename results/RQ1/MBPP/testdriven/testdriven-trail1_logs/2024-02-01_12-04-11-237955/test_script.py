def check_integer(text):
    try:
        text = text.strip()
        int(text)  # try to convert the text to an integer
        return True
    except ValueError:
        return False
    except Exception as e:
        raise e

assert check_integer("python")==False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_integer('python'), False)

if __name__ == '__main__':
    unittest.main()