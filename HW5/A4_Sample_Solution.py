import random
import json

# CSC 401

# Ximan Liu


def encrypt_file(filename):

    try:
        open_file = open(filename, 'r', encoding='utf-8')
        file_content = open_file.read()
        open_file.close()

        char_set = set(file_content)
        char_list = list(char_set)
        random.shuffle(char_list)

        encrypt_dict = {}
        for a_char in char_list:
            encrypt_dict[a_char] = char_set.pop()

        enc_file = open(filename+'.enc', 'w', encoding='utf-8')
        for s_char in file_content:
            enc_file.write(encrypt_dict[s_char])
        enc_file.close()

        dict_file = open(filename+'.dict', 'w', encoding='utf-8')
        dict_file.write(json.dumps(encrypt_dict))
        dict_file.close()
        return True

    except FileNotFoundError:
        return None

    except PermissionError:
        return None



def decrypt_file(dict_filename, enc_filename):

    try:
        dict_file = open(dict_filename, 'r', encoding='utf-8')
        orig_dict = json.load(dict_file)
        dict_file.close()

        decrypt_dict = {}
        for each_key in orig_dict:
            decrypt_dict[orig_dict[each_key]] = each_key

        enc_file = open(enc_filename, 'r', encoding='utf-8')
        file_content = enc_file.read()
        enc_file.close()

        dec_filename = enc_filename.replace('.enc', '.dec')
        output_file = open(dec_filename, 'w', encoding='utf=8')
        for each_char in file_content:
            output_file.write(decrypt_dict[each_char])
        output_file.close()
        return True

    except FileNotFoundError:
        return None

    except PermissionError:
        return None



if __name__ == '__main__':
    print("Run the program using 'main.py'")


