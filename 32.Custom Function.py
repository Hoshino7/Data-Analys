#Fungsi bawaan dapat menghemat banyak pekerjaan, namun anda juga ahrus membuat fungsi kustom anda sendiri untuk menyelesaikan tugas tertentu.
#Fungsi adalah blok kode yang dapat digunakan kembali ingat itu.
#Untuk mengunakan fungsi anda sendiri, Anda perlu mendefinisikannya terlebih dahulu
#Setelah fungsi ditentunkan, Anda dapat memanggilnya sebanya anda butuhkan.
#Fungsi greet() dibawah ini berisi kode untuk menampilkan pesan yang menyambut saat di panggil

#definisi fungsi
def greet():
    print("Have a great day")

#memanggil fungsi
greet()

#Setelah fungsi di tentukan, Anda dapat memanggilnya
#Ini membuat kode anda singkat dan mudah di kelolah
#manggilnya tinggal ketik kode yang di bikin di def itu 
greet()

#Gunakan def diikuti dengan nama yang menentukan fungsi anda sendiri
#contoh
def alarm():
    print("Snooze?")
    print("Wake up!")

#body suatu fungsi yang berisi kode yang dapat digunakan kembali yang dieksekusi ketika fungsi tersebut di panggil
#Kode untuk isi fungsi harus diindentasi.
#Gunakan indentasi untuk memudahkan penjelasan kode.
#Contohnya kek def alarm di atas memiliki 2 baris kode dan bisa kamu tambahkan tapi jan kebanyakan nanti pusing :v
#Saat suatu fungsi didefinisikan, anda perlu memasitikan parentheses() ditambahkan setelah namanya.
#titik dua/colon : harus di tambahkan di akhir baris definisi
#Contoh
def waktu():
    print("Selamat Malam")
    print("Selamat Pagi")
    print("Selamat Siang")
    print("Selamat Sore")

#Suatu fungsi melakukan tugasnya contoh fungsi great yang tadi diatas fungsinya untuk menampilkan pesan sambutan nah intinya pahami lah kodemu sendiri
#Anda dapat mendefinisikan fungsi yang menggunakan sejumlah argumen (termasuk nol). 
#Argumen di letakkan di dalam tanda kurung () setelah nama fungsi
#contoh 
def personal_greet(name):
    print("Hello", name)
    print("Have a great day!")

#memanggil fungsi
personal_greet("Asep")
personal_greet("Rizki")

#Contoh lainnya
def double(number):
    print(number * 2)
double(10)
#Bisa di pake ke perhitungan :v

#Suatu fungsi dapat mengambil argumen sebanyak yang di perlukan untuk menyelesaikan tugas.
#Contohnya kode di bawah mendefinisikan fungsi yang menampilkan indeks massa tubuh (BMI).
#Berapa banyak argumen yang dimiliki fungsi ini?
def bmi(weight, height):
    index = weight / (height * height)
    print(index)
bmi(70, 1.75)
#Ada 2 argument
#saat calling suatu fungsi, anda perlu menggunakan jumlah argumen yang sama dengan yang telah di tentukan, dalam urutan yang sama

#Hasil dari suatu fungsi dapat dikirim kembali dengan pernyataan return.
#Hal ini sangat membantu ketika anda perlu terus menggunakan nilai hasil dalam program anda.
#Contoh
def BT(Berat, Tinggi):
    index = Berat / (Tinggi * Tinggi)
    return index
patient_1 = BT(70, 1.75)
print("underweight", patient_1 < 18.5)
#Jadi logikanya saya membuat kode untuk berat dan tinggi
#Lalu saya masukkan berat dan tinggi namun tingginya di kali tinggi
#lakukan pengulangan terhadap indek yang saya buat
#lalu saya memasukkan data pasien berat dan tingginya
#lakukan print jika benar pasien itu dibawah berat badan normal makan hasilnya akan underweight true jika tidak yah sebaliknya
