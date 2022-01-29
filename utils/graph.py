import matplotlib.pyplot as p
from itertools import count
import numpy as np
import pylab
import csv

def plot_classes(x, y, plotfun=p.scatter, **kwargs):
    classes = sorted(set(x))
    class_dict = dict(zip(classes, count()))
    class_map = lambda x: class_dict[x]
    plotfun(map(class_map, x), y, **kwargs)
    p.xticks(np.arange(len(classes)), classes)
#
# plot_classes(data["class"], data["y"], marker="+")

dates = []
numbers = []
lastnumbers = []
with open("mm.csv", "r", newline="") as file:
    reader = csv.reader(file, delimiter=",")
    for row in reader:
        dates.append(row[0])
        numbers.append(row[1])
        lastnumbers.append(row[2])
    dates.pop(0)
    numbers.pop(0)
    lastnumbers.pop(0)

# pylab.figure(1)
# x = range(len(dates))
# pylab.xticks(x, dates)
# pylab.plot(x,lastnumbers,"g")
p.bar(range(len(lastnumbers)), lastnumbers) #bar example
# p.plot(lastnumbers)
p.show()

# make up some data for this example
# t = range(len(numbers))
# s = 7 * t + 5
# # make up some data labels which we want to appear in place of the symbols
# x = 8 * "dp".split()
# y = map(str, range(8))
# data_labels = [ i+j for i, j in zip(x, y)]
# fig = p.figure()
# ax1 = fig.add_subplot(111)
# ax1.plot(t, s, "o", mfc="#FFFFFF")     # set the symbol color so they are invisible
# for a, b, c in zip(t, s, data_labels) :
#     ax1.text(a, b, c, color="green")
#
# p.show()