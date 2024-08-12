#Berapa banyak argumen yang ada dalam fungsi print()?
print("Hello World", "Hello World", "Hello World", 91)

#Fungsi dapat melakukan operasi matematika 
#Contohnya fungsi print() dapat melakukan operasi matematika
print(5 + 5)
print(5 - 5)
print(5 * 5)
print(5 / 5)
print(5 // 5)
print(5 ** 5)
print(5 % 5)

#atau...
x = "air"
y = "plane"
print(x + y)

#Namun beberapa fungsi hanya menerima satu jenis type argument contohnya range() hanya menerima tipe data integer 
range(4)

#Kamu bisa menggunakan value yang tersimpan di variabel sebagai argumen
balance = "780"
print("Your balance is", balance)
#Contoh lainnya
name = "John"
country = "USA"
age = 25
print("My name is", name, "I am", age, "years old and I am from", country)
#contoh lagi
temperature = 25
humidity = 75
print("temperature", "C")

#Sebuah fungsi dapat menjadii sebuah argument di fungsi lain 
print(type("Hello World"))
print(range(5))

#int(), str(), float() adalah suatu instruksi yang juga sebagai fungsi contoh
x = str(5)

#Kode anda akan error jika memasukkan tipe data yang salah sebagai argument.
#Beberapa fungsi memerlukan tipe data tertentu sebagai argumen.
#Misalnya, fungsi int() tidak akan dapat mengubah karakter non-numerik (misal a-z) menjadi angka dan akan menghasilkan error
num = '45'
print(int(num)+3)