# Take user Input 
a = input("Enter Yor name : ")
print("Good Morning ",a)
print(f"Good Morning {a}") #f string function

#Letter create
latter = '''\nDear <|Name|>,
You are selected!
<|Date|>
 '''
print(latter.replace("<|Name|>",a).replace("<|Date|>" , "12/04/2024"))

# ==========================

# Double Space Detetaion 
name = "I am  chayan"
print(name.find("  "))

#Replace Double Space
name = "I am  chayan"
print(name.replace("  "," "))

