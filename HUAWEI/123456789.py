a = input()
while len(a)>8:
        print(a[0:8],'\n')
        del a[0:8]
print( a + '0'*(8-len(a)))
 
