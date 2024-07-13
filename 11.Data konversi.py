#Data bisa saja menjadi format yang tidak valid.Data dari survey dan web form bisa aja ada kualitas issue
#Input selalu membuat input user ke string apapun yang mereka masukkan
tahun_lahir= input()
print(type(tahun_lahir))

#kamu bisa melakukan konversi jenis data dengan memasukan instruksi int() dengan instruksi ini semua data yang di pilih akan menjadi jenis integer
x = "55" # x itu sebuah string
y = int(x) # y itu sebuah integer

#kamu bisa menggunakan insturksi int() untuk melakukan konversi pada user input
berat = int(input())

#Jadi...
a = input() #hasilnya pasti string
b = int(input()) #hasilnya pasti integer

#sekarang ada juga instruksi mengubah data menjadi type floats dengan instruksi float()
d = 15
b =float(d)
#Atau...
n = 3
m = float(n)
print(m)
#datanya jadi type float cuy atau pake desimal :v

#sama aja cuy cara ubah data menjadi string itu yah pake instruksi str()
v = 2.8
l =str(v)

# Jadi int(),str(),float() adalah contoh dari explicit conversi, maksudnya mereka melakukan instruksi dari apa yang programmer berikan 
#contoh implicit(otomatis) data type konversi
z = 4 #integer
o = 2 #integer

u = z/o #float (implicit data)