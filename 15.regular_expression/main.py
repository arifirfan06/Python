# Regular expression
import re

string1 = 'Testing program translate .As a program with nice syntax testing this should be easy'

print('result without re =','Testing' in string1)
#pattern can be use in regex code the syntax example is r"([a-zA-Z]).([a])"
pattern = re.compile(r"([a-zA-Z]).([a])") # to get advanced or simmilar to the input
res_re1 = re.search('Testing',string1)
res_re2 = pattern.search(string1) # .findall(), fullmatch(), match()
print('result with re =',res_re2.group()) # you can use .start() to get start index and .group() to get the matched text

# the example of real life regex is when you create email collecting app where you filter user email with suitable bussiness
# you can search "python email validation regex" take the regex code and test it