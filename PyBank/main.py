## PyBank Financial Analysis

#Import and read csv file

import os
import csv

pybank_csv = os.path.join("Resources", "budget_data.csv")

# The total number of months included in the dataset

num_rows = 0

# The net total amount of "Profit/Losses" over the entire period

total = 0

#   * Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes



#   * The greatest increase in profits (date and amount) over the entire period
#max(changes) and which date

#   * The greatest decrease in losses (date and amount) over the entire period

#min(changes) and which date

# * As an example, your analysis should look similar to the one below:

#   ```text
#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)
#   ```

# * In addition, your final script should both print the analysis to the terminal and export a text file with the results.

with open(pybank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    header = next(csvreader)

    for row in csvreader:
        num_rows += 1
        total += int(row[1])

print(num_rows)
print(total)
