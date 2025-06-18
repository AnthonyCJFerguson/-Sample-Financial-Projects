# Manual Stock Price Calculator
print("=== MANUAL STOCK PRICE CALCULATOR ===")

# Get stock name
stock_name = input("Enter stock name (like Apple, Tesla): ")

# Get number of days
num_days = int(input("How many days of prices to enter? "))

# Get prices from user
prices = []
print(f"\nEnter {num_days} stock prices:")

for i in range(num_days):
    while True:
        try:
            price = float(input(f"Day {i+1} price: $"))
            if price > 0:
                prices.append(price)
                break
            else:
                print("Price must be positive!")
        except:
            print("Please enter a valid number!")

# Calculate daily returns
daily_returns = []
for i in range(1, len(prices)):
    daily_return = ((prices[i] - prices[i-1]) / prices[i-1]) * 100
    daily_returns.append(daily_return)

# Calculate total return
total_return = ((prices[-1] - prices[0]) / prices[0]) * 100
avg_return = sum(daily_returns) / len(daily_returns)

# Show results
print(f"\n=== RESULTS FOR {stock_name.upper()} ===")
print(f"Prices: {prices}")
print(f"Daily Returns: {[round(r, 2) for r in daily_returns]}")
print(f"Total Return: {total_return:.2f}%")
print(f"Average Daily Return: {avg_return:.2f}%")

# Simple chart
print(f"\n=== PRICE CHART ===")
for i, price in enumerate(prices):
    bar_length = int(price / max(prices) * 20)
    bar = "█" * bar_length
    print(f"Day {i+1}: {bar} ${price:.2f}")

