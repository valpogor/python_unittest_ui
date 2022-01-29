from decimal import Decimal, getcontext
import csv
from datetime import datetime
import datetime
import random, math
from collections import Counter
from dateutil.parser import parse

myfilepath='mm.csv'
myfilepathPB='pb.csv'

def pi_mm(n):
    TERMS = [(12, 18), (8, 57), (-5, 239)]  # ala Gauss
    def arctan(talj, kvot):
        summation = 0
        talj *= product
        qfactor = 1
        while talj:
            talj //= kvot
            summation += (talj // qfactor)
            qfactor += 2
        return summation
    number_of_places = int(n)
    getcontext().prec = number_of_places
    product = 10 ** number_of_places
    result = 0
    for multiplier, denominator in TERMS:
        denominator = Decimal(denominator)
        result += arctan(- denominator * multiplier, - (denominator ** 2))
    result *= 4  # pi == atan(1) * 4
    string = str(result)
    p = string[0:string.index("E")]
    return p

def convertStrListToInt(list):
    for i in range(0, len(list)):
        list[i] = int(list[i])
    return list
# print(convertStrListToInt(print_win_n(0, 0)))

def users():
    d1 = datetime.date(2021, 1, 1)
    d2 = datetime.date(2021, 12, 31)
    days = [d1 + datetime.timedelta(days=x) for x in range((d2 - d1).days + 1)]
    us=[]
    for day in days:
        us.append(day.strftime('%d%m%Y'))
    return us

def userTimesPi(user, pi):
    user=convertStrListToInt(users())[user]
    p=pi_mm(pi)
    return (Decimal(p) * user)

def numberYears(days):
    n=[]
    for day in range(days):
        n.append(str(Decimal(userTimesPi(day,366))).replace(".", ""))
    return (n)

# print(convertStrListToInt(users())[0])
# print(pi_mm(366))
# print(userTimesPi(0,366))
# print(numberYears(365)[2])#second user number
print(str(numberYears(365)[1]).replace(".",""))#first user number
print(numberYears(365)[1])#first user number

def checkIfPresent(n, user):
    if n in str(numberYears(365)[user]).replace(".",""):
        return True
# print(checkIfPresent("2057", 2))

# def print_win_n(line_number, n):
#     with open(myfilepath, 'r') as f:
#         mycsv = csv.reader(f)
#         mycsv = list(mycsv)
#         text = mycsv[line_number][n]+" "+mycsv[line_number][n+1]
#     return text

def filePars(file, year):
    with open(file, 'r') as f:
        mycsv = csv.reader(f)
        mycsv = list(mycsv)
        all=[]
        years=[]
        new=[]
        for i in range(len(mycsv)):
            all.append(mycsv[i][1])
            years.append(mycsv[i][0])
        # else:
        # for i in range(len(mycsv)):
        #     all.append(mycsv[i][1] + " " + mycsv[i][2])
        #     years.append(mycsv[i][0])
        y = []
        # for i in range(len(years)):
        #     y.append(convertDate(years[i]))
        for i in range(len(mycsv)):
            new.append([convertDate(mycsv[i][0]),mycsv[i][1]])
        if str(year)!="":
            for i in range(len(new)):
                if str(year) in new[i][0]:
                    y.append(new[i][1])
            return y
        else:
            return all

def fileParsYear(file):
    with open(file, 'r') as f:
        mycsv = csv.reader(f)
        mycsv = list(mycsv)
        # all=[]
        years=[]
        new=[]
        for i in range(len(mycsv)):
            # all.append(mycsv[i][1])
            years.append(mycsv[i][0])
        # else:
        # for i in range(len(mycsv)):
        #     all.append(mycsv[i][1] + " " + mycsv[i][2])
        #     years.append(mycsv[i][0])
        # y = []
        # for i in range(len(years)):
        #     y.append(convertDate(years[i]))
        for i in range(len(mycsv)):
            new.append([convertDate(mycsv[i][0]),mycsv[i][1]])
        # if year!="":
        # for i in range(len(new)):
        #     if year in new[i][0]:
        #         y.append(new[i][1])
        return new
        # else:
        #     return all


def parsingFile(file, line_n, n):
    with open(file, 'r') as f:
        mycsv = csv.reader(f)
        mycsv = list(mycsv)
        all=[]
        if line_n != 0 and n != 0:
            text = mycsv[line_n][n]+" "+mycsv[line_n][n+1]
            return text
        else:
            for i in range(len(mycsv)):
                all.append(mycsv[i][1])
            # all.pop(0)
            return all

def print_win_n(line_n, n):
    with open(myfilepath, 'r') as f:
        mycsv = csv.reader(f)
        mycsv = list(mycsv)
        all=[]
        if line_n != 0 and n != 0:
            text = mycsv[line_n][n]+" "+mycsv[line_n][n+1]
            return text
        else:
            for i in range(len(mycsv)):
                all.append(mycsv[i][1])
            # all.pop(0)
            return all
# print(print_win_n(0,0))
def print_win_nPB(line_n, n):
    with open(myfilepathPB, 'r') as f:
        mycsv = csv.reader(f)
        mycsv = list(mycsv)
        all=[]
        if line_n != 0 and n != 0:
            text = mycsv[line_n][n]+" "+mycsv[line_n][n+1]
            return text
        else:
            for i in range(len(mycsv)):
                all.append(mycsv[i][1])
            # all.pop(0)
            return all

def removeAllSpaceInList(list):
    l = [num.replace(' ', '') for num in list]
    return l

def sumAllNumbers(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

def testSumAllInlist(list):
    result = []
    for i in range(len(list)):
        result.append(sumAllNumbers(int(list[i])))
    return result


# print(sumAllNumbers(int("042642506024")))
# print(testSumAllInlist(removeAllSpaceInList(print_win_n(0, 0))))
# print(testSumAllInlist(removeAllSpaceInList(print_win_nPB(0, 0))))
# l2=['03 10 43 61 51 14', '03 07 43 51 56 14', '07 13 25 64 71 20', '02 17 31 46 52 7','03 13 49 56 37 25', '01 12 39 53 59 24']
# print(testSumAllInlist(removeAllSpaceInList(l2)))
# print(removeAllSpacveInList(print_win_n(0, 0)))
# print(print_win_n(2, 1))

def reverseNumber(n):
    reversed = int(str(n)[::-1])
    return reversed

def reverseString(n):
    reversed = str(n)[::-1]
    return reversed

def reverseAllNumbersInList(list):
    l=[]
    for i in range(len(list)):
        l.append(reverseNumber(list[i]))
    return l

def reverseAllNumbersStringInList(list):
    l=[]
    for i in range(len(list)):
        l.append(reverseString(list[i]))
    return l

def splitList(list):
    l=[]
    for i in range(len(list)):
        l.append(list[i].split())
    return l

def returnElementFromList(list, n):
    l=[]
    for i in range(len(list)):
        l.append(list[i][n])
    return l

def printDuplicates(list):
    temp = set(list)
    result = {}
    for i in temp:
        result[i] = list.count(i)
    # for key, values in result.items():
    #     if values>1:
    #         print(key, ":", values)
    return max(result, key=result.get)

def printDuplicatesMin(list):
    temp = set(list)
    result = {}
    for i in temp:
        result[i] = list.count(i)
    # for key, values in result.items():
    #     if values>1:
    #         print(key, ":", values)
    return min(result, key=result.get)


# print(printDuplicates(print_win_n(0, 0)))
# print(printDuplicates(testSumAllInlist(removeAllSpaceInList(print_win_n(0, 0)))))
# print(printDuplicates(testSumAllInlist(removeAllSpaceInList(print_win_nPB(0, 0)))))
# print(print_win_n(0, 0))

def print_win_numbers_return_string(line_n, n):
    with open(myfilepath, 'r') as f:
        mycsv = csv.reader(f)
        mycsv = list(mycsv)
        all=[]
        if line_n != 0 and n != 0:
            text = mycsv[line_n][n]+" "+mycsv[line_n][n+1]
            return text
        else:
            for i in range(len(mycsv)):
                all.append(str(mycsv[i][1]+" "+mycsv[i][2]).replace(" ",""))
            all.pop(0)
            return all

# print(print_win_numbers_return_string(0, 0))

def getShortestNumber(n):
    numbers=[]
    for i in range(len(print_win_numbers_return_string(0, 0))):
        numbers.append(print_win_numbers_return_string(0, 0)[i][:-n])
    return numbers

# print(getShortestNumber(2))#removed last 2 digits
def checkAllNumbersIn365():
    # print(getShortestNumber(2))
    # print(len(getShortestNumber(2)))
    # print(getShortestNumber(2)[0])
    # print(len(numberYears(365)))
    # print(numberYears(365)[0])
    # for i in range(len(getShortestNumber(2))):
    for i in range(365):
        # print(getShortestNumber(2)[i])
        # print(numberYears(365)[i])
        # for j in range(len(numberYears(365))):
            if getShortestNumber(2)[i] in numberYears(365)[i]:
                print(i+") " +getShortestNumber(2)[i]+" win number found in user: "+numberYears(365)[i] +" is : "+True)
        #         break
            else:
                print(i)

            # print(len(print_win_numbers_return_string(0, 0)))
# print(checkAllNumbersIn365())

def split_by_num(n):
    return print_win_n(0, 0)[n].split()
# print(split_by_num(0))


def createListByNumber(n):
    list=[]
    for i in range(len(print_win_n(0, 0))):
        list.append(split_by_num(i)[n])
    return list
# print(createListByNumber(0))

def createListSplitNumber(list):
    l=[]
    for i in range(len(list)):
        l.append(split_by_num(i))
    return l
# print(createListSplitNumber(print_win_n(0, 0)))

def countAllNumberBy2(list):
    l=[]
    # n=[]
    for i in range(len(list)):
        # print(len(list[i]))
        for j in range(len(list[i])):
            # print(list[i][j])
            # print("1: ",len(list[j]))
            # print("2: ",len(list[i]))
            # print("3: ",len(list))
            # n = []
            # n.append(list[i])
            print(list[i][j])
            # print(sum(n))
            break
    return l
# print(countAllNumberBy2(createListSplitNumber(print_win_n(0, 0))))




def findInPi(n):
    if int(createListByNumber(n)[n]) in int(pi_mm()):
        print(int(createListByNumber(n)[n]))

def lenghtOfList(list):
    lenght=len(list)
    return lenght

def countDuplicates(list):
    my_dict = {i: list.count(i) for i in list}
    return my_dict

# print(lenghtOfList(createListByNumber(1)))
# print(int(createListByNumber(0)[0]))
# print(createListByNumber(1)) #print all seconds numbers from all winners
# print(createListByNumber(2))
# print(createListByNumber(3))
# print(createListByNumber(4))
# print(createListByNumber(5))
# print(split_by_num(1)) #print second from list whole win number
# print(print_win_n(0, 0)[1].split()) #print second from list whole win number
# print(convertStrListToInt(createListByNumber(1))) #int print second from list whole win number
# print(countDuplicates(convertStrListToInt(createListByNumber(1))))

# print(print_win_n(0,0))


# 70
# 25
def unique_rand():
    data = []
    i = 0
    while i < 5:
        number = random.randint(1, 70)
        if number not in data:
            data.append(number)
            i += 1
    data.sort()
    data.append(random.randint(1, 25))
    return data
# print(unique_rand())



def createBanchOfNumbers(n):
    numbers=[]
    for i in range(n):
        numbers.append(unique_rand())
    return numbers
# print(createBanchOfNumbers(100))

def comparingNumver(numbers, n):
    for i in range(numbers):
        if n == createBanchOfNumbers(numbers)[i]:
            print(createBanchOfNumbers(numbers)[i])
        # else:
        #     print(createBanchOfNumbers(numbers)[i], " no matches")

# comparingNumver(10000, "[10, 19, 26, 28, 50, 16]")


# print(fiveRandow())

def printWinsReversed(file, freq):
    n = []
    if freq=='offen':
        for i in range(6):
            n.append(printDuplicates(returnElementFromList(splitList(reverseAllNumbersStringInList(parsingFile(file,0, 0))), i)))
        results = ' '.join(n)
        print(file, "offen: ", results)
    else:
        for i in range(6):
            n.append(printDuplicatesMin(
                returnElementFromList(splitList(reverseAllNumbersStringInList(parsingFile(file, 0, 0))), i)))
        results = ' '.join(n)
        print(file, "not offen: ", results)

def printWins(file, freq):
    n = []
    if freq=='offen':
        for i in range(6):
            n.append(printDuplicates(returnElementFromList(splitList(parsingFile(file,0, 0)), i)))
        results = ' '.join(n)
        print(file, "offen: ", results)
    else:
        for i in range(6):
            n.append(printDuplicatesMin(
                returnElementFromList(splitList(parsingFile(file, 0, 0)), i)))
        results = ' '.join(n)
        print(file, "not offen: ", results)

def printWinsList(list, freq):
    n = []
    # print(printDuplicates(returnElementFromList(splitList(reverseAllNumbersStringInList(parsingFile(file, 0, 0))), i)))
    # for i in range(6):
    #     print(printDuplicates(returnElementFromList(splitList(reverseAllNumbersStringInList(list)), i)))

    # print(printDuplicates(list))
    # print(list)
    # print(splitList(list))
    #     print(printDuplicates(returnElementFromList(splitList(list), i)))

    if freq=='offen':
        for i in range(6):
            n.append(printDuplicates(returnElementFromList(splitList(list), i)))
        results = ' '.join(n)
        # print(list, "offen: ", results)
    else:
        for i in range(6):
            n.append(printDuplicatesMin(returnElementFromList(splitList(list), i)))
        results = ' '.join(n)
        # print(list, "not offen: ", results)
    return results

def convertDate(d):
    dt = parse(d)
    return dt.strftime('%m/%d/%Y')

def overwriteFile(file, first, second):
    x = [first, second]
    with open (file,'wb') as f:
        wtr = csv.writer(f)
        wtr.writerow(x)

def sum_digits(digit):
    return sum(int(x) for x in digit if x.isdigit())

