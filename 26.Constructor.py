class Employee:
    language = "py"  # This is an class attribute
    salary = 12000
    def __init__(self):
         print("I am chyan roy") # Dunder method which is called automaticlly 

    def __init__(self, lg, sl):
         self.language = lg
         self.salary = sl
         

chayan = Employee("Python" ,100000)
print(chayan.language, chayan.salary)
Roni = Employee("Java",234564)
print(Roni.language, Roni.salary)

