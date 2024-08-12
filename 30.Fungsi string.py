#Menangani data teks dengan benar adalah keterampilan utama yang harus dikuasai semua pembuat kode.
#Fungsi string akan meningkatkan produktivitias anda saat bekerja dengan data teks.

#Fungsi upper() dan lower() memungkinkan anda dengan cepat mengubah setiap huruf besar/kecil string menjadi sebaliknya.
#contoh
'SmArTpHoNe'.lower()
'SmArTpHoNe'.upper()

#upper() dan lower() fungsi hanya bisa digunakan pada string
#Fungsi yang hanya bekerja pada objek tertentu di panggil menggunakan titik atau notasi
#Contoh 
'LaPtOp'.lower() 

#Banyak fungsi bawaan yang perlu dipanggil menggunakan notasi titik.
#Contoh
'LaPtOp'.upper()

#Ingat bahwa fungsi print() diperlukan untuk menampilkan hasil ke layar
print("bmw".upper())

#Ingat kamu bisa menggunakan variabel di fungsi
brand = "ikea"
print(brand.upper())

#Fungsi capitalize() akan menghemat waktu anda saat perlu mengubah karakter pertama string menjadi huruf kapital sekaligus membuat karakter lainnya menjadi huruf kecil
#contoh
city = "semARANG"
print(city.capitalize())

#String itu immutable yang bearti tidak dapat diubah
#Anda harus menyimpan modifikasi string di variable untuk menyimpanyan perubahan
item = "sepatu"
item = item.upper()
print(item)

#Fungsi find() memeriksa apakah karakter atau pola karakter ada dalam string.
#Fungsi mengembalikan indeks(posisi) dari nilai yang diberikan
#Jika nilai yang diberikan ada beberapa kali, fungsi akan mengembalikan indeks yang pertama yang ditemukan
#Find() digunakan pada string jadi gunakan dot notasi
#Contoh
print("Robot".find("o"))

#find() akan menghasilkan kesalahan jika anda tidak menyertakan argumen diantara kurung.
#Jika tidak ada yang perlu dicari dalam string, fungsi tersebut tidak dapaat melakukan tugasnya
#Find() akan mengembalikan -1 jika nilainya tidak dapat ditemukan di string
print("Robot".find("z"))