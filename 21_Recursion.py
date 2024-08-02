def factroial(n):
    if(n==1 or n==0):
        return 1
    return n * factroial(n-1)

n = int(input("Enter Your Number : "))
print(f"The Ans is : {factroial(n)}")
