
mevalar = []
mevalar.append("gilos")
mevalar.append("anor")
mevalar.append("shaftoli")
mevalar.append("olma")
mevalar.append("nok")
print(mevalar)

mevalar[1] = "o`rik"
print(mevalar)

#  3. topshiriq
mevalar.remove("gilos")
print(mevalar)

#  4. topshiriq
print(len(mevalar))

# 5-misol
mevalar.sort()
print(mevalar)

# 6-misol
mevalar.reverse()
print(mevalar)

# 7-misol
mevalar.index("nok")
print(mevalar)

# 9
raqam = [1, 2, 2, 3, 4, 5]
mevalar.extend(raqam)
print(mevalar)
#
# 10

n = raqam.count(2)
print(n)
