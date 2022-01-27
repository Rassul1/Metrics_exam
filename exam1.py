import unittest
import math

MORE = "More zero"
INV = "Invalid"
LESS = "Less zero"

def results(x):
    print("Input:",x)
    result = ""
    if type(x) == float:
        num = math.gamma(x)
        if num> 0:
            result = MORE
        else:
            result = LESS
    else:
        result = INV
    print(result,"\n")
    return result


class TestDevisionResults(unittest.TestCase):
    def test_MoreThatZero(self):
        self.assertEqual(results(8), MORE)

    def test_LessThatZero(self):
        self.assertEqual(results(-0.1), LESS)

    def test_invalid(self):
        self.assertEqual(results("d"), INV)

if __name__ == 'main':
    unittest.main()