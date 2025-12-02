def extract_quotation(text):
    values = []
    start = 0
    while True:
        start = text.find('"', start)
        if start == -1:
            break
        end = text.find('"', start + 1)
        if end == -1:
            break
        values.append(text[start + 1:end])
        start = end + 1
    return values
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_quotation('Cortex "A53" Based "multi" tasking "Processor"'), ['A53', 'multi', 'Processor'])

if __name__ == '__main__':
    unittest.main()