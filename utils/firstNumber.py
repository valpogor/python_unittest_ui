import csv
from getFile import getFiles
import unittest
import random as r
from datetime import date
from em import sendEmail
mm_file='mm.csv'
pb_file='pb.csv'

getFiles()
def win_n(file, line_n, n):
    with open(file, 'r') as f:
        mycsv = csv.reader(f)
        mycsv = list(mycsv)
        all=[]
        if line_n != 0 and n != 0:
            if file == 'mm.csv':
                text = mycsv[line_n][n]+" "+mycsv[line_n][n+1]
            else:
                text = mycsv[line_n][n]
            return text
        else:
            for i in range(len(mycsv)):
                if file == 'mm.csv':
                    all.append(str(mycsv[i][1]+" "+mycsv[i][2]))
                else:
                    all.append(str(mycsv[i][1]))
            all.pop(0)
            return all
def last_win(file):
    with open(file, 'r') as f:
        last_line = f.readlines()[-1]
    return last_line

def num_order(list, n1, n2):
    l=[]
    for i in list:
        l.append(i[n1:n2])
    return l


def mostBig(list_):
    l = list(map(int, list_))
    highest = max(l)
    return highest

def duplicates(list, min_max):
    temp = set(list)
    result = {}
    for i in temp:
        result[i] = list.count(i)
    if min_max=="min":
        return min(result, key=result.get)
    else:
        return max(result, key=result.get)

def array(lottery,n):
    l=''
    if n==1:
        l=num_order(win_n(lottery, 0, 0), 0, 2)
    elif n==2:
        l=num_order(win_n(lottery, 0, 0), 3, 5)
    elif n==3:
        l=num_order(win_n(lottery, 0, 0), 6, 8)
    elif n==4:
        l=num_order(win_n(lottery, 0, 0), 9, 11)
    elif n==5:
        l=num_order(win_n(lottery, 0, 0), 12, 14)
    elif n == 6:
        l = num_order(win_n(lottery, 0, 0), 15, 17)
    return l

def valid_list(l):
    evens, odds = 0, 0
    lows, highs = 0, 0
    for elem in l:
        if elem%2 == 0:
            evens += 1
        else:
            odds += 1
        if elem < 52:
            lows += 1
        else:
            highs += 1
    return evens <= 3 and odds <= 2 and lows <= 3 and highs <= 2

first_list = [r.randint(0, 70)]
second_list = []

for i in range(date.today().day):
    second_list.append(r.sample(range(1, 70), 5))
    while len(first_list) < 5:
        if not valid_list(first_list):
            first_list[-1] = r.randint(0, 70)
        else:
            first_list.append(r.randint(0, 70))

def luckyPrint():
    first = sorted(first_list)
    second = sorted(r.sample(range(1, 70), 5))+r.sample(range(1, 25), 1)
    third = []
    fourth = []
    mm = last_win(mm_file)
    pb = last_win(pb_file)
    for i in range(6):
        third.append(duplicates(array(mm_file, i+1), "max"))
        fourth.append(duplicates(array(pb_file, i+1), "max"))
    html = '''<html><body><p>Hi, I have the following numbers for you!</p>
            <p>1: '''+str(first)+'''</p>
            <p>2: '''+str(second)+'''</p>
            <p>MM: '''+str(third)+'''</p>
            <p>PB: '''+str(fourth)+'''</p>
            <p>"================="</p>
            <p>MM last won: '''+str(mm)+'''</p>
            <p>PB last won: '''+str(pb)+'''</p>
            </body></html>'''
    return html

if __name__ == '__main__':
    sendEmail(luckyPrint())
    unittest.main()
