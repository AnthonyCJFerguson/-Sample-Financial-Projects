#!/usr/bin/env python3
"""
Stock Price Calculator
Calculates daily returns from stock price data
"""

def main():
    """Main program function"""
    # Display program header
    print("=== MANUAL STOCK PRICE CALCULATOR ===")
    
    # Get stock information
    stock_name = get_stock_name()
    num_days = get_number_of_days()
    prices = collect_prices(num_days)
    
    # Calculate and display results
    calculate_returns(prices, stock_name)

def get_stock_name():
    """Get stock name from user"""
    return input("Enter stock name (like Apple, Tesla): ")

def get_number_of_days():
    """Get number of days with input validation"""
    while True:
        try:
            days = int(input("How many days of prices to enter? "))
            if days > 0:
                return days
            else:
                print("Please enter a positive number!")
        except ValueError:
            print("Please enter a valid number!")

def collect_prices(num_days):
    """Collect stock prices with error handling"""
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
            except ValueError:
                print("Please enter a valid number!")
    
    return prices

def calculate_returns(prices, stock_name):
    """Calculate and display daily returns"""
    if len(prices) < 2:
        print("Need at least 2 prices to calculate returns!")
        return
    
    print(f"\nDaily returns for {stock_name}:")
    print("-" * 30)
    
    for i in range(1, len(prices)):
        daily_return = ((prices[i] - prices[i-1]) / prices[i-1]) * 100
        print(f"Day {i} to Day {i+1}: {daily_return:.2f}%")

if __name__ == "__main__":
    main()
