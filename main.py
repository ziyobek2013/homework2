#  1. topshiriq
mevalar = []
mevalar.append("olma")
mevalar.append("banan")
mevalar.append("shaftoli")
mevalar.append("gilos")
mevalar.append("nok")
print("1. Mevalar ro'yxati:", mevalar)

#  2. Elementlarni indeks orqali o‘zgartirish
mevalar[1] = "anor"
print("2. 2-element o‘zgartirilgan:", mevalar)

#  3. topshiriq
mevalar.remove("gilos")
print("3. 'gilos' o‘chirildi:", mevalar)

#  4. topshiriq
print("4. Ro‘yxat uzunligi:", len(mevalar))

#  5. topshiriq
sonlar = [12, 5, 8, 1, 19]
sonlar.sort()
print("5. Tartiblangan ro‘yxat:", sonlar)

#  6. topshiriq
sonlar.reverse()
print("6. Teskari tartib:", sonlar)

#  7. topshiriq
indeks = mevalar.index("anor")
print("7. 'anor' indeksi:", indeks)

#  9. topshiriq
mevalar.insert(2, "uzum")
print("9. 2-indeksgacha 'uzum' qo‘shildi:", mevalar)

#  10. topshiriq
raqamlar = [1, 2, 2, 3, 4, 2, 5]
takror_soni = raqamlar.count(2)
print("10. Raqam 2 necha marta ishtirok etgan:", takror_soni)