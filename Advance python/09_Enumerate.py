l =[3,65,4,2,5,3]
index =0
for item in l:
   
    print(f"The item number  {index} is {item}")
    index +=1

# Simplefy this code with Enumerate Function
print("Enumerate Function")
for index,item in enumerate(l):
    print(f"The item number  {index} is {item}")