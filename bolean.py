#oprasi logika(boolean)

#not, or, and, xor

#NOT
print("=====not====")
a = False
c = not a
print("data a =",a)
print("-----Not-----")
print('data c =',c)

#OR(jika salah satu true = true)
print("=====Or====")
a =False
b = False
c = a or b
print(a," OR",b,'=',c)
a = True
b = False
c = a or b
print(a,"  OR",b,'=',c)

#AND (dua buah true = true)
print("====AND====")
a = True
b = False
c = a and b
print(a," and",b,'=',c)

#EXOR (hanya satu true = true)
print("====EXOR====")
a = True
b = False
c = a ^ b
print(a," EXOR",b,'=',c)
a = True
b = True
c = a ^ b
print(a," EXOR",b,'=',c)