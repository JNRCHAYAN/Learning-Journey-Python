class employee:
    company = "ITC"
    def __init__(self) -> None:
        print("Constructor of Emplpyee")
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

class codder(employee):
    programming = "Python"
    def __init__(self) -> None:
        super().__init__() # For Super class constructor Function Access
        print("Codder Constructor Function")

class programmer(codder):
    companyw = "IIC Company"
    def showLanguage(self):
        print(f"The name is {self.name} and the salary is {self.language}")


# a = employee()
b = programmer()
print(b.company , b.companyw, b.programming)

# We can also use multipal inhertance and mulitlevel inhertance 

