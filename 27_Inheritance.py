class employee:
    company = "ITC"
    def __init__(self) -> None:
        print("Constructor of Emplpyee")
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

class codder:
    programming = "Python"

class programmer(employee,codder):
    companyw = "IIC Company"
    def showLanguage(self):
        print(f"The name is {self.name} and the salary is {self.language}")


# a = employee()
b = programmer()
print(b.company , b.companyw, b.programming)

# We can also use multipal inhertance and mulitlevel inhertance 

