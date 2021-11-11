data = [1,2,3,4,5,31,21]
#akses list
subdata = data[-3]
subdata_1 = data[3]
#potong list
subdata1 = data[0:4]
subdata2 = data[2:]
subdata3 = data[-2:]
subdata4 = data[:2]

data1 = [100,200,330,200,320,]

#tambah list
data2 = data + data1

#merubah conten list
print(data)
#data[2] = 87
a = data[:]
a[4] = 40
print(data)