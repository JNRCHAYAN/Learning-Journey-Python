class Employee:
    language = "py"  # This is an class attribute
    salary = 12000

    def getinfo(self):  # Must be use an arrgumet other wise we can see some error
        print(f"The language is {self.language}. The salary is {self.salary}")
    def greet(self):
        print("Good Morning")

chayan = Employee()
chayan.name = "Harry" # This is instance attribute
print(chayan.name ,chayan.language , chayan.salary)

chayan.getinfo()  
chayan.greet()