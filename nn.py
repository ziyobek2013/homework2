# def karta_raqam (rqam):
#     return rqam
# print(karta_raqam("************5678"))
# print(karta_raqam("************3213"))
# print(karta_raqam("************5523"))
def bro(word):
    jami = 0
    vowels = "aeio"
    for x in word:
        for i in vowels:
            if x == i:
                jami += 1

    return jami

print(bro("Celebration"))
print(bro("Palm"))
print(bro("Prediction"))