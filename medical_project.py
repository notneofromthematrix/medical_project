#!/usr/bin/python3.11

import csv

with open('insurance.csv') as records_csv:
    output = records_csv.read()

print(output)

