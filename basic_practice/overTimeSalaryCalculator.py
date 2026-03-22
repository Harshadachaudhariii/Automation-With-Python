# how much time employee work.
hours = float(input("Enter Total Working Hours: "))

# if less than threshold of overtime offer rate 500
rate = 500
# if more than threshold of overtime offer rate 500
overtime_rate = 700

# if working hour is greater than 8 means overtime 
if hours>8:
    overtime = hours - 8
    salary = (8* rate) +(overtime * overtime_rate)
    print("Over Time Pay Applied! Total Salary = ", salary)
else:
    salary = hours * rate
    print("Regular Pay = ", salary)