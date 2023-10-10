# 1. Total # of Months in the dataset
# 2. The net total of profit/losses over the entire period
# 3. The Changes in profit/losses over the entire period and then the average of those changes
# 4. The greatest increase in profits date and amount over the entire period
# 5. the greatest decrease in profits date and amount over the entire period


 # Financial Analysis

#import files
import os
import csv

#open read files 
budget_data_csv = os.path.join('..', 'Resources', 'budget_data.csv')
with open('budget_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)

    #create the lists to hold the months/date & profit losses for csv files
    date_count = []
    total_profit = []
    change_profit_change = []

    #loop to find the total number of months & net profits over time
    for row in csvreader:
        date_count.append(row[0])
        total_profit.append(int(row[1]))

     #find the average over time   
    for i in range(len(total_profit)-1):
        change_profit_change.append(total_profit[i+1]-total_profit[i])
#find the greatest increase and decrease in profits
greatest_increase = max(change_profit_change)
greatest_decrease = min(change_profit_change)

#find where the month where the greatest increase happens and greatest decrease happens
greatest_month_increase = change_profit_change.index(max(change_profit_change)) + 1
greatest_month_decrease = change_profit_change.index(min(change_profit_change)) + 1



    

# -->>  Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------------------------------------")
print(f"Total Months:  {len(date_count)}")
print(f"Total Profits: ${sum(total_profit)}")
print(f"Average Change: {round(sum(change_profit_change)/len(change_profit_change),2)}")
print(f"Greatest Increase in Profits: {date_count[greatest_month_increase]} (${(str(greatest_increase))})")
print(f"Greatest Decrease in Profits: {date_count[greatest_month_decrease]} (${(str(greatest_decrease))})")

#text_path= "output.txt"

output = os.path.join(".", 'output.txt')
with open(output, "w") as new:
    new.write("Financial Analysis")
    new.write("\n")
    new.write("-------------------------")
    new.write("\n")
    new.write(f"Total Months:  {len(date_count)}")
    new.write("\n")
    new.write(f"Total Profits: ${sum(total_profit)}")
    new.write("\n")
    new.write(f"Average Change: {round(sum(change_profit_change)/len(change_profit_change),2)}")
    new.write("\n")
    new.write(f"Greatest Increase in Profits: {date_count[greatest_month_increase]} (${(str(greatest_increase))})")
    new.write("\n")
    new.write(f"Greatest Decrease in Profits: {date_count[greatest_month_decrease]} (${(str(greatest_decrease))})")