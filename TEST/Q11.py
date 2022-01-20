#ref

def Repeat(x):
    size = len(x)
    repeated = []
    for i in range(size):
        k=i+1
        for j in range(k,size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated


lst1=[10,20,30,40,20,20,30,50,60,40,50]
print(Repeat(lst1))
