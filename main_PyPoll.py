import os
import csv

# Initialize variables
TotalVotes=0.0
List=[]
CandidatesList=[]
VoteNo=0
EachVote=[]
Percentage=0.0
PercentageList=[]
Greatvalue=0
Winner=""

# open and read the csv file
csvpath=os.path.join('PyPoll','Resources', 'election_data.csv')
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    print(csvreader)

# store header row
    csv_header=next(csvreader)

# analysis

    for row in csvreader:

        TotalVotes += 1
        List.append(row[2])
       
        if row[2] not in CandidatesList:
             CandidatesList.append(row[2])
             
    for i in CandidatesList:

        VoteNo=List.count(i)

        Percentage='{:.3%}'.format(VoteNo/TotalVotes)
        EachVote.append(VoteNo)
        PercentageList.append(Percentage)

        if VoteNo> Greatvalue:
            Greatvalue=VoteNo
            Winner=i

        VoteNo=0          
    

    
    z=zip(CandidatesList,PercentageList,EachVote)
   


# print
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {str(int(TotalVotes))}")
print(f"-------------------------")
for EachVote in z:
        print(EachVote)   
print(f"-------------------------")        
print(f"Winner: {Winner}")
print(f"-------------------------")



# export to text

with open('PyPoll/analysis/results_PyRoll.txt','w') as text:

        text.writelines(f"Election Results")
        text.writelines('\n')
        text.writelines(f"-------------------------")
        text.writelines('\n')
        text.writelines(f"Total Votes: {str(int(TotalVotes))}")
        text.writelines('\n')
        text.writelines(f"-------------------------")
        text.writelines('\n')
        text.writelines(''.join(map(str, z)))
        text.writelines('\n')
        text.writelines(f"-------------------------")
        text.writelines('\n')
        text.writelines(f"Winner: {Winner}")
        text.writelines('\n')
        text.writelines(f"-------------------------")
        text.writelines('\n')

