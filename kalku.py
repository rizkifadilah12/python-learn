
print(20*"=")
print("kalkulator sederhana")
print(20*"=" + "\n")

angka1 = float(input("masukan angka = "))
oprator = input("oprator (+,-,x,/) = ")
angka2 = float(input("masukan angka = "))

if oprator== "+" :
    hasil = angka1 + angka2
    print("hasil = ",hasil)
elif oprator == "-":
    hasil = angka1 - angka2
    print("hasil = ",hasil)
elif oprator == "x" or oprator == "*":
    hasil = angka1 * angka2
    print("hasil = ",hasil)
elif oprator == "/":
    hasil = angka1 / angka2
    print("hasil = ",hasil)
else:
    print("oprator yang anda masukan salah")
