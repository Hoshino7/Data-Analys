#Fungsi khusus(yang dibuat user) membantu memecah program besar menjadi segmen-segmen kecil agar mudah dipahami,dipelihara,dan di-debug.
#Fungsi argumen adalah nilai yang teruskan saat memanggil suatu fungsi
def convert_km(miles):
    kilometers = miles * 1.61
    return kilometers
distance = convert_km(10)
print(distance) 

#Suatu fungsi dapat mereturn beberapa nilai sekaligus
#Contoh saya membuat fungsi rect() membantu agen real estat menghitung luas dan keliling sebuah tanah berbentuk persegi panjang.Dibutuhkan dua dimensi parsel sebagai argumen
def rect(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter,
area, perimeter = rect(10, 5)
price = 1000 * area, 1000 * perimeter
print(area, perimeter, price)
#Multiple return values di pisah dari comma
#Suka-suka mu sebagai yang buat kode untuk menentukan operasi apa yang terjadi di dalam fungsi anda
#Kemudian kontrol tipe mana yang dapat di tangani dan di return
#Contoh di bawah saya membuat fungsi profitable() menentukan apakah membeli sebidang tanah merupakan investasi yang baik untuk agen di lokasi tertentu
def profitable(d1, d2):
    area = d1 * d2
    invest = area > 700
    return invest
buy = profitable(90, 120)
print(buy)
#Yang mana tipe datanya itu
#Argumen sebagai numerik
#return sebagai boolean true/false
#Eksekusi kode di dalam baris kode tambahan setelah baris kembali akan di abaikan
def ref(d1, d2):
    area = 0
    return area
#End of function execution
#area = d1 * d2 #Not executed
x = ref(90, 120)
print(x)
#Tidak ada return value awkoakwok 