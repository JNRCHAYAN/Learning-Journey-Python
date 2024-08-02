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
    return "Done"

goodday("Chayan" ,"Thank You")
goodday("Roni","Thanks")
a = goodday("Miltan" ,"Thank You")
print(a)

#Function with Default Argument

def goodday(name, ending= "Thank you"):
    print("Good day " +name+ " " +ending)

goodday("Chayan")
goodday("Roni" , "Nice to meet You")

