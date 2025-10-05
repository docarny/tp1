def unite(n):
    a = n*n
    while n*n != 9 :
        print("trop bas")
    elif n*n > 9 :
        print("trop haut")
    elif a == 9:
        print('untite trouve')
    return unite(3)
print(unite(3))



