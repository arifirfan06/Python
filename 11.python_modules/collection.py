from collections import defaultdict

dictionary = defaultdict(lambda: 0, {'a': 2, 'b': 1}) # with defaultdict it wont return error 
print(dictionary['c'])