import csv
import os

infile="resources/election_data.csv"

#name all variables
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0



with open(infile) as inputpydata:
    rows=csv.reader(inputpydata)
    header=next(rows)

    for row in rows:

        

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name and county name from rows.
        candidate_name = row[2]

    

        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1


    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")


 # whats the winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage




print(winning_count)

output=f"""
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
{candidate_results}
-------------------------
Winner: {winning_candidate}
"""

print(output)

with open("Analysis/election_data.txt", "w") as txt_file:
    txt_file.write(output)

