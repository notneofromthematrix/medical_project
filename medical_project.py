#!/usr/bin/python3.11

import csv

with open('insurance.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]
    for row in data:
        print(row)



