# Error Handling
# We can use try and except

# Error Handling 1
while True:  # we can use while true to keep input running until there is no error or the data is valid
    try:
        age = int(input('Please input your age'))
        print(age)
        10/age
        # raise Exception('this function has error') # this is rare case, if you want to throw error msg
    except ValueError:  # valueerror, zerodivisionerror are type of python error according in the docs
        print('Please enter valid number')
    except ZeroDivisionError:
        print('Please enter number above 0')
    else:  # else work in try except block
        print('thank you')
        break  # stop the loop
    finally:  # this triggered when all statement above are executed
        print('Done!')
    # this wont triggered if the meet condition have break statement
    print('try again')

# Error Handling 2
# def sum(num1, num2):
#     try:
#         return num1 / num2
#     except (TypeError, ZeroDivisionError) as err: #err return object
#         print(f'Please input valid number {err}')

# print(sum(2,0))

# Error Handling 3
