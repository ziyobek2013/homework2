# kontaktlar = {}
#
# m = input("Ismingizni kriting: ")
# n = int(input("Raqam kiriting"))
#
# kontaktlar[m] = n
# print(kontaktlar)
#
# m = input("Ism kiriting")
# for x,v in kontaktlar.items():
#     if x == m :



def tictets():
    ism = input("Ismingizni kirriting: ")
    age = int(input("Yoshingizni kiriting:" ))
    if age <= 5 and 60 < age:
        return f"Siz uchun chipta tekin"

    elif age > 5 and age <18:
        return "Siz uchun chipta narxi 10ming som"

    elif age > 18 and age < 60:
        return "siz uchun chipta narxi 15ming som"

print(tictets())