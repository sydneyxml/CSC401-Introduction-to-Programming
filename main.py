import sys

# CSC 401

# Ximan Liu


sys.path.append("hw5")

from A4_Sample_Solution import encrypt_file, decrypt_file

if __name__ == '__main__':

    source_file = "MobyDick.txt"

    print("Encrypting input file " + source_file)

    text_file = encrypt_file(source_file)
    if text_file is True:
        print("-"*20)
        print("Decrypting input file " + source_file)
        decrypt_file(source_file + ".dict", source_file + ".enc")
