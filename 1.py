
# CSC 401

# Ximan Liu


#Part A

c = 22
f = c * (9/5) + 32
print("Fahrenheit:", f)


#Part B

varl = "Pseudohypoparathyroidism"
c = "popar"
print(c in varl)


#Part C

my_list = ['Pear']

my_list.append('Apple')

my_list.append('Orange')

my_list.append('Raspberry')

my_list.append('Kiwi')

my_list.append('Fig')

print(my_list)

print(len(my_list))

print(max(my_list, key = len))

print(min(my_list, key = len))


#Part D

n = [70, 92, 68, 67, 89, 75, 89, 77, 81, 60, 81, 90]

print(n)

print(len(n))

print(min(n))

print(max(n))

print(sum(n) / len(n))


#Part E

name = ['Vito', 'Michael', 'Kay', 'Fredo', 'Connie', 'Luca']

name.sort()

print(name[0])

print(name[-1])

