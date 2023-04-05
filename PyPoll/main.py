import os
import csv

#Path to collect data from the resource folder
election_data_csv = os.path.join('.', 'PyPoll','Resources', 'election_data.csv')

#Path to output data into analysis text document
election_data_analysis = os.path.join('.', 'PyPoll', 'analysis', 'election_data_analysis.txt')

#name dictionary to import data into
tally_dict = {}

#open the csv file and read it
with open (election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
      #read (and then ignore) the header row
    header=next(csvreader)

#for each row in the csv count 1 vote for acndidate name and add to dictionary
    for row in csvreader:
        #if candidate's name is contained in the dictionary
        if row[2] in tally_dict:
            #add 1 vote to the existing tally for that candidate
            tally_dict[row[2]] += 1
        
        #otherwise, add the candidate to the dictionary and add one vote for them to their tally
        else: 
            tally_dict[row[2]] = 1

#Find the total nuber of votes cast
#initialize count to 0
total_votes = 0
#add tally for each candidate in dictionary to total votes tally
for candidate in tally_dict:
    total_votes += tally_dict[candidate]

#define function for finding percentages of votes
def vote_percentage(candidate):
    percentage = (tally_dict[candidate]/total_votes)*100
    return round(percentage, 3)

#define function for printing values
def printing_values(candidate):
    print(f"{candidate}: {vote_percentage(candidate)}% ({tally_dict[candidate]})")

#define function for writing the values into the txt file


#print election results header
print("Election Results\n------------------------")

#print total votes
print(f"Total Votes: {total_votes}\n------------------------")

#print all candidates with votes, their tallies, and percentages
for candidate in tally_dict:
    
    printing_values(candidate)

#print dash delineater
print("------------------------")

#calculate and print winner
#initialize winner_count to 0
winner_count = 0
for candidate in tally_dict:
    if tally_dict[candidate] > winner_count:
        winner_count = tally_dict[candidate]
        winner = candidate
    

#print winner name
print(f"Winner: {winner}")

#print dash delineater
print("------------------------")