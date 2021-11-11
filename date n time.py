import datetime as dt



print("silahkan masukan tanggal bulan laihr anda")
tanggal = int(input("tanggal \t:"))
bulan   = int(input("bulan  \t\t:"))
tahun   = int(input("tahun  \t\t:"))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print("tanggal lahir anda adalah = ",tanggal_lahir)
tanggal = dt.date.today()
print(f"hari ini adalah tanggal = {tanggal}")
print(f"harinya adalah : {tanggal_lahir:%A}")


umur = tanggal - tanggal_lahir
umur_tahun = umur.days// 365
umur_bulan = (umur.days % 365) // 30
print(f"umur anda adalah : {umur_tahun} tahun, {umur_bulan} bulan")