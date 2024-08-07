#Kode di Bawah mengekstrak 2nd Value di seuah list menggunakan Indexing
animals = ['kucing', 'burung', 'kucing', 'kucing', 'kucing', 'kucing', 'kucing']
print(animals[1])

#kode di bawah mengekstrak 2nd dan 3nd currency symbol menggunakan slicing
c = ['$','$', '$', '$', '$']
print(c[1:3])

#kode di bawah mengekstrak 2 value terakhir dari list
k = ['$', '3', '4', '5']
print(k[1:3])

#Python support "indexing dari akhir" dipanggil negative indexing, maksudnya last value of sequence has an index of -1
hewan = ['kucing', 'burung', 'kucing', 'kucing', 'kucing', 'kucing', 'kucing']
print(hewan[-1])

#output kode di bawah apa?
p = ['1', '2', '3', '4', '5']
print(p[-1])

Kendaraan = 'motorbike'
print(Kendaraan[-1])

#kode dibawah memiliki output 2 last value
h = ['1', '2', '3', '4', '5']   
print(h[-2:])

#kode di bawah memiliki output 2 value di tengah tengah data dari belakang
q = ['1', '2', '3', '4',]
print(q[1:-1])

#kode di bawah memiliki output bike
vehicle = 'motorbike'
print(vehicle[-4:])

#kamh bisa mengabungkan positive dengan negative indexing ketika slicing
j = ['1', '2', '3', '4', '5']
print(j[1:-2])