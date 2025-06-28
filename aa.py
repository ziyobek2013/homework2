#     natija = []
#      for soz in sozlar:
# if soz == soz[::-1]:
#  natija.append(soz)
#     return natija
# kiritilgan_sozlar = ["olma", "non", "ikki", "bob", "salom"]
# print(palindrom_sozlar(kiritilgan_sozlar))

teskari_soz = input("Soz kiritin:")
lst = []
if teskari_soz == teskari_soz[::-1]:
    lst.append(teskari_soz)

else:
    print(f"{teskari_soz} bu soz togri kelmaydi")