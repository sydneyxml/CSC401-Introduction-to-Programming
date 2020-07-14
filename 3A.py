
# CSC 401

# Ximan Liu

# Problem A

def word_finder(filename, search_string):

    input_file = open(filename, 'r')
    lines = input_file.readlines()
    input_file.close()

    counter = 0
    for line in lines:
        counter += line.count(search_string)  #精简，所以没有出现if判断find the string
    return counter

name = input("File name: ")
word = input("Search word: ")

num = word_finder(name, word)

print("{} appears in {} {} times".format(word, name, num))
print(word, "appears in", name, num, "times.")


# 1. 定义完函数 [函数名+变量都有哪些] --> 打开文档 [要打开的文档变量, "r"] + read一切 [readlines--按line by line读取] + 关闭文档.close()
# 2. 开始计数从counter = 0开始 [此处一个等号就可以] --> 建立for loop: for line in lines: --> counter += line.count(search_string) [要找的字符] --> return counter

# def函数部分正式结束

# 3. name = input("Enter: ") --[get a file name] --> word = input("Enter: ") --[get the specific search_string name]

# 4. [call the function]: num = word_finder(name, word) --[起一个要找的名字，之后call the function, 括号里是上一步input的变量名，input变量名不加引号]

# 5. 按格式输出 print("() appears in () () times".format(word, name, num)) --[format格式，输入三变量]
