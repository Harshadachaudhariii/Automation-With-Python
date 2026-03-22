print("Welcome To Personal Expense Tracker")

food = 0.0
transport = 0.0
bills = 0.0
shopping=0.0
others = 0.0

while True:
    print("\nChoose an option")
    print("Add Expense")
    print("Show Summary")
    print("Data Export")
    print("Exit")
    
    choice = input("\nEnter your Choice")
    
    match choice:
        case "1":
            print("\nCategories : Food, Transport, Biils, Shopping, Others")
            category = input("Enter Category: ").lower()
            amount =float(input("Enter your amount: "))   
            
            if category =="food":
                food +=amount
            elif category =="transport":
                transport += amount
            elif category =="bills":
                bills += amount
            elif category == "shopping":
                shopping += amount
            else:
                others += amount
            total_amount = food + transport + bills + shopping + others
            print(f"Added ${amount} to {category} Category")
        case "2":
            print("Show Summary")
            print(f"Food ${food}")
            print(f"Transport ${transport}")
            print(f"Biils ${bills}")
            print(f"Shopping ${shopping}")
            print(f"Others ${others}")
            print(f"Total Expense {total_amount}")
            
            if total_amount> 500:
                print("Warning! You have spent more than 500 in this month")
            elif total_amount ==0:
                print("You have not added any expense yet!")
            else:
                print("Your are managing your budget wisly")
        
        case "3":
            print("Data Export")
            
        case "4":
            print("Exit....")
            break
                
        case _:
            print("Invalid input")