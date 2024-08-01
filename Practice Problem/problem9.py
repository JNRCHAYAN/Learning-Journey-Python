n = int(input("Enter a Number: "))

for i in range(1,11):
    print(f"{n} X {i} = {n * i}")

#===========================

# List with for loop 

l = ["Harry", "Soham" , "Sachin","Rahul"]

for name in l:
    if(name.startswith("S")):
        print(f"Hello {name}")

#===========================
# prime number 
n = int(input("Enter a Number: "))

for i in range(2 ,n):
    if(n%i) == 0:
        print("Number is not prime")
        break
else:
    print("Number is prime")

#===========================
# Star number 
n = int(input("Enter a Number: "))

for i in range (1,n+1):
    print(" "* (n-1), end="")
    print("*"* (2*i-1), end="")
    print("")

n = int(input("Enter a Number: "))
for i in range (1,n+1):
   if(i==1 or i==n):
       print("*"* n, end="")
   else:
       print("*", end="")
       print(" "* (n-2), end="")
       print("*", end="")
   print("")
