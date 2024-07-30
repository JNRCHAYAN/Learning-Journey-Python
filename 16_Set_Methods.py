s = {1,3,4,3 ,"Chayan"}
s1 = {1,3,5,3,7,8,4,3 ,"Chayan"}
print(s,type(s))


s.add(44)
print(s)

# Set unindex element so that we can access any value with index number
print(len(s))

s.remove(1)
print(s)

# s.pop()  #Remove Random Value
# print(s)

# s.clear()  #clear all value
# print(s)

print(s.union(s1))  # Same as math union (all Value print)
print(s.intersection(s1))  ## Same as math union (common Value print)