#oprasi komparasi
#>,<,>=,<=,==,!=,is, is not
a = 5
b = 3
#> 
print("=========lebih besar dari================")
hasil = a > 4
print(a,'>',4,'=',hasil)
hasil = b > 3
print(b,'>',3,'=',hasil)

#< 
print("========lebih kecil dari========")
hasil = a < 4
print(a,'<',4,'=',hasil)
hasil = b < 3
print(b,'<',3,'=',hasil)

#>=
print("========lebih kecil dari sama dengan========")
hasil = a >= 4
print(a,'>=',4,'=',hasil)
hasil = b >= 3
print(b,'>=',3,'=',hasil)

#<=
print("========lebih kecil dari sama dengan========")
hasil = a <= 4
print(a,'<=',4,'=',hasil)
hasil = b <= 3
print(b,'<=',3,'=',hasil)

#==
print("========sama dengan========")
hasil = a == 4
print(a,'==',4,'=',hasil)
hasil = b == 3
print(b,'==',3,'=',hasil)

#!=
print("========tidak sama dengan========")
hasil = a != 4
print(a,'!=',4,'=',hasil)
hasil = b != 3
print(b,'!=',3,'=',hasil)

#is komparai objek
x =  5
y = 5
print("nilai x =",x,"id =",hex(id(x)))
print("nilai y =",y,"id =",hex(id(y)))
hasil = x is y
print('x is y =',hasil)

#is not
x =  5
y = 6
print("nilai x =",x,"id =",hex(id(x)))
print("nilai y =",y,"id =",hex(id(y)))
hasil = x is not y
print('x is not y =',hasil)