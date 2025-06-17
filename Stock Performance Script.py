# Basic Stock Return Calculator

# Sample Stock prices for 5 days 
prices = [100, 102, 101, 105, 107]

# Initialize a list to store daily returns
daily_returns = []

# Loop to calculate daily returns
for i in range(1, len(prices)):
    daily_return = ((prices[i] - prices[i - 1]) / prices[i - 1]) * 100
    daily_returns.append(daily_return)

# Calculate total return from first to last day
total_return = ((prices[-1] - prices[0]) / prices[0]) * 100

# Calculate average daily return
average_daily_return = sum(daily_returns) / len(daily_returns)

# Print results
print("Stock Prices (5 days):", prices)
print("Daily Returns (%):", [round(r, 2) for r in daily_returns])
print("Total Return over 5 days: {:.2f}%".format(total_return))
print("Average Daily Return: {:.2f}%".format(average_daily_return))