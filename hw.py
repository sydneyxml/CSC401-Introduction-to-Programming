import time
import os

# CSC 401

# Ximan Liu


# 1)

def timer(n):

    if n <= 0:
        print("Timer Done")

    else:
        print(n, "<1 sec pause>")   # 不用加 <1 sec pause>
        time.sleep(1)
        timer(n-1)


# 2)

def find_file(path, file):
    try:
        my_list = os.listdir(path)
        for filename in my_list:
            if filename == file:
                print(os.path.join(path, filename))
            if os.path.isdir(filename):   # 这行的filename应为os.path.join(path, filename)
                find_file(filename, file)   # 这行的filename应为os.path.join(path, filename)
    except PermissionError:
        pass
                

# 3)

def game(money, result=''):

    value = [50, 20, 10, 5, 1]

    for list_value in value:    
        if money >= list_value:
            count = int(money // list_value)
            result += '${} '.format(list_value) * count
            remaining_count = money - (list_value * count)

            return game(remaining_count, result)

    return result[:-1]  # 除去空格


