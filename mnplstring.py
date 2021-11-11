#tambah
n_awal = "mhmmd"
n_tengah = "rizki"
n_akhir = "padilah"

n_lengkap = n_awal +" "+ n_tengah +" "+ n_akhir
print('selamat datang! ',n_lengkap)
#hitung
panjang = len(n_lengkap)
print("panjang dari"+ n_lengkap + "=" + str(panjang))

#oprator string
#-cek komponen char/string
d = "d"
status = d in n_lengkap
print(d + " ada di " + n_lengkap +"="+ str(status) )

#index
print("index 0 = " + n_lengkap[0])
print("index 0,6 = " + n_lengkap[0:6])
print("index 0,3,5,7,9 = " + n_lengkap[0:9:2])

#mengulang string
print("wk"*10)
print(10*"wk")

#item paling kecil
print("paling kecil =" + min(n_lengkap))
#item paling besar
print("paling besar = " + max(n_lengkap))

asci_code = ord(" ")
print("ASCI CODE adalah = " + str(asci_code))
data = 117
print("karakter adalah = " + chr(data))

#oprator dalam method

data = "gatau lagi"
jumlah =data.count("a")
print("jumlah a pada data " + data +" = " + str(jumlah))