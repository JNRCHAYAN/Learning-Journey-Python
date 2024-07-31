p1 = "Make a lot of money"
p2 = "Buy Now" 
p3 = "Subscribe this" 
p4 = "Click this"

mess = input("Enter Your Commnent ")

if((p1 in mess) or (p2 in mess) or (p3 in mess) or (p4 in mess)):
    print("This  is scam")
else:
    print("Comment is not spam")