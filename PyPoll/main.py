#PyPoll

import os
import pandas as pd 
import csv
#Dependencies

csv_poll = os.path.join('Resources', 'election_data.csv')


with open(csv_poll, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # print(csvreader)

    # Read the header row first 
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        #print(row)

# create a dictionary of a candidate
# add dictionary to an array
# run loop through array for each candidate get count.
# count total votes
# count each candidate's votes
# Percentage for each candidate is candidate / votes
# Print Results
# Export Results