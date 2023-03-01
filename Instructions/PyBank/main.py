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
changetotal1=0
changecount1=0


with open(infile) as inputpydata:
    rows = csv.reader(inputpydata)
    header=next(rows)


    for row in rows:
        totalamount=totalamount+int(row[1])
        totalmonth=totalmonth+1
        
        current_net=int(row[1])
        if previous_net !=0:
            change=current_net-previous_net
            changecount1=changecount1+1
            changetotal1=changetotal1+change

        previous_net=current_net 


        currentinc=int(row[1])
        if change>greatestincrease:  
            greatestincrease=change
            changecount=changecount+1
            changetotal=changetotal+change 
            if greatestincrease==change:
                greatestincmonth=str(row[0])
            

            
        previousinc=greatestincrease    
 

        currentdec=int(row[1])
        if change<greatestdecrease:
            greatestdecrease=change
            changecount=changecount+1
            changetotal=changetotal-change    
            if greatestdecrease==change:
                greatestdecmonth=str(row[0])

        previousdec=greatestdecrease




                





print(changetotal1)
         
    
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


