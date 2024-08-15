#list adalah konsep penting dalam coding.
#Memungkinkan anda menyimpan beberapa nilai dalam satu variabel,membuat program lebih efisien dan rapi

#Apa indeks untuk perahu di bawah ini? 
items = ["sepeda", "mobil", "perahu", "scooter"]

#Gunakan indexing untuk melengkapi kode di bawah untuk menampilkan Avenger di layar
movies = ["avenger", "thor", "hulk", "ironman"]
print(movies[0])

#len() singkatan dari lenght dan, ketika digunakan pada daftar, ia mengembalikan jumlah item dalaam daftar
#Fungsi len() tidak hanya untuk daftar.Ia menerima sebagai argumen urutan apapun, termasuk string.
#Contoh
film = "avatar"
print(len(film))

#len() adalah fungsi yang sangat berguna yang menerima berbagai argumen
#Ini tidak spesifik untuk tipe data atau objek tertentu, jadi anda tidak perlu menggunakan notasi titik untuk memanggilnya.
print(len(items))

#Fungsi append() untuk menambahkan item baru ke akhir data 
#Fungsi append() di panggil menggunakan notasi titik akrena khusus untuk list
#append() mengubah daftar
#Ini berarti daftar baru yang di perpanjang akan di simpan dengan nama yang sama    
#hal ini memungkinkan karena list itu mutbale atau bisa di ubah kapan saja
#Fungsi append() untuk list
#Jika di coba menggunakan append() pada sebuah string, akan terjadi error karena string itu immutable tidak dapat di ubah
Cerita = ["Avenger", "Thor", "Hulk", "Ironman"]
Cerita.append("Spiderman")
print(Cerita[4])

#Fungsi insert() memungkinkan anda menambahkan element ke daftar pada posisi tertentu.
#Fungsi insert() membutuhkan 2 argumen
#Yang pertama adalah indext(tempat memasukkan data)
#Yang kedua adalah item (apa yang dimasukkan)

colors = ["red", "green", "blue"]
colors.insert(1, "yellow")
print(colors)
#Identifikasi elemen dengan index setelah eksekusi kode
#"Red": index 0
#"Yellow": index 1
#"Green": index 2
#"Blue": index 3
warna = ["red", "green", "blue"]
warna.insert(1, "yellow")
warna.append("white")
print(warna[1])

#Fungsi pop() menghapus element dari daftar
#Posisi yang ditunjukkan oleh index adalah satu-satunya argumen yang diterima fungsi pop()
topic = ["math", "science", "english"]
topic.pop(1)
print(topic)