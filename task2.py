#Use both Bus_Stops.csv and Street_Centerlines.csv to find out number of busstops that are

import csv

f = open("Bus_Stops.csv", 'r')
f1 = open("Street_Centrelines.csv", 'r')


def task2():
    street = []
    nstreet = []
    for r in f1:
        nr = r.split(",")
        if nr[10] == "ARTERIAL":
            s = nr[4].strip()
            if s not in street:
                 street.append(s)
    buss = []
    for st in nstreet:
        for d in f1:
            n = d.split(",")
            if n[7] == "Accessible":
                h = n[6].strip()
                h = h.lower()
                if h.find(st) >= 0:
                     buss.append(n[2])

print(task2())
