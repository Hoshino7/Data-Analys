for i in range(3):
    print(i < 1)
#maka akan menghasilkan type data boolean
#loop bisa meakukan pengulangan berkali-kali pada statement contohnya 
for i in range(3):
    print("Pertama")
    print("Kedua")
#ada berapa banyak kata dari output diatas? ada 6 kata

#selesai melakukan loop, komputer akan melakukan execute pada statement berikutnya contoh 
for i in range(3):
    print("a")
print("B")
#berapa banyak outputnya? jadi A 3 kali dan B sekali
#kenapa pesan selamattinggal di bawah ini hanya di tampilkan sekali?
for i in range(5):
    print("Halo")
print("Selamat Tinggal")
#maka ada 5 output dan 1 output selamat tinggal

#berapa sequence number dari range(3)? 0,1,2
#kamu bisa menggunakan operasi kompresi contoh
print (5 == 5)
print (5 == 7)
print (5!= 5)
print (5!= 7)
print (5 <= 7)
print (5 >= 7)
#kamu juga bisa menggunakan operator logika contoh
print (5 == 5 and 7 == 7)
print (5 == 5 and 7 != 7)
print (5 == 5 or 7 == 7)
print (5 == 5 or 7 != 7)
#kamu juga bisa menggabungkan operasi kompresi dan logika seperti di atas

#contoh program yang mengulangi pertanyaanya untuk user supaya bisa memasukkan password dengan benar maka loop apa yang akan di gunakan?
#kamu bisa menggunakan while loop  

password = "hutan rimba"
guess = "farhan"
print(guess != password)
while guess != password:
    guess = input("Password: ")
    print(guess == password)
print("Selamat Datang")

