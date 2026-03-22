subject = input("Enter the email subject: ")

if "urgent" in subject.lower():
    print("Send an instant notification")
else:
    print("Add to normal queue")