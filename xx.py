def raqamlar(integer):
    natija = []
    for x in integer:
        if x % 2 != 0:
            natija.append(x ** 2)
    return natija

print(raqamlar([1,2,3,4,5,6,7]))
print(raqamlar([8,9,10,11,12,13,14]))
print(raqamlar([15,16,17,18,19,20]))

