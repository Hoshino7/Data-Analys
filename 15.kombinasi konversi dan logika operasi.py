##kamu bisa memasukkan boolean value dalam variabel dengan data lainnya contoh
sleep = True
#bisa juga...
detak_jantung = 167
peak_rate = detak_jantung>120
print(peak_rate)
#kamu bisa memasukkan hasil dari logika vale di variabel
n = True and False
print(n)
#juga kau bisa melakukan hal di bawah ini 
lampu_nyala = True
lampu_mati = False
print(lampu_nyala or lampu_mati)
print(lampu_nyala and lampu_mati)
#rumah pintar meyimpat data temperature dengan celcius(cel) dan farenheit(far)
#contohnya sistem akan menyalan ac ketika temperatur di atas 30 celcius
temp = 35
ac_nyala = temp > 30
print(ac_nyala)
#kamu juga bisa mengecek apakah ac nyala atau mati
print(not ac_nyala)
#kamu bisa memasukkan prentheses di sekeliling operasi duluan, dan membuat kodenya mudah di baca
a = (3 > 2) or False
#rumah pintar bisa mendeteksi jumlah orang di rumah contoh
presence = True
(temp > 30) or presence
#temperatur rumah akan menyata ketika lebih dari 30 celcius dan ada presence dalam rumah
presence and (temp > 30)
#code di bawahg  ini akan menyalakan ac ketika mendeteksi temperature lebih tinggi dari 40 dan ada orang di rumah
ac_nyala = temp > 40 and presence
print(ac_nyala)
