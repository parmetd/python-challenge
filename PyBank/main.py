#PyBank

import os
import pandas as pd 
import csv
#Dependencies

csv_bank = os.path.join('Resources', 'budget_data.csv')

total_months = 0
total_pl = 0
value = 0
change = 0
dates = []
profits = []

with open(csv_bank, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first 
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")


    #Reading the first row (so that we track the changes properly)
    first_row = next(csvreader)
    total_months += 1
    total_pl += int(first_row[1])
    value = int(first_row[1])

    # Read each row of data after the header
    for row in csvreader:
     #   print(row)
        # Keeping track of the dates
        dates.append(row[0])
        
        # Calculate the change, then add it to list of changes
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])
        
        #Total number of months
        total_months += 1

        #Total net amount of "Profit/Losses over entire period"
        total_pl = total_pl + int(row[1])
        #total_pl = '${:,.2f}'.format(total_pl)
        #total_pl = addCommas(total_pl)
#format... ("${:,}".format)
#pandas work because _df=pd. etc
#file_df["avg_cost"] = file_df["avg_cost"].map("${:.2f}".format)
#file_df["population"] = file_df["population"].map("{:,}".format)
#file_df["other"] = file_df["other"].map("{:.2f}".format)

    #Greatest increase in profits
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]
    greatest_increase = '${:,.2f}'.format(greatest_increase)

    #Greatest decrease (lowest increase) in profits 
    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = dates[worst_index]
    greatest_decrease = '${:,.2f}'.format(greatest_decrease)

    #Average change in "Profit/Losses between months over entire period"
    avg_change = sum(profits)/len(profits)
    avg_change = round(avg_change,2)
    avg_change = '${:,.2f}'.format(avg_change)

    total_pl = '${:,.2f}'.format(total_pl)

#Displaying information
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: {str(total_pl)}")
print(f"Average Change: {str(avg_change)}")
print(f"Greatest Increase in Profits: {greatest_date} ({str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {worst_date} ({str(greatest_decrease)})")
print("--------------------------")
print("Output.txt created")
print("--------------------------")

#Exporting to .txt file
output = open("output.txt", "w")

line1 = "Financial Analysis"
line2 = "---------------------"
line3 = str(f"Total Months: {str(total_months)}")
line4 = str(f"Total: ${str(total_pl)}")
line5 = "---------------------"
line6 = str(f"Average Change: ${str(avg_change)}")
line7 = str(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
line8 = str(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7,line8))

#total_pl = '${:,.2f}'.format(total_pl)
