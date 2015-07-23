from unittest import TestCase, TestLoader, TextTestRunner
from DetectEmpties import *

class DetectEmptyFolderTests(TestCase):

   def setup(self):
      print "setup"

def main():
	suite = TestLoader().loadTestsFromTestCase(DetectEmptyFolderTests)
	TextTestRunner().run(suite)
	
if __name__ == "__main__":
	main()
