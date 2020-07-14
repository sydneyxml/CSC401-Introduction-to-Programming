
# CSC 401

# Ximan Liu

# Problem A

def word_finder(filename, search_string):

    input_file = open(filename, 'r')
    lines = input_file.readlines()
    input_file.close()

    counter = 0
    for line in lines:
        counter += line.count(search_string)
    return counter

name = input("File name: ")
word = input("Search word: ")

num = word_finder(name, word)

print("{} appears in {} {} times".format(word, name, num))
print(word, "appears in", name, num, "times.")

