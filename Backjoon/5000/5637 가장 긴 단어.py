import re

string = ""
tmp = ""
while "E-N-D" not in tmp:
    tmp = input()
    string += tmp

pattern = re.compile('[a-zA-Z\-]+')
search = pattern.findall(string)

length = 0
most = ""
for word in search[:-1]:
    if length < len(word):
        most = word
        length = len(word)
        # print(length)
# print(word)
print(most.lower())