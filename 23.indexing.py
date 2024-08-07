#ingat list harus di bagi menggunakan comma
#you can refer to values in a list using their position or index
#include index in square brackets to refer to the second value in the list
animals=["kucing", "tranggiling", "cihuy"]
animals[1]

#gunakan indexing untuk mengakses value yang berbeda dari list diatas
#"kucing": animals[0]
#"tranggiling": animals[1]
#"cihuy": animals[2]

#kamu bisa menggunakan orint untuk menunjukkan value indivi di layar
prikitiw=['leman', 'asep', 'jupri']
print(prikitiw[0])

#bisa juga list value ke variabel contoh
#saya sambungkan dengan list prikitiw
my_host=prikitiw[1]

#list itu mutable, maksudnya kamu bisa mengubah valuenta setelah membuat list contoh
nums = [8, 6, 19]
nums[0] = 1 
print(nums[0])

#bisa juga di gabungkan
word=['rise', 'bangkit', 'manipulasi']
print(word[0] + word[2]) 

#jadi output list dibawah apanih?
produk=['apel', ' keju', 'pisang']
produk[0]='lime'
print(produk[2]+produk[1])