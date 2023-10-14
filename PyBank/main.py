import os
import csv

# Set path for file
budget_file = os.path.join("Resources", "budget_data.csv") 

# Open the csv file
with open(budget_file, mode="r", encoding="UTF-8") as budget_csv:
    budget_data = csv.reader(budget_csv, delimiter=",")
    # Skip headers
    next(budget_data, None)

    # Append dates and profit/losses to lists
    budget_list = []
    for row in budget_data:
        budget_list.append(row)

#----------Create variables and grab respective data using for Loop------------------

total_months = len(budget_list)
total_pl = int(budget_list[0][1])
total_pl_changes = []
increase_max = 0
decrease_min = 0
max_month = ""
min_month = ""

# Create for loop to loop through all data in budget list
for x in range(len(budget_list)-1):

    # Store the current month in month_1 and upcoming month in month_2 variables
    month_1 = int(budget_list[x][1])
    month_2 = int(budget_list[x+1][1])

    # Calculate the net amount of Profit/Loss over the entire period.
    monthly_sum = month_1 + month_2
    total_pl += month_2

    # Calculate the changes in "Profit/Losses" over the entire period
    monthly_diff = month_2 - month_1
    total_pl_changes.append(monthly_diff)

    # Calculate the greatest increase in profits (date and amount) over the entire period
    if monthly_diff > increase_max:
        increase_max = monthly_diff
        max_month = budget_list[x+1][0]

    # Calculate the greatest decrease in profits (date and amount) over the entire period    
    if monthly_diff < decrease_min:
        decrease_min = monthly_diff
        min_month = budget_list[x+1][0]

# Calculate the average of changes in "Profit/Losses" over the entire period
avg_change = round(sum(total_pl_changes)/len(total_pl_changes), 2)

#--------Group results into variables that will be used in final analysis--------------------

results_1 = (f"Total months: {total_months}")
results_2 = (f"Total: ${total_pl}")
results_3 = (f"Average Change: ${avg_change}")
results_4 = (f"Greatest Increase in Profits: {max_month} (${increase_max})")
results_5 = (f"Greatest Decrease in Profits: {min_month} (${decrease_min})")

#------------------------------Export a text file--------------------------------------------

final_analysis_txt = (f"Financial Analysis\n\n----------------------------\n\n{results_1}\n\n{results_2}\n\n{results_3}\n\n{results_4}\n\n{results_5}")

# Set path for file
analysis_file = os.path.join("Analysis", "pybank_analysis.txt")

# Write message on text file
with open(analysis_file, mode="w", encoding="UTF-8") as text:
    text.write(final_analysis_txt)

#---------------------------------Print to terminal----------------------------------------
 
print(final_analysis_txt)