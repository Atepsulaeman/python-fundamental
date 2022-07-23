"""
Semua Sintaksis dasar bahasa Pemograman  diantaranya :
1. Sekuensial : Langkah Berurutan
2. Percabangan : Langkah Melompat Jika Kondisi Terpenuhi
3. Perulangan : Mengulang Langkah Yang Sama Berkali -kali Selama/sampai Kondisi Terpenuhi
"""
# Sekuensial Tugas 1

print('Ibu berkata,"Pergi Ke toko"')
print('Budi Menjawab,"apa yang harus saya lakukan di Toko?"')
print ('Ibu Menjawab,"Belikan 1 botol Susu"')
print('Maka Budi berangkat ke toko')
print('dan Mulai Berbelanja')

# Percabangan
jumlah_botol_susu = 173
jumlah_telur = 1587
print(f"jumlah botol susu {jumlah_botol_susu} botol")
print(f"jumlah telur {jumlah_telur} butir")

if jumlah_botol_susu >0:
    print("Budi mengecek harganya, dan ternyata uangnya cukup")
    if jumlah_telur >0:
         print("budi membeli 1 botol susu")
         print ("dan budi membeli juga 6 butir telur")
    else :
        print("budi membeli 6 botol susu")
else :
    print("budi tidak jadi membeli 1 botol susu")
print("budi pulang kerumah")
print("menyampaikan hasilnya kepada ibu")








