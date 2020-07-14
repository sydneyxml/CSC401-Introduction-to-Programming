import random
import json

# CSC 401

# Ximan Liu


# Encryption

def encrypt_file(filename):
    in_file = open(filename, "r", encoding='utf-8')
    text = in_file.read()
    in_file.close()

    a_set = set()
    for char in text:
        a_set.add(char)

    new_list = list(a_set)
    random.shuffle(new_list)

    d1 = dict()
    for key in new_list:
        d1[key]=a_set.pop()
        
    file_out = open(filename+".enc", "w", encoding='utf-8')
    s = ''
    for char in text:
        s += d1[char]

    file_out.write(s)
    file_out.close()

    file_out = open(filename+'.dict', 'w', encoding='utf-8')
    file_out.write(json.dumps(d1))
    file_out.close()
    

# Decrypt

def decrypt_file(dict_filename, decrypt_filename):
    # a
    file_in = open(dict_filename, "r", encoding='utf-8')
    # b
    orig_dict = json.load(dict_filename)
    file_in.close()
    # c
    new_dict = {}
    # d
    new_dict = {v: x for x, v in orig_dict.items()}

    # e
    encrypted_file = open(decrypt_filename, "r", encoding='utf-8')
    text_decrypt_filename = encrypted_file.read()
    encrypted_file.close()
    # f
    decrypt_filename = decrypt_filename.replace(".enc", ".dec")
    output_file = open(decrypt_filename, 'w', encoding='utf-8')
    result = ''
    for c in text_decrypt_filename:
        result += new_dict[c]
    
    # g
    output_file.write(result)
    output_file.close()



source_file = "MobyDick.txt"

print("Encrypting input file " + source_file)
encrypt_file(source_file)

print("-"*20)

print("Decrypting input file " + source_file)
decrypt_file(source_file + ".dict", source_file + ".enc")



# Extra Credit

def top_word(filename):
    in_file = open(filename, 'r', encoding='utf-8')
    text = in_file.read()
    in_file.close

    text = text.replace(",", "")
    text = text.replace("$", "")
    text = text.replace("*", "")
    text = text.replace(";", "")
    text = text.replace(".", "")
    text = text.replace("&", "")
    text = text.replace("!", "")
    text = text.replace("(", "")
    text = text.replace("-", "")
    text = text.replace(")", "")

    words = text.split()

    di = {}
    for word in words:
        if word not in di:
            di[word] = 1
        else:
            di[word] = di[word] + 1

    max_count = 0
    max_item = ''
    for word in di:
        if di[word] > max_count:
            max_count = di[word]
            max_item = word

    return (max_item, max_count)


print(top_word("MobyDick.txt"))


