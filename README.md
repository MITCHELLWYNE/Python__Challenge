# **Python__Challenge**
### PyBank 
---

![ImageLink](https://github.com/MITCHELLWYNE/Python__Challenge/blob/main/Instructions/Images/revenue-per-lead.png)


''' python

This code prints the sollution for PyBank into a txt.file



output=f"""
Financial Analysis
----------------------------

Total Months: {totalmonth}
Total: ${totalamount}
Average Change: ${changetotal1/changecount1:.2f}
Greatest Increase in Profits: {greatestincmonth} ${greatestincrease}
Greatest Decrease in Profits: {greatestdecmonth} ${greatestdecrease}
"""

print(output)

with open("Analysis/buget_analysis.txt", "w") as txt_file:
    txt_file.write(output)

###  PyBank  txt.file
Financial Analysis
----------------------------
Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 $1862002
Greatest Decrease in Profits: Feb-14 $-1825558

---
###PyPoll
---

![ImageLink](https://github.com/MITCHELLWYNE/Python__Challenge/blob/main/Instructions/Images/Vote_counting.png)

'''python

This Code Prints the sollution for Pypoll into a txt.file

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

### Pypoll txt.file
Election Results
-------------------------
Total Votes: 369711
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette