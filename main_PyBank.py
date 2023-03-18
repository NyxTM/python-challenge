import os
import csv

# Initialize variables
TotalMonths=0
Net=0.0
Changes=0.0
TotalChanges=0.0
AverageChange=0.0
GreatestIncrease=0.0
GreatestDecrease=0.0

# open and read the csv file
csvpath=os.path.join('Pybank','Resources', 'budget_data.csv')
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    print(csvreader)

# store header row
    csv_header=next(csvreader)

# analysis

    for row in csvreader:

        TotalMonths += 1
        Net += float(row[1])

        if TotalMonths>1:
            Changes = float(row[1])-Changes
            TotalChanges=TotalChanges+Changes

        if Changes > GreatestIncrease:
            GreatestIncrease=Changes
            IncreaseDate=row[0]
        if Changes < GreatestDecrease:
            GreatestDecrease=Changes
            DecreaseDate=row[0]

        Changes = float(row[1])
        

    AverageChange=round(TotalChanges/(TotalMonths-1),2)

# print
print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {str(TotalMonths)}")
print(f"Total: ${str(int(Net))}")
print(f"Average Change: ${str(AverageChange)}")
print(f"Greatest Increase in Profits: {str(IncreaseDate)} (${int(GreatestIncrease)})")
print(f"Greatest Decrease in Profits: {str(DecreaseDate)} (${int(GreatestDecrease)})")


# export to text
lines=["Financial Analysis",
        "----------------------------", 
        f"Total Months: {str(TotalMonths)}",
        f"Total: ${str(int(Net))}",
        f"Average Change: ${str(AverageChange)}",
        f"Greatest Increase in Profits: {str(IncreaseDate)} (${int(GreatestIncrease)})",
        f"Greatest Decrease in Profits: {str(DecreaseDate)} (${int(GreatestDecrease)})"]


with open('PyBank/analysis/results_PyBank.txt','w') as text:

    for line in lines:
        text.writelines(line)
        text.writelines('\n')
    