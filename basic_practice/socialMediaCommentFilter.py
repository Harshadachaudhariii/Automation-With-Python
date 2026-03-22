comment = input("Enter your comment: ")

if "stupid" in comment or "hate" in comment or "idiot" in comment:
    print("Comment Blocked")
else:
    print("Comment Approved.")