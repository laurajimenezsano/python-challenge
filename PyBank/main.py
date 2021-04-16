## PyBank Financial Analysis

#Import and read csv file

import os
import csv

pybank_csv = os.path.join("Resources", "budget_data.csv")

# Define the data

def analysis(budget_data):
    month = str(budget_data[0])
    profit_losses = int(budget_data[1])

# The total number of months included in the dataset
    

# The net total amount of "Profit/Losses" over the entire period

netincome = sum(profit_losses)

#   * Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

#   * The greatest increase in profits (date and amount) over the entire period

#   * The greatest decrease in losses (date and amount) over the entire period

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
    csv_reader = csv.reader(csvfile, delimiter=",")

    for row in csvreader:
        print(sum(netincome)