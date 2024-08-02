# Function Defination
def avg():
    a= int(input("Enter Your Number : "))
    b= int(input("Enter Your Number : "))
    c= int(input("Enter Your Number : "))
    avag = (a+b+c)/3
    print(avag)

#Function Call
avg()


#Function with argument

def goodday(name, ending):
    print("Good Day "+name)
    print(ending)

goodday("Chayan" ,"Thank You")
goodday("Roni","Thanks")