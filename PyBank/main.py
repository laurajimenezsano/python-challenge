## PyBank Financial Analysis

#Import and read csv file

import os
import csv

# ADD new columns for new data: month count and difference between profits and losses.
months = []
profit_losses = []

# setting counts to 0

num_rows = 0
total = 0
current_month = 0
prev_month = 0
change = 0
difference = 0

# open file
pybank_csv = os.path.join("Resources", "budget_data.csv")

# reader and next row to avoid headers
with open(pybank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    header = next(csvreader)

# for each row: count number of rows
    for row in csvreader:
        #count of months, given that they are unique
        num_rows += 1
        #setting current month as the first row and taking total as the value
        current_month = int(row[1])
        total += current_month

        #setting conditional to start with difference on the following row
        if (num_rows == 1):
            prev_month = current_month
            continue
        
        else:
                #difference between rows
                difference = current_month - prev_month
                months.append(row[0])
                profit_losses.append(difference)
                prev_month = current_month


# average of difference

difference_total = sum(profit_losses)
difference_avg = round(difference_total/(num_rows - 1),2)

#   * The greatest increase in profits (date and amount) over the entire period
#max(changes) and which date; identify row for each

difference_max = max(profit_losses)
index_max = profit_losses.index(difference_max)
month_max = months[index_max]

#   * The greatest decrease in losses (date and amount) over the entire period

difference_min = min(profit_losses)
index_min = profit_losses.index(difference_min)
month_min = months[index_min]

# * In addition, your final script should both print the analysis to the terminal and export a text file with the results.

print(f'''

"Financial Analysis"
________________________________________

"Total Months: " {num_rows}
"Total: $" {total}
"Average ChangeL $" {difference_avg}
"Greatest Increase in Profits: "{month_max} " $"{difference_max}
"Greatest Decrease in Profits: "{month_max} " $"{difference_max}
''')
