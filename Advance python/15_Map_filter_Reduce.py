from functools import reduce
# Map Function in python
x = [2,4,5,4,567,8,6,4]
sq = lambda x: x*x
sqlist = map(sq, x)
print(list(sqlist))

#Filter function in python

def even(n):
    if(n%2 ==0):
        return True
    return False
onlyEven = filter(even, x)
print(list(onlyEven))

#Reduce fucntion

def sum (a,b):
    return a+b
print(reduce(sum,x))