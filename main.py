def removeLast(x):
    x.pop(x[len(x)- 2])
    return x


print(removeLast([1, 2, 3, 4, 5]))