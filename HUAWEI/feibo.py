# a = 10
# d = [1,1]
# for i in range(a-2):
#     d.append(d[i]+d[i+1])
# print(d[5-1])

# def feobo(a):
#
#     if a <= 1:
#
#         return a
#     else:
#         return feobo(a-1)+feobo(a-2)
#
# print(str(feobo(5)))

# pre = [0,0,0,0,1,0,2,3,5]
# val = [0,5,1,8,4,6,3,2,4]
#
# f = [0]*9
# for i in range(1,8+1):
#     f[i] = max(f[i-1],
#                f[pre[i]]+val[i])
# print(str(f))

# val = [0,0,1,2,4,1,7,8,3]
val = [0,0,4,1,1,9,1]
f = [0]*len(val)
f[1] =1
for i in range(2,len(val)):
    f[i] = max(f[i-1],f[i-2]+val[i])
print(f)

a = [0,3,34,4,12,5,2]
s=9
for i in range(1,len(a)):
    f[i] = f[]