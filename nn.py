# # def karta_raqam (rqam):
# #     return rqam
# # print(karta_raqam("************5678"))
# # print(karta_raqam("************3213"))
# # print(karta_raqam("************5523"))
# def bro(word):
#     jami = 0
#     vowels = "aeio"
#     for x in word:
#         for i in vowels:
#             if x == i:
#                 jami += 1
#
#     return jami
#
# print(bro("Celebration"))
# print(bro("Palm"))
# print(bro("Prediction"))
def kopaytir(*args):
    natija = 1
    for son in args:
        natija *= son
    return natija
print(kopaytir(2, 3, 4))
print(kopaytir(5))        # Natija: 5
print(kopaytir())         # Natija: 1
