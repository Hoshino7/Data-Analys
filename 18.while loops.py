#while loops adalah looping yang berulang
#kita harus menentukan syarat ketika looping berulang
#contohnya
i = 1
while i <= 5:
    print(i)
    i = i + 1
#atau sederhananya
while duduk > 0:
    print("jual tiket")
    duduk = duduk - 1
#atau dengan membuat kondisi jumlah loopinganya seperti ini dan memberitahukan ke layar jika kursinya sudah habis
duduk = 10
while duduk > 0:
    print("jual tiket")
    duduk = duduk - 1
    if duduk == 0:
        print("tiket habis")
#loop usually include counters. counter adalah variabel tetap yang melacak nomor perulangan contohnya di atas
#counter di atas adalah? duduk :v
#apa yang terjadi ketika value duduk dengan tiap iteraton yang terjadi? iyap berkurang
#bisa loh kodenya terjadi kesalahan atau menjadi infinite loop contoh terjadinya infinite loop di bawah ini
duduk = 10
while duduk > 0:
    print("beli tiket")
    #duduk = duduk - 1
#ayo lebih dalam apa yang terjadi dalam loop
counter = 0
while counter < 4:
    print(counter)
    counter = counter + 1
#ini bermaksud menyelesaikan loop dengan menambahkan counter dengan 1 tapi tidak lebih dari 4