import sys

# CSC 401

# Ximan Liu


sys.path.append("test")

from hw import timer, find_file, game

if __name__ == '__main__':
    
    timer(5)
    
    print("-"*20)
    
    find_file("/Users/liuximan/Desktop/", "3.py")
    
    print("-"*20)
    
    print(game(12))
    
