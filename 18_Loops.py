#  While Loop ands for loop 

i =0
while(i<=10):
    print(i)
    i+=1

# list using while loop 

l = [1,3,5,"chayan", False,"This" , "Roni"]
i=0
while(i<len(l)):
    print(l[i])
    i+=1

# For Loop 
print("\nFor Loop")
for i in range(4):
    print(i)
print("\nFor Loop Rnage")
for i in range(0,10,4):
    print(i)

print("\nFor Loop in list")

l = [1,4,6,7,3,6,"Chayan",4]
for i in l:
    print(i)

print("\nFor Loop with else")

l = [1,4,6,7,3,6,"Chayan",4]
for i in l:
    print(i)
else:
    print("Print all item done")