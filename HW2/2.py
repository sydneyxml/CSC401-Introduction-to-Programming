
import math


# CSC 401

# Ximan Liu


#Problem A

P1 = [1.4, 5.2]

P2 = [7.8, 1.6]

# Distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)

distance = math.sqrt((P2[0]-P1[0])**2 + (P2[1]-P1[1])**2)

print("Distance:", distance)


#Problem B

wall_widths = [8, 4, 4, 6, 4, 10]

print(math.ceil(10*sum(wall_widths) / 250))


#Problem C

x = float(input("Enter x:"))

y = float(input("Enter y:"))

new_user_point = [x,y]

P1 = [1.4, 5.2]

P2 = [7.8, 1.6]

if (new_user_point[0] > P1[0] and new_user_point[0] < P2[0] and new_user_point[1] > P2[1] and new_user_point[1] < P1[1]):
    print("True")
else:
    print("False")


#Problem D

# Div by 6 but not 4
# range (1, 151)

numbers = []
for x in range (1, 151):
    if x % 6 == 0 and x % 4 != 0:
        numbers.append(x)
print("Numbers:", numbers)

