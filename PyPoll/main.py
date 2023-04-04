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

print(tally_dict)
        