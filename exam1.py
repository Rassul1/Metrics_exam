import unittest
import math

MORE = "More zero"
INV = "Invalid"
LESS = "Less zero"

def results(X):
    print("Input:",X)
    result = ""
    if type(X) == float():
        num = math.gamma(X)
        if num> 0:
            result = MORE
        else:
            result = LESS
    else:
        result = INV
    print(result,"\n")
    return result


class TestDevisionResults(unittest.TestCase):
    def test_morethatzero(self):
        self.assertEqual(results(8), MORE)

    def test_lessthatzero(self):
        self.assertEqual(results(-0.1), LESS)

    def test_invalid(self):
        self.assertEqual(results("d"), INV)

if __name__ == 'main':
    unittest.main()
