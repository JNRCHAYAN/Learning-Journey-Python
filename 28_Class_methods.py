#Normally Show the instace value 

class employee:
    a = 1
    def show(self):
        print(f"The class vlaue of a is {self.a}")

e = employee()
e.show()
e.a = 45
e.show()
# When we can use classmethod it show only class value
class employee:
    a = 1
    @classmethod
    def show(self):
        print(f"The class vlaue of a is {self.a}")

e = employee()
e.show()
e.a = 45
e.show()

