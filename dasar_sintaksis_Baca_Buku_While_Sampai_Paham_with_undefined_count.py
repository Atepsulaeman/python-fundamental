"""
Program Perulangan membaaca buku dengan while sampai paham undifined with undefined count
"""
jumlah_buku = 10
print(f'jumlah Buku {jumlah_buku}')#penambahan impropisasi
print('Ibu berkata, "baca semua buku')
jumlah_baca = 0

jumlah_dipahami = 0
print(f'jumlah buku yang sudah dibaca dan dipahami {jumlah_dipahami}')

while jumlah_baca < jumlah_buku * 2:
    jumlah_baca = jumlah_baca + 1
    if jumlah_dipahami  == 9 :
        print(f"Buku Ke {jumlah_dipahami + 1} belum paham")
    else :
        jumlah_dipahami = jumlah_dipahami + 1
        print(f"Buku Ke {jumlah_dipahami} sudah dibaca dan dipahami")

print(f'jumlah_dipahami {jumlah_dipahami}')
if jumlah_dipahami == jumlah_buku :
    print('"Bu Semua Buku Sudah dibaca dan dipahami ')
else:
    print(f'"Bu Tidak Semua Buku bisa dipahami.Budi hanya bisa memahami {jumlah_dipahami} Buku')

## while : selama kondisi belum terpenuhi maka program berjalan sampai kondisi terpenuhi #



print("**note : Perulangan dengan while dengan jumlah tak terbatas dan ada variabel perberhentian")
