#Abstraction and Encapsulation

class employee:
    a = 1
    @classmethod
    def show(self):
        print(f"The class vlaue of a is {self.a}")
    @property
    def name(self):
        return self.ename
    @name.setter
    def name (self ,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = employee()
e.a = 45
print(e.a)
e.name = "Chayan Roy"
print(f"First Name : {e.fname}")
print(f"Last Name : {e.lname}")
