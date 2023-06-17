import csv
from collections import deque, defaultdict
import math

def ai_n(file):
    def process_csv(filename, n):
        years = []
        first_numbers = []
        second_numbers = []
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                line = ', '.join(row)
                date_string = row[0]
                year = get_year(date_string)
                years.append(year)
                first_number = get_first_number_after_comma(line, n)
                second_number = get_first_number_after_second_comma(line)
                first_numbers.append(first_number)
                second_numbers.append(second_number)
        return years, first_numbers, second_numbers

    def get_year(date_string):
        parts = date_string.split('/')
        return parts[2]

    def get_first_number_after_comma(date_string, n):
        parts = date_string.split(',')
        numbers = parts[1]
        first_number = numbers.split()[n]
        return first_number
    def get_first_number_after_second_comma(date_string):
        parts = date_string.split(',')
        numbers = parts[2]
        first_number = numbers.strip()
        return first_number


    years, first, n = process_csv(file,0)
    years, second, n = process_csv(file,1)
    years, third, n = process_csv(file,2)
    years, fourth, n = process_csv(file,3)
    years, five, n = process_csv(file,4)
    years, six, n = process_csv(file,0)
    # print(years)
    # print(first[0],second[0],third[0],fourth[0],five[0])

    # class MostProbableNumber:
    #     def __init__(self, capacity):
    #         self.capacity = capacity
    #         self.queue = deque()
    #         self.counter = defaultdict(int)
    #     def new_number(self, num):
    #         if len(self.queue) == self.capacity:
    #             old_num = self.queue.popleft()
    #             self.counter[old_num] -= 1
    #             if self.counter[old_num] == 0:
    #                 del self.counter[old_num]
    #         self.queue.append(num)
    #         self.counter[num] += 1
    #
    #     def most_probable(self):
    #         return max(self.counter.items(), key=lambda x: x[1])[0]
    class MostUnprobableNumber:
        def __init__(self, capacity):
            self.capacity = capacity
            self.queue = deque()
            self.counter = defaultdict(int)
        def new_number(self, num):
            if len(self.queue) == self.capacity:
                old_num = self.queue.popleft()
                self.counter[old_num] -= 1
                if self.counter[old_num] == 0:
                    del self.counter[old_num]
            self.queue.append(num)
            self.counter[num] += 1

        def most_probable(self):
            return min(self.counter.items(), key=lambda x: x[1])[0]
    golden_ratio=1.61803398875
    pi=math.pi
    mpn = MostUnprobableNumber(1000)
    mpn1 = MostUnprobableNumber(1000)
    mpn2 = MostUnprobableNumber(1000)
    mpn3 = MostUnprobableNumber(1000)
    mpn4 = MostUnprobableNumber(1000)
    mpn5 = MostUnprobableNumber(1000)
    lot=[]
    for num in first:
        mpn.new_number(num)
    for num1 in second:
        mpn1.new_number(num1)
    for num2 in third:
        mpn2.new_number(num2)
    for num3 in fourth:
        mpn3.new_number(num3)
    for num4 in five:
        mpn4.new_number(num4)
    for num5 in n:
        mpn5.new_number(num5)
    lot.append(mpn.most_probable())
    lot.append(mpn1.most_probable())
    lot.append(mpn2.most_probable())
    lot.append(mpn3.most_probable())
    lot.append(mpn4.most_probable())
    lot.append(mpn5.most_probable())
    return lot
