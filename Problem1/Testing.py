import unittest
import Problem1
class TestStringMethods(unittest.TestCase):

    def test1(self):
        input = "https://www.google.com/some-path"
        expected = ["https","www.google.com","some-path"]
        actual = Problem1.URLSplit("https://www.google.com/some-path")
        self.assertEqual(expected, actual)
    
    def test2(self):
        input = "ftp://bu.edu/"
        expected = ["ftp","bu.edu",""]
        actual = Problem1.URLSplit("ftp://bu.edu/")
        self.assertEqual(expected, actual)

    

if __name__ == '__main__':
    unittest.main()
