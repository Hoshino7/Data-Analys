is_student = True
if is_student:
    print("Anda adalah pelajar")
else:
    print("Anda bukan pelajar")
print("Selesai")

temperatue : 40
if temperatue > 30:
    print("Hari ini panas")
else:
    print("Hari ini dingin")
print("Selesai")

age = 18
if age < 20:
    print("anda keterima")
print("melanjutkan ke pembayaran")

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

#if, elif dan else harus berada pada statement yang benar 
#pada baris paling atas itu pasti if, kedua itu elif, dan ketiga itu else

if age < 18: 
    if is_student:
        print("diskon 20%")
    else:
        print("diskon 10%")
else:
    print("regular")
print("done")
#ngerti ngak kenapa diatas ada 2 else? 
#itu dinamakan nested blok adalah ketika if kedua yang bersarang di bagian indentasi dari pernyataan if pertama
#contoh
#if condisi == True:
#   if kondisi_kedua == True
#       print("if kedua yang nested")
#nested if membuat kondisi ini seperi gerbang dan jika ini true dan itu juga true, maka lakunlah ini