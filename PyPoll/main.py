#PyPoll

import os
import pandas as pd 
import csv
#Dependencies

csv_poll = os.path.join('Resources', 'election_data.csv')

Candidates = []
candidate_options = []
candidate_votes = []
total_votes = 0
# create a list of a candidate

with open(csv_poll, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # print(csvreader)

    # Read the header row first 
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

# search of unique for Candidates.append("") to candidates
# count total votes
# Read each row of data after the header
    for row in csvreader:
        #print(row)
        total_votes = total_votes + 1
        total_candidates = row["Candidate"]

        if row["Candidate"] not in candidate_options:

            candidate_options.append(row["Candidate"])

            candidate_votes[row["Candidate"]] = 1

        else:
            candidate_votes[row["Candidate"]] = candidate_votes[row["Candidate"]] + 1

print(candidate_options)
print(total_votes)
 
# run loop through (array/index?) for each candidate get count.
# count each candidate's votes
# Percentage for each candidate is candidate / votes
# Print Results
# Export Results