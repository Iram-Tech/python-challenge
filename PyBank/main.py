# Importing Dependencies
import pandas as pd
import csv

location = 'Resources/budget_data.csv'

budget_df = pd.read_csv(location)
budget_Analysis = {
	"Total Months": len(budget_df["Date"]),
	"Total Profit": budget_df['Profit/Losses'].sum(),
	"Average Change": round(budget_df['Profit/Losses'].mean(), 2),
	"Greatest Profit": budget_df.max(),
	"Greatest Loss": budget_df.min()
}
budget_zipped = zip(pd.DataFrame.from_dict(budget_Analysis))

Total_Months = len(budget_df["Date"])
Total_Profit = budget_df['Profit/Losses'].sum()
Average_Change = round(budget_df['Profit/Losses'].mean(), 2)
Greatest_profit_series = budget_df.max()
Greatest_loss_series = budget_df.min()
	

print(f'Total Months: {Total_Months}')
print(f'Total: {Total_Profit}')
print(f'Average change: {Average_Change}')
print(f'Greatest Increase in Profits: {Greatest_profit_series["Date"]} (${Greatest_profit_series["Profit/Losses"]})')
print(f'Greatest Decrease in Profits: {Greatest_loss_series["Date"]} (${Greatest_loss_series["Profit/Losses"]})')

budget_file = open('Resources/budget_data.txt', 'x')
budget_file = open('Resources/budget_data.txt', 'w')
budget_file.write(f'Total Months: {Total_Months}\nTotal: {Total_Profit}\nAverage change: {Average_Change}\n\
Greatest Increase in Profits: {Greatest_profit_series["Date"]} (${Greatest_profit_series["Profit/Losses"]})\
\nGreatest Decrease in Profits: {Greatest_loss_series["Date"]} (${Greatest_loss_series["Profit/Losses"]})')