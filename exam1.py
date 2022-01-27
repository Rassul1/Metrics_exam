import unittest
import math

more = "More zero"
inv = "Invalid"
less = "Less zero"

def results(x):
    print("Input:",x)
    result = ""
    if type(x) == float:
        num = math.gamma(x)
        if num> 0:
            result = more
        else:
            result = less
    else:
        result = inv
    print(result,"\n")
    return result


class TestDevisionResults(unittest.TestCase):
    def test_MoreThatZero(self):
        self.assertEqual(results(8), more)

    def test_LessThatZero(self):
        self.assertEqual(results(-0.1), less)

    def test_Invalid(self):
        self.assertEqual(results("d"), inv)

if __name__ == 'main':
    unittest.main()