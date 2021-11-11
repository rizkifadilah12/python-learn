#oprator dalam method
salam = "Halo"
print("normal =" + salam)

#capslck All (upper)
salam = salam.upper()
print("upper =" + salam)

#Normal All
cap = "AkU GaTaU LAGI"
print("normal = " + cap)
cap = cap.lower()
print("lower = " + cap)

#pengecekan IsX method
#lower/uper
salam = "sist"
apa = salam.islower()
print(salam + "  is lower = " + str(apa))
apa_u = salam.isupper()
print(salam + "  is lower = " + str(apa_u))

#isaslpha <-- cek semua huruf
#isnum  <-- angka dan huruf
#isdecimal <-- semua angka
#is space <-- spasi,tab,newline
#istitle <-- semua kata di mulai dengan huruf besar

judul = "Maku"
cek = judul.istitle()
print(judul +" is title" + " = " + str(cek))

#chek componet starswiht() endswith()
cek = "Sangkiang Pp".startswith("Sangkiang")
print("starswith = " + str(cek))

cek_e ="Sangkiang Pp".endswith("Pp")
print("endswith = " + str(cek_e))

#penggabungan dan pemisahan join() split()
pisah = ['aku','benci','kamu']
gabung =','.join(pisah)
print(pisah)
print(gabung)

gabung =' '.join(pisah)
print(gabung)

gabung = "aku benci kamu"
print(gabung.split(' '))

#alokasi karakter rjust() ljust() center()
kanan = "kanan".rjust(10)
print("'"+kanan+"'")


kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "tengah".center(20,"-")
print("'"+tengah+"'")

#kebalikan stript
tengah = tengah.strip("-")
print("'"+tengah+"'")
kanan = kanan.strip()
print("'"+kanan+"'")