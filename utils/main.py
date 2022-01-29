from utils import *
import unittest

class main(unittest.TestCase):
    def setUp(self):
        return self

    # def test_returnAllList(self):
    #     print(print_win_n(0, 0))
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

    # def test_returnWinNumberRepeatedOffenReversed(self):
    #     n=[]
    #     for i in range(6):
    #         n.append(printDuplicates(returnElementFromList(splitList(reverseAllNumbersStringInList(print_win_n(0, 0))), i)))
    #     results = ' '.join(n)
    #     print("mm offen: ",results)
    #
    # def test_returnWinNumberRepeatedNotOffenReversed(self):
    #     n = []
    #     for i in range(6):
    #         n.append(printDuplicatesMin(returnElementFromList(splitList(reverseAllNumbersStringInList(print_win_n(0, 0))), i)))
    #     results = ' '.join(n)
    #     print("mm not offen: ", results)

    # def test_printWins(self):
    #     printWins('mm.csv', 'offen')
    # #     printWins('mm.csv', 'not')
    #     printWins('pb.csv', 'offen')
    # #     printWins('pb.csv', 'not')

    def test_numbers_year(self):
        for i in range(12):
            year=2010+i
            win=printWinsList(filePars('pb.csv', year),'offen')
            print(year," PB offen is: "+win)
            n = int(win.replace(' ', ''))
            print(sumAllNumbers(n))
        for i in range(20):
            year = 2002 + i
            win=printWinsList(filePars('mm.csv', year),'offen')
            print(year, " MM offen is: " + win)
            n = int(win.replace(' ', ''))
            print(sumAllNumbers(n))

    # def test_numbers_month(self)://not ready
    #     for i in range(12):
    #         print(2010+i," PB offen is: "+printWinsList(filePars('pb.csv', 2010+i),'offen'))
    #     for i in range(20):
    #         print(2002 + i, " MM offen is: " + printWinsList(filePars('mm.csv', 2002 + i), 'offen'))


    # def test_returnAllListNoSpace(self):
    #     print(removeAllSpacveInList(print_win_n(0, 0)))
    #
    # def test_returnSum_6_repeatedOffen(self):
    #     print(printDuplicates(testSumAllInlist(removeAllSpaceInList(print_win_n(0, 0)))))
    #
    # def test_return_6_repeated(self):
    #     print(printDuplicates(print_win_n(0, 0)))


#######
    # def test_returnWinNumberRepeatedOffen(self):
    #     n=[]
    #     for i in range(6):
    #         n.append(printDuplicates(returnElementFromList(splitList(print_win_n(0, 0)), i)))
    #     print("repeated offen: ",n)
    #
    # def test_returnWinNumberRepeatedNotOffen(self):
    #     n = []
    #     for i in range(6):
    #         n.append(printDuplicatesMin(returnElementFromList(splitList(print_win_n(0, 0)), i)))
    #     print("repeated not offen: ",sorted(n))
    #
    # def test_returnSum(self):
    #     print("MM sum: ",printDuplicates(testSumAllInlist(removeAllSpaceInList(print_win_n(0, 0)))))
    #     print("PB sum: ",printDuplicates(testSumAllInlist(removeAllSpaceInList(print_win_nPB(0, 0)))))

if __name__ == "__main__":
    unittest.main()

