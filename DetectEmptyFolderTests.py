from unittest import TestCase, TestLoader, TextTestRunner
from DetectEmpties import DetectEmpties


class DetectEmptyFolderTests(TestCase):
    def setup(self):
        self.empty = DetectEmpties()

    def testRecurseDeleteFolders(self):
        print("test todo")


def main():
    suite = TestLoader().loadTestsFromTestCase(DetectEmptyFolderTests)
    TextTestRunner().run(suite)


if __name__ == "__main__":
    main()
