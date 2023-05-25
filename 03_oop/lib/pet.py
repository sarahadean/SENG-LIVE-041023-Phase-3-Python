#!/usr/bin/env python3
# Demonstrate classes 
# 1. ✅ Create a Pet class
# 2. ✅ Instantiate a few pet instance 
    # Compare the pet instances to demonstrate they are not the same object
    # Note: add 'pass' to the pet class 

import ipdb

#1. define a pet class
#class keyword
# class Pet: #UpperCamelCase #PascalCase

#     pass

# ipdb.set_trace()

# baboi = Pet()  # instantiate a new instance 
# fiona = Pet()
# beau = Pet()
# winnie = Pet()
# chloe = Pet()
# moseph = Pet()
# beau            # calling the instance  
# <__main__.Pet object at 0x106c61160> #instance detail 

# ipdb> winnie == chloe
# False

# winnie and chloe are not the same. They are different objects in memory 
# they are coming the same source, Pet class


# 3. ✅ Demonstrate __init__ 
    # Add arguments to instances  
    # use dot notation to access their attributes 
    # update attributes with new values 

class Pet:
    # initialization method / init method

    #species = "Canis lupus familiaris" # class attribute

    def __init__(self, name, age, breed, temperament): #attributes
        # to provide objects(instances) with unique attributes upon the instantiation
        # print(self, name, age, breed)

        # Attached incoming parameters to the self's attributes
        # self is always the instance
        self.name = name  #instance attribute #1
        self.age = age #instance attribute #2 
        self.breed = breed #instance attribute #3
        self.temperament = temperament # instance attribute #4
        self.park = "central park"
    pass

# baboi = Pet("Baboi", 2, "chihuahua", "Tranquil") 
#instantiate a new instance with attribute details

# ipdb.set_trace()
# print(baboi)

# what is self? 
    # self => instance of Pet class
    # <__main__.Pet object at 0x100e17910>
    # we know that the self is `baboi`, exactly same as the instance  


# 4.✅ Demonstrate instance methods by creating a print_pet_details function that will print the pet attributes

    #instance method
    def print_pet_detail(self): #self refers to the instance  
        #Review the self keyword 

        #f string with multiline with triple single quotes
        print(f'''
            name:{self.name}
            age:{self.age}
            breed:{self.breed}
            temperament:{self.temperament} 
        ''')

# baboi = Pet("Baboi", 2, "chihuahua", "Tranquil") 

#baboi.print_pet_detail() # invoking the instance method using the dot notation 
#ipdb.set_trace()
#     Invoke the print_pet_details on an instance 
#           -> 
            # name:rose
            # age:11
            # breed:domestic longhair
            # temperament:sweet


# Object Properties => Attributes that are controlled by methods
    # 1. Create an Owner class 
class Owner:
    def __init__(self, age): #provide parameters
        self.age = age #set the attribute of the instance

    # Create an Owner class with two instance methods:

    #2. get_name => Retrieve Owner's name
    def get_name(self):
        print("Retrieving Owner's name")
        return self._name #property, not attribute so we are using the '_'

    #3. set_name => Set Owner's name
    def set_name(self, name):
        print("Setting Owner's name...")
            #conditional logic
            #3-1. Ensure that Owner's name is a string
        if(isinstance(name, str)): #if the name is str, if its TRUE
            #assign the incoming "name"as "_name" for the owner instance
            self._name = name

            #3-2. If not, issue warning of "Name must be a string"
        else:
            print("Name must be a string")

    #4. Use property() to compile get_name / set_name and invoke them
    name = property(get_name, set_name)



eugene = Owner(24)
print(eugene)
eugene.set_name("Eugene")
print(eugene.get_name())
print(eugene.name)

    #Whenever we access an Owner instance's name