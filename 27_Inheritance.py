class employee:
    company = "ITC"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

class programmer(employee):
    companyw = "IIC Company"
    def showLanguage(self):
        print(f"The name is {self.name} and the salary is {self.language}")


a = employee()
b = programmer()
print(b.company , b.companyw)

# We can also use multipal inhertance and mulitlevel inhertance 

