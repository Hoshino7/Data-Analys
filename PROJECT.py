Nama = "ASEP"
Asal = "Kota"
Tinggal = "Balikpapan"
print(Asal+Tinggal)
Level = 10*12
Skill = "Koding"
print(str(Level)+Skill)

Pesan_mu = (input())
print(Pesan_mu)

price = 2030/10.5
print(type(price))

a = 2
b = 3
print(type(a+b))

tahun_lahir = int(input())
print(type(tahun_lahir))

nilai1 = int(input())
nilai2 = int(input())
total = nilai1+nilai2
print(total)

print (type(35+45))

print(True or False)
print(True and False)

detak_jantung = 167
peak_rate = detak_jantung>120
print(peak_rate)

lampu_nyala = True
lampu_mati = False
print(lampu_nyala or lampu_mati)
print(lampu_nyala and lampu_mati)

temp = 35
ac_nyala = temp > 30
print(ac_nyala)
#kamu juga bisa mengecek apakah ac nyala atau mati
print(not ac_nyala)

presence = True
(temp > 30) or presence

ac_nyala = temp > 40 and presence
print(ac_nyala)

password = "password"
input = input()
if input == "password":
  print("Correct")
else:
  print("Incorrect")

  for i in range(5):
    print("Berurutan")

i = 1
while i <= 5:
    print(i)
    i = i + 1
#atau sederhananya
while duduk > 0:
    print("jual tiket")
    duduk = duduk -1

#atau dengan membuat kondisi jumlah loopinganya seperti ini dan memberitahukan ke layar jika kursinya sudah habis
duduk = 10
while duduk > 0:
    print("jual tiket")
    duduk = duduk - 1
    if duduk == 0:
        print("tiket habis")

password = "hutan rimba"
guess = "farhan"
print(guess != password)
while guess != password:
    guess = input("Password: ")
    print(guess == password)
print("Selamat Datang")

#anda bisa membuat code anda lebih simple
#contoh
umur = 21
if umur >= 18: print("anda berusia 18 tahun keatas")
print("anda diterima")

#kamu bisa menggunakan elif statement (short for else if statement) contoh
usia = 67
if usia < 18:
    print("anda masih muda")
elif usia <= 65:
    print("anda belum pensiun")
else:
    print("anda sudah pensiun")
print("Dan tidak perlu bekerja lagi")

#list
compositor=[
    "simpony1",
    "simpony2",
    "simpony3"
]
print(compositor)
#index di hitung dari 0 atau value pertama dari kiri maupun paling atas

prikitiw=['leman', 'asep', 'jupri']
print(prikitiw[0])
my_host=prikitiw[1]

produk=['apel', ' keju', 'pisang']
produk[0]='lime'
print(produk[2]+produk[1])

#vending machine
produk = ['apel', 'manggis', 'air']
choice = int(input)
print(produk[choice])