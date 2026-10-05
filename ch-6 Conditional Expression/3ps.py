# Spam detection using conditional expression
p1 = "make money fast"
p2 = "click here"
p3 = "free gift"
p4 = "act now"

message = input("Enter the message: ")
if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This is a spam message.")
else:
    print("This is not a spam message.")