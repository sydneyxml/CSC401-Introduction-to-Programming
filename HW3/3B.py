
# CSC 401

# Ximan Liu

# Problem B

def extract(filename, search_string):
    
    input_file = open(filename, 'r')
    file_content = input_file.read()      #read: read all contents in a long string, 便于处理定位后剪辑片段
    input_file.close()     #复制粘贴

    file_content = file_content.replace('\n', '|')  #打开文档读取完并关闭后，处理content的格式，用replace(), 括号中'\n'代表换行，'|'人为插入符号，括号中输入的就是要replace改正的
    instances = file_content.count(search_string)

    extracts = []      #建立空列表，[]之间不用空格
    for c in range(instances):  #range后面为什么instance?

        location = file_content.find(search_string)     #不是要计数，而是要找寻到关键词
        start = location - 30
        end = location + len(search_string) +30

        #可替换成end = min(len(file_content), location + len(search_string) + 30)

        sub = file_content[start:end]
        extracts.append(sub)    #空列表里添加sub, 和+=同理
        

        file_content = file_content[location + len(search_string):]
        #move and get rid of the part of the string you've already looked at, 找寻下一个string
        
    return extracts             #function部分结束


file = input("File name: ")
word = input("Search string: ")

results = extract(file, word)   #call the function

parts = file.split('.')         #分割文档名，少用hard-coded, split(".") ---- 可被符号隔开

new_file = parts[0] + '_' + word + '.' + parts[1]
print(new_file)                 #print function才能出结果

#命名文档名

output_file = open(new_file, 'w')

#write文档

for c in range(len(results)):
    output_file.write("{}) {}\n".format((c+1), results[c]))    #为什么会有results[c]: elements from my list of c     #(c+1)是序号从1开始

#给每一行文档从1开始计数

output_file.flush()     #刷新缓冲区。在用了write后，将缓冲区中的数据立刻写入文件，同时清空缓冲区，不需要是被动的等待输出缓冲区写入。一般的，文件关闭后会自动刷新缓冲区，但有时需要在关闭前刷新它，这时用到flush()
output_file.close()

#关闭文档



#什么是hard-coded: 例如extract("Dracula.txt", "Whitby") --手动输入关键词加引号，但是不能这样做，因为是强行手动输入，应该让用户做
#直接输入这部错在哪里？错在没有看题意，change the nature of your output改变输出内容的性质，所以要adjust form of content

#不能是 new_file = file[0:7] + word + ".txt" 的原因是，solution应该是通用解，[0:7]只适用于特定的文档，不够通用，这也说明了为什么不能hard-coded
#设想的方法是，split('.'), 用'.'来分割文档名和txt

