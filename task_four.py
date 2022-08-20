n, m = map(int, input().split())
 
lab = []
for i in range(n):
    vr_ls = [int(s) for s in input().split()]
    lab.append(vr_ls)
 
a, b = map(int, input().split())
 
if lab[0][0] == 1:
    print ('-1')
else:
 
    for i in range(len(lab)):
        for j in range(len(lab[i])):
            if lab[i][j] == 0:
                lab[i][j] = -1
            elif lab[i][j] == 1:
                lab[i][j] = -2
 

    lab[0][0] = 0
    t = [(0, 0)]

    while len(t) != 0:
        t_vr = []
        for koo in t:
            i, j = koo[0], koo[1]
            count = lab[i][j] + 1
 
            if i > 0 and lab[i-1][j] == -1:
                lab[i-1][j] = count
                t_vr.append((i-1, j))
            if i < n - 1 and lab[i+1][j] == -1:
                lab[i+1][j] = count
                t_vr.append((i+1, j))
            if j > 0 and lab[i][j-1] == -1:
                lab[i][j-1] = count
                t_vr.append((i, j-1))
            if j < m - 1 and lab[i][j+1] == -1:
                lab[i][j+1] = count
                t_vr.append((i, j+1))
 
        t = t_vr
    print(lab[a][b])

