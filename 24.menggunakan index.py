#kamu bisa membuat list dengan value untuk di simpan di variabel
nama = 'putra'
umur = '17'
negara = 'indonesia'
info=[nama, umur, negara]
print(info[0])

#berikut program vending machine
produk = ['apel', 'manggis', 'air']
choice = int(input)
print(produk[choice])
#atau bisa gunakanan 
user_choice = 1
print(produk[user_choice])

#indexing bekerja juga dengan string.kamu bisa mengakses satu huruf karakter di sebuah string 
animal="dog"
print(animal[0])

#karakter di sebuah string bisa termasuk spasi dan punctuation mark
notification = "new message"
print(notification[4])
#kamu bisa menambahkan jenis list pada indeks yang lain seperti di bawah ini
print(notification[0:4]) 

#kamu juga bisa meganti huruf pada list contoh 
kata = "car"
kata[2] = "t"

z = "antartika"
print( z[2] + z[0] + z[4] + z[3] + z[1] ) 