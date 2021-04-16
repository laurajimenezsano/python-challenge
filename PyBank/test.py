## PyBank Financial Analysis

#Import and read csv file

import os
import csv

pybank_csv = os.path.join("Resources", "budget_data.csv")

#Define the data

num_rows = 0

with open(pybank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)

    for row in csvreader:
        num_rows += 1

print(num_rows)
        