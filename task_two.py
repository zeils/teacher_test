from itertools import combinations, permutations


all_names = input().split()
names_with_K =[]
names_without_K =[]



for name in all_names:
    if name[0] == 'K':
        names_with_K.append(name)
    else:
        names_without_K.append(name)

if len(names_with_K) == 0:
    print ('-1')
else:
    for k in permutations(names_with_K):
        for no_k in permutations(names_without_K):
            print (k + no_k)

