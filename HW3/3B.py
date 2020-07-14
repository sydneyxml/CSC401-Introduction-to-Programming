
# CSC 401

# Ximan Liu

# Problem B

def extract(filename, search_string):
    
    input_file = open(filename, 'r')
    file_content = input_file.read()
    input_file.close()

    file_content = file_content.replace('\n', '|')
    instances = file_content.count(search_string)

    extracts = []
    for c in range(instances):

        location = file_content.find(search_string)
        start = location - 30
        end = location + len(search_string) +30

        sub = file_content[start:end]
        extracts.append(sub)
        

        file_content = file_content[location + len(search_string):]
        
    return extracts


file = input("File name: ")
word = input("Search string: ")

results = extract(file, word)

parts = file.split('.')

new_file = parts[0] + '_' + word + '.' + parts[1]
print(new_file)

output_file = open(new_file, 'w')


for c in range(len(results)):
    output_file.write("{}) {}\n".format((c+1), results[c]))


output_file.flush()
output_file.close()

