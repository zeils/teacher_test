n = 1+int(input()) 
m = 1000*int(input())

weight_count = []
for i in range (n):
    weight_count.append(3**i)

print (weight_count)

weight_result = []

while (m > 0):
    print (m)
    if m-weight_count[n-1] >= 0:
        m=m-weight_count[n-1]
        weight_result.append(weight_count[n-1])
    if m-weight_count[n-1] >= 0:
        m=m-weight_count[n-1]
        weight_result.append(weight_count[n-1])


    n= n-1
    if n < 0:
        print ('завершено с ошибкой')
        print ('-1')
        break
    if m == 0:
        print ('завершено успешно')
        print (weight_result)
        break



