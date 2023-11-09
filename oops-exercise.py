#Object-oriented programming (OOP) is a style of programming characterized by the identification of classes of objects closely linked with the methods (functions) with which they are associated

#create a user class with properties i.e name,age,location
class User:
    def __init__(my, name, age, location):
        my.name ='joan' 
        my.age = 18
        my.location = 'kawempe'

    def __str__(my):
        return f"User(name: {my.name}, age: {my.age}, location: {my.location})"
  
#second option
class User:
    my_name = 'joan'
    my_age = 18
    my_location = 'kawempe'
  
 

#create a new instance of the user class(a new object)
#access the user name and age

class User:
# The __init__() function is called automatically every time the class is being used to create a new object
#we use  the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
  def __init__(my, name, age):
    my.name = name
    my.age = age
  
#creating  an object to be used = info
info = User("Joan", 18)

print(info.name)
print(info.age)

#create a function for the user class that prints a user's location.
#print the users's location using this function.
class User:
    #the  my parameter is a reference to the current instance of the class, and is used to access variables that belong to the class
  def __init__(my, location):
    my.location = location
    
#insert a function that prints the location
  def my_location(my):
    print("I stay in " + my.location)

#calling the information
info = User('kawempe')
info.my_location()