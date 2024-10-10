with open('currency_exchange.txt') as f:
    lines = f.readlines()
currencyDict = {}
for line in lines:
    parsed = line.split("\t")
    currencyDict[parsed[0]] = parsed[1]
amount = int(input("Enter the amount: \n"))
print("Enter the name of currency you want to convert this amount to? Available options: \n")
[print(item) for item in currencyDict.keys()] 
currency = input("Enter one of these values: \n")
print(f"{amount} PKR is equal to {amount * float(currencyDict[currency])} {currency}")

