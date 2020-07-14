import sys

# CSC 401

# Ximan Liu


sys.path.append("test")     # 其实 import sys 和这步 sys.path.append("test")没有必要

from hw import timer, find_file, game

if __name__ == '__main__':
    
    timer(5)
    
    print("-"*20)
    
    find_file("/Users/liuximan/Desktop/", "3.py")
    
    print("-"*20)
    
    print(game(12))
    

'''
Windows的路径 "c:\\Users\\Downloads\\Ximan"
iOS的路径 "/Users/liuximan/Desktop/"
'''
