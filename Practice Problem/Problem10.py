#Find a maxmum number
def great(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>b and c>a):
        return c
 
maxnum = great(290,4,100)
print(maxnum)

# Fahrenheit to Celsius

def fahr(f):
    return 5*(f-32)/9

calsius = fahr(100)
print(calsius)