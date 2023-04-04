import os
import csv

#Path to collect data from the resource folder
budget_data_csv = os.path.join('.', 'PyBank','Resources', 'budget_data.csv')

#Path to output data into analysis text document
budget_data_analysis = os.path.join('.', 'PyBank', 'analysis', 'budget_data_analysis.txt')

#Set variables, lists, and counters
#set month counter at 0
total_months = 0
#set net total counter at 0
net_total = 0
#store months of profits/losses in a list
month_of_change = []
#store change per month in profits/losses in list
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
    #add one to  months counter to account for month in first row
    total_months = total_months + 1
    #add the total from the first row to the net total counter
    net_total = net_total + int(first_row[1])
    #set the first, previous net total as total in first row of data to use to find 
    #difference between it and next value to derive net change per month
    previous_net = int(first_row[1])
    #for each following row do the following
    for row in csvreader:

        #add one to month counter for each row
        total_months = total_months + 1
        #collect net profits/losses in net_total counter
        net_total = net_total + int(row[1])

        #add month of increase/decrease in list
        month_of_change.append(str(row[0]))
        #calculate net chgange between this month and last month and add it to list
        net_change_list.append(int(row[1]) - previous_net)
        #change the value of previous net to the value of current row
        previous_net = int(row[1])

        #compare value of net change list to that held in greatest increase to see 
        # if it should append value or not and add the month associated with increase
        #to list
        if net_change_list[-1] > greatest_increase[1]:
           greatest_increase[1] = net_change_list[-1]
           greatest_increase[0] = month_of_change[-1]

        #compare value of net change list to that held in greatest decrease to see 
        # if it should append value or not and add the month associated with decrease
        #to list
        if net_change_list[-1] < greatest_decrease[1]:
           greatest_decrease[1] = net_change_list[-1]
           greatest_decrease[0] = month_of_change[-1]
    
    #Find the average of the net_change_list
    net_change_average = round(sum(net_change_list)/len(net_change_list), 2)

    #Print header
    print("Financial Analysis\n------------------------------")

    #Print total months
    print(f"Total Months:{total_months}")

    #Print net total
    print(f"Total :${net_total}")

    #Print average of net_change_list
    print(f"Average Change :${net_change_average}")

    #Print Greatest increase in profits
    print(f"Greatest Increase in Profits:{greatest_increase[0]} ${greatest_increase[1]}")

    #Print greatest decrease in profits
    print(f"Greatest Decrease in Profits:{greatest_decrease[0]} ${greatest_decrease[1]}")

#open analysis txt file
with open(budget_data_analysis, "w") as txtfile:
    txtfile.write(f"Financial Analysis\n------------------------------\nTotal Months:{total_months}\nTotal :${net_total}\nAverage Change :${net_change_average}\nGreatest Increase in Profits:{greatest_increase[0]} ${greatest_increase[1]}\nGreatest Decrease in Profits:{greatest_decrease[0]} ${greatest_decrease[1]}")
