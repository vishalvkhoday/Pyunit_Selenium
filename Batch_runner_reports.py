import unittest
import HtmlTestRunner


class StringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        print("1st statement\n\t")
        self.assertFalse('Foo'.isupper())
        print("This as been passed in isupper\n")
        print("second statement")
    def test_ValuePass(self):
        self.assertGreaterEqual(9,7, "True")
        print("Step pass")
        pass

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
    def Suite(self):
        suite= unittest.TestSuite()
        suite.addTest('test')
        map

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../Pyunit_Selenium/Reports', report_title="Functional Testing", report_name="TestExecution"))
    
    
    