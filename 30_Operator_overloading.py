class number:
    def __init__(self , n) -> None:
        self.n = n

    def __add__(self ,num):
        return self.n + num.n
    def __sub__(self ,num):
        return self.n - num.n
    def __mul__(self ,num):
        return self.n * num.n
    
# __add__
# __sub__
# __mul__
# __truediv__
# __floordic__

n = number(1)
m = number(2)
print(n+m)
print(n-m)
print(n*m)