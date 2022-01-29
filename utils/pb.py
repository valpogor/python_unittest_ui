from utils import *
import unittest

class pb(unittest.TestCase):
    def setUp(self):
        return self

    # .['03 07 43 51 56 14']
    # ['02 17 31 46 52 7']
    # '07 13 25 64 71 20'

    # def test_returnAllList(self):
    #     print(print_win_nPB(0, 0))
    #
    # def test_returnAllListReversed(self):
    #     print(reverseAllNumbersInList(removeAllSpaceInList(print_win_n(0, 0))))

    # def test_returnAllListReversed(self):
    #     print(reverseAllNumbersStringInList(print_win_n(0, 0)))

    # def test_splitList(self):
    #     print(splitList(print_win_n(0, 0)))

    # def test_returnFirstElementFromList(self):
    #     print(returnElementFromList(splitList(print_win_n(0, 0)),0))

    # def test_returnSum_1_repeatedOffen(self):
    #     print(printDuplicates(returnElementFromList(splitList(print_win_n(0, 0)),0)))
    #
    # def test_returnSum_2_repeatedOffen(self):
    #     print(printDuplicates(returnElementFromList(splitList(print_win_n(0, 0)), 1)))
    #
    # def test_returnSum_3_repeatedOffen(self):
    #     print(printDuplicates(returnElementFromList(splitList(print_win_n(0, 0)),2)))
    #
    # def test_returnSum_4_repeatedOffen(self):
    #     print(printDuplicates(returnElementFromList(splitList(print_win_n(0, 0)), 3)))
    #
    # def test_returnSum_5_repeatedOffen(self):
    #     print(printDuplicates(returnElementFromList(splitList(print_win_n(0, 0)), 4)))
    #
    # def test_returnSum_6_repeatedOffen(self):
    #     print(printDuplicates(returnElementFromList(splitList(print_win_n(0, 0)), 5)))
# win numbers
    def test_returnWinNumberRepeatedOffen(self):
        n=[]
        for i in range(6):
            n.append(printDuplicates(returnElementFromList(splitList(print_win_nPB(0, 0)), i)))
        results = ' '.join(n)
        print("pb offen: ", results)

    def test_returnWinNumberRepeatedNotOffen(self):
        n = []
        for i in range(6):
            n.append(printDuplicatesMin(returnElementFromList(splitList(print_win_nPB(0, 0)), i)))
        results = ' '.join(n)
        print("pb not offen: ", results)
    # def test_returnWinNumberRepeatedOffenReversed(self):
    #     n=[]
    #     for i in range(6):
    #         n.append(printDuplicates(returnElementFromList(splitList(reverseAllNumbersStringInList(print_win_n(0, 0))), i)))
    #     print(n)
    #
    # def test_returnWinNumberRepeatedNotOffenReversed(self):
    #     n = []
    #     for i in range(6):
    #         n.append(printDuplicatesMin(returnElementFromList(splitList(reverseAllNumbersStringInList(print_win_n(0, 0))), i)))
    #     print(n)

    # def test_returnAllListNoSpace(self):
    #     print(removeAllSpacveInList(print_win_n(0, 0)))
    #
    # def test_returnSum_6_repeatedOffen(self):
    #     print(printDuplicates(testSumAllInlist(removeAllSpaceInList(print_win_n(0, 0)))))
    #
    # def test_return_6_repeated(self):
    #     print(printDuplicates(print_win_n(0, 0)))



if __name__ == "__main__":
    unittest.main()

