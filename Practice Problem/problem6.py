# Find Data in a dictionary 
dic = {
    "Madad" : "Help",
    "billi" : "cat"
}

word = input("Enter Your word : ")

print(dic[word])

# ================================= 
s = set()
n = input("Enter Number 1 : ")
s.add(int(n))
n = input("Enter Number 2 : ")
s.add(int(n))
n = input("Enter Number 3 : ")
s.add(int(n))
n = input("Enter Number 4 : ")
s.add(int(n))
n = input("Enter Number 5 : ")
s.add(int(n))
print(s)

#=========================
d = {}

name = input("Enter Friends name : ")
lang = input ("Enter Your Language : ")
d.update({name:lang})
name = input("Enter Friends name : ")
lang = input ("Enter Your Language : ")
d.update({name:lang})
name = input("Enter Friends name : ")
lang = input ("Enter Your Language : ")
d.update({name:lang})

print(d)
