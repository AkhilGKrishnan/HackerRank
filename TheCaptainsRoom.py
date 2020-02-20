k,arr = int(input()),list(map(int, input().split()))
myset = set(arr)
counte = list(filter(lambda j: arr.count(j)==1 ,myset))
print(counte[0])
