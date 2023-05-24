#!/usr/bin/env python3
# Demonstrate classes 
# 1. ✅ Create a Pet class
# 2. ✅ Instantiate a few pet instance 
    # Compare the pet instances to demonstrate they are not the same object
    # Note: add 'pass' to the pet class 

# import ipdb

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
    def __init__(self): # initialization method
        # to provide objects(instances) with unique attributes upon the instantiation
        print(self)
    pass

baboi = Pet()


# what is self? 
    # self => instance of Pet class
    # <__main__.Pet object at 0x100e17910>
    # we know that the self is `baboi`, exactly same as the instance  


# 4.✅ Demonstrate instance methods by creating a print_pet_details function that will print the pet attributes
#     Review the self keyword 
#     Invoke the print_pet_details on an instance 
#           -> 
            # name:rose
            # age:11
            # breed:domestic longhair
            # temperament:sweet
            # image_url:rose.jpg


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

