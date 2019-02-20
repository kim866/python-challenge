#Dependencies
import csv

#Loading the CSV file
budget_data_csv = "Resources/budget_data.csv"

#Tracking parameters
months = []
profits_or_losses = []
net_profit = 0

#Reading the CSV file & converting into a list of dictionaries
with open(budget_data_csv) as budget_data:
    reader = csv.reader(budget_data)
    
    # Skiping the header row
    next(reader)

    #Looping through the each row
    
    for row in reader:
        months.append(row[0])
        net_profit = net_profit + int(row[1])
        profits_or_losses.append(row[1])

#Declaring variables
total_months = len(months)
average_change = round(net_profit/total_months, 2)
highest_profit = max(profits_or_losses)
highest_loss = min(profits_or_losses)

months_profits_or_losses = dict(zip(profits_or_losses, months))
month_highest_profit = months_profits_or_losses[highest_profit]
month_highest_loss = months_profits_or_losses[highest_loss]


#Printing the results
print("Financial Analysis")
print("------------------------------")
print("Total Months: "+ str(total_months))
print("Total: $"+str(net_profit))
print("Average Change: $"+str(average_change))
print("Greatest Increase in Profits: "+month_highest_profit+" ($"+highest_profit+")")
print("Greatest Decrease in Profits: "+month_highest_loss+" ($"+highest_loss+")")

#Exporting the results to a text file

f= open("budget_analysis.txt","w+")
f= open("budget_analysis.txt","a+")
f.write("Financial Analysis"  + "\n") 
f.write("----------------------------"  + "\n")     
f.write(f"Total Months: {str(total_months)}"  + "\n")
f.write(f"Total: ${str(net_profit)}"  + "\n")
f.write(f"Average Change: ${str(average_change)}" + "\n")
f.write(f"Greatest Increase in Profits: {month_highest_profit} (${highest_profit})" + "\n")
f.write(f"Greatest Decrease in Profits: {month_highest_loss} (${highest_loss})") 
f.close()