#logika dan komparasi

#gabungan area rentang dari angka

inputuser =float (input("masukan angka kurang dari 3 \nlebih dari 10 \n="))

#periksa kurang dari 3
kurang = (inputuser < 3)
print("kurang dari 3 =",kurang)

#priksa angka lebih dari 10
lebih = (inputuser > 10)
print("lebih dari 10 =",lebih)

#gabungan

#irisan
inputuser =float (input("masukan angka lebih dari 3 \n dan kurang dari 10 \n="))

#lebih dati tiga
lebih = inputuser > 3
print("lebih dari 3 =",lebih)

kurang = inputuser < 10
print("kurang dari 10 =",kurang)

benar = kurang and lebih
print("hasil =",benar)