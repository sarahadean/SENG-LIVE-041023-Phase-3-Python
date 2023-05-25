#!/usr/bin/env python3
# Demonstrate classes 
# 1. ✅ Create a Pet class
# 2. ✅ Instantiate a few pet instance 
    # Compare the pet instances to demonstrate they are not the same object
    # Note: add 'pass' to the pet class 

# import ipdb

class Pet:

    pass

# ipdb.set_trace()

#All pets but each pet is different
# chloe = Pet()
# maggie = Pet()
# winnie = Pet()
# beau = Pet()

# beau
# <__main__.Pet object at 0x102880e50>
# chloe
# <__main__.Pet object at 0x102880eb0>
# winnie
# <__main__.Pet object at 0x10289ffd0>
# maggie
# <__main__.Pet object at 0x1028ff1c0>
# winnie == chloe
# False

# 3. ✅ Demonstrate __init__ 
    # Add arguments to instances  
    # use dot notation to access their attributes 
    # update attributes with new values 

class Pet:
    def __init__(self, name, age, breed, temperament):
        self.name = name
        self.age = age
        self.breed = breed
        self.temperament = temperament # initialization method
        # to provide objects(instances) with unique attributes 
        # upon the instantiation

    def print_pet_detail(self):
        print(f'''
            name:{self.name}
            age:{self.age}
            breed:{self.breed}
            temperament:{self.temperament}
        ''')

baboi = Pet("Baboi", 2, "Collie", "Energetic")
# <__main__.Pet object at 0x104dbb580>
# 
# # 4.✅ Demonstrate instance methods by creating a print_pet_details function that will print the pet attributes
#     Review the self keyword 
#     Invoke the print_pet_details on an instance 

##f string with multiline with triple singe quotes

# baboi.print_pet_detail()
            # name:rose
            # age:11
            # breed:domestic longhair
            # temperament:sweet
            # image_url:rose.jpg

chloe = Pet("Chloe", 5, "Heeler", "Diva")
chloe.print_pet_detail()

# Object Properties => Attributes that are controlled by methods
# 1. Create Owner class with two instance method

class Owner:
    def __init__(self, age): #provide parameters
        self.age = age #setting the attribute for the instance of the owner
    
    def get_name(self):
        print("Retrieving Owner's name")
        return self._name #property, not attribute so are are using '_'
    
    def set_name(self, name):
        print("Setting Owner's name")
        #conditional logic
        if(isinstance(name, str)):
            self._name = name
        else:
            print("Name must be a string")
    
    name = property(set_name, get_name) #attribute = property(methods attribute is assigned to)
    #property is attribute but performing more complicated computation


eugene = Owner(24)
print(eugene)
eugene.set_name("Eugene")
print(eugene.get_name())
# eugene.name #gives error that attribute name has not been set

#Use property() to compile get_name / set_name

# Demonstrate instances 
    # Different Instances are Different Objects
# Demonstrate __init__
# Demonstrate instance method
# Demonstrate the self keyword 
# Stretch Goals
# Demonstrate object properties

# Instances 

# Run in ipdb session
# rose == cookie
#   False

#Read Attributes 
# rose.name -> rose
# rose.age -> 11

#Update
# rose.age -> 11
# rose.age = 12
# rose.age -> 12

