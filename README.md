# Smart Stock Portfolio Tracker

## Project Description

Smart Stock Portfolio Tracker is a Python-based project that helps users track their stock investment and calculate portfolio performance.

The program allows the user to select a stock, enter the number of shares and purchase price, and automatically calculates the current value, profit/loss and profit percentage.

## Features

- Displays available stocks
- Reads stock information from a CSV file
- Allows users to select a stock
- Accepts number of shares
- Accepts purchase price
- Calculates total investment
- Calculates current portfolio value
- Calculates profit or loss
- Calculates profit percentage
- Displays profit/loss status
- Generates a portfolio report

## Technologies Used

- Python
- CSV file handling
- VS Code

## Project Files

### main.py
Contains the main Python program and calculations.

### stocks.csv
Stores stock symbols, company names and sample stock prices.

### portfolio_report.txt
Automatically generated report containing the portfolio details.

## How the Project Works

1. The program reads stock information from `stocks.csv`.
2. It displays the available stocks.
3. The user selects a stock.
4. The user enters the number of shares.
5. The user enters the purchase price per share.
6. The program gets the current price from the CSV file.
7. It calculates the total investment.
8. It calculates the current value.
9. It calculates profit/loss and profit percentage.
10. A portfolio report is saved as a text file.

## Formulas

### Total Investment

Total Investment = Number of Shares × Purchase Price

### Current Value

Current Value = Number of Shares × Current Price

### Profit/Loss

Profit/Loss = Current Value − Total Investment

### Profit Percentage

Profit Percentage = (Profit/Loss ÷ Total Investment) × 100

## Example

For 5 AAPL shares:

- Purchase Price = 200
- Current Price = 250
- Total Investment = 1000
- Current Value = 1250
- Profit = 250
- Profit Percentage = 25%

## Future Improvements

- Add live stock market prices
- Add multiple stocks to one portfolio
- Add graphical charts
- Add a graphical user interface
- Store portfolio history
- Add database support

## Conclusion

The Smart Stock Portfolio Tracker demonstrates the use of Python programming, file handling, user input, calculations and basic data processing to build a practical financial tracking application.