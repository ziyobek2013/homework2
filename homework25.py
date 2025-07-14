def teskari(lst, val):
    yangi = []
    val_list = []
    for x in lst:
        if x == val:
            yangi.append(x)
        else:
            val_list.append(x)
    new_list = yangi + val_list
    return sorted(new_list, reverse=True)
print(teskari([1, 2, 1, 3], 1))
