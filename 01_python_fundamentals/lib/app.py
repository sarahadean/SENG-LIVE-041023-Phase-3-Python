#!/usr/bin/env python3

# 📚 Review With Students:
    # Python environment set up
	# Python debugging tools 
	# Python datatypes 

# 🚨 To enable ipdb debugging, first import "ipdb"
#import ipdb

# def hello_world():
#     sleepy = "bear"
#     print(sleepy)

#     ipdb.set_trace() # pause the execution of code. #debugger here

#     not_interpreted_yet = "coffee"
#     print(not_interpreted_yet)

# hello_world()

# 1. ✅ Create a condition to check a pet's mood
    # If "pet_mood" is "Hungry!", "Rose needs to be fed."
    # If "pet_mood" is "Rowdy!", "Rose needs a walk."
    # In all other cases, "Rose is all good."

    # Note => Feel free to set your own values for "pet_mood" to view various outputs.

#JS => camelCase
#python => snake_case

# JS => can declare variable without assignment
# python => cannot declare variable without assignment



#conditional syntax 
# if pet_mood == "Hungry!":
#     print("Rose needs to be fed.")
# elif pet_mood == "Rowdy":
#     print("Rose needs a walk.")
# else:
#     print("Rose is all good.")


# 2. ✅ Create a ternary operator using "pet_mood" as a condition:
    # If pet_food is "Hungry!" => "Rose needs to be fed."
    # In all other cases => "Rose is all good."

#JS
    #condition? true: false

#python
    #true, if condition else default val

# pet_mood = "Hungry!"
# pet_name = "Rose"

# print("Rose needs to be fed.") if pet_mood == "Hungry!" else print("Rose is all good.")

# 3. ✅ Create a function (say_hello) that returns the string "Hello, world!"
    # Test invocation of "say_hello" in ipdb using "say_hello()"
    # say_hello() => "Hello, world!"

#python => def (define)
#JS => function



# import ipdb

# def say_hello():
#     print("Hello, world!")
#     return "Hello, world!"

# say_hello()


# JS
    #can invoke function containing params without argument 

# python 
    #cannot invoke function containing params without argument 
    #unless we've supplied a default argument

#default argument
# def say_hello(param = "hello"):
#     print(param)
#     return "Hello World!"

# say_hello()



# 4. ✅ Create a function (pet_greeting) that will return a string with interpolated pet's name
    # Test invocation of "pet_greeting" in ipdb using "pet_greeting()"
    # pet_greeting("Rose") => "Rose says hello!"
    # pet_greeting("Spot") => "Spot says hello!"

# def pet_greeting(name):
#     return f"{name} says hello!"

# print(pet_greeting("Rose"))
# print(pet_greeting("Spot"))

# 5. ✅ Move conditional logic from Deliverable 1 into a function (pet_status) so that we may use it with different pets / moods
    # Test invocation of "pet_status" in ipdb using "pet_status(pet_name, pet_mood)"
    # pet_status("Rose", "Hungry!") => "Rose needs to be fed."
    # pet_status("Spot", "Rowdy!") => "Spot needs a walk."
    # pet_status("Bud", "Relaxed") => "Bud is all good."
    
    # Take a moment to note that "pet_name" and "pet_mood" parameters are within Local Scope and take priority over "pet_name" and "pet_mood"
    # in Global Scope.
# import ipdb
# def pet_status(name, mood):
#     if mood == "Hungry!":
#         #ipdb.set_trace()
#         return f"{name} needs to be fed."  
#     elif mood == "Rowdy!":
#         return f"{name} needs a walk."
#     else:
#         return f"{name} is all good."

# print(pet_status("Rose", "Hungry!"))
# print(pet_status("Spot", "Rowdy!"))
# print(pet_status("Bud", "Relaxed"))
         

# 6. ✅ Create a function (pet_birthday) that will increment a pet's age up by 1. Use try / except to handle errors. 
    # If our function is given an incorrect datatype, it should handle the TypeError exception and alert the user.
    # pet_birthday(10) => "Happy Birthday! Your pet is now 11."
    # pet_birthday("oops") => "Type Error Occurred"

def pet_birthday(age):

    #attempt to execute code
    try: 
        return f"Happy Birthday! Your pet is now {age+1}"
    
    #if an error of a particular type occurs,
    #execute some other bit of code

    except TypeError:
        return "Type Error Occurred"

print(pet_birthday(14))

    # Note => To view more common Python exceptions, visit https://docs.python.org/3/library/exceptions.html

# 🚨 To create an ipdb breakpoint, comment / uncomment line below:
# ipdb.set_trace()


