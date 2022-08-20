n, m, a = list(map(int, input().split()))
my_list = []
x = 0
y = 0
b = 1
c = 1
d = 1
e = 1
for g in range(n):
    my_list.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        if my_list[i][j] == a:
            x = i
            y = j


if (m == 1) or (n == 1):
    b = a

elif y == 0:
    if x == 0:
        b = my_list[x + 1][y + 1]
    elif x == m - 1:
        c = my_list[x - 1][y + 1]
    else:
        b = my_list[x + 1][y + 1]
        c = my_list[x - 1][y + 1]
elif y == n - 1:
    if x == 0:
        d = my_list[x + 1][y - 1]
    elif x == m - 1:
        e = my_list[x - 1][y - 1]
    else:
        d = my_list[x + 1][y - 1]
        e = my_list[x - 1][y - 1]
else:
    if x == 0 :
        d = my_list[x + 1][y - 1]
        b = my_list[x + 1][y + 1]
    elif x == m-1:
        e = my_list[x - 1][y - 1]
        c = my_list[x - 1][y + 1]
    else:
        b = my_list[x + 1][y + 1]
        c = my_list[x - 1][y + 1]
        d = my_list[x + 1][y - 1]
        e = my_list[x - 1][y - 1]
    
print(b * c * d * e)