# parent class
class Person (object):

                 #__init__is known as the constructor
                 def __init__(self, name, idnumber):
                       self.name=name
                       self.idnumber=idnumber
                 def display(self):
                       print(self.name)
                       print(self.idnumber)

#child class
class Employee(Person):
 def __init__(self, name, idnumber, salary, post):
         self.salary=salary
         self.post=post

         #invoking the __init__of the parent class
         Person.__init__(self, name, idnumber)

#creation of anobject variable or an instance
a=Employee('Penguin', 202010401, 15000, "Intern")


#calling a functionof the class Personusing its instance
a.display()