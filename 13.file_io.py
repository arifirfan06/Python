# File Input/Output
# my_file = open('test.txt')
# print(my_file.read())
# my_file.seek(0)
# print(my_file.read()) # you can read same file once if you want to read twice use my_file.seek(0)
# .readline() use to read single line and readlines() read multi and convert to list
# my_file.close() # if done use close so it can be used somewhere else

# the better way without using .close is using with statement
with open('file_test/test.txt', mode='a') as test_text: # param 2 is mode, r means read, to read and write use w, a, r+
    text = test_text.write('worked?') # .write will add text characters to existing note if mode is r+
    print(text) # mode 'a' means append

# if you want to create new file the mode is w
# the common way in handling file is using try and except
try:
    with open('book.txt', mode='w') as book_text: 
        text = book_text.write('here is a nice book') 
        print(text)
except (FileNotFoundError, IOError) as err:
    raise err
