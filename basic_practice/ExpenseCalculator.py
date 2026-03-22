print("----Month Expense Tracker---")

rent = float(input("Enter your house rent = "))
grocries = float(input("Enter groceries expense = "))
utilities = float(input("Enter your utilities bills = "))
transport = float(input("Enter transport cost = "))

total = rent+ grocries + utilities+transport

income = float(input("\nEnter your monthly income = "))

if total > income:
    print("Warning! Your are over spending")
elif total == income:
    print("your are breaking over")
else:
    savings = income - total
    print("Good job! You saved Rs. ", savings)