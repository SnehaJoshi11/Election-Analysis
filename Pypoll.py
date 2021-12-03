# 1.Total number of votes cast
# 2.A complete list of candidates who received votes
# 3.Total number of votes each candidate received
# 4.Percentage of votes each candidate won
# 5.The winner of the election based on popular vote

# Add our dependencies.

import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes=0
# Candidate options and candidate votes
candidate_options=[]
# 1. Declare the empty dictionary.
candidates_votes={}
# Winning Candidate and Winning Count Tracker
winning_candidate=""
winning_count=0
winning_percentage=0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        #print(row)
        #total_votes=total_votes+1
        total_votes +=1 

        candidate_name = row[2]
        #candidate_options.append(candidate_name)
        
        if candidate_name not in candidate_options:

            #add candidate name to cantidate list
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count.
            candidates_votes[candidate_name] = 0
            # 2. Begin tracking that candidate's vote count.
        
        #print(candidates_votes)
        candidates_votes[candidate_name] += 1 

    for candidate_name in candidates_votes:
        votes = candidates_votes[candidate_name]
        votes_percentage = float(votes)/float (total_votes)*100
       #print(f'{candidate_name}:received {votes_percentage:.1f}% of the votes')

        if(votes> winning_count and votes_percentage>winning_percentage):
            winning_count=votes
            winning_percentage=votes_percentage
            winning_candidate=candidate_name
        #print out the winning candidate, vote count and percentage to
        #   terminal.
        print(f"{candidate_name}:received {votes_percentage:.1f}({votes:,})\n")

    winning_candidate_summary=(
            f"---------------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning vote count: {winning_count:,}\n"
            f"Winnig Percentage: {winning_percentage:.1f}\n"
            f"---------------------------------\n")

    print(winning_candidate_summary)
