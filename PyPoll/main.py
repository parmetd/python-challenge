#PyPoll
# run loop through (array/index?) for each candidate get count.
# if using Pandas then datagroupby

import os
import pandas as pd 
import csv
#Dependencies

csv_poll = os.path.join('Resources', 'election_data.csv')

Candidates = []
candidate_votes = []
total_votes = 0
percent_votes = []
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
        #reader = csv.DictReader(election_data)
        total_votes += 1

        if row[2] not in Candidates:

            Candidates.append(row[2])
            index = Candidates.index(row[2])
            candidate_votes.append(1)

        else:
            index = Candidates.index(row[2])
            candidate_votes[index] +=1
    
    # Percentage for each candidate is candidate / votes
    for votes in candidate_votes:
        percentage = (votes / total_votes)
        # percentage = round(percentage, 1)
        #percentage = percentage / 100
        percentage = "{:.1%}".format(percentage)
        percent_votes.append(percentage)
        
        

    # count each candidate's votes
    # Find the winning candidate
    winner = max(candidate_votes)
    can_index = candidate_votes.index(winner)
    winning_candidate = Candidates[can_index]

# Displaying results
# Print Results
#print(Candidates)
#print(total_votes)
#print(percentage)
#print(f"Winner: {winning_candidate}")
#print(f"Results: {candidate_votes}")
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(total_votes)}")
print("--------------------------")
for i in range(len(Candidates)):
    print(f"{Candidates[i]}: {str(percent_votes[i])} ({str(candidate_votes[i])})")
print("--------------------------")
print(f"Winner: {winning_candidate}")
print("--------------------------")
print("Output.txt created")
print("--------------------------")

# Exporting Results
# Exporting to .txt file
output = open("output.txt", "w")
line1 = "Election Results"
line2 = "--------------------------"
line3 = str(f"Total Votes: {str(total_votes)}")
line4 = str("--------------------------")
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for i in range(len(Candidates)):
    line = str(f"{Candidates[i]}: {str(percent_votes[i])} ({str(candidate_votes[i])})")
    output.write('{}\n'.format(line))
line5 = "--------------------------"
line6 = str(f"Winner: {winning_candidate}")
line7 = "--------------------------"
output.write('{}\n{}\n{}\n'.format(line5, line6, line7))