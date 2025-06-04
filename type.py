class parent:
    def __init__(self, name,age,salary,password,subject):
       #Public Instance variables
        self.name = name
        self.age = age

       #Private Instance Variables
        self.__salary = salary
        self.__password = password
        self.__subject = subject
    
       #To get all the attributes
    def first__child(self):
        return{
            "name": self.name,
            "age": self.age,
            "salary": self.__salary,
            "password": self.__password,
            "subject": self.__subject
        }
 
    #Instances of the Parent class
parent1 = parent("Ada", 24, 20000, "bobby456", "civic")
parent2 = parent("Ben", 23, 30000, "alice123", "biology")
   
    #Display the attribute of the class
print("attributes of parent1:")
print(parent1.first__child())

print("attributes of parent2:")
print(parent2.first__child())

    
