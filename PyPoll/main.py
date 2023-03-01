import csv

infile="resources/election_data.csv"


Candidate=[]





        

        






output=f"""
Election Results
-------------------------
Total Votes: 369711
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
"""

print(output)

with open("Analysis/election_data.txt", "w") as txt_file:
    txt_file.write(output)

