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

if __name__ == '__main__':
    # sendEmail(n)
    # print(extract_numbers())
    unittest.main()
