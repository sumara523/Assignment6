import unittest
import Problem4

class TestStringMethods(unittest.TestCase):

    def test1(self):
        input = 17
        expected = 10
        actual = Problem4.NumOnes(input)
        self.assertEqual(expected, actual)

    def test2(self):
        input = 8
        expected = 1
        actual = Problem4.NumOnes(input)
        self.assertEqual(expected, actual)

    def test3(self):
        input = 22
        expected = 13
        actual = Problem4.NumOnes(input)
        self.assertEqual(expected, actual)

    def test4(self):
        input = -3
        expected = 0
        actual = Problem4.NumOnes(input)
        self.assertEqual(expected, actual)

    def test5(self):
        input = 41
        expected = 15
        actual = Problem4.NumOnes(input)
        self.assertEqual(expected, actual)

    
    def test6(self):
        input = 134
        expected = 68
        actual = Problem4.NumOnes(input)
        self.assertEqual
        
if __name__ == '__main__':
    unittest.main()
