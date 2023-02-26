import csv

infile="resources/budget_data.csv"


totalamount=0
totalmonth=0
previous_net=0
change=0
changetotal=0
changecount=0
greatestincrease=0
greatestincmonth=[]
greatestdecrease=0
greatestdecmonth=[]


with open(infile) as inputpydata:
    rows = csv.reader(inputpydata)
    header=next(rows)


    for row in rows:
        totalamount=totalamount+int(row[1])
        totalmonth=totalmonth+1
        
        current_net=int(row[1])
        if previous_net !=0:
            change=current_net-previous_net
            changecount=changecount+1
            changetotal=changetotal+change

        previous_net=current_net 


        currentinc=int(row[1])
        greatestincmonth=str(row[1])
        if change>greatestincrease:  
            greatestincrease=change+currentinc
            changecount=changecount+1
            changetotal=changetotal+change 
            
            

            
        previousinc=greatestincrease    
 

        currentdec=int(row[1])
        greatestdecmonth=str(row[1])
        if change<greatestdecrease:
            greatestdecrease=change-currentdec
            changecount=changecount+1
            changetotal=changetotal-change    


print()
         
    
output=f"""
Financial Analysis
----------------------------
Total Months: {totalmonth}
Total: ${totalamount}
Average Change: ${changetotal/changecount:.2f}
Greatest Increase in Profits: Aug-16 ${greatestincrease}
Greatest Decrease in Profits: Feb-14 ${greatestdecrease}
"""

print(output)

with open("Analysis/buget_analysis.txt", "w") as txt_file:
    txt_file.write(output)


