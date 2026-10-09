import csv

# Read stock data from CSV
with open("stocks.csv", "r") as file:
    stocks = list(csv.DictReader(file))

print("========================================")
print("     SMART STOCK PORTFOLIO TRACKER")
print("========================================")
print("Welcome!\n")

# Display available stocks
print("Available Stocks:")
for item in stocks:
    print(f"{item['symbol']} - {item['company']}")

print()

# Get stock choice
stock = input("Enter the stock symbol: ").upper()

# Find selected stock
selected_stock = None

for item in stocks:
    if item["symbol"] == stock:
        selected_stock = item
        break

# Check whether stock exists
if selected_stock is None:
    print("Stock not found. Please enter a valid stock symbol.")
else:
    print(f"\nYou selected: {selected_stock['company']} ({stock})")

    # Get number of shares
    quantity = int(input("Enter the number of shares: "))

    # Get purchase price
    purchase_price = float(
        input("Enter purchase price per share: ")
    )

    # Get current price from CSV
    current_price = float(selected_stock["price"])

    # Calculations
    total_investment = quantity * purchase_price
    current_value = quantity * current_price
    profit_loss = current_value - total_investment

    if total_investment != 0:
        profit_percentage = (profit_loss / total_investment) * 100
    else:
        profit_percentage = 0

    # Display results
    print("\n========================================")
    print("          PORTFOLIO SUMMARY")
    print("========================================")

    print("Stock:", stock)
    print("Company:", selected_stock["company"])
    print("Number of Shares:", quantity)
    print("Purchase Price:", purchase_price)
    print("Current Price:", current_price)
    print("Total Investment:", total_investment)
    print("Current Value:", current_value)
    print("Profit/Loss:", round(profit_loss, 2))
    print("Profit Percentage:", round(profit_percentage, 2), "%")

    # Profit/Loss status
    if profit_loss > 0:
        print("Status: PROFIT")
    elif profit_loss < 0:
        print("Status: LOSS")
    else:
        print("Status: NO PROFIT / NO LOSS")

    # Save report
    with open("portfolio_report.txt", "w") as file:
        file.write("SMART STOCK PORTFOLIO REPORT\n")
        file.write("============================\n")
        file.write(f"Stock: {stock}\n")
        file.write(f"Company: {selected_stock['company']}\n")
        file.write(f"Number of Shares: {quantity}\n")
        file.write(f"Purchase Price: {purchase_price}\n")
        file.write(f"Current Price: {current_price}\n")
        file.write(f"Total Investment: {total_investment}\n")
        file.write(f"Current Value: {current_value}\n")
        file.write(f"Profit/Loss: {round(profit_loss, 2)}\n")
        file.write(f"Profit Percentage: {round(profit_percentage, 2)}%\n")

    print("\nReport saved successfully!")
    print("========================================")