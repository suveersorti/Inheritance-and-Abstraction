# import necessary packages
from abc import abc, abstractmethod
#create a base class
class animal(ABC):
     
     # abstract method
     #should be implemented by all sub classes
     def move(self):
          pass
     
    #sub classes
class Human(Animal):
     def move(self):
          print("I can walk and run"))
