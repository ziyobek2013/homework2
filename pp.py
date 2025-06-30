talabalar = {
    "Shoxjaxon": [5,4,3,2,],
    "Ozodbek": [5, 4, 5, 3],
    "Ziyobek": [4, 4, 5, 4],
    "Sayyodbek": [3, 4, 3, 4]
}

m = input("Isim kiritig: ")

for k, v in talabalar.items():
    if m == k:
        print(v)

    elif m != k:
        print("yoq bu odam ")