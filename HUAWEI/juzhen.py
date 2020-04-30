while True:
    try:

        hang1 = int(input())
        lie1 = int(input())
        lie2 = int(input())
        f = [[] for _ in range(hang1)]
        g = [[] for _ in range(lie1)]
        result = [[0 for i in range(lie2)] for j in range(hang1)]
        # f = [[int(i) for i in input().split()] for j in range(hang1)]
        # g = [[int(i) for i in input().split()] for j in range(lie1)]
        for i in range(hang1):
            f[i]= list(map(int,input().split(' ')))

        for i in range(lie1):
            g[i]= list(map(int,input().split(' ')))

        # func = lambda x,y:x*y
        # result[0][0]=f[0][i]*g[j][0]
        for i in range(hang1):
            for j in range(lie2):
                sum1 = 0
                for k in range(lie1):
                    sum1 = sum1 + f[i][k] * g[k][j]
                result[i][j] = sum1

        for i in range(hang1):
            str2 = ' '.join([str(x) for x in result[i]])
            print(str2)
            # for item in a:
            # print(str(item)+' ')

    except:
        break