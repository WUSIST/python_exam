str1 = '"a b" c d "c a"'
str2 = str1.split('"')
while '' in str2:
    str2.remove('')
for i in range(len(str2)):
    if str2[i][0]== ' ':
        b = str2[i].split(' ')
        while '' in b:
            b.remove('')
        for item in b:
            print(item)
    else:
        print(str2[i])
