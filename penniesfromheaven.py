amount = int(input("Enter the number of pennies: "))

denominations = {
    "Dollar Bills": 100,
    "Quarters": 25,
    "Dimes": 10,
    "Nickels": 5,
    "Pennies": 1,
}

for name, value in denominations.items():
    count, amount = divmod(amount, value)
    print(f"{name} = {count}")