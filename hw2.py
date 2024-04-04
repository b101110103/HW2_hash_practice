with open("hw2_data.txt", 'r') as file:
    content = file.read()

dict = {}

for i in content.split():
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1

num = len(dict)

print('總共有', num, '個不重複的英文字')

for key in dict:
    print(key, '有', dict[key], '個')