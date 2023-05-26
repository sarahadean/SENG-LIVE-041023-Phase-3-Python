# # 1. ✅ Demonstrate First Class Functions
#     # Create functions to be used as callbacks 

# def dance(music):
#     print(f'We dance to {music}!')

# def listen(music):
#     print(f'We listen to {music}!')

#     # Create a higher-order function that will take a callback as an argument
# #higher order function accepting a callback as a param
# def activate_fun(callbackfunc):
#     #callback function invocation
#     return callbackfunc("Price")

# #activate_fun(dance)
# # activate_fun(listen)

# # 2. ✅ Create a higher-order function that returns a function

# #1. outer function : activate fun
# def activate_fun(): 
#     #2. inner function 
#     def dance(music):
#         return f'We dance to {music}' # 3. inner func logic
#     return dance #4. return the inner func

# print(activate_fun()) # 5. dance function reference
# # dance = activate_fun()
# # print(dance("Prince"))
# print(activate_fun()("Prince"))

# 3. ✅ Demonstrate a decorator
# 1. Create a function that takes a function as an argument, 
# 2. has an inner function, 
# 3. returns the inner function

#1. decorator 
def coupon_calculator(callbackfunc): #7. func as a param

    #2. inner function 
    def report_price():
        print('Initial price = $28.00') #3. print initial price
        final_price = callbackfunc(28.00) #4. calculate the final price w a new func
        #8. whatever func is passed in , invoke the func
        print(f'Newly Discounted price = ${final_price}') #5. interpolate the calculated final price

    return report_price # 6. return the report price 




# Demo examples of the decorator with and without pie syntax '@'

    # Without pie syntax 
# #9. 
# def calculate_price(price):
#     return '{:.2f}'.format(round(price/2, 2)) # with 2 decimal points 

# coupon_calculator(calculate_price)()

    # With pie syntax

@coupon_calculator
def calculate_price(price):
    return '{:.2f}'.format(round(price/2, 2)) 

calculate_price()