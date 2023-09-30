from gpt_number import ai
from gpt_number_unProbable import ai_n
from firstNumber import first_list, last_win, duplicates, array
import random as r
from em import sendEmail
from utils import extract_numbers
import csv
from getFile import getFiles
import unittest
from collections import defaultdict

mm_file = 'mm.csv'

getFiles()
def extract_mega_ball_numbers(filename):
    mega_balls = []
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            mega_ball = int(row['Mega Ball'])
            mega_balls.append(mega_ball)
    return mega_balls
def predict_next_number(numbers):
    successors = defaultdict(list)
    for i in range(len(numbers) - 1):
        successors[numbers[i]].append(numbers[i + 1])
    last_number = numbers[-1]
    if not successors[last_number]:
        return None
    return max(set(successors[last_number]), key=successors[last_number].count)
n=predict_next_number(extract_mega_ball_numbers(mm_file))
def luckyPrint():
    html = '''<html><body><p>Hi, I have the following numbers for you!</p>
            <p>MM last number is: 
            </p>''' + str(n) + '''</p>
            </body></html>'''
    return html


if __name__ == '__main__':
    sendEmail(luckyPrint())
    print(luckyPrint())
    unittest.main()
