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

    def test3(self):
        input = "https://www.facebook.com/messages/t/2972109159468035"
        expected = ["https","www.facebook.com","messages/t/2972109159468035"]
        actual = Problem1.URLSplit("https://www.facebook.com/messages/t/2972109159468035")
        self.assertEqual(expected, actual)
    
    def test4(self):
        input = "https://github.com/sumara523/cs591_c2_assignment_6"
        expected = ["https","github.com","sumara523/cs591_c2_assignment_6"]
        actual = Problem1.URLSplit("https://github.com/sumara523/cs591_c2_assignment_6")
        self.assertEqual(expected, actual)

    def test5(self):
        input = "https://cs-people.bu.edu/dharmesh/teaching/cs591_sp20/assignments/assignment6/"
        expected = ["https","cs-people.bu.edu","dharmesh/teaching/cs591_sp20/assignments/assignment6/"]
        actual = Problem1.URLSplit("https://cs-people.bu.edu/dharmesh/teaching/cs591_sp20/assignments/assignment6/")
        self.assertEqual(expected, actual)

    def test6(self):
        input = "https://www.netflix.com/watch/70152014?trackId=200257859"
        expected = ["https","www.netflix.com","watch/70152014?trackId=200257859"]
        actual = Problem1.URLSplit("https://www.netflix.com/watch/70152014?trackId=200257859")
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
