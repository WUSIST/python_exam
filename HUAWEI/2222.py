str1 = input()
index = 0
def strremove(str2):
    while  ''  in str2:
        str2.remove('') 
    return str2
for item in str1:
    if item == '"':
        index = 1
if index == 0:
    print(len(str1))
    for i in str1.split(' '):
        print(i)
else:
    str2 = str1.split('"')
    print(len(str2)
strremove(str1)
    
    for i in range(len(str2)):
        if str2[i][0]== ' ':
            b = str2[i].split(' ')
            strremove(b)
            for item in b:
                print(item)
        else:
            print(str2[i])
