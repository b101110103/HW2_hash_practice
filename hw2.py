#開啟檔案
with open("hw2_data.txt", 'r') as file:
    content = file.read()

#設立一個新的dictionary
dict = {}

#逐行讀取
#如果是不曾讀取過的key，則相對的value先設為1，若是讀取過的key，相對應的value加1
for i in content.split():
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1

#輸出結果
num = len(dict)

print('總共有', num, '個不重複的英文字')

for key in dict:
    print(key, '有', dict[key], '個')