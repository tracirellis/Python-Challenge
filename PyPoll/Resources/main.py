#pypoll exercise -voting results
#1 The total number of votes cast
#2 A complete list of candidates who received the votes
#3 The % of votes each candidate won
#4 The total number of votes each candidate won
#5 The winner of the election based on the popular vote

#import the file with the voter/election data
import csv
import os
#define the stupid path
csv_file = "election_data.csv"

#define Variables
total_votes = 0
candidates = {}
winner = ""
max_votes = 0

#open the file for reading
with open(csv_file, "r") as file:
    csvreader = csv.reader(file)
    #skip the header row
    header = next(csvreader, None)

    #loop through each row
    for row in csvreader:
        #count the total votes
        total_votes += 1
        candidate = row[2]

        if candidate not in candidates:
            candidates[candidate] = 1
        
        else:
            candidates[candidate] +=1
            
    results = []
    for candiate, votes in candidates.items():
        percentage = (votes/total_votes) * 100
        results.append((candidate, votes, percentage))
    
    winner = max(candidates, key=candidates.get)



print("Election Results")
print("-" * 30)
print(f"Total Votes: {total_votes}")
print("-" * 30)
print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-" * 30)
print(f"Winner: {winner}")
print("-" * 30)

#text_path= "output.txt"

output = os.path.join(".", 'output.txt')
with open(output, "w") as new:
    new.write("Election Results")
    new.write("\n")
    new.write("-" * 30)
    new.write("\n")
    new.write(f"Total Votes: {total_votes}")
    new.write("\n")
    new.write("-" * 30)
    new.write("\n")
    new.write(f"Candidates: {candidate}: {percentage:.3f}% ({votes})")
    new.write("\n")
    new.write("-" * 30)
    new.write("\n")
    new.write(f"Winner: {winner}")
    new.write("\n")
    new.write("-" * 30)
    