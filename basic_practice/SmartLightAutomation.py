time = int(input("Enter time in 24-format (0-23)"))

if time >=18 or time <6:
    print("Turn on lights")
else:
    print("Turn off lights")