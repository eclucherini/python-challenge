# Start with necessary imports
import os
import csv

# Use csv path
csvpath = os.path.join("Resources","budget_data.csv")
csvpath

# Define variables
total_months = 0
total_profits = 0
monthly_profit_change = 0
monthly_profit_change_list = []
greatest_increase = 0
greatest_increase_month = ("")
greatest_decrease = 0
greatest_decrease_month = ("")

# Open csv file
with open(csvpath) as budget_file:
    csvreader = csv.reader(budget_file,delimiter=',')
    csv_header = next(csvreader)

    # Create new lists from each column of data to calculate total number of months and total profits/losses
    dates = []
    profits_losses = []

    # Read each row of data after the header
    for row in csvreader:

        # Loop through each column to append each row of data to lists
        date_row = row[0]
        profit_loss_row = row[1]

        dates.append(date_row)
        profits_losses.append(profit_loss_row)
    
      #   print(dates)
      #   print(profits_losses)

        # Create list to calculate monthly change
        monthly_profit_change_list.append(row)

        # Loop through list and get monthly profit/loss change (current month - previous month)
        for i in range(len(monthly_profit_change_list)-1):       
            monthly_profit_change = int(monthly_profit_change_list[i + 1][1]) - int(monthly_profit_change_list[i][1])

            # Greatest increase in profits (date and amount)
            if greatest_increase < monthly_profit_change:
               greatest_increase = monthly_profit_change
               greatest_increase_month = monthly_profit_change_list[i + 1][0]

            # Greatest decrease in profits (date and amount)
            if greatest_decrease > monthly_profit_change:
               greatest_decrease = monthly_profit_change
               greatest_decrease_month = monthly_profit_change_list[i + 1][0]
            
            # Average change in profits/losses
            average_change = round(int((monthly_profit_change_list)[-1][1]) - int((monthly_profit_change_list)[0][1]) / (len(monthly_profit_change_list)-1),2)

# Change Profits/Losses list into integers
for i in range(0,len(profits_losses)):
    profits_losses[i] = int(profits_losses[i])

# Count total number of months in first column
total_months = len(dates)
print(total_months)

# Sum total of Profit/Losses in second column
def sum():
    for profit_loss_row in range(len(profits_losses)):
        sum = 0
        sum += profits_losses[profit_loss_row]
    return sum
    
total_profits = sum()
print(total_profits)   

# Create output txt file
output_txt_file = os.path.join("Analysis","analysis.txt")
with open(output_txt_file,"w") as txt_data_file:
    txtwriter = ["Financial Analysis \n",
                 "---------------------------- \n",
                 f"Total Months: {total_months} \n",
                 f"Total: ${total_profits} \n",
                 f"Average Change: ${average_change} \n",
                 f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase}) \n",
                 f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease}) \n"]
    txt_data_file.writelines(txtwriter)
    txt_data_file.close()

# Show the output in the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profits}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")
