students = []
while True:
    name, age, wei = input().split()
    age = int(age)
    wei = int(wei)
    if name == "#":
        break
    students.append((name, age, wei))

for n, a, i in students:
    if a > 17 or i >= 80:
        print(n, "Senior")
    else:
        print(n, "Junior")
