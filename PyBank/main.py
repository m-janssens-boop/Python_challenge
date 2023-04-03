import os
import csv

#Path to collect data from the resource folder
budget_data_csv = os.path.join('..' ,'Resources', 'budget_data_csv')

#Path to output data into analysis text document
budget_data_analysis = os.path.join('..', 'analysis', 'budget_data_analysis.txt')

#Set variables, lists, and counters
#set counter at 0
total_months = 0
#set counter at 0
net_total = 0
#store months in a list
month_of_change = []
#store change in profits/losses in list
net_change_list = []
#collect date and start comparison at 0
greatest_increase = ["", 0]
#collect date and start comparison much larger than any number in the data set
greatest_decrease = ["", 9999999999999999999]


#open the csv file and read it
with open (budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
      #read (and then ignore) the header row
    header=next(csvreader)

    #remove the first row to avoid it being added to net_change_list
    #since there can be no change at the first month
    first_row = next(csvreader)
    total_months += 1
    net_total += int(first_row[1])
    #set the first, previous net total as total in row 2 to use to find 
    #difference between it and next value to derive net change per month
    previous_net = int(first_row[1])
    for row in csvreader:

        #add one to month counter for each row
        #collect net profits/losses in net_total counter
        total_months += 1
        net_total += int(row[1])

        #add month of increase/decrease in list
        month_of_change.append(str(row[0]))
        net_change_list.append(previous_net-int(row[1]))

