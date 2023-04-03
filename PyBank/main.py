import os
import csv

#Path to collect data from the resource folder
budget_data = os.path.join('..' ,'Resources', 'budget_data_csv')

#Define the function and set the budget_data.csv as its sole parameter
def print_financial_analysis (budget_data):

    #Define date as 0th column in csv file
    date = str(budget_data[0])
    #Define profit/losses as 1st column in csv file
    profit_losses = float(budget_data[1])
