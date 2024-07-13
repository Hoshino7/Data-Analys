#eksekusi dalam program mu akan gagal jika ada data dalam incoreect format
#masih ingat instruksi apa yang digunakan untuk mengubah format data menjadi integer? 
#ayo kita ulangi lagi
role=input()
score=int(input())

#code berikut mengambl 2 nomor dan mengabungkanya
score1=int(input())
score2=int(input())
total_score=score1+score2

#hasil dari code output dibawah ini setelah mendapatkan nomor dari user?
age = int(input())
print(type(age))

#code output <class 'int'>
x=15
print(type(x))
#maksudnya apa?
#jadi variabel x itu menyimpan sebuah type data integer

#ayo kita ingat lagi
#code di bawah menunjukkan snowball di layar
a="bola"
b="salju"
c="kaki"
print(a+b)

#ingat integer tidak bisa tergabung ke string hasilnya jadi error contohnya dibawah
jauh = 14
unit = "km"
print(jauh+unit)
#kecuali gini 
print("14"+"km")
#baru bisa :v

#tapi bisa juga kamu akali menggunakan str() contohnya
jarak = 14
diameter = "km"
print(str(jarak)+diameter)
#jadi jarak akan di ubah ke type string dulu maka ia bisa digabungkan dengan diameter semoga anda mengerti

#operasi matematika antara integer dan float akan menghasilkan data float
c=9
d=3.0
print(c+d)

#kode di bawah akan menunjukkan data float
print(12/6)
#ini contoh dari implicit data type conversion