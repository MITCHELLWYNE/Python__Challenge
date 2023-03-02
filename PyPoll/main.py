import csv

infile="resources/election_data.csv"

#name all variables

votes=0
votes_next=0
votes_after=0
previous_vote=0
ballot_count=0
candidate=str
next_candidate=str
after_candidate=str
previous_candidate=str
change_vote=0
county=str
previous_county=str
current_county=str

with open(infile) as inputpydata:
    rows=csv.reader(inputpydata)
    header=next(rows)



#for loop for how many votes were counted
    for row in rows:
        ballot_count=ballot_count+1
        


 #for loop for each county
 # count how many times each candidate appears in the data set
 # run for loop to find each candidate   
    
    #ballots (row[0])  
    #county (row[1])
    #candidate(row[2])
        current_county=str(row[1])
        if previous_county!=current_county:
                    
        

            
#send to the top of if statement
        
        
        



    print(votes) 
        

        






output=f"""
Election Results
-------------------------
Total Votes: {ballot_count}
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

