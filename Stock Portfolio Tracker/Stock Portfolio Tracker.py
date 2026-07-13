stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 300,
    "AMZN": 200
}

total_investment = 0

file = open("portfolio.txt", "w")
file.write("----- Stock Portfolio -----\n\n")

num = int(input("How many stocks do you want to add? "))

for i in range(num):
    stock = input("\nEnter Stock Name: ").upper()

    if stock in stock_prices:
        quantity = int(input("Enter Quantity: "))

        investment = stock_prices[stock] * quantity
        total_investment += investment

        print(f"{stock} = ${investment}")

        file.write(f"Stock : {stock}\n")
        file.write(f"Quantity : {quantity}\n")
        file.write(f"Price : ${stock_prices[stock]}\n")
        file.write(f"Investment : ${investment}\n\n")

    else:
        print("Stock not available!")

print("\n---------------------------")
print("Total Investment = $", total_investment)

file.write("---------------------------\n")
file.write(f"Total Investment = ${total_investment}")

file.close()

print("\nData saved successfully in portfolio.txt")