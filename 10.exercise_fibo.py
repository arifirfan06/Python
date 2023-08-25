def fibo(length):
    num_list= []
    for i in range(length):
        if num_list == [] :
            num_list.append(i)
        if len(num_list) == 1:
            num_list.append(len(num_list))
        else:
            num_list.append(num_list[-1] + num_list[-2])
    return num_list


print(fibo(20))

# with generator according to tutorial
def fib(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        temp = a
        a = b
        b = temp + b

for num in fib(20): # blazingly fast!
    print(num)